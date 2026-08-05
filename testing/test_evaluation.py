from __future__ import annotations

import unittest

import numpy as np
import pandas as pd

from evaluation.cross_validation import run_nested_cross_validation
from evaluation.metrics import (
    bootstrap_many_conditions,
    calculate_metrics,
    paired_stratified_bootstrap,
)
from models.ridge_classifier import (
    build_ridge_classifier,
    ridge_parameter_grid,
)
from testing.test_models import model_frame


class EvaluationTests(unittest.TestCase):
    def test_perfect_predictions_receive_perfect_main_metrics(self) -> None:
        labels = [1, 2, 3, 4]
        metrics = calculate_metrics(labels, labels)
        self.assertEqual(metrics["quadratic_weighted_kappa"], 1.0)
        self.assertEqual(metrics["accuracy"], 1.0)
        self.assertEqual(metrics["weighted_f1"], 1.0)
        self.assertEqual(metrics["mean_absolute_error"], 0.0)

    def test_nested_cross_validation_preserves_all_identifiers(self) -> None:
        data = model_frame(rows_per_class=6)
        result = run_nested_cross_validation(
            estimator=build_ridge_classifier("B", max_features=50),
            parameter_grid=ridge_parameter_grid([0.1, 1.0]),
            data=data,
            outer_folds=3,
            inner_folds=2,
            seed=42,
        )
        self.assertEqual(len(result.predictions), len(data))
        self.assertEqual(
            set(result.predictions["row_index"]),
            set(data["row_index"]),
        )
        self.assertEqual(len(result.fold_metrics), 3)

    def test_duplicate_transcripts_never_cross_outer_folds(self) -> None:
        original = model_frame(rows_per_class=6)
        duplicate = original.iloc[[0]].copy()
        duplicate["row_index"] = original["row_index"].max() + 1
        combined = pd.concat([original, duplicate], ignore_index=True)
        result = run_nested_cross_validation(
            estimator=build_ridge_classifier("A", max_features=50),
            parameter_grid=ridge_parameter_grid([1.0]),
            data=combined,
            outer_folds=3,
            inner_folds=2,
            seed=7,
        )
        duplicated = result.predictions[
            result.predictions["row_index"].isin(
                [original.iloc[0]["row_index"], duplicate.iloc[0]["row_index"]]
            )
        ]
        self.assertEqual(duplicated["fold"].nunique(), 1)

    def test_paired_bootstrap_detects_better_predictions(self) -> None:
        labels = np.tile([1, 2, 3, 4], 5)
        perfect = labels.copy()
        worse = np.roll(labels, 1)
        comparison = paired_stratified_bootstrap(
            labels,
            perfect,
            worse,
            resamples=100,
            seed=42,
        )
        self.assertGreater(comparison["observed_difference"], 0)

    def test_shared_bootstrap_returns_every_metric_and_pair(self) -> None:
        labels = np.tile([1, 2, 3, 4], 3)
        intervals, differences = bootstrap_many_conditions(
            labels,
            {"perfect": labels, "shifted": np.roll(labels, 1)},
            resamples=30,
            seed=3,
        )
        self.assertEqual(len(intervals), 8)
        self.assertEqual(len(differences), 4)
        qwk = next(row for row in differences if row["metric"] == "quadratic_weighted_kappa")
        self.assertGreater(qwk["observed_a_minus_b"], 0)


if __name__ == "__main__":
    unittest.main()
