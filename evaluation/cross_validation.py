"""Leakage-safe cross-validation for Ridge, frozen MiniLM, and BERT."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV, StratifiedGroupKFold

from evaluation.metrics import calculate_metrics, quadratic_weighted_kappa
from features.content_groups import content_group_ids, validate_group_labels
from models.finetuned_bert import predict_bert, train_bert_model


@dataclass
class CrossValidationResult:
    fold_metrics: pd.DataFrame
    predictions: pd.DataFrame
    best_parameters: list[dict[str, Any]] = field(default_factory=list)
    best_epochs: list[int] = field(default_factory=list)
    fitted_estimators: list[Any] = field(default_factory=list, repr=False)


def _check_group_fold_counts(
    labels: pd.Series,
    groups: np.ndarray,
    folds: int,
    context: str,
) -> None:
    frame = pd.DataFrame({"label": labels.to_numpy(), "group": groups})
    minimum = int(frame.drop_duplicates("group")["label"].value_counts().min())
    if minimum < folds:
        raise ValueError(
            f"{context} needs at least {folds} content groups per class; "
            f"found {minimum}."
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
    """Run grouped outer evaluation with grouped fold-local model selection."""
    data = data.reset_index(drop=True).copy()
    if index_column not in data.columns:
        data.insert(0, index_column, np.arange(len(data), dtype=int))
    data[target_column] = pd.to_numeric(data[target_column]).astype(int)
    validate_group_labels(data, target_column)
    labels = data[target_column]
    groups = content_group_ids(data)
    _check_group_fold_counts(labels, groups, outer_folds, "Outer CV")
    scorer = make_scorer(quadratic_weighted_kappa)
    outer_splitter = StratifiedGroupKFold(
        n_splits=outer_folds,
        shuffle=True,
        random_state=seed,
    )

    metric_rows: list[dict[str, object]] = []
    prediction_frames: list[pd.DataFrame] = []
    selected_parameters: list[dict[str, Any]] = []
    fitted_estimators: list[Any] = []

    for fold, (training_index, validation_index) in enumerate(
        outer_splitter.split(data, labels, groups),
        start=1,
    ):
        outer_training = data.iloc[training_index].reset_index(drop=True)
        outer_validation = data.iloc[validation_index].reset_index(drop=True)
        training_groups = content_group_ids(outer_training)
        _check_group_fold_counts(
            outer_training[target_column],
            training_groups,
            inner_folds,
            f"Inner CV in outer fold {fold}",
        )
        inner_splitter = StratifiedGroupKFold(
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
            groups=training_groups,
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
        fitted_estimators.append(search.best_estimator_)

    return CrossValidationResult(
        fold_metrics=pd.DataFrame(metric_rows),
        predictions=pd.concat(prediction_frames, ignore_index=True),
        best_parameters=selected_parameters,
        fitted_estimators=fitted_estimators,
    )


def _grouped_early_stopping_split(
    data: pd.DataFrame,
    requested_fraction: float,
    seed: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Choose a group-safe stratified fold closest to the requested fraction."""
    labels = data["label"].astype(int)
    groups = content_group_ids(data)
    group_frame = pd.DataFrame({"label": labels, "group": groups}).drop_duplicates(
        "group"
    )
    minimum_groups = int(group_frame["label"].value_counts().min())
    requested_folds = max(2, int(round(1.0 / requested_fraction)))
    folds = min(requested_folds, minimum_groups)
    if folds < 2:
        raise ValueError("Not enough content groups for BERT early stopping.")
    splitter = StratifiedGroupKFold(
        n_splits=folds,
        shuffle=True,
        random_state=seed,
    )
    expected_labels = set(labels.unique())
    candidates: list[tuple[float, np.ndarray, np.ndarray]] = []
    for fitting_index, validation_index in splitter.split(data, labels, groups):
        fitting_labels = set(labels.iloc[fitting_index].unique())
        validation_labels = set(labels.iloc[validation_index].unique())
        if fitting_labels == expected_labels and validation_labels == expected_labels:
            difference = abs(len(validation_index) / len(data) - requested_fraction)
            candidates.append((difference, fitting_index, validation_index))
    if not candidates:
        raise ValueError(
            "Could not create an early-stopping subset containing every class."
        )
    _, fitting_index, validation_index = min(candidates, key=lambda item: item[0])
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
    """Run grouped BERT outer folds with training-only early stopping."""
    data = data.reset_index(drop=True).copy()
    if "row_index" not in data.columns:
        data.insert(0, "row_index", np.arange(len(data), dtype=int))
    data["label"] = pd.to_numeric(data["label"]).astype(int)
    validate_group_labels(data)
    labels = data["label"]
    groups = content_group_ids(data)
    _check_group_fold_counts(labels, groups, outer_folds, "BERT outer CV")
    splitter = StratifiedGroupKFold(
        n_splits=outer_folds,
        shuffle=True,
        random_state=seed,
    )
    metric_rows: list[dict[str, object]] = []
    prediction_frames: list[pd.DataFrame] = []
    best_epochs: list[int] = []

    for fold, (training_index, validation_index) in enumerate(
        splitter.split(data, labels, groups),
        start=1,
    ):
        outer_training = data.iloc[training_index].reset_index(drop=True)
        outer_validation = data.iloc[validation_index].reset_index(drop=True)
        fitting, early_stopping = _grouped_early_stopping_split(
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
            output_directory=None,
            device=device,
        )
        if fold_directory is not None:
            fold_directory.mkdir(parents=True, exist_ok=True)
            pd.DataFrame(training_result.history).to_csv(
                fold_directory / "training_history.csv",
                index=False,
            )
            fold_record = {
                "fold": fold,
                "best_epoch": training_result.best_epoch,
                "outer_training_rows": len(outer_training),
                "fitting_rows": len(fitting),
                "early_stopping_rows": len(early_stopping),
                "outer_validation_rows": len(outer_validation),
                "settings": training_result.settings,
                "model_name": training_result.settings.get("model_name"),
                "encoder_commit_hash": getattr(
                    training_result.model.bert.config,
                    "_commit_hash",
                    None,
                ),
                "tokenizer_commit_hash": getattr(
                    training_result.tokenizer,
                    "init_kwargs",
                    {},
                ).get("_commit_hash"),
            }
            (fold_directory / "fold_training_record.json").write_text(
                json.dumps(fold_record, indent=2),
                encoding="utf-8",
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
