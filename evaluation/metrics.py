"""Shared four-class and ordinal evaluation metrics."""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    precision_recall_fscore_support,
)


LABELS = (1, 2, 3, 4)


def quadratic_weighted_kappa(
    true_labels: object,
    predictions: object,
) -> float:
    return float(
        cohen_kappa_score(true_labels, predictions, weights="quadratic")
    )


def calculate_metrics(
    true_labels: object,
    predictions: object,
) -> dict[str, object]:
    """Calculate the metrics specified in the thesis."""
    true_array = np.asarray(true_labels, dtype=int)
    prediction_array = np.asarray(predictions, dtype=int)
    if true_array.shape != prediction_array.shape:
        raise ValueError("True labels and predictions must have equal shapes.")

    precision, recall, class_f1, support = precision_recall_fscore_support(
        true_array,
        prediction_array,
        labels=LABELS,
        zero_division=0,
    )
    per_class = {
        str(label): {
            "precision": float(precision[index]),
            "recall": float(recall[index]),
            "f1": float(class_f1[index]),
            "support": int(support[index]),
        }
        for index, label in enumerate(LABELS)
    }
    return {
        "quadratic_weighted_kappa": quadratic_weighted_kappa(
            true_array,
            prediction_array,
        ),
        "accuracy": float(accuracy_score(true_array, prediction_array)),
        "weighted_f1": float(
            f1_score(
                true_array,
                prediction_array,
                labels=LABELS,
                average="weighted",
                zero_division=0,
            )
        ),
        "mean_absolute_error": float(
            mean_absolute_error(true_array, prediction_array)
        ),
        "per_class": per_class,
        "confusion_matrix": confusion_matrix(
            true_array,
            prediction_array,
            labels=LABELS,
        ).tolist(),
    }


def metric_function(name: str) -> Callable[[object, object], float]:
    functions = {
        "quadratic_weighted_kappa": quadratic_weighted_kappa,
        "accuracy": lambda true, predicted: float(
            accuracy_score(true, predicted)
        ),
        "weighted_f1": lambda true, predicted: float(
            f1_score(true, predicted, average="weighted", zero_division=0)
        ),
        "mean_absolute_error": lambda true, predicted: float(
            mean_absolute_error(true, predicted)
        ),
    }
    if name not in functions:
        raise ValueError(f"Unknown metric: {name}")
    return functions[name]


def paired_stratified_bootstrap(
    true_labels: object,
    predictions_a: object,
    predictions_b: object,
    metric_name: str = "quadratic_weighted_kappa",
    resamples: int = 10000,
    seed: int = 42,
) -> dict[str, float]:
    """Compare two aligned prediction arrays with label-stratified resampling."""
    true_array = np.asarray(true_labels, dtype=int)
    first = np.asarray(predictions_a, dtype=int)
    second = np.asarray(predictions_b, dtype=int)
    if not (len(true_array) == len(first) == len(second)):
        raise ValueError("Bootstrap inputs must contain the same videos.")

    calculate = metric_function(metric_name)
    random_generator = np.random.default_rng(seed)
    class_indices = [
        np.flatnonzero(true_array == label)
        for label in np.unique(true_array)
    ]
    differences = np.empty(resamples, dtype=float)
    for iteration in range(resamples):
        sampled_parts = [
            random_generator.choice(indices, size=len(indices), replace=True)
            for indices in class_indices
        ]
        sampled = np.concatenate(sampled_parts)
        differences[iteration] = calculate(
            true_array[sampled],
            first[sampled],
        ) - calculate(
            true_array[sampled],
            second[sampled],
        )

    return {
        "observed_difference": calculate(true_array, first)
        - calculate(true_array, second),
        "bootstrap_mean_difference": float(np.mean(differences)),
        "ci_2_5": float(np.percentile(differences, 2.5)),
        "ci_97_5": float(np.percentile(differences, 97.5)),
    }
