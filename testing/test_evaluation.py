from __future__ import annotations

import unittest
import tempfile
import json
from pathlib import Path

import numpy as np
import pandas as pd

from evaluation.cross_validation import run_nested_cross_validation
from evaluation.feature_associations import NAMED_FEATURES, association_statistics
from evaluation.metrics import (
    bootstrap_many_conditions,
    calculate_metrics,
    paired_stratified_bootstrap,
)
from models.condition_registry import BASELINE_NAMES, CONDITION_NAMES
from scripts.generate_results import load_cv_files, load_prediction_files
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

    def test_metric_validation_rejects_fractional_labels_before_casting(self) -> None:
        with self.assertRaisesRegex(ValueError, "without truncation"):
            calculate_metrics([1, 2, 3, 4], [1, 2.9, 3, 4])

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

    def test_named_feature_bootstrap_records_its_complete_protocol(self) -> None:
        labels = np.repeat([1, 2, 3, 4], 3)
        features = pd.DataFrame({"label": labels})
        for offset, name in enumerate(NAMED_FEATURES):
            features[name] = labels + np.arange(len(labels)) * (offset + 1) / 100
        result = association_statistics(
            features,
            population="training_only",
            bootstrap_resamples=20,
            seed=42,
            confidence_level=0.95,
        )
        self.assertEqual(set(result["feature"]), set(NAMED_FEATURES))
        self.assertTrue(result["bootstrap_resamples_requested"].eq(20).all())
        self.assertTrue(result["bootstrap_valid_resamples"].eq(20).all())
        self.assertTrue(result["bootstrap_confidence_level"].eq(0.95).all())

    def test_result_loader_rejects_collectively_stale_heldout_rows(self) -> None:
        settings = {
            "reporting": {"include_baselines": True},
            "evaluation": {"outer_folds": 2},
        }
        expected = pd.DataFrame(
            {"row_index": [10, 11, 12, 13], "label": [1, 2, 3, 4]}
        )
        stale = pd.DataFrame(
            {
                "row_index": [20, 21, 22, 23],
                "true_label": [1, 2, 3, 4],
                "prediction": [1, 2, 3, 4],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            predictions = Path(directory) / "predictions"
            predictions.mkdir()
            for condition in (*CONDITION_NAMES, *BASELINE_NAMES):
                frame = stale.copy()
                frame.insert(1, "condition", condition)
                frame.to_csv(
                    predictions / f"{condition}_heldout.csv",
                    index=False,
                )
            with self.assertRaisesRegex(ValueError, "Held-out prediction"):
                load_prediction_files(Path(directory), settings, expected)

    def test_result_loader_recalculates_saved_cv_metrics(self) -> None:
        settings = {
            "reporting": {"include_baselines": True},
            "evaluation": {"outer_folds": 2},
        }
        labels = np.tile([1, 2, 3, 4], 2)
        predictions = pd.DataFrame(
            {
                "row_index": np.arange(8),
                "fold": np.repeat([1, 2], 4),
                "true_label": labels,
                "prediction": labels,
            }
        )
        rows = []
        for fold in (1, 2):
            metrics = calculate_metrics(
                predictions.loc[predictions["fold"].eq(fold), "true_label"],
                predictions.loc[predictions["fold"].eq(fold), "prediction"],
            )
            rows.append(
                {
                    "fold": fold,
                    "quadratic_weighted_kappa": metrics[
                        "quadratic_weighted_kappa"
                    ],
                    "accuracy": metrics["accuracy"],
                    "weighted_f1": metrics["weighted_f1"],
                    "mean_absolute_error": metrics["mean_absolute_error"],
                }
            )
        rows[0]["accuracy"] = 0.5
        condition = CONDITION_NAMES[0]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "metrics").mkdir()
            (root / "predictions").mkdir()
            pd.DataFrame(rows).to_csv(
                root / "metrics" / f"{condition}_cv.csv",
                index=False,
            )
            predictions.to_csv(
                root / "predictions" / f"{condition}_cv.csv",
                index=False,
            )
            with self.assertRaisesRegex(ValueError, "does not match"):
                load_cv_files(root, settings)

    def test_result_loader_recalculates_individual_heldout_metric_json(self) -> None:
        settings = {
            "reporting": {"include_baselines": True},
            "evaluation": {"outer_folds": 2},
        }
        expected = pd.DataFrame(
            {"row_index": [10, 11, 12, 13], "label": [1, 2, 3, 4]}
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "metrics").mkdir()
            (root / "predictions").mkdir()
            for condition in (*CONDITION_NAMES, *BASELINE_NAMES):
                frame = pd.DataFrame(
                    {
                        "row_index": expected["row_index"],
                        "condition": condition,
                        "true_label": expected["label"],
                        "prediction": expected["label"],
                    }
                )
                frame.to_csv(
                    root / "predictions" / f"{condition}_heldout.csv",
                    index=False,
                )
                metrics = calculate_metrics(frame["true_label"], frame["prediction"])
                if condition == CONDITION_NAMES[0]:
                    metrics["accuracy"] = 0.5
                (root / "metrics" / f"{condition}_heldout.json").write_text(
                    json.dumps(metrics), encoding="utf-8"
                )
            with self.assertRaisesRegex(ValueError, "does not match"):
                load_prediction_files(root, settings, expected)

    def test_cv_loader_rejects_near_duplicate_content_split_across_folds(self) -> None:
        settings = {
            "reporting": {"include_baselines": True},
            "evaluation": {"outer_folds": 2},
        }
        training = model_frame(rows_per_class=2)
        long_text = " ".join(f"token{index}" for index in range(30))
        training.loc[0, "transcript"] = long_text
        duplicate = training.iloc[[0]].copy()
        duplicate["row_index"] = 99
        duplicate["transcript"] = long_text + " extra"
        training = pd.concat([training, duplicate], ignore_index=True)
        assignments = pd.DataFrame(
            {
                "row_index": training["row_index"],
                "fold": [1, 1, 1, 1, 2, 2, 2, 2, 2],
                "true_label": training["label"],
                "prediction": training["label"],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "metrics").mkdir()
            (root / "predictions").mkdir()
            metric_rows = []
            for fold in (1, 2):
                selected = assignments.loc[assignments["fold"].eq(fold)]
                metrics = calculate_metrics(
                    selected["true_label"], selected["prediction"]
                )
                metric_rows.append(
                    {"fold": fold, **{name: metrics[name] for name in (
                        "quadratic_weighted_kappa",
                        "accuracy",
                        "weighted_f1",
                        "mean_absolute_error",
                    )}}
                )
            for condition in (*CONDITION_NAMES, *BASELINE_NAMES):
                assignments.to_csv(
                    root / "predictions" / f"{condition}_cv.csv", index=False
                )
                pd.DataFrame(metric_rows).to_csv(
                    root / "metrics" / f"{condition}_cv.csv", index=False
                )
            with self.assertRaisesRegex(ValueError, "near-duplicate"):
                load_cv_files(root, settings, training)


if __name__ == "__main__":
    unittest.main()
