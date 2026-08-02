"""Stratified cross-validation for Ridge, frozen MiniLM, and BERT."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import make_scorer
from sklearn.model_selection import (
    GridSearchCV,
    StratifiedKFold,
    StratifiedShuffleSplit,
)

from evaluation.metrics import calculate_metrics, quadratic_weighted_kappa
from models.finetuned_bert import predict_bert, train_bert_model


@dataclass
class CrossValidationResult:
    fold_metrics: pd.DataFrame
    predictions: pd.DataFrame
    best_parameters: list[dict[str, Any]] = field(default_factory=list)
    best_epochs: list[int] = field(default_factory=list)


def _check_fold_counts(labels: pd.Series, folds: int, context: str) -> None:
    minimum = int(labels.value_counts().min())
    if minimum < folds:
        raise ValueError(
            f"{context} needs at least {folds} rows per class; found {minimum}."
        )


def run_nested_cross_validation(
    estimator: Any,
    parameter_grid: dict[str, list[Any]],
    data: pd.DataFrame,
    target_column: str = "label",
    index_column: str = "row_index",
    outer_folds: int = 5,
    inner_folds: int = 3,
    seed: int = 42,
    n_jobs: int = 1,
) -> CrossValidationResult:
    """Run stratified outer evaluation with fold-local parameter selection."""
    data = data.reset_index(drop=True).copy()
    if index_column not in data.columns:
        data.insert(0, index_column, np.arange(len(data), dtype=int))
    data[target_column] = pd.to_numeric(data[target_column]).astype(int)
    labels = data[target_column]
    _check_fold_counts(labels, outer_folds, "Outer CV")

    scorer = make_scorer(quadratic_weighted_kappa)
    outer_splitter = StratifiedKFold(
        n_splits=outer_folds,
        shuffle=True,
        random_state=seed,
    )
    metric_rows: list[dict[str, object]] = []
    prediction_frames: list[pd.DataFrame] = []
    selected_parameters: list[dict[str, Any]] = []

    for fold, (training_index, validation_index) in enumerate(
        outer_splitter.split(data, labels),
        start=1,
    ):
        outer_training = data.iloc[training_index].reset_index(drop=True)
        outer_validation = data.iloc[validation_index].reset_index(drop=True)
        _check_fold_counts(
            outer_training[target_column],
            inner_folds,
            f"Inner CV in outer fold {fold}",
        )
        inner_splitter = StratifiedKFold(
            n_splits=inner_folds,
            shuffle=True,
            random_state=seed + fold,
        )
        search = GridSearchCV(
            estimator=clone(estimator),
            param_grid=parameter_grid,
            scoring=scorer,
            cv=inner_splitter,
            refit=True,
            n_jobs=n_jobs,
            error_score="raise",
        )
        search.fit(
            outer_training.drop(columns=[target_column]),
            outer_training[target_column],
        )
        predictions = search.predict(
            outer_validation.drop(columns=[target_column])
        )
        metrics = calculate_metrics(
            outer_validation[target_column],
            predictions,
        )
        metric_rows.append(
            {
                "fold": fold,
                "quadratic_weighted_kappa": metrics[
                    "quadratic_weighted_kappa"
                ],
                "accuracy": metrics["accuracy"],
                "weighted_f1": metrics["weighted_f1"],
                "mean_absolute_error": metrics["mean_absolute_error"],
                "best_parameters": json.dumps(search.best_params_, sort_keys=True),
            }
        )
        prediction_frames.append(
            pd.DataFrame(
                {
                    index_column: outer_validation[index_column].astype(int),
                    "fold": fold,
                    "true_label": outer_validation[target_column].astype(int),
                    "prediction": np.asarray(predictions, dtype=int),
                }
            )
        )
        selected_parameters.append(dict(search.best_params_))

    return CrossValidationResult(
        fold_metrics=pd.DataFrame(metric_rows),
        predictions=pd.concat(prediction_frames, ignore_index=True),
        best_parameters=selected_parameters,
    )


def _stratified_early_stopping_split(
    data: pd.DataFrame,
    requested_fraction: float,
    seed: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Reserve a training-only, label-stratified subset for early stopping."""
    if not 0.0 < requested_fraction < 1.0:
        raise ValueError("early_stopping_fraction must be between zero and one.")
    labels = data["label"].astype(int)
    if labels.value_counts().min() < 2:
        raise ValueError("BERT early stopping needs at least two rows per class.")
    splitter = StratifiedShuffleSplit(
        n_splits=1,
        test_size=requested_fraction,
        random_state=seed,
    )
    try:
        fitting_index, validation_index = next(splitter.split(data, labels))
    except ValueError as exc:
        raise ValueError(
            "Could not create a stratified BERT early-stopping subset."
        ) from exc
    return (
        data.iloc[fitting_index].reset_index(drop=True),
        data.iloc[validation_index].reset_index(drop=True),
    )


def run_bert_outer_cross_validation(
    data: pd.DataFrame,
    settings: dict[str, Any],
    outer_folds: int = 5,
    seed: int = 42,
    output_directory: str | Path | None = None,
    device: str | None = None,
) -> CrossValidationResult:
    """Run stratified BERT outer folds with training-only early stopping."""
    data = data.reset_index(drop=True).copy()
    if "row_index" not in data.columns:
        data.insert(0, "row_index", np.arange(len(data), dtype=int))
    data["label"] = pd.to_numeric(data["label"]).astype(int)
    labels = data["label"]
    _check_fold_counts(labels, outer_folds, "BERT outer CV")
    splitter = StratifiedKFold(
        n_splits=outer_folds,
        shuffle=True,
        random_state=seed,
    )
    metric_rows: list[dict[str, object]] = []
    prediction_frames: list[pd.DataFrame] = []
    best_epochs: list[int] = []

    for fold, (training_index, validation_index) in enumerate(
        splitter.split(data, labels),
        start=1,
    ):
        outer_training = data.iloc[training_index].reset_index(drop=True)
        outer_validation = data.iloc[validation_index].reset_index(drop=True)
        fitting, early_stopping = _stratified_early_stopping_split(
            outer_training,
            float(settings.get("early_stopping_fraction", 0.1)),
            seed + fold,
        )
        fold_directory = None
        if output_directory is not None:
            fold_directory = Path(output_directory) / f"fold_{fold}"
        fold_settings = dict(settings)
        fold_settings["seed"] = seed + fold
        training_result = train_bert_model(
            fitting,
            early_stopping,
            settings=fold_settings,
            output_directory=fold_directory,
            device=device,
        )
        predicted = predict_bert(
            training_result,
            outer_validation,
            device=device,
        )
        aligned = outer_validation[["row_index", "label"]].merge(
            predicted,
            on="row_index",
            validate="one_to_one",
        )
        metrics = calculate_metrics(aligned["label"], aligned["prediction"])
        metric_rows.append(
            {
                "fold": fold,
                "quadratic_weighted_kappa": metrics[
                    "quadratic_weighted_kappa"
                ],
                "accuracy": metrics["accuracy"],
                "weighted_f1": metrics["weighted_f1"],
                "mean_absolute_error": metrics["mean_absolute_error"],
                "best_epoch": training_result.best_epoch,
            }
        )
        prediction_frames.append(
            aligned[["row_index", "label", "prediction"]]
            .rename(columns={"label": "true_label"})
            .assign(fold=fold)
        )
        best_epochs.append(training_result.best_epoch)

    return CrossValidationResult(
        fold_metrics=pd.DataFrame(metric_rows),
        predictions=pd.concat(prediction_frames, ignore_index=True),
        best_epochs=best_epochs,
    )


def save_cross_validation_result(
    result: CrossValidationResult,
    condition_name: str,
    metrics_directory: str | Path,
    predictions_directory: str | Path,
) -> None:
    """Save fold metrics and identifier-aligned predictions."""
    metrics_path = Path(metrics_directory)
    predictions_path = Path(predictions_directory)
    metrics_path.mkdir(parents=True, exist_ok=True)
    predictions_path.mkdir(parents=True, exist_ok=True)
    result.fold_metrics.to_csv(
        metrics_path / f"{condition_name}_cv.csv",
        index=False,
    )
    result.predictions.to_csv(
        predictions_path / f"{condition_name}_cv.csv",
        index=False,
    )
