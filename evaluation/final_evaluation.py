"""Final training, held-out prediction, and result persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV

from evaluation.metrics import (
    calculate_metrics,
    quadratic_weighted_kappa,
    validate_label_array,
)
from evaluation.reproducibility import sha256_file
from evaluation.stratification import StratifiedGroupKFoldByColumns
from features.content_groups import (
    CONTENT_GROUP_METHOD,
    EXACT_CONTENT_GROUP_METHOD,
    content_group_ids,
    validate_group_labels,
)
from models.finetuned_bert import predict_bert, train_bert_model
from scripts.prepare_data import (
    EXACT_SPLIT_GROUPING,
    file_sha256,
    validate_dataset,
    verify_saved_split,
)


def _load_indices(path: str | Path) -> np.ndarray:
    frame = pd.read_csv(path)
    if tuple(frame.columns) != ("row_index",):
        raise ValueError(f"{path} must contain only row_index.")
    numeric = pd.to_numeric(frame["row_index"], errors="coerce")
    if numeric.isna().any() or not np.isfinite(numeric.to_numpy(dtype=float)).all():
        raise ValueError(f"{path} contains a missing or non-finite row index.")
    if not np.equal(numeric.to_numpy(dtype=float), np.floor(numeric)).all():
        raise ValueError(f"{path} must contain integer row indices.")
    values = numeric.astype(int).to_numpy()
    if len(values) != len(np.unique(values)):
        raise ValueError(f"{path} contains duplicate row indices.")
    if not np.array_equal(values, np.sort(values)):
        raise ValueError(
            f"{path} row indices must be strictly increasing so model and CV "
            "order is reproducible."
        )
    return values


def load_saved_split(
    dataset_path: str | Path,
    train_indices_path: str | Path,
    test_indices_path: str | Path,
    excluded_indices_path: str | Path,
    split_manifest_path: str | Path | None = None,
    split_settings: dict[str, Any] | None = None,
    data_contract: dict[str, Any] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Recover labelled rows while proving full 250-row source coverage."""
    source = pd.read_csv(dataset_path).reset_index(drop=True)
    manifest: dict[str, Any] | None = None
    if split_manifest_path is not None:
        manifest = json.loads(Path(split_manifest_path).read_text(encoding="utf-8"))
    expected_rows = (
        data_contract.get("expected_rows")
        if data_contract is not None
        else manifest.get("source_rows") if manifest is not None else None
    )
    minimum_claims = int(
        data_contract.get("minimum_claims_for_assigned_label", 2)
        if data_contract is not None
        else manifest.get("minimum_claims_for_assigned_label", 2)
        if manifest is not None
        else 2
    )
    unassigned_threshold = int(
        data_contract.get("unassigned_allowed_below_claims", 2)
        if data_contract is not None
        else manifest.get("unassigned_allowed_below_claims", 2)
        if manifest is not None
        else 2
    )
    maximum_duration = (
        data_contract.get("maximum_duration_seconds", 180)
        if data_contract is not None
        else manifest.get("maximum_duration_seconds", 180)
        if manifest is not None
        else 180
    )
    validate_dataset(
        source,
        expected_rows=int(expected_rows) if expected_rows is not None else None,
        minimum_claims_for_assigned_label=minimum_claims,
        unassigned_allowed_below_claims=unassigned_threshold,
        maximum_duration_seconds=maximum_duration,
    )
    if manifest is not None:
        active_split = split_settings or {
            "heldout_folds": manifest.get("heldout_folds"),
            "heldout_fold": manifest.get("heldout_fold_setting"),
            "seed": manifest.get("seed"),
            "generation_grouping": manifest.get("split_generation_grouping"),
        }
        verify_saved_split(
            source,
            Path(train_indices_path),
            Path(test_indices_path),
            Path(excluded_indices_path),
            Path(split_manifest_path),
            file_sha256(dataset_path),
            int(active_split["heldout_folds"]),
            active_split["heldout_fold"],
            int(active_split["seed"]),
            minimum_claims,
            unassigned_threshold,
            maximum_duration,
            str(active_split.get("generation_grouping", EXACT_SPLIT_GROUPING)),
        )
    data = source.copy()
    data.insert(0, "row_index", np.arange(len(data), dtype=int))
    train_indices = _load_indices(train_indices_path)
    test_indices = _load_indices(test_indices_path)
    excluded_indices = _load_indices(excluded_indices_path)
    if manifest is not None:
        if manifest.get("dataset_sha256") != sha256_file(dataset_path):
            raise ValueError("Dataset bytes do not match the frozen split manifest.")
        if manifest.get("split_generation_group_method") != EXACT_CONTENT_GROUP_METHOD:
            raise ValueError(
                "The split manifest does not honestly identify the original "
                "exact-transcript generation protocol."
            )
        if manifest.get("split_generation_grouping") != EXACT_SPLIT_GROUPING:
            raise ValueError("The split manifest uses an unknown generation grouping.")
        if manifest.get("leakage_audit_group_method") != CONTENT_GROUP_METHOD:
            raise ValueError(
                "The split manifest uses a different duplicate-content "
                "leakage-audit protocol."
            )
        for key, path in (
            ("train_indices_sha256", train_indices_path),
            ("test_indices_sha256", test_indices_path),
            ("excluded_indices_sha256", excluded_indices_path),
        ):
            recorded = manifest.get(key)
            if recorded is not None and recorded != sha256_file(path):
                raise ValueError(f"{path} does not match the frozen split manifest.")
    split_sets = [set(values) for values in (train_indices, test_indices, excluded_indices)]
    if any(
        split_sets[first] & split_sets[second]
        for first in range(3)
        for second in range(first + 1, 3)
    ):
        raise ValueError("Training, held-out, and excluded row indices overlap.")
    if set.union(*split_sets) != set(range(len(data))):
        raise ValueError("Saved index files do not cover the complete source CSV.")

    expected_excluded = set(
        data.loc[data["label"].isna(), "row_index"].astype(int)
    )
    if split_sets[2] != expected_excluded:
        raise ValueError("Excluded rows do not match the unassigned source rows.")

    training = data.iloc[train_indices].reset_index(drop=True)
    heldout = data.iloc[test_indices].reset_index(drop=True)
    for frame in (training, heldout):
        if frame["label"].isna().any():
            raise ValueError("Supervised split contains an unassigned label.")
        frame["label"] = pd.to_numeric(frame["label"]).astype(int)
        validate_group_labels(frame)
    all_groups = content_group_ids(data)
    if set(all_groups[train_indices]) & set(all_groups[test_indices]):
        raise ValueError(
            "Exact or near-duplicate transcript content crosses the held-out split."
        )

    if manifest is not None:
        def class_counts(frame: pd.DataFrame) -> dict[str, int]:
            return {
                str(key): int(value)
                for key, value in frame["label"]
                .value_counts()
                .sort_index()
                .items()
            }

        expected_manifest_values: dict[str, object] = {
            "source_rows": len(data),
            "modelled_rows": len(training) + len(heldout),
            "excluded_rows": len(excluded_indices),
            "training_rows": len(training),
            "heldout_rows": len(heldout),
            "training_class_distribution": class_counts(training),
            "heldout_class_distribution": class_counts(heldout),
        }
        observed_manifest_values = {
            key: manifest.get(key) for key in expected_manifest_values
        }
        if observed_manifest_values != expected_manifest_values:
            raise ValueError(
                "Split-manifest counts or class distributions do not match "
                "the frozen index files."
            )
    return training, heldout


def fit_selected_estimator(
    estimator: Any,
    parameter_grid: dict[str, list[Any]],
    training_data: pd.DataFrame,
    target_column: str = "label",
    folds: int = 5,
    seed: int = 42,
    n_jobs: int = 1,
    stratification_columns: tuple[str, ...] = (),
) -> tuple[Any, dict[str, Any]]:
    """Select parameters with grouped CV and refit on all training rows."""
    groups = content_group_ids(training_data)
    splitter = StratifiedGroupKFoldByColumns(
        n_splits=folds,
        shuffle=True,
        random_state=seed,
        stratification_columns=stratification_columns,
    )
    search = GridSearchCV(
        estimator=clone(estimator),
        param_grid=parameter_grid,
        scoring=make_scorer(quadratic_weighted_kappa),
        cv=splitter,
        refit=True,
        n_jobs=n_jobs,
        error_score="raise",
    )
    search.fit(
        training_data.drop(columns=[target_column]),
        training_data[target_column],
        groups=groups,
    )
    return search.best_estimator_, dict(search.best_params_)


def predict_selected_estimator(
    estimator: Any,
    heldout_data: pd.DataFrame,
    condition_name: str,
    index_column: str = "row_index",
    target_column: str = "label",
) -> pd.DataFrame:
    """Create the common held-out prediction format."""
    predictions = validate_label_array(
        estimator.predict(heldout_data.drop(columns=[target_column])),
        f"{condition_name} held-out predictions",
    )
    if len(predictions) != len(heldout_data):
        raise ValueError(f"{condition_name} did not predict every held-out row.")
    result = pd.DataFrame(
        {
            index_column: heldout_data[index_column].astype(int),
            "condition": condition_name,
            "true_label": heldout_data[target_column].astype(int),
            "prediction": np.asarray(predictions, dtype=int),
        }
    )
    for identity_column in ("record_id", "platform"):
        if identity_column in heldout_data.columns:
            result[identity_column] = heldout_data[identity_column].astype(str)
    return result


def fit_final_bert(
    training_data: pd.DataFrame,
    heldout_data: pd.DataFrame,
    settings: dict[str, Any],
    outer_best_epochs: list[int],
    output_directory: str | Path | None = None,
    device: str | None = None,
) -> pd.DataFrame:
    """Train BERT for the median selected epoch and predict held-out rows."""
    if not outer_best_epochs:
        raise ValueError("Outer-fold BERT epochs are required for final training.")
    final_epochs = max(1, int(np.median(outer_best_epochs)))
    result = train_bert_model(
        train_data=training_data,
        validation_data=None,
        settings=settings,
        fixed_epochs=final_epochs,
        output_directory=output_directory,
        device=device,
    )
    predictions = predict_bert(result, heldout_data, device=device)
    identity_columns = [
        column
        for column in ("row_index", "record_id", "platform", "label")
        if column in heldout_data.columns
    ]
    aligned = heldout_data[identity_columns].merge(
        predictions,
        on="row_index",
        validate="one_to_one",
    )
    aligned.insert(1, "condition", "E_FINETUNED_BERT")
    return aligned.rename(columns={"label": "true_label"})


def save_heldout_predictions(
    predictions: pd.DataFrame,
    output_path: str | Path,
) -> dict[str, object]:
    """Save predictions before calculating and saving aggregate metrics."""
    required = {"row_index", "condition", "true_label", "prediction"}
    if not required.issubset(predictions.columns):
        raise ValueError("Held-out predictions are missing required columns.")
    if predictions["row_index"].duplicated().any():
        raise ValueError("Held-out predictions repeat row indices.")
    metrics = calculate_metrics(
        predictions["true_label"],
        predictions["prediction"],
    )
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    predictions.to_csv(path, index=False)
    metrics_path = path.parent.parent / "metrics" / f"{path.stem}.json"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics
