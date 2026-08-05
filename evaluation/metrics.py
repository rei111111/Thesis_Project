"""Shared four-class and ordinal evaluation metrics."""

from __future__ import annotations

from collections.abc import Callable
import itertools
from statistics import NormalDist

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
    values = np.asarray(labels, dtype=int)
    if not set(values).issubset(LABELS):
        raise ValueError("Class distribution labels must be between 1 and 4.")
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
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Reuse the same stratified resamples for all models and all pairs.

    Computing every model once per bootstrap replicate avoids repeating the
    expensive metric calculation separately for each of the 91 condition
    pairs in the fourteen-condition design.
    """
    truth = np.asarray(true_labels, dtype=int)
    condition_names = list(predictions_by_condition)
    predictions = {
        name: np.asarray(values, dtype=int)
        for name, values in predictions_by_condition.items()
    }
    if not condition_names:
        raise ValueError("At least one condition is required.")
    if any(len(values) != len(truth) for values in predictions.values()):
        raise ValueError("Every condition must predict the same held-out rows.")
    if resamples < 1:
        raise ValueError("resamples must be positive.")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one.")

    functions = {name: metric_function(name) for name in metric_names}
    samples = {
        metric: np.empty((resamples, len(condition_names)), dtype=float)
        for metric in metric_names
    }
    generator = np.random.default_rng(seed)
    class_indices = [np.flatnonzero(truth == label) for label in np.unique(truth)]
    for iteration in range(resamples):
        sampled = np.concatenate(
            [
                generator.choice(indices, size=len(indices), replace=True)
                for indices in class_indices
            ]
        )
        sampled_truth = truth[sampled]
        for condition_index, condition in enumerate(condition_names):
            sampled_predictions = predictions[condition][sampled]
            for metric, function in functions.items():
                samples[metric][iteration, condition_index] = function(
                    sampled_truth,
                    sampled_predictions,
                )

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
                    "higher_is_better": higher_is_better,
                }
            )
    return intervals, differences


def ordinal_error_summary(
    true_labels: object,
    predictions: object,
) -> dict[str, object]:
    """Direction and distance of held-out errors for sensitive-task analysis."""
    truth = np.asarray(true_labels, dtype=int)
    predicted = np.asarray(predictions, dtype=int)
    if truth.shape != predicted.shape:
        raise ValueError("True labels and predictions must align.")
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
