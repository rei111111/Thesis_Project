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

from evaluation.metrics import (
    calculate_metrics,
    quadratic_weighted_kappa,
    validate_label_array,
)
from evaluation.stratification import (
    StratifiedGroupKFoldByColumns,
    check_group_fold_counts,
    joint_stratification_labels,
)
from features.content_groups import content_group_ids, validate_group_labels
from models.finetuned_bert import predict_bert, train_bert_model


@dataclass
class CrossValidationResult:
    fold_metrics: pd.DataFrame
    predictions: pd.DataFrame
    best_parameters: list[dict[str, Any]] = field(default_factory=list)
    best_epochs: list[int] = field(default_factory=list)
    fitted_estimators: list[Any] = field(default_factory=list, repr=False)


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
    stratification_columns: tuple[str, ...] = (),
) -> CrossValidationResult:
    """Run grouped outer evaluation with grouped fold-local model selection."""
    data = data.reset_index(drop=True).copy()
    if index_column not in data.columns:
        data.insert(0, index_column, np.arange(len(data), dtype=int))
    data[target_column] = validate_label_array(
        data[target_column], f"{target_column} values"
    )
    validate_group_labels(data, target_column)
    labels = data[target_column]
    groups = content_group_ids(data)
    strata = joint_stratification_labels(data, labels, stratification_columns)
    check_group_fold_counts(strata, groups, outer_folds, "Outer CV")
    scorer = make_scorer(quadratic_weighted_kappa)
    outer_splitter = StratifiedGroupKFoldByColumns(
        n_splits=outer_folds, shuffle=True, random_state=seed,
        stratification_columns=stratification_columns,
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
        training_strata = joint_stratification_labels(
            outer_training,
            outer_training[target_column],
            stratification_columns,
        )
        check_group_fold_counts(
            training_strata,
            training_groups,
            inner_folds,
            f"Inner CV in outer fold {fold}",
        )
        inner_splitter = StratifiedGroupKFoldByColumns(
            n_splits=inner_folds,
            shuffle=True,
            random_state=seed + fold,
            stratification_columns=stratification_columns,
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
        predictions = validate_label_array(
            search.predict(outer_validation.drop(columns=[target_column])),
            f"outer-fold {fold} predictions",
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
        prediction_frame = pd.DataFrame(
            {
                index_column: outer_validation[index_column].astype(int),
                "fold": fold,
                "true_label": outer_validation[target_column].astype(int),
                "prediction": np.asarray(predictions, dtype=int),
            }
        )
        for identity_column in ("record_id", "platform"):
            if identity_column in outer_validation.columns:
                prediction_frame[identity_column] = outer_validation[
                    identity_column
                ].astype(str)
        prediction_frames.append(prediction_frame)
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
    stratification_columns: tuple[str, ...] = (),
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Choose a group-safe stratified fold closest to the requested fraction."""
    if not 0 < requested_fraction < 1:
        raise ValueError("BERT early_stopping_fraction must be between zero and one.")
    labels = data["label"].astype(int)
    groups = content_group_ids(data)
    strata = joint_stratification_labels(data, labels, stratification_columns)
    group_frame = pd.DataFrame(
        {"stratum": strata.to_numpy(), "group": groups}
    ).drop_duplicates(["group", "stratum"])
    minimum_groups = int(group_frame["stratum"].value_counts().min())
    requested_folds = max(2, int(round(1.0 / requested_fraction)))
    folds = min(requested_folds, minimum_groups)
    if folds < 2:
        raise ValueError("Not enough content groups for BERT early stopping.")
    splitter = StratifiedGroupKFold(
        n_splits=folds,
        shuffle=True,
        random_state=seed,
    )
    expected_strata = set(strata.unique())
    candidates: list[tuple[float, np.ndarray, np.ndarray]] = []
    for fitting_index, validation_index in splitter.split(data, strata, groups):
        fitting_strata = set(strata.iloc[fitting_index].unique())
        validation_strata = set(strata.iloc[validation_index].unique())
        if fitting_strata == expected_strata and validation_strata == expected_strata:
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
    data["label"] = validate_label_array(data["label"], "BERT labels")
    validate_group_labels(data)
    labels = data["label"]
    groups = content_group_ids(data)
    stratification_columns = tuple(settings.get("stratification_columns", ()))
    strata = joint_stratification_labels(data, labels, stratification_columns)
    check_group_fold_counts(strata, groups, outer_folds, "BERT outer CV")
    splitter = StratifiedGroupKFoldByColumns(
        n_splits=outer_folds, shuffle=True, random_state=seed,
        stratification_columns=stratification_columns,
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
            stratification_columns,
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
                ) or training_result.settings.get("resolved_revision"),
                "tokenizer_commit_hash": getattr(
                    training_result.tokenizer,
                    "init_kwargs",
                    {},
                ).get("_commit_hash") or training_result.settings.get("resolved_revision"),
                "hidden_size": int(training_result.model.bert.config.hidden_size),
                "metadata_dimension": int(
                    training_result.model.classifier.in_features
                    - training_result.model.bert.config.hidden_size
                ),
                "classifier_input_dimension": int(
                    training_result.model.classifier.in_features
                ),
                "num_labels": int(training_result.model.classifier.out_features),
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
        identity_columns = [
            column
            for column in ("row_index", "record_id", "platform", "label")
            if column in outer_validation.columns
        ]
        aligned = outer_validation[identity_columns].merge(
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
            aligned[
                [
                    column
                    for column in (
                        "row_index",
                        "record_id",
                        "platform",
                        "label",
                        "prediction",
                    )
                    if column in aligned.columns
                ]
            ]
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
