"""Shared four-class and ordinal evaluation metrics."""

from __future__ import annotations

from collections.abc import Callable
import itertools
from statistics import NormalDist

from evaluation.resampling import bootstrap_indices

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


def validate_label_array(values: object, name: str) -> np.ndarray:
    """Return a strict 1--4 integer array without lossy coercion."""
    try:
        numeric = np.asarray(values, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must contain numeric integer labels.") from exc
    if numeric.ndim != 1 or numeric.size == 0:
        raise ValueError(f"{name} must be a non-empty one-dimensional array.")
    if not np.isfinite(numeric).all():
        raise ValueError(f"{name} must contain finite labels.")
    if not np.equal(numeric, np.floor(numeric)).all():
        raise ValueError(f"{name} must contain integer labels without truncation.")
    result = numeric.astype(np.int64)
    if not set(np.unique(result)).issubset(LABELS):
        raise ValueError(f"{name} must contain only labels 1 through 4.")
    return result


def _validate_label_pair(
    true_labels: object,
    predictions: object,
) -> tuple[np.ndarray, np.ndarray]:
    truth = validate_label_array(true_labels, "True labels")
    predicted = validate_label_array(predictions, "Predictions")
    if truth.shape != predicted.shape:
        raise ValueError("True labels and predictions must have equal shapes.")
    return truth, predicted


def _qwk(true_labels: object, predictions: object) -> float:
    # Keep the ordinal spacing even if a subset has no observations of a class.
    value = float(cohen_kappa_score(
        true_labels, predictions, labels=LABELS, weights="quadratic"
    ))
    if not np.isfinite(value):
        raise ValueError("Quadratic weighted kappa is undefined for these labels.")
    return value


def quadratic_weighted_kappa(
    true_labels: object,
    predictions: object,
) -> float:
    truth, predicted = _validate_label_pair(true_labels, predictions)
    return _qwk(truth, predicted)


def calculate_metrics(
    true_labels: object,
    predictions: object,
) -> dict[str, object]:
    """Calculate the metrics specified in the thesis."""
    true_array, prediction_array = _validate_label_pair(true_labels, predictions)

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
        "quadratic_weighted_kappa": _qwk(true_array, prediction_array),
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
        "quadratic_weighted_kappa": _qwk,
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
    true_array = validate_label_array(true_labels, "True labels")
    first = validate_label_array(predictions_a, "First predictions")
    second = validate_label_array(predictions_b, "Second predictions")
    if not (len(true_array) == len(first) == len(second)):
        raise ValueError("Bootstrap inputs must contain the same videos.")
    if (
        not isinstance(resamples, (int, np.integer))
        or isinstance(resamples, (bool, np.bool_))
        or int(resamples) < 1
    ):
        raise ValueError("resamples must be a positive integer.")
    resamples = int(resamples)

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


def wilson_interval(
    successes: int,
    total: int,
    confidence_level: float = 0.95,
) -> tuple[float, float]:
    """Wilson score interval for an observed sample proportion."""
    if total < 1 or not 0 <= successes <= total:
        raise ValueError("Wilson interval requires 0 <= successes <= total.")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one.")
    z = NormalDist().inv_cdf(0.5 + confidence_level / 2.0)
    proportion = successes / total
    denominator = 1.0 + z * z / total
    centre = (proportion + z * z / (2.0 * total)) / denominator
    half_width = (
        z
        * np.sqrt(
            proportion * (1.0 - proportion) / total
            + z * z / (4.0 * total * total)
        )
        / denominator
    )
    return float(centre - half_width), float(centre + half_width)


def class_distribution_table(
    labels: object,
    confidence_level: float = 0.95,
) -> list[dict[str, object]]:
    """Counts, proportions, and Wilson intervals for RQ1."""
    values = validate_label_array(labels, "Class distribution labels")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one.")
    rows: list[dict[str, object]] = []
    for label in LABELS:
        count = int(np.sum(values == label))
        low, high = wilson_interval(count, len(values), confidence_level)
        rows.append(
            {
                "label": label,
                "count": count,
                "proportion": count / len(values),
                "percentage": 100.0 * count / len(values),
                "wilson_ci_low": low,
                "wilson_ci_high": high,
                "confidence_level": confidence_level,
            }
        )
    return rows


def bootstrap_many_conditions(
    true_labels: object,
    predictions_by_condition: dict[str, object],
    metric_names: tuple[str, ...] = (
        "quadratic_weighted_kappa",
        "accuracy",
        "weighted_f1",
        "mean_absolute_error",
    ),
    resamples: int = 10000,
    seed: int = 42,
    confidence_level: float = 0.95,
    groups: object = None,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Reuse the same stratified resamples for all models and all pairs.

    Computing every model once per bootstrap replicate avoids repeating the
    expensive metric calculation separately for each of the 91 condition
    pairs in the fourteen-condition design.
    """
    truth = validate_label_array(true_labels, "True labels")
    condition_names = list(predictions_by_condition)
    predictions = {
        name: validate_label_array(values, f"Predictions for {name}")
        for name, values in predictions_by_condition.items()
    }
    if not condition_names:
        raise ValueError("At least one condition is required.")
    if any(len(values) != len(truth) for values in predictions.values()):
        raise ValueError("Every condition must predict the same held-out rows.")
    if (
        not isinstance(resamples, (int, np.integer))
        or isinstance(resamples, (bool, np.bool_))
        or int(resamples) < 1
    ):
        raise ValueError("resamples must be a positive integer.")
    resamples = int(resamples)
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one.")

    functions = {name: metric_function(name) for name in metric_names}
    samples = {
        metric: np.empty((resamples, len(condition_names)), dtype=float)
        for metric in metric_names
    }
    # Compute every condition/replicate from its fixed 4x4 confusion matrix.
    # This is algebraically the same metric calculation as sklearn and avoids
    # hundreds of thousands of estimator-validation calls during reporting.
    prediction_matrix = np.stack([predictions[name] for name in condition_names])
    distances = np.abs(np.arange(4)[:, None] - np.arange(4)[None, :])
    for iteration, sampled in enumerate(
        bootstrap_indices(truth, resamples, seed, groups)
    ):
        encoded = 4 * (truth[sampled][None, :] - 1) + prediction_matrix[:, sampled] - 1
        matrices = np.stack([
            np.bincount(row, minlength=16).reshape(4, 4) for row in encoded
        ]).astype(float)
        actual = matrices.sum(axis=2)
        predicted = matrices.sum(axis=1)
        totals = actual.sum(axis=1)
        correct = np.diagonal(matrices, axis1=1, axis2=2)
        expected = actual[:, :, None] * predicted[:, None, :] / totals[:, None, None]
        denominator = (expected * distances ** 2).sum(axis=(1, 2))
        with np.errstate(divide="ignore", invalid="ignore"):
            qwk = 1 - (matrices * distances ** 2).sum(axis=(1, 2)) / denominator
        class_f1 = np.divide(
            2 * correct, actual + predicted,
            out=np.zeros_like(correct), where=(actual + predicted) != 0,
        )
        values = {
            "quadratic_weighted_kappa": qwk,
            "accuracy": correct.sum(axis=1) / totals,
            "weighted_f1": (class_f1 * actual).sum(axis=1) / totals,
            "mean_absolute_error": (matrices * distances).sum(axis=(1, 2)) / totals,
        }
        for metric in functions:
            samples[metric][iteration] = values[metric]

    tail = (1.0 - confidence_level) / 2.0
    intervals: list[dict[str, object]] = []
    differences: list[dict[str, object]] = []
    for metric, function in functions.items():
        higher_is_better = metric != "mean_absolute_error"
        observed = np.asarray(
            [function(truth, predictions[name]) for name in condition_names],
            dtype=float,
        )
        for index, condition in enumerate(condition_names):
            distribution = samples[metric][:, index]
            intervals.append(
                {
                    "condition": condition,
                    "metric": metric,
                    "observed": float(observed[index]),
                    "bootstrap_mean": float(np.nanmean(distribution)),
                    "ci_low": float(np.nanquantile(distribution, tail)),
                    "ci_high": float(np.nanquantile(distribution, 1.0 - tail)),
                    "confidence_level": confidence_level,
                    "valid_resamples": int(np.isfinite(distribution).sum()),
                    "resampling_unit": "content_group" if groups is not None else "label_stratified_row",
                    "bootstrap_resamples_requested": resamples,
                    "bootstrap_seed": seed,
                    "higher_is_better": higher_is_better,
                }
            )
        for first_index, second_index in itertools.combinations(
            range(len(condition_names)),
            2,
        ):
            distribution = (
                samples[metric][:, first_index] - samples[metric][:, second_index]
            )
            differences.append(
                {
                    "condition_a": condition_names[first_index],
                    "condition_b": condition_names[second_index],
                    "metric": metric,
                    "observed_a_minus_b": float(
                        observed[first_index] - observed[second_index]
                    ),
                    "bootstrap_mean_a_minus_b": float(np.nanmean(distribution)),
                    "ci_low": float(np.nanquantile(distribution, tail)),
                    "ci_high": float(np.nanquantile(distribution, 1.0 - tail)),
                    "confidence_level": confidence_level,
                    "valid_resamples": int(np.isfinite(distribution).sum()),
                    "resampling_unit": "content_group" if groups is not None else "label_stratified_row",
                    "bootstrap_resamples_requested": resamples,
                    "bootstrap_seed": seed,
                    "higher_is_better": higher_is_better,
                }
            )
    return intervals, differences


def ordinal_error_summary(
    true_labels: object,
    predictions: object,
) -> dict[str, object]:
    """Direction and distance of held-out errors for sensitive-task analysis."""
    truth, predicted = _validate_label_pair(true_labels, predictions)
    distance = predicted - truth
    absolute = np.abs(distance)
    return {
        "rows": len(truth),
        "correct": int(np.sum(distance == 0)),
        "underestimates_severity": int(np.sum(distance < 0)),
        "overestimates_severity": int(np.sum(distance > 0)),
        "errors_distance_1": int(np.sum(absolute == 1)),
        "errors_distance_2": int(np.sum(absolute == 2)),
        "errors_distance_3": int(np.sum(absolute == 3)),
        "severe_errors_distance_at_least_2": int(np.sum(absolute >= 2)),
        "mean_signed_error": float(np.mean(distance)),
        "mean_absolute_error": float(np.mean(absolute)),
    }
