"""Validate the source CSV and create a reproducible leakage-safe split."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import StratifiedGroupKFold

from features.content_groups import (
    content_group_ids,
    duplicate_group_count,
    validate_group_labels,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_COLUMNS = (
    "title",
    "transcript",
    "likes",
    "comments",
    "views",
    "duration_sec",
    "total_claims",
    "false_claims",
    "label",
)
INTEGER_COLUMNS = (
    "likes",
    "comments",
    "views",
    "duration_sec",
    "total_claims",
    "false_claims",
)


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def label_from_claims(total_claims: object, false_claims: object) -> np.ndarray:
    """Apply the thesis thresholds to videos with at least one claim."""
    total = np.asarray(total_claims, dtype=float)
    false = np.asarray(false_claims, dtype=float)
    if np.any(total < 1):
        raise ValueError("Assigned labels require at least one eligible claim.")
    if np.any(false < 0) or np.any(false > total):
        raise ValueError("false_claims must be between zero and total_claims.")
    supported_ratio = (total - false) / total
    return np.select(
        [
            supported_ratio >= 0.80,
            supported_ratio >= 0.60,
            supported_ratio >= 0.16,
        ],
        [1, 2, 3],
        default=4,
    ).astype(int)


def _require_nonnegative_integers(data: pd.DataFrame, column: str) -> None:
    values = pd.to_numeric(data[column], errors="coerce")
    if values.isna().any():
        raise ValueError(f"{column} contains a non-numeric or missing value.")
    if (values < 0).any():
        raise ValueError(f"{column} cannot contain negative values.")
    if not np.allclose(values, np.floor(values)):
        raise ValueError(f"{column} must contain whole numbers.")


def validate_dataset(
    data: pd.DataFrame,
    expected_rows: int | None = None,
    minimum_claims_for_assigned_label: int = 1,
    unassigned_allowed_below_claims: int = 2,
) -> dict[str, object]:
    """Validate exact schema, annotation fields, labels, and duplicate groups."""
    observed = tuple(data.columns)
    if observed != CSV_COLUMNS:
        missing = [column for column in CSV_COLUMNS if column not in observed]
        extra = [column for column in observed if column not in CSV_COLUMNS]
        raise ValueError(
            "CSV columns must exactly match the documented nine-column schema. "
            f"Missing: {missing}; extra: {extra}; order: {list(observed)}"
        )
    if expected_rows is not None and len(data) != expected_rows:
        raise ValueError(f"Expected {expected_rows} rows but found {len(data)}.")

    for column in ("title", "transcript"):
        values = data[column].fillna("").astype(str).str.strip()
        if values.eq("").any():
            rows = data.index[values.eq("")].tolist()
            raise ValueError(f"{column} is blank at zero-based rows {rows}.")

    for column in INTEGER_COLUMNS:
        _require_nonnegative_integers(data, column)
    if (data["false_claims"] > data["total_claims"]).any():
        raise ValueError("false_claims cannot exceed total_claims.")

    labels = pd.to_numeric(data["label"], errors="coerce")
    nonblank_label_text = data["label"].notna()
    invalid_numeric = nonblank_label_text & labels.isna()
    if invalid_numeric.any():
        raise ValueError("Nonblank labels must be numeric integers from 1 to 4.")
    assigned = labels.notna()
    if assigned.any():
        assigned_values = labels[assigned]
        if not np.allclose(assigned_values, np.floor(assigned_values)):
            raise ValueError("Assigned labels must be whole numbers.")
        if not set(assigned_values.astype(int)).issubset({1, 2, 3, 4}):
            raise ValueError("Assigned labels must be integers from 1 through 4.")

    invalid_assigned = assigned & (
        data["total_claims"] < minimum_claims_for_assigned_label
    )
    if invalid_assigned.any():
        rows = data.index[invalid_assigned].tolist()
        raise ValueError(
            "Assigned labels require at least one eligible claim; labels were "
            f"found at rows {rows}."
        )
    invalid_unassigned = ~assigned & (
        data["total_claims"] >= unassigned_allowed_below_claims
    )
    if invalid_unassigned.any():
        rows = data.index[invalid_unassigned].tolist()
        raise ValueError(f"Videos with sufficient claims are missing labels at {rows}.")

    calculated = label_from_claims(
        data.loc[assigned, "total_claims"],
        data.loc[assigned, "false_claims"],
    )
    stored = labels.loc[assigned].astype(int).to_numpy()
    mismatch_positions = np.flatnonzero(stored != calculated)
    if len(mismatch_positions):
        row_indices = data.index[assigned].to_numpy()[mismatch_positions].tolist()
        raise ValueError(
            "Stored labels disagree with claim counts at zero-based rows: "
            f"{row_indices}"
        )

    model_data = data.loc[assigned].copy()
    model_data["label"] = labels.loc[assigned].astype(int)
    validate_group_labels(model_data)
    return {
        "source_rows": int(len(data)),
        "modelled_rows": int(assigned.sum()),
        "excluded_unassigned_rows": int((~assigned).sum()),
        "class_distribution": {
            str(key): int(value)
            for key, value in model_data["label"].value_counts().sort_index().items()
        },
        "duplicate_transcript_groups": duplicate_group_count(data),
        "source_columns": list(CSV_COLUMNS),
        "derived_columns_written_to_source": [],
    }


def modelled_rows(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """Return labelled rows with stable original row indices."""
    eligible = data["label"].notna()
    result = data.loc[eligible].copy()
    result.insert(0, "row_index", data.index[eligible].astype(int))
    result["label"] = pd.to_numeric(result["label"]).astype(int)
    return result.reset_index(drop=True)


def _class_counts(data: pd.DataFrame) -> dict[str, int]:
    return {
        str(key): int(value)
        for key, value in data["label"].value_counts().sort_index().items()
    }


def _read_index_file(path: Path) -> set[int]:
    frame = pd.read_csv(path)
    if tuple(frame.columns) != ("row_index",):
        raise ValueError(f"{path} must contain only row_index.")
    return set(frame["row_index"].astype(int))


def _verify_saved_split(
    data: pd.DataFrame,
    train_path: Path,
    test_path: Path,
    excluded_path: Path,
    manifest_path: Path,
    dataset_sha256: str,
    heldout_folds: int,
    heldout_fold: int | str,
    seed: int,
) -> None:
    required = (train_path, test_path, excluded_path, manifest_path)
    if not all(path.exists() for path in required):
        raise ValueError(
            "A partial or legacy split was found. Re-run with --overwrite-split."
        )
    training = _read_index_file(train_path)
    heldout = _read_index_file(test_path)
    excluded = _read_index_file(excluded_path)
    if training & heldout or training & excluded or heldout & excluded:
        raise ValueError("Saved training, held-out, and excluded indices overlap.")
    if training | heldout | excluded != set(range(len(data))):
        raise ValueError("Saved index files do not cover the current source CSV.")
    expected_excluded = set(data.index[data["label"].isna()].astype(int))
    if excluded != expected_excluded:
        raise ValueError("Saved excluded indices do not match unassigned rows.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("dataset_sha256") != dataset_sha256:
        raise ValueError(
            "The CSV bytes changed after the split was frozen. Review the change "
            "and re-run with --overwrite-split if it is intentional."
        )
    expected_settings = {
        "heldout_folds": int(heldout_folds),
        "heldout_fold_setting": heldout_fold,
        "seed": int(seed),
    }
    observed_settings = {
        key: manifest.get(key) for key in expected_settings
    }
    if observed_settings != expected_settings:
        raise ValueError(
            "The frozen split settings differ from the active configuration. "
            f"Expected {expected_settings}; found {observed_settings}. "
            "Review the change and re-run with --overwrite-split."
        )
    for name, path in (
        ("train_indices_sha256", train_path),
        ("test_indices_sha256", test_path),
        ("excluded_indices_sha256", excluded_path),
    ):
        recorded = manifest.get(name)
        if recorded is not None and recorded != file_sha256(path):
            raise ValueError(f"{path} changed after the split manifest was written.")
    split_groups = {
        "training": set(content_group_ids(data.iloc[sorted(training)])),
        "heldout": set(content_group_ids(data.iloc[sorted(heldout)])),
    }
    if split_groups["training"] & split_groups["heldout"]:
        raise ValueError("Duplicate transcript content crosses the held-out split.")


def create_or_validate_split(
    data: pd.DataFrame,
    train_indices_path: str | Path,
    test_indices_path: str | Path,
    excluded_indices_path: str | Path,
    manifest_path: str | Path,
    heldout_folds: int,
    heldout_fold: int | str,
    seed: int,
    dataset_sha256: str,
    overwrite: bool = False,
) -> dict[str, object]:
    """Create or verify a grouped, stratified held-out fold."""
    train_path = Path(train_indices_path)
    test_path = Path(test_indices_path)
    excluded_path = Path(excluded_indices_path)
    manifest = Path(manifest_path)
    if not overwrite and any(
        path.exists() for path in (train_path, test_path, excluded_path, manifest)
    ):
        _verify_saved_split(
            data,
            train_path,
            test_path,
            excluded_path,
            manifest,
            dataset_sha256,
            heldout_folds,
            heldout_fold,
            seed,
        )
        return json.loads(manifest.read_text(encoding="utf-8"))

    modelling = modelled_rows(data)
    groups = content_group_ids(modelling)
    splitter = StratifiedGroupKFold(
        n_splits=heldout_folds,
        shuffle=True,
        random_state=seed,
    )
    splits = list(splitter.split(modelling, modelling["label"], groups))
    if isinstance(heldout_fold, str):
        if heldout_fold != "auto":
            raise ValueError("heldout_fold must be an integer or 'auto'.")
        target_size = int(math.ceil(len(modelling) / heldout_folds))
        overall = modelling["label"].value_counts(normalize=True)
        candidates: list[tuple[float, float, int]] = []
        for fold_index, (_, candidate_heldout) in enumerate(splits):
            candidate_labels = modelling.iloc[candidate_heldout]["label"]
            counts = candidate_labels.value_counts()
            distribution_error = float(
                sum(
                    abs(float(counts.get(label, 0)) - float(overall.get(label, 0)) * target_size)
                    for label in sorted(modelling["label"].unique())
                )
            )
            candidates.append(
                (
                    abs(len(candidate_heldout) - target_size),
                    distribution_error,
                    fold_index,
                )
            )
        selected_fold = min(candidates)[2]
    else:
        selected_fold = int(heldout_fold)
        target_size = int(math.ceil(len(modelling) / heldout_folds))
        if selected_fold < 0 or selected_fold >= len(splits):
            raise ValueError("heldout_fold is outside the available split range.")
    training_position, heldout_position = splits[selected_fold]
    training = modelling.iloc[training_position]
    heldout = modelling.iloc[heldout_position]
    excluded = data.index[data["label"].isna()].astype(int)

    if set(content_group_ids(training)) & set(content_group_ids(heldout)):
        raise RuntimeError("Grouped splitter allowed duplicate-content leakage.")

    for path in (train_path, test_path, excluded_path, manifest):
        path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        {"row_index": np.sort(training["row_index"].to_numpy(dtype=int))}
    ).to_csv(train_path, index=False)
    pd.DataFrame(
        {"row_index": np.sort(heldout["row_index"].to_numpy(dtype=int))}
    ).to_csv(test_path, index=False)
    pd.DataFrame({"row_index": np.sort(excluded.to_numpy(dtype=int))}).to_csv(
        excluded_path,
        index=False,
    )

    result = {
        "dataset_sha256": dataset_sha256,
        "source_rows": int(len(data)),
        "modelled_rows": int(len(modelling)),
        "excluded_rows": int(len(excluded)),
        "training_rows": int(len(training)),
        "heldout_rows": int(len(heldout)),
        "training_class_distribution": _class_counts(training),
        "heldout_class_distribution": _class_counts(heldout),
        "splitter": "StratifiedGroupKFold",
        "group_key": "sha256(normalized transcript)",
        "heldout_folds": int(heldout_folds),
        "heldout_fold": int(selected_fold),
        "heldout_fold_setting": heldout_fold,
        "heldout_target_rows": target_size,
        "heldout_fold_selection_rule": (
            "minimum absolute size error; then minimum class-distribution "
            "error; then lowest fold index"
            if heldout_fold == "auto"
            else "explicit fold index"
        ),
        "seed": int(seed),
        "unassigned_rows_are_excluded": True,
        "train_indices_sha256": file_sha256(train_path),
        "test_indices_sha256": file_sha256(test_path),
        "excluded_indices_sha256": file_sha256(excluded_path),
    }
    manifest.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.csv")
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--overwrite-split", action="store_true")
    parser.add_argument("--expected-rows", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    config_path = PROJECT_ROOT / arguments.config
    data_path = PROJECT_ROOT / arguments.data
    settings = load_yaml(config_path)
    data_settings = settings["data"]
    split_settings = settings["split"]

    source_checksum = file_sha256(data_path)
    data = pd.read_csv(data_path)
    summary = validate_dataset(
        data,
        expected_rows=(
            arguments.expected_rows
            if arguments.expected_rows is not None
            else data_settings.get("expected_rows")
        ),
        minimum_claims_for_assigned_label=int(
            data_settings["minimum_claims_for_assigned_label"]
        ),
        unassigned_allowed_below_claims=int(
            data_settings["unassigned_allowed_below_claims"]
        ),
    )
    summary["dataset_sha256"] = source_checksum
    report_path = PROJECT_ROOT / data_settings["validation_report_path"]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    split = create_or_validate_split(
        data=data,
        train_indices_path=PROJECT_ROOT / data_settings["train_indices_path"],
        test_indices_path=PROJECT_ROOT / data_settings["test_indices_path"],
        excluded_indices_path=PROJECT_ROOT
        / data_settings["excluded_indices_path"],
        manifest_path=PROJECT_ROOT / data_settings["split_manifest_path"],
        heldout_folds=int(split_settings["heldout_folds"]),
        heldout_fold=split_settings["heldout_fold"],
        seed=int(split_settings.get("seed", settings["seed"])),
        dataset_sha256=source_checksum,
        overwrite=arguments.overwrite_split,
    )
    if file_sha256(data_path) != source_checksum:
        raise RuntimeError("Preparation unexpectedly modified the source CSV.")
    print(
        f"Validated {summary['source_rows']} source rows; "
        f"{split['modelled_rows']} labelled rows are split into "
        f"{split['training_rows']} training and {split['heldout_rows']} held-out "
        f"rows; {split['excluded_rows']} unassigned rows are retained but excluded."
    )


if __name__ == "__main__":
    main()
