"""Final training, held-out prediction, and result persistence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold

from evaluation.metrics import calculate_metrics, quadratic_weighted_kappa
from evaluation.reproducibility import sha256_file
from features.content_groups import content_group_ids, validate_group_labels
from models.finetuned_bert import predict_bert, train_bert_model


def _load_indices(path: str | Path) -> np.ndarray:
    frame = pd.read_csv(path)
    if tuple(frame.columns) != ("row_index",):
        raise ValueError(f"{path} must contain only row_index.")
    values = frame["row_index"].astype(int).to_numpy()
    if len(values) != len(np.unique(values)):
        raise ValueError(f"{path} contains duplicate row indices.")
    return values


def load_saved_split(
    dataset_path: str | Path,
    train_indices_path: str | Path,
    test_indices_path: str | Path,
    excluded_indices_path: str | Path,
    split_manifest_path: str | Path | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Recover labelled rows while proving full 250-row source coverage."""
    data = pd.read_csv(dataset_path).reset_index(drop=True)
    data.insert(0, "row_index", np.arange(len(data), dtype=int))
    train_indices = _load_indices(train_indices_path)
    test_indices = _load_indices(test_indices_path)
    excluded_indices = _load_indices(excluded_indices_path)
    if split_manifest_path is not None:
        manifest = json.loads(Path(split_manifest_path).read_text(encoding="utf-8"))
        if manifest.get("dataset_sha256") != sha256_file(dataset_path):
            raise ValueError("Dataset bytes do not match the frozen split manifest.")
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
    if set(content_group_ids(training)) & set(content_group_ids(heldout)):
        raise ValueError("Duplicate transcript content crosses the held-out split.")
    return training, heldout


def fit_selected_estimator(
    estimator: Any,
    parameter_grid: dict[str, list[Any]],
    training_data: pd.DataFrame,
    target_column: str = "label",
    folds: int = 5,
    seed: int = 42,
    n_jobs: int = 1,
) -> tuple[Any, dict[str, Any]]:
    """Select parameters with grouped CV and refit on all training rows."""
    groups = content_group_ids(training_data)
    splitter = StratifiedGroupKFold(
        n_splits=folds,
        shuffle=True,
        random_state=seed,
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
    predictions = estimator.predict(heldout_data.drop(columns=[target_column]))
    return pd.DataFrame(
        {
            index_column: heldout_data[index_column].astype(int),
            "condition": condition_name,
            "true_label": heldout_data[target_column].astype(int),
            "prediction": np.asarray(predictions, dtype=int),
        }
    )


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
    aligned = heldout_data[["row_index", "label"]].merge(
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
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    predictions.to_csv(path, index=False)
    metrics = calculate_metrics(
        predictions["true_label"],
        predictions["prediction"],
    )
    metrics_path = path.parent.parent / "metrics" / f"{path.stem}.json"
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics
