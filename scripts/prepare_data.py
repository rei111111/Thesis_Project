"""Check the CSV runtime contract and create a reproducible stratified split.

The authors own annotation correctness. This module deliberately does not
recalculate labels from claim counts, repair rows, or detect/group repeated
transcripts. It checks only the contract required for the supervised code to
run safely and keeps the source CSV unchanged.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import train_test_split


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
MODEL_NUMERIC_COLUMNS = ("likes", "comments", "views", "duration_sec")


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require_usable_numeric_column(data: pd.DataFrame, column: str) -> None:
    values = pd.to_numeric(data[column], errors="coerce")
    if values.isna().any() or not np.isfinite(values.to_numpy(dtype=float)).all():
        raise ValueError(f"{column} contains a missing or non-numeric value.")
    if (values < 0).any():
        raise ValueError(f"{column} cannot contain negative values.")


def validate_dataset(
    data: pd.DataFrame,
    expected_rows: int | None = None,
) -> dict[str, object]:
    """Check only the schema and values needed by the model pipeline.

    `total_claims` and `false_claims` remain author annotation fields. They are
    intentionally neither recalculated nor compared with `label` here.
    """
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

    for column in MODEL_NUMERIC_COLUMNS:
        _require_usable_numeric_column(data, column)

    labels = pd.to_numeric(data["label"], errors="coerce")
    explicitly_supplied = data["label"].notna()
    invalid_numeric = explicitly_supplied & labels.isna()
    if invalid_numeric.any():
        rows = data.index[invalid_numeric].tolist()
        raise ValueError(f"Nonblank labels must be numeric at rows {rows}.")

    assigned = labels.notna()
    if assigned.any():
        assigned_values = labels.loc[assigned]
        if not np.allclose(assigned_values, np.floor(assigned_values)):
            raise ValueError("Assigned labels must be whole numbers.")
        if not set(assigned_values.astype(int)).issubset({1, 2, 3, 4}):
            raise ValueError("Assigned labels must be integers from 1 through 4.")

    model_data = data.loc[assigned].copy()
    model_data["label"] = labels.loc[assigned].astype(int)
    return {
        "source_rows": int(len(data)),
        "modelled_rows": int(assigned.sum()),
        "excluded_unassigned_rows": int((~assigned).sum()),
        "class_distribution": {
            str(key): int(value)
            for key, value in model_data["label"].value_counts().sort_index().items()
        },
        "source_columns": list(CSV_COLUMNS),
        "author_annotations_recalculated": False,
        "duplicate_content_handling": False,
        "derived_columns_written_to_source": [],
    }


def modelled_rows(data: pd.DataFrame) -> pd.DataFrame:
    """Return labelled rows with their stable original CSV row indices."""
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
    values = frame["row_index"].astype(int)
    if values.duplicated().any():
        raise ValueError(f"{path} repeats a row_index.")
    return set(values)


def _verify_saved_split(
    data: pd.DataFrame,
    train_path: Path,
    test_path: Path,
    excluded_path: Path,
    manifest_path: Path,
    dataset_sha256: str,
) -> dict[str, object]:
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
            "The CSV bytes changed after the split was saved. Review the author "
            "change and re-run with --overwrite-split."
        )
    if int(manifest.get("training_rows", -1)) != len(training):
        raise ValueError("The split manifest disagrees with train_indices.csv.")
    if int(manifest.get("heldout_rows", -1)) != len(heldout):
        raise ValueError("The split manifest disagrees with test_indices.csv.")
    return manifest


def create_or_validate_split(
    data: pd.DataFrame,
    train_indices_path: str | Path,
    test_indices_path: str | Path,
    excluded_indices_path: str | Path,
    manifest_path: str | Path,
    test_size: float,
    seed: int,
    dataset_sha256: str,
    overwrite: bool = False,
) -> dict[str, object]:
    """Create or verify an ordinary label-stratified held-out split."""
    if not 0.0 < test_size < 1.0:
        raise ValueError("test_size must be strictly between zero and one.")

    train_path = Path(train_indices_path)
    test_path = Path(test_indices_path)
    excluded_path = Path(excluded_indices_path)
    manifest_path = Path(manifest_path)
    split_paths = (train_path, test_path, excluded_path, manifest_path)
    if not overwrite and any(path.exists() for path in split_paths):
        return _verify_saved_split(
            data,
            train_path,
            test_path,
            excluded_path,
            manifest_path,
            dataset_sha256,
        )

    modelling = modelled_rows(data)
    training, heldout = train_test_split(
        modelling,
        test_size=test_size,
        random_state=seed,
        shuffle=True,
        stratify=modelling["label"],
    )
    excluded = data.index[data["label"].isna()].astype(int)

    for path in split_paths:
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
        "splitter": "train_test_split(stratified)",
        "test_size": float(test_size),
        "seed": int(seed),
        "unassigned_rows_are_excluded": True,
        "duplicate_content_handling": False,
    }
    manifest_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/dataset.csv")
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--overwrite-split", action="store_true")
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
        expected_rows=data_settings.get("expected_rows"),
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
        test_size=float(split_settings["test_size"]),
        seed=int(split_settings.get("seed", settings["seed"])),
        dataset_sha256=source_checksum,
        overwrite=arguments.overwrite_split,
    )
    if file_sha256(data_path) != source_checksum:
        raise RuntimeError("Preparation unexpectedly modified the source CSV.")
    print(
        f"Accepted {summary['source_rows']} source rows; "
        f"{split['modelled_rows']} labelled rows are split into "
        f"{split['training_rows']} training and {split['heldout_rows']} held-out "
        f"rows; {split['excluded_rows']} unassigned rows remain in the CSV."
    )


if __name__ == "__main__":
    main()
