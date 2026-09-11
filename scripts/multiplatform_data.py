"""Immutable two-source loading and pooled, group-safe split management."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import warnings
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import StratifiedGroupKFold

from evaluation.stratification import (
    check_group_fold_counts,
    joint_stratification_labels,
)
from features.content_groups import (
    CONTENT_GROUP_METHOD,
    content_group_ids,
    duplicate_group_count,
    exact_duplicate_group_count,
    validate_group_labels,
)
from scripts.prepare_data import CSV_COLUMNS, file_sha256, validate_dataset


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MULTIPLATFORM_PROTOCOL = "pooled_multiplatform_v1"
MULTIPLATFORM_GROUPING = "near_duplicate_transcript_connected_components"
AUDIT_COLUMNS = ("row_index", "record_id", "platform", "source_row")


def is_multiplatform(settings: dict[str, Any]) -> bool:
    """Return whether an experiment declares multiple immutable sources."""
    return bool(settings.get("data", {}).get("sources"))


def validate_multiplatform_experiment(settings: dict[str, Any]) -> None:
    """Enforce the pooled experiment's platform-comparable feature contract."""
    if not is_multiplatform(settings):
        raise ValueError("The selected configuration is not multi-platform.")
    if settings["data"].get("mode") != "pooled_multiplatform":
        raise ValueError("The multi-platform data mode must be pooled_multiplatform.")
    text_columns = tuple(settings.get("features", {}).get("text_columns", ()))
    if text_columns != ("transcript",):
        raise ValueError(
            "The pooled experiment must use transcript as its sole text column."
        )
    if settings["features"].get("engagement_transform") != (
        "within_platform_percentile"
    ):
        raise ValueError(
            "The pooled experiment requires fold-local within-platform "
            "engagement percentiles."
        )
    if settings["features"].get("platform_column") != "platform":
        raise ValueError(
            "The pooled engagement router must use the in-memory platform column."
        )
    if tuple(settings["split"].get("stratification_columns", ())) != (
        "platform",
    ):
        raise ValueError(
            "The pooled split must be jointly stratified by platform and label."
        )
    if settings["split"].get("generation_grouping") != MULTIPLATFORM_GROUPING:
        raise ValueError(
            "The pooled split must be generated from near-duplicate content groups."
        )
    if not bool(settings.get("reporting", {}).get("report_by_platform", False)):
        raise ValueError("The pooled experiment must report held-out results by platform.")


def _normalise_placeholder(value: object) -> str:
    return str(value).strip().casefold()


def _class_distribution(data: pd.DataFrame) -> dict[str, int]:
    return {
        str(int(label)): int(count)
        for label, count in data["label"].value_counts().sort_index().items()
    }


def _joint_distribution(data: pd.DataFrame) -> dict[str, int]:
    counts = data.groupby(["platform", "label"], sort=True).size()
    return {
        f"{platform}|{int(label)}": int(count)
        for (platform, label), count in counts.items()
    }


def source_input_files(
    project_root: str | Path,
    data_settings: dict[str, Any],
) -> dict[str, Path]:
    """Return stable source names and paths for run-manifest hashing."""
    root = Path(project_root)
    sources = data_settings.get("sources", [])
    if len(sources) < 2:
        raise ValueError("A pooled multi-platform experiment needs at least two sources.")
    names = [str(source.get("name", "")).strip() for source in sources]
    if any(not name for name in names) or len(set(names)) != len(names):
        raise ValueError("Multi-platform source names must be nonblank and unique.")
    return {
        f"dataset_{name}": root / str(source["path"])
        for name, source in zip(names, sources, strict=True)
    }


def _combined_source_sha256(source_records: list[dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for record in source_records:
        digest.update(str(record["name"]).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(record["path"]).encode("utf-8"))
        digest.update(b"\0")
        digest.update(str(record["sha256"]).encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def load_multiplatform_data(
    project_root: str | Path,
    data_settings: dict[str, Any],
) -> tuple[pd.DataFrame, dict[str, object]]:
    """Read, validate, and concatenate sources without changing either CSV."""
    root = Path(project_root)
    paths = source_input_files(root, data_settings)
    minimum_claims = int(data_settings["minimum_claims_for_assigned_label"])
    unassigned_threshold = int(data_settings["unassigned_allowed_below_claims"])
    maximum_duration = data_settings.get("maximum_duration_seconds")
    maximum_duration = (
        int(maximum_duration) if maximum_duration is not None else None
    )
    minimum_latin_fraction = float(
        data_settings.get("minimum_latin_letter_fraction_for_review", 0.80)
    )

    frames: list[pd.DataFrame] = []
    source_records: list[dict[str, object]] = []
    placeholder_records: list[dict[str, object]] = []
    validation_records: dict[str, object] = {}
    source_by_name = {
        str(source["name"]).strip(): source for source in data_settings["sources"]
    }
    global_offset = 0
    for input_name, path in paths.items():
        name = input_name.removeprefix("dataset_")
        source = source_by_name[name]
        if not path.is_file():
            raise FileNotFoundError(f"Configured source CSV is missing: {path}")
        before = file_sha256(path)
        frame = pd.read_csv(path).reset_index(drop=True)
        summary = validate_dataset(
            frame,
            expected_rows=int(source["expected_rows"]),
            minimum_claims_for_assigned_label=minimum_claims,
            unassigned_allowed_below_claims=unassigned_threshold,
            maximum_duration_seconds=maximum_duration,
            minimum_latin_letter_fraction_for_review=minimum_latin_fraction,
            required_text_columns=("transcript",),
        )
        if file_sha256(path) != before:
            raise RuntimeError(f"Validation unexpectedly changed source CSV: {path}")

        declared = tuple(
            _normalise_placeholder(value)
            for value in source.get("title_placeholders", [])
        )
        title_values = frame["title"].map(_normalise_placeholder)
        matches = title_values.isin(declared) if declared else pd.Series(
            False, index=frame.index
        )
        if bool(source.get("require_all_titles_placeholder", False)) and not matches.all():
            unexpected = frame.index[~matches].astype(int).tolist()
            warnings.warn(
                f"Source {name} declares every title as a placeholder, but rows "
                f"{unexpected} do not match {list(declared)}. Titles are excluded "
                "from pooled models; execution is not blocked.",
                UserWarning,
                stacklevel=2,
            )
        placeholder_records.append(
            {
                "source": name,
                "declared_values": list(declared),
                "placeholder_rows": int(matches.sum()),
                "advisory_only": True,
                "excluded_from_pooled_text": True,
            }
        )

        annotated = frame.copy()
        annotated.insert(0, "source_row", np.arange(len(frame), dtype=int))
        annotated.insert(0, "platform", name)
        annotated.insert(
            0,
            "record_id",
            [f"{name}:{index:06d}" for index in range(len(frame))],
        )
        annotated.insert(
            0,
            "row_index",
            np.arange(global_offset, global_offset + len(frame), dtype=int),
        )
        global_offset += len(frame)
        frames.append(annotated)
        validation_records[name] = summary
        source_records.append(
            {
                "name": name,
                "path": str(path.resolve().relative_to(root.resolve())),
                "sha256": before,
                "rows": len(frame),
                "columns": list(frame.columns),
            }
        )

    combined = pd.concat(frames, ignore_index=True)
    expected_combined_rows = data_settings.get("expected_rows")
    if (
        expected_combined_rows is not None
        and len(combined) != int(expected_combined_rows)
    ):
        raise ValueError(
            f"Combined source has {len(combined)} rows; expected "
            f"{int(expected_combined_rows)}."
        )
    if combined["row_index"].tolist() != list(range(len(combined))):
        raise RuntimeError("Combined row indices are not deterministic.")
    if combined["record_id"].duplicated().any():
        raise ValueError("Combined record identifiers are not unique.")
    labelled = combined.loc[combined["label"].notna()].copy()
    labelled["label"] = pd.to_numeric(labelled["label"]).astype(int)
    validate_group_labels(labelled)
    groups = content_group_ids(combined)
    group_frame = combined[
        ["row_index", "record_id", "platform", "source_row"]
    ].copy()
    group_frame.insert(0, "content_group", groups)
    group_sizes = group_frame.groupby("content_group").size()
    duplicate_groups: list[dict[str, object]] = []
    for group in sorted(group_sizes.loc[group_sizes.gt(1)].index):
        members = group_frame.loc[group_frame["content_group"].eq(group)].copy()
        duplicate_groups.append(
            {
                "content_group": str(group),
                "member_count": len(members),
                "platforms": sorted(members["platform"].astype(str).unique()),
                "members": members[
                    ["row_index", "record_id", "platform", "source_row"]
                ].to_dict(orient="records"),
            }
        )
    cross_platform_groups = [
        record for record in duplicate_groups if len(record["platforms"]) > 1
    ]
    report: dict[str, object] = {
        "protocol": MULTIPLATFORM_PROTOCOL,
        "source_files": source_records,
        "combined_source_sha256": _combined_source_sha256(source_records),
        "source_rows": len(combined),
        "modelled_rows": len(labelled),
        "excluded_unassigned_rows": int(combined["label"].isna().sum()),
        "platform_distribution": {
            str(key): int(value)
            for key, value in combined["platform"].value_counts().sort_index().items()
        },
        "class_distribution": _class_distribution(labelled),
        "platform_label_distribution": _joint_distribution(labelled),
        "exact_duplicate_transcript_groups": exact_duplicate_group_count(combined),
        "duplicate_or_near_duplicate_content_groups": duplicate_group_count(combined),
        "cross_platform_content_groups": len(cross_platform_groups),
        "duplicate_or_near_duplicate_content_group_records": duplicate_groups,
        "cross_platform_content_group_records": cross_platform_groups,
        "content_group_method": CONTENT_GROUP_METHOD,
        "title_placeholder_audit": placeholder_records,
        "source_validation": validation_records,
        "raw_csvs_modified": False,
        "audit_columns_added_in_memory": list(AUDIT_COLUMNS),
    }
    return combined, report


def deterministic_multiplatform_split(
    data: pd.DataFrame,
    heldout_folds: int,
    heldout_fold: int | str,
    seed: int,
    stratification_columns: tuple[str, ...] = ("platform",),
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray, int, int]:
    """Split labelled rows jointly by platform/label and content group."""
    if isinstance(heldout_folds, bool) or int(heldout_folds) < 2:
        raise ValueError("heldout_folds must be an integer of at least two.")
    heldout_folds = int(heldout_folds)
    modelling = data.loc[data["label"].notna()].copy().reset_index(drop=True)
    modelling["label"] = pd.to_numeric(modelling["label"]).astype(int)
    all_groups = content_group_ids(data)
    groups = all_groups[modelling["row_index"].to_numpy(dtype=int)]
    strata = joint_stratification_labels(
        modelling,
        modelling["label"],
        stratification_columns,
    )
    check_group_fold_counts(strata, groups, heldout_folds, "Pooled held-out split")
    splitter = StratifiedGroupKFold(
        n_splits=heldout_folds,
        shuffle=True,
        random_state=int(seed),
    )
    splits = list(splitter.split(modelling, strata, groups))
    target_size = int(math.ceil(len(modelling) / heldout_folds))
    expected_strata = set(strata.unique())
    if isinstance(heldout_fold, str):
        if heldout_fold != "auto":
            raise ValueError("heldout_fold must be an integer or 'auto'.")
        proportions = strata.value_counts(normalize=True)
        candidates: list[tuple[float, float, int]] = []
        for fold, (training, heldout) in enumerate(splits):
            if (
                set(strata.iloc[training].unique()) != expected_strata
                or set(strata.iloc[heldout].unique()) != expected_strata
            ):
                continue
            counts = strata.iloc[heldout].value_counts()
            distribution_error = float(
                sum(
                    abs(float(counts.get(value, 0)) - proportions[value] * target_size)
                    for value in sorted(expected_strata)
                )
            )
            candidates.append(
                (abs(len(heldout) - target_size), distribution_error, fold)
            )
        if not candidates:
            raise ValueError(
                "No grouped fold contains every platform/label stratum in both "
                "training and held-out data."
            )
        selected_fold = min(candidates)[2]
    else:
        if isinstance(heldout_fold, bool):
            raise ValueError("heldout_fold must be an integer or 'auto'.")
        selected_fold = int(heldout_fold)
        if selected_fold < 0 or selected_fold >= len(splits):
            raise ValueError("heldout_fold is outside the available split range.")
    training_position, heldout_position = splits[selected_fold]
    if set(strata.iloc[training_position].unique()) != expected_strata or set(strata.iloc[heldout_position].unique()) != expected_strata:
        raise ValueError("The selected pooled fold omits a platform/label stratum.")
    if set(groups[training_position]) & set(groups[heldout_position]):
        raise ValueError("A content group crosses the pooled held-out split.")
    return (
        modelling,
        training_position,
        heldout_position,
        selected_fold,
        target_size,
    )


def _read_indices(path: Path) -> np.ndarray:
    frame = pd.read_csv(path)
    if tuple(frame.columns) != ("row_index",):
        raise ValueError(f"{path} must contain only row_index.")
    numeric = pd.to_numeric(frame["row_index"], errors="coerce")
    if (
        numeric.isna().any()
        or not np.isfinite(numeric.to_numpy(dtype=float)).all()
        or not np.equal(numeric, np.floor(numeric)).all()
    ):
        raise ValueError(f"{path} must contain finite integer row indices.")
    values = numeric.astype(int).to_numpy()
    if len(values) != len(set(values)) or not np.array_equal(values, np.sort(values)):
        raise ValueError(f"{path} must contain unique, increasing row indices.")
    return values


def _split_manifest_values(
    data: pd.DataFrame,
    report: dict[str, object],
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    excluded: np.ndarray,
    split_settings: dict[str, Any],
    selected_fold: int,
    target_size: int,
) -> dict[str, object]:
    return {
        "protocol": MULTIPLATFORM_PROTOCOL,
        "combined_source_sha256": report["combined_source_sha256"],
        "source_files": report["source_files"],
        "source_rows": len(data),
        "modelled_rows": len(training) + len(heldout),
        "excluded_rows": len(excluded),
        "training_rows": len(training),
        "heldout_rows": len(heldout),
        "training_platform_distribution": {
            str(key): int(value)
            for key, value in training["platform"].value_counts().sort_index().items()
        },
        "heldout_platform_distribution": {
            str(key): int(value)
            for key, value in heldout["platform"].value_counts().sort_index().items()
        },
        "training_class_distribution": _class_distribution(training),
        "heldout_class_distribution": _class_distribution(heldout),
        "training_platform_label_distribution": _joint_distribution(training),
        "heldout_platform_label_distribution": _joint_distribution(heldout),
        "splitter": "StratifiedGroupKFold",
        "heldout_folds": int(split_settings["heldout_folds"]),
        "heldout_fold": int(selected_fold),
        "heldout_fold_setting": split_settings["heldout_fold"],
        "heldout_target_rows": int(target_size),
        "seed": int(split_settings["seed"]),
        "stratification_columns": list(
            split_settings.get("stratification_columns", ["platform"])
        ),
        "stratification_target": "label",
        "split_generation_grouping": MULTIPLATFORM_GROUPING,
        "split_generation_group_method": CONTENT_GROUP_METHOD,
        "unassigned_rows_are_excluded": True,
        "title_placeholder_audit": report["title_placeholder_audit"],
        "raw_csvs_modified": False,
    }


def create_or_validate_multiplatform_split(
    project_root: str | Path,
    settings: dict[str, Any],
    overwrite: bool = False,
) -> dict[str, object]:
    """Create or exactly replay the pooled split and its two-source receipt."""
    root = Path(project_root)
    validate_multiplatform_experiment(settings)
    data_settings = settings["data"]
    split_settings = dict(settings["split"])
    split_settings.setdefault("seed", settings["seed"])
    data, report = load_multiplatform_data(root, data_settings)
    paths = {
        "train": root / data_settings["train_indices_path"],
        "test": root / data_settings["test_indices_path"],
        "excluded": root / data_settings["excluded_indices_path"],
        "manifest": root / data_settings["split_manifest_path"],
        "validation": root / data_settings["validation_report_path"],
    }
    split_files = [
        paths[key]
        for key in ("train", "test", "excluded", "manifest", "validation")
    ]
    if not overwrite and any(path.exists() for path in split_files):
        if not all(path.exists() for path in split_files):
            raise ValueError(
                "A partial pooled split exists. Re-run with --overwrite-split."
            )
        verify_multiplatform_split(root, settings, data=data, report=report)
        return json.loads(paths["manifest"].read_text(encoding="utf-8"))

    modelling, training_position, heldout_position, selected_fold, target_size = (
        deterministic_multiplatform_split(
            data,
            int(split_settings["heldout_folds"]),
            split_settings["heldout_fold"],
            int(split_settings["seed"]),
            tuple(split_settings.get("stratification_columns", ("platform",))),
        )
    )
    training = modelling.iloc[training_position].copy()
    heldout = modelling.iloc[heldout_position].copy()
    excluded = data.loc[data["label"].isna(), "row_index"].to_numpy(dtype=int)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        {"row_index": np.sort(training["row_index"].to_numpy(dtype=int))}
    ).to_csv(paths["train"], index=False)
    pd.DataFrame(
        {"row_index": np.sort(heldout["row_index"].to_numpy(dtype=int))}
    ).to_csv(paths["test"], index=False)
    pd.DataFrame({"row_index": np.sort(excluded)}).to_csv(
        paths["excluded"], index=False
    )
    manifest = _split_manifest_values(
        data,
        report,
        training,
        heldout,
        excluded,
        split_settings,
        selected_fold,
        target_size,
    )
    manifest.update(
        {
            "train_indices_sha256": file_sha256(paths["train"]),
            "test_indices_sha256": file_sha256(paths["test"]),
            "excluded_indices_sha256": file_sha256(paths["excluded"]),
        }
    )
    paths["manifest"].write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    paths["validation"].write_text(json.dumps(report, indent=2), encoding="utf-8")
    verify_multiplatform_split(root, settings, data=data, report=report)
    return manifest


def verify_multiplatform_split(
    project_root: str | Path,
    settings: dict[str, Any],
    data: pd.DataFrame | None = None,
    report: dict[str, object] | None = None,
) -> None:
    """Prove source bytes, split membership, ordering, and protocol replay."""
    root = Path(project_root)
    validate_multiplatform_experiment(settings)
    data_settings = settings["data"]
    split_settings = dict(settings["split"])
    split_settings.setdefault("seed", settings["seed"])
    if data is None or report is None:
        data, report = load_multiplatform_data(root, data_settings)
    paths = {
        "train": root / data_settings["train_indices_path"],
        "test": root / data_settings["test_indices_path"],
        "excluded": root / data_settings["excluded_indices_path"],
        "manifest": root / data_settings["split_manifest_path"],
        "validation": root / data_settings["validation_report_path"],
    }
    if not all(path.is_file() for path in paths.values()):
        raise FileNotFoundError("The frozen pooled split is incomplete.")
    train_indices = _read_indices(paths["train"])
    test_indices = _read_indices(paths["test"])
    excluded_indices = _read_indices(paths["excluded"])
    sets = [set(values) for values in (train_indices, test_indices, excluded_indices)]
    if any(
        sets[first] & sets[second]
        for first in range(3)
        for second in range(first + 1, 3)
    ):
        raise ValueError("Pooled training, held-out, and excluded rows overlap.")
    if set.union(*sets) != set(range(len(data))):
        raise ValueError("Pooled split indices do not cover both complete sources.")

    modelling, training_position, heldout_position, selected_fold, target_size = (
        deterministic_multiplatform_split(
            data,
            int(split_settings["heldout_folds"]),
            split_settings["heldout_fold"],
            int(split_settings["seed"]),
            tuple(split_settings.get("stratification_columns", ("platform",))),
        )
    )
    recreated_train = np.sort(
        modelling.iloc[training_position]["row_index"].to_numpy(dtype=int)
    )
    recreated_test = np.sort(
        modelling.iloc[heldout_position]["row_index"].to_numpy(dtype=int)
    )
    recreated_excluded = np.sort(
        data.loc[data["label"].isna(), "row_index"].to_numpy(dtype=int)
    )
    if not (
        np.array_equal(train_indices, recreated_train)
        and np.array_equal(test_indices, recreated_test)
        and np.array_equal(excluded_indices, recreated_excluded)
    ):
        raise ValueError("The frozen pooled split cannot be recreated exactly.")

    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    saved_report = json.loads(paths["validation"].read_text(encoding="utf-8"))
    if saved_report != report:
        raise ValueError("The pooled validation report is stale.")
    expected = _split_manifest_values(
        data,
        report,
        modelling.iloc[training_position],
        modelling.iloc[heldout_position],
        recreated_excluded,
        split_settings,
        selected_fold,
        target_size,
    )
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise ValueError(f"Pooled split manifest field {key} is stale.")
    for key, path in (
        ("train_indices_sha256", paths["train"]),
        ("test_indices_sha256", paths["test"]),
        ("excluded_indices_sha256", paths["excluded"]),
    ):
        if manifest.get(key) != file_sha256(path):
            raise ValueError(f"Pooled split index checksum is stale: {path}")


def load_multiplatform_saved_split(
    project_root: str | Path,
    settings: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load the exact pooled training and held-out frames plus full source view."""
    root = Path(project_root)
    validate_multiplatform_experiment(settings)
    data_settings = settings["data"]
    data, report = load_multiplatform_data(root, data_settings)
    verify_multiplatform_split(root, settings, data=data, report=report)
    train = _read_indices(root / data_settings["train_indices_path"])
    test = _read_indices(root / data_settings["test_indices_path"])
    training = data.iloc[train].copy().reset_index(drop=True)
    heldout = data.iloc[test].copy().reset_index(drop=True)
    for frame in (training, heldout):
        frame["label"] = pd.to_numeric(frame["label"]).astype(int)
    return training, heldout, data


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment_multiplatform.yaml")
    parser.add_argument("--overwrite-split", action="store_true")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    config_path = PROJECT_ROOT / arguments.config
    with config_path.open("r", encoding="utf-8") as file:
        settings = yaml.safe_load(file)
    if not is_multiplatform(settings):
        raise ValueError("The selected configuration is not multi-platform.")
    manifest = create_or_validate_multiplatform_split(
        PROJECT_ROOT,
        settings,
        overwrite=arguments.overwrite_split,
    )
    print(
        "Validated both immutable sources and frozen pooled split: "
        f"{manifest['training_rows']} training, {manifest['heldout_rows']} held "
        f"out, and {manifest['excluded_rows']} unassigned rows excluded."
    )


if __name__ == "__main__":
    main()
