from __future__ import annotations

import unittest

import numpy as np

from evaluation.cross_validation import run_nested_cross_validation
from evaluation.metrics import (
    calculate_metrics,
    paired_stratified_bootstrap,
)
from models.frozen_minilm import FrozenMiniLMClassifier, minilm_parameter_grid
from models.ridge_classifier import (
    build_ridge_classifier,
    ridge_parameter_grid,
)
from testing.test_models import FakeSentenceEncoder, model_frame


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

    def test_outer_folds_are_label_stratified(self) -> None:
        data = model_frame(rows_per_class=6)
        result = run_nested_cross_validation(
            estimator=build_ridge_classifier("A", max_features=50),
            parameter_grid=ridge_parameter_grid([1.0]),
            data=data,
            outer_folds=3,
            inner_folds=2,
            seed=7,
        )
        counts = result.predictions.groupby(["fold", "true_label"]).size()
        self.assertTrue((counts == 2).all())

    def test_nested_minilm_path_accepts_frozen_encoder(self) -> None:
        data = model_frame(rows_per_class=4)
        result = run_nested_cross_validation(
            estimator=FrozenMiniLMClassifier(encoder=FakeSentenceEncoder()),
            parameter_grid=minilm_parameter_grid([0.5, 1.0]),
            data=data,
            outer_folds=2,
            inner_folds=2,
            seed=11,
        )
        self.assertEqual(len(result.predictions), len(data))
        self.assertEqual(len(result.best_parameters), 2)

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


if __name__ == "__main__":
    unittest.main()
