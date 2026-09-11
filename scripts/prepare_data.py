"""Validate the source CSV and create a reproducible leakage-safe split."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any
import unicodedata

import numpy as np
import pandas as pd
import yaml
from sklearn.model_selection import StratifiedGroupKFold

from features.content_groups import (
    CONTENT_GROUP_METHOD,
    EXACT_CONTENT_GROUP_METHOD,
    NEAR_DUPLICATE_MINIMUM_LENGTH_RATIO,
    NEAR_DUPLICATE_MINIMUM_TOKENS,
    NEAR_DUPLICATE_MINIMUM_TOKEN_JACCARD,
    NEAR_DUPLICATE_SEQUENCE_THRESHOLD,
    content_group_ids,
    duplicate_group_count,
    exact_content_group_ids,
    exact_duplicate_group_count,
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
SOURCE_LINK_PATTERN = re.compile(r"^\s*(\d+)\s+(https?://\S+)\s*$")
YOUTUBE_SHORT_ID_PATTERN = re.compile(
    r"(?:youtube\.com/shorts/|youtu\.be/)([A-Za-z0-9_-]+)",
    flags=re.IGNORECASE,
)
EXACT_SPLIT_GROUPING = "exact_normalized_transcript_sha256"


def load_yaml(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def label_from_claims(
    total_claims: object,
    false_claims: object,
    minimum_claims: int = 2,
) -> np.ndarray:
    """Apply the exact thesis thresholds to label-eligible videos."""
    if minimum_claims < 1:
        raise ValueError("minimum_claims must be positive.")
    total_values = np.atleast_1d(np.asarray(total_claims, dtype=float))
    false_values = np.atleast_1d(np.asarray(false_claims, dtype=float))
    if total_values.shape != false_values.shape:
        raise ValueError("total_claims and false_claims must have equal shapes.")
    if not np.isfinite(total_values).all() or not np.isfinite(false_values).all():
        raise ValueError("Claim counts must be finite numbers.")
    if not np.equal(total_values, np.floor(total_values)).all() or not np.equal(
        false_values, np.floor(false_values)
    ).all():
        raise ValueError("Claim counts must be whole numbers.")
    total = total_values.astype(np.int64)
    false = false_values.astype(np.int64)
    if np.any(total < minimum_claims):
        raise ValueError(
            f"Assigned labels require at least {minimum_claims} eligible claims."
        )
    if np.any(false < 0) or np.any(false > total):
        raise ValueError("false_claims must be between zero and total_claims.")
    supported = total - false
    return np.select(
        [
            5 * supported >= 4 * total,
            5 * supported >= 3 * total,
            25 * supported >= 4 * total,
        ],
        [1, 2, 3],
        default=4,
    ).astype(int)


def _require_nonnegative_integers(
    data: pd.DataFrame,
    column: str,
) -> pd.Series:
    values = pd.to_numeric(data[column], errors="coerce")
    if values.isna().any() or not np.isfinite(values.to_numpy(dtype=float)).all():
        raise ValueError(f"{column} contains a non-numeric or missing value.")
    if (values < 0).any():
        raise ValueError(f"{column} cannot contain negative values.")
    if not np.equal(values.to_numpy(dtype=float), np.floor(values)).all():
        raise ValueError(f"{column} must contain whole numbers.")
    return values.astype(np.int64)


def audit_source_links(
    path: str | Path,
    expected_rows: int | None = None,
) -> dict[str, object]:
    """Audit the collection list without silently altering the study sample."""
    source = Path(path)
    if not source.exists():
        raise FileNotFoundError(f"Source-link list is missing: {source}")
    records: list[tuple[int, str, str]] = []
    invalid_lines: list[int] = []
    for line_number, raw_line in enumerate(
        source.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        if not raw_line.strip():
            continue
        match = SOURCE_LINK_PATTERN.fullmatch(raw_line)
        if match is None:
            invalid_lines.append(line_number)
            continue
        ordinal = int(match.group(1))
        url = match.group(2).rstrip("/")
        video_match = YOUTUBE_SHORT_ID_PATTERN.search(url)
        source_id = video_match.group(1) if video_match else url.casefold()
        records.append((ordinal, url, source_id))
    ordinals = [record[0] for record in records]
    expected_ordinals = list(range(1, len(records) + 1))
    if invalid_lines or ordinals != expected_ordinals:
        raise ValueError(
            "Source-link list must contain consecutively numbered '<row> <URL>' "
            f"records. Invalid lines: {invalid_lines}."
        )
    if expected_rows is not None and len(records) != int(expected_rows):
        raise ValueError(
            f"Source-link list has {len(records)} records; expected {expected_rows}."
        )
    counts = Counter(record[2] for record in records)
    duplicated_ids = sorted(key for key, count in counts.items() if count > 1)
    duplicate_groups = [
        {
            "source_id": source_id,
            "zero_based_rows": [
                ordinal - 1
                for ordinal, _, observed_id in records
                if observed_id == source_id
            ],
            "urls": sorted(
                {
                    url
                    for _, url, observed_id in records
                    if observed_id == source_id
                }
            ),
        }
        for source_id in duplicated_ids
    ]
    return {
        "audit_completed": True,
        "record_count": len(records),
        "unique_source_id_count": len(counts),
        "duplicate_source_id_count": len(duplicate_groups),
        "duplicate_source_groups": duplicate_groups,
        "has_duplicate_source_ids": bool(duplicate_groups),
        "warnings": (
            [
                "Duplicate source video IDs were detected. Review the "
                "author-controlled source list; execution is not blocked."
            ]
            if duplicate_groups
            else []
        ),
    }


def predominantly_non_latin_rows(
    values: pd.Series,
    minimum_latin_fraction: float = 0.80,
) -> list[int]:
    """Flag transcripts requiring manual English-language eligibility review."""
    if not 0 <= minimum_latin_fraction <= 1:
        raise ValueError("minimum_latin_fraction must be between zero and one.")
    flagged: list[int] = []
    for row_index, value in values.items():
        letters = [character for character in str(value) if character.isalpha()]
        latin = [
            character
            for character in letters
            if "LATIN" in unicodedata.name(character, "")
        ]
        fraction = len(latin) / len(letters) if letters else 0.0
        if fraction < minimum_latin_fraction:
            flagged.append(int(row_index))
    return flagged


def validate_dataset(
    data: pd.DataFrame,
    expected_rows: int | None = None,
    minimum_claims_for_assigned_label: int = 2,
    unassigned_allowed_below_claims: int = 2,
    maximum_duration_seconds: int | None = 180,
    minimum_latin_letter_fraction_for_review: float = 0.80,
    required_text_columns: tuple[str, ...] = ("title", "transcript"),
) -> dict[str, object]:
    """Validate exact schema, annotation fields, labels, and duplicate groups."""
    if minimum_claims_for_assigned_label < 1:
        raise ValueError("minimum_claims_for_assigned_label must be positive.")
    if unassigned_allowed_below_claims < 1:
        raise ValueError("unassigned_allowed_below_claims must be positive.")
    if minimum_claims_for_assigned_label != unassigned_allowed_below_claims:
        raise ValueError(
            "The assigned-label and unassigned-label claim thresholds must "
            "match so every row has exactly one valid annotation state."
        )
    if maximum_duration_seconds is not None and maximum_duration_seconds < 1:
        raise ValueError("maximum_duration_seconds must be positive when set.")
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

    for column in required_text_columns:
        values = data[column].fillna("").astype(str).str.strip()
        if values.eq("").any():
            rows = data.index[values.eq("")].tolist()
            raise ValueError(f"{column} is blank at zero-based rows {rows}.")

    numeric = {
        column: _require_nonnegative_integers(data, column)
        for column in INTEGER_COLUMNS
    }
    if (numeric["duration_sec"] < 1).any():
        raise ValueError("duration_sec must be at least one second.")
    if (numeric["false_claims"] > numeric["total_claims"]).any():
        raise ValueError("false_claims cannot exceed total_claims.")
    if maximum_duration_seconds is not None:
        excessive_duration = numeric["duration_sec"] > maximum_duration_seconds
        if excessive_duration.any():
            rows = data.index[excessive_duration].tolist()
            raise ValueError(
                f"duration_sec exceeds the {maximum_duration_seconds}-second "
                f"inclusion limit at zero-based rows {rows}."
            )

    labels = pd.to_numeric(data["label"], errors="coerce")
    nonblank_label_text = data["label"].notna()
    invalid_numeric = nonblank_label_text & labels.isna()
    if invalid_numeric.any():
        raise ValueError("Nonblank labels must be numeric integers from 1 to 4.")
    assigned = labels.notna()
    if assigned.any():
        assigned_values = labels[assigned]
        if not np.isfinite(assigned_values.to_numpy(dtype=float)).all():
            raise ValueError("Assigned labels must be finite integers from 1 to 4.")
        if not np.equal(
            assigned_values.to_numpy(dtype=float),
            np.floor(assigned_values.to_numpy(dtype=float)),
        ).all():
            raise ValueError("Assigned labels must be whole numbers.")
        if not set(assigned_values.astype(int)).issubset({1, 2, 3, 4}):
            raise ValueError("Assigned labels must be integers from 1 through 4.")

    invalid_assigned = assigned & (
        numeric["total_claims"] < minimum_claims_for_assigned_label
    )
    if invalid_assigned.any():
        rows = data.index[invalid_assigned].tolist()
        raise ValueError(
            "Assigned labels require at least "
            f"{minimum_claims_for_assigned_label} eligible claims; labels "
            f"were found at rows {rows}."
        )
    invalid_unassigned = ~assigned & (
        numeric["total_claims"] >= unassigned_allowed_below_claims
    )
    if invalid_unassigned.any():
        rows = data.index[invalid_unassigned].tolist()
        raise ValueError(f"Videos with sufficient claims are missing labels at {rows}.")

    calculated = label_from_claims(
        numeric["total_claims"].loc[assigned],
        numeric["false_claims"].loc[assigned],
        minimum_claims=minimum_claims_for_assigned_label,
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
        "exact_duplicate_transcript_groups": exact_duplicate_group_count(data),
        "duplicate_or_near_duplicate_content_groups": duplicate_group_count(data),
        "content_group_method": CONTENT_GROUP_METHOD,
        "transcript_language_warnings": {
            "criterion": (
                "transcript Latin-letter fraction below "
                f"{minimum_latin_letter_fraction_for_review:.2f}"
            ),
            "zero_based_rows": predominantly_non_latin_rows(
                data["transcript"],
                minimum_latin_letter_fraction_for_review,
            ),
            "advisory_only": True,
            "message": (
                "Review flagged transcripts manually. This automated script "
                "warning does not determine eligibility or block execution."
            ),
        },
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


def deterministic_split(
    data: pd.DataFrame,
    heldout_folds: int,
    heldout_fold: int | str,
    seed: int,
) -> tuple[pd.DataFrame, np.ndarray, np.ndarray, int, int]:
    """Recreate the declared exact-group split and apply the stricter audit."""
    if isinstance(heldout_folds, bool) or int(heldout_folds) < 2:
        raise ValueError("heldout_folds must be an integer of at least two.")
    heldout_folds = int(heldout_folds)
    modelling = modelled_rows(data)
    generation_groups = exact_content_group_ids(modelling)
    # Calculate audit components on the complete source population. An
    # excluded claim-sparse row can otherwise hide a transitive similarity
    # connection between two labelled rows.
    all_audit_groups = content_group_ids(data)
    audit_groups = all_audit_groups[
        modelling["row_index"].to_numpy(dtype=int)
    ]
    splitter = StratifiedGroupKFold(
        n_splits=heldout_folds,
        shuffle=True,
        random_state=int(seed),
    )
    splits = list(
        splitter.split(modelling, modelling["label"], generation_groups)
    )
    target_size = int(math.ceil(len(modelling) / heldout_folds))
    if isinstance(heldout_fold, str):
        if heldout_fold != "auto":
            raise ValueError("heldout_fold must be an integer or 'auto'.")
        overall = modelling["label"].value_counts(normalize=True)
        candidates: list[tuple[float, float, int]] = []
        for fold_index, (candidate_training, candidate_heldout) in enumerate(splits):
            if set(audit_groups[candidate_training]) & set(
                audit_groups[candidate_heldout]
            ):
                continue
            candidate_labels = modelling.iloc[candidate_heldout]["label"]
            counts = candidate_labels.value_counts()
            distribution_error = float(
                sum(
                    abs(
                        float(counts.get(label, 0))
                        - float(overall.get(label, 0)) * target_size
                    )
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
        if not candidates:
            raise ValueError(
                "No generated fold keeps every exact or near-duplicate group "
                "within a single partition. A new split protocol is required."
            )
        selected_fold = min(candidates)[2]
    else:
        if isinstance(heldout_fold, bool):
            raise ValueError("heldout_fold must be an integer or 'auto'.")
        selected_fold = int(heldout_fold)
        if selected_fold < 0 or selected_fold >= len(splits):
            raise ValueError("heldout_fold is outside the available split range.")
    training_position, heldout_position = splits[selected_fold]
    if set(audit_groups[training_position]) & set(audit_groups[heldout_position]):
        raise ValueError(
            "Selected split crosses an exact or near-duplicate content group."
        )
    return (
        modelling,
        training_position,
        heldout_position,
        selected_fold,
        target_size,
    )


def _read_index_file(path: Path) -> set[int]:
    frame = pd.read_csv(path)
    if tuple(frame.columns) != ("row_index",):
        raise ValueError(f"{path} must contain only row_index.")
    numeric = pd.to_numeric(frame["row_index"], errors="coerce")
    if (
        numeric.isna().any()
        or not np.isfinite(numeric.to_numpy(dtype=float)).all()
        or not np.equal(numeric, np.floor(numeric)).all()
    ):
        raise ValueError(f"{path} must contain integer row indices.")
    values = numeric.astype(int)
    if values.duplicated().any():
        raise ValueError(f"{path} contains duplicate row indices.")
    if values.tolist() != sorted(values.tolist()):
        raise ValueError(
            f"{path} row indices must be strictly increasing so model and CV "
            "order is reproducible."
        )
    return set(values)


def verify_saved_split(
    data: pd.DataFrame,
    train_path: Path,
    test_path: Path,
    excluded_path: Path,
    manifest_path: Path,
    dataset_sha256: str,
    heldout_folds: int,
    heldout_fold: int | str,
    seed: int,
    minimum_claims_for_assigned_label: int,
    unassigned_allowed_below_claims: int,
    maximum_duration_seconds: int | None,
    generation_grouping: str,
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
    (
        recreated_modelling,
        recreated_training_position,
        recreated_heldout_position,
        recreated_fold,
        recreated_target_size,
    ) = deterministic_split(data, heldout_folds, heldout_fold, seed)
    recreated_training = set(
        recreated_modelling.iloc[recreated_training_position]["row_index"].astype(int)
    )
    recreated_heldout = set(
        recreated_modelling.iloc[recreated_heldout_position]["row_index"].astype(int)
    )
    if training != recreated_training or heldout != recreated_heldout:
        raise ValueError(
            "Saved row assignments cannot be recreated from the declared "
            "splitter, grouping method, fold rule, and seed."
        )
    selection_rule = (
        "minimum absolute size error; then minimum class-distribution "
        "error; then lowest fold index"
        if heldout_fold == "auto"
        else "explicit fold index"
    )
    expected_settings = {
        "splitter": "StratifiedGroupKFold",
        "heldout_folds": int(heldout_folds),
        "heldout_fold": int(recreated_fold),
        "heldout_fold_setting": heldout_fold,
        "heldout_target_rows": int(recreated_target_size),
        "heldout_fold_selection_rule": selection_rule,
        "seed": int(seed),
        "unassigned_rows_are_excluded": True,
        "minimum_claims_for_assigned_label": int(
            minimum_claims_for_assigned_label
        ),
        "unassigned_allowed_below_claims": int(unassigned_allowed_below_claims),
        "maximum_duration_seconds": (
            int(maximum_duration_seconds)
            if maximum_duration_seconds is not None
            else None
        ),
        "split_generation_grouping": generation_grouping,
        "split_generation_group_method": EXACT_CONTENT_GROUP_METHOD,
        "leakage_audit_group_method": CONTENT_GROUP_METHOD,
        "near_duplicate_sequence_threshold": NEAR_DUPLICATE_SEQUENCE_THRESHOLD,
        "near_duplicate_minimum_tokens": NEAR_DUPLICATE_MINIMUM_TOKENS,
        "near_duplicate_minimum_length_ratio": (
            NEAR_DUPLICATE_MINIMUM_LENGTH_RATIO
        ),
        "near_duplicate_minimum_token_jaccard": (
            NEAR_DUPLICATE_MINIMUM_TOKEN_JACCARD
        ),
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
        if recorded != file_sha256(path):
            raise ValueError(f"{path} changed after the split manifest was written.")
    all_groups = content_group_ids(data)
    split_groups = {
        "training": set(all_groups[np.asarray(sorted(training), dtype=int)]),
        "heldout": set(all_groups[np.asarray(sorted(heldout), dtype=int)]),
    }
    if split_groups["training"] & split_groups["heldout"]:
        raise ValueError(
            "Exact or near-duplicate transcript content crosses the held-out split."
        )

    labelled = data.loc[data["label"].notna()].copy()
    labelled["label"] = pd.to_numeric(labelled["label"]).astype(int)
    training_data = data.iloc[sorted(training)].copy()
    heldout_data = data.iloc[sorted(heldout)].copy()
    for frame in (training_data, heldout_data):
        frame["label"] = pd.to_numeric(frame["label"]).astype(int)
    expected_counts = {
        "source_rows": int(len(data)),
        "modelled_rows": int(len(labelled)),
        "excluded_rows": int(len(excluded)),
        "training_rows": int(len(training_data)),
        "heldout_rows": int(len(heldout_data)),
        "training_class_distribution": _class_counts(training_data),
        "heldout_class_distribution": _class_counts(heldout_data),
    }
    observed_counts = {key: manifest.get(key) for key in expected_counts}
    if observed_counts != expected_counts:
        raise ValueError(
            "The frozen split manifest counts do not match its index files. "
            f"Expected {expected_counts}; found {observed_counts}."
        )


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
    minimum_claims_for_assigned_label: int = 2,
    unassigned_allowed_below_claims: int = 2,
    maximum_duration_seconds: int | None = 180,
    generation_grouping: str = EXACT_SPLIT_GROUPING,
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
        verify_saved_split(
            data,
            train_path,
            test_path,
            excluded_path,
            manifest,
            dataset_sha256,
            heldout_folds,
            heldout_fold,
            seed,
            minimum_claims_for_assigned_label,
            unassigned_allowed_below_claims,
            maximum_duration_seconds,
            generation_grouping,
        )
        return json.loads(manifest.read_text(encoding="utf-8"))

    if generation_grouping != EXACT_SPLIT_GROUPING:
        raise ValueError(
            "The frozen thesis split requires generation_grouping="
            f"'{EXACT_SPLIT_GROUPING}'."
        )
    (
        modelling,
        training_position,
        heldout_position,
        selected_fold,
        target_size,
    ) = deterministic_split(data, heldout_folds, heldout_fold, seed)
    training = modelling.iloc[training_position]
    heldout = modelling.iloc[heldout_position]
    excluded = data.index[data["label"].isna()].astype(int)

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
        "split_generation_grouping": generation_grouping,
        "split_generation_group_method": EXACT_CONTENT_GROUP_METHOD,
        "leakage_audit_group_method": CONTENT_GROUP_METHOD,
        "near_duplicate_sequence_threshold": (
            NEAR_DUPLICATE_SEQUENCE_THRESHOLD
        ),
        "near_duplicate_minimum_tokens": NEAR_DUPLICATE_MINIMUM_TOKENS,
        "near_duplicate_minimum_length_ratio": (
            NEAR_DUPLICATE_MINIMUM_LENGTH_RATIO
        ),
        "near_duplicate_minimum_token_jaccard": (
            NEAR_DUPLICATE_MINIMUM_TOKEN_JACCARD
        ),
        "minimum_claims_for_assigned_label": int(
            minimum_claims_for_assigned_label
        ),
        "unassigned_allowed_below_claims": int(unassigned_allowed_below_claims),
        "maximum_duration_seconds": (
            int(maximum_duration_seconds)
            if maximum_duration_seconds is not None
            else None
        ),
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
    source_links_path = PROJECT_ROOT / data_settings["source_links_path"]
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
        maximum_duration_seconds=(
            int(data_settings["maximum_duration_seconds"])
            if data_settings.get("maximum_duration_seconds") is not None
            else None
        ),
        minimum_latin_letter_fraction_for_review=float(
            data_settings.get("minimum_latin_letter_fraction_for_review", 0.80)
        ),
    )
    summary["dataset_sha256"] = source_checksum
    source_links_checksum: str | None = None
    try:
        if source_links_path.is_file():
            source_links_checksum = file_sha256(source_links_path)
        summary["source_link_audit"] = audit_source_links(
            source_links_path,
            expected_rows=len(data),
        )
    except (OSError, ValueError) as error:
        summary["source_link_audit"] = {
            "audit_completed": False,
            "warnings": [
                f"Source-link audit could not be completed: {error}. "
                "Review the author-controlled source list; execution is not blocked."
            ],
        }
    summary["source_links_sha256"] = source_links_checksum
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
        minimum_claims_for_assigned_label=int(
            data_settings["minimum_claims_for_assigned_label"]
        ),
        unassigned_allowed_below_claims=int(
            data_settings["unassigned_allowed_below_claims"]
        ),
        maximum_duration_seconds=(
            int(data_settings["maximum_duration_seconds"])
            if data_settings.get("maximum_duration_seconds") is not None
            else None
        ),
        generation_grouping=str(split_settings["generation_grouping"]),
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
    for warning in summary["source_link_audit"].get("warnings", []):
        print(f"WARNING: {warning}")
    flagged_rows = summary["transcript_language_warnings"]["zero_based_rows"]
    if flagged_rows:
        print(
            "WARNING: transcripts at zero-based rows "
            f"{flagged_rows} triggered the advisory script/language check. "
            "Review them manually; execution is not blocked."
        )


if __name__ == "__main__":
    main()
