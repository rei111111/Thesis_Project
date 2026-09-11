from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import pandas as pd

from evaluation.interpretability import (
    aggregate_fold_stability,
    extract_global_features,
    local_linear_contributions,
    local_tree_paths,
    save_interpretability_artifacts,
    extract_minilm_auxiliary_features,
    save_minilm_auxiliary_artifacts,
    select_top_features,
)
from models.decision_tree import build_decision_tree
from models.logistic_regression import build_logistic_regression
from testing.test_models import model_frame
from testing.test_models import FakeSentenceEncoder
from models.frozen_minilm import FrozenMiniLMClassifier


class InterpretabilityTests(unittest.TestCase):
    def test_linear_exports_named_scores_and_local_contributions(self) -> None:
        data = model_frame(rows_per_class=5)
        model = build_logistic_regression("C", max_features=50).fit(
            data.drop(columns=["label"]), data["label"]
        )
        features = extract_global_features(model, "C_LOGISTIC_REGRESSION")
        self.assertIn("certainty_score", set(features["feature"]))
        self.assertIn("hedge_score", set(features["feature"]))
        local = local_linear_contributions(
            model, data, "C_LOGISTIC_REGRESSION", top_k=4
        )
        self.assertEqual(local.groupby("row_index").size().min(), 4)

    def test_tree_exports_exact_paths(self) -> None:
        data = model_frame(rows_per_class=5)
        model = build_decision_tree("C", max_features=50).fit(
            data.drop(columns=["label"]), data["label"]
        )
        paths = local_tree_paths(model, data, "C_DECISION_TREE")
        self.assertEqual(paths.loc[paths["is_leaf"]].groupby("row_index").size().min(), 1)

    def test_fold_stability_counts_missing_vocabulary_as_zero(self) -> None:
        data = model_frame(rows_per_class=5)
        fold_frames = []
        models = []
        for fold in range(1, 3):
            model = build_logistic_regression("A", max_features=10 + fold).fit(
                data.drop(columns=["label"]), data["label"]
            )
            models.append(model)
            fold_frames.append(
                extract_global_features(model, "A_LOGISTIC_REGRESSION", fold=fold)
            )
        stability = aggregate_fold_stability(
            pd.concat(fold_frames, ignore_index=True), fold_count=2, top_k=3
        )
        self.assertTrue(stability["fold_presence_fraction"].le(1.0).all())

    def test_complete_interpretability_artifacts_are_written(self) -> None:
        data = model_frame(rows_per_class=5)
        model = build_logistic_regression("C", max_features=40).fit(
            data.drop(columns=["label"]), data["label"]
        )
        with tempfile.TemporaryDirectory() as directory:
            summary = save_interpretability_artifacts(
                model,
                [model, model],
                data,
                "C_LOGISTIC_REGRESSION",
                directory,
                top_k=3,
                local_top_k=2,
            )
            self.assertGreater(summary["global_feature_rows"], 0)
            self.assertTrue(
                (Path(directory) / "C_LOGISTIC_REGRESSION_feature_stability.csv").exists()
            )

    def test_minilm_exports_only_six_named_auxiliary_dimensions(self) -> None:
        data = model_frame(rows_per_class=5)
        model = FrozenMiniLMClassifier(encoder=FakeSentenceEncoder()).fit(
            data.drop(columns=["label"]), data["label"]
        )
        features = extract_minilm_auxiliary_features(model)
        self.assertEqual(len(features), 24)
        self.assertEqual(features["feature"].nunique(), 6)
        with tempfile.TemporaryDirectory() as directory:
            summary = save_minilm_auxiliary_artifacts(
                model,
                [model, model],
                data.drop(columns=["label"]),
                directory,
            )
            self.assertEqual(summary["unnamed_embedding_dimensions_excluded"], 384)

    def test_top_feature_views_have_correct_sign_and_unique_ranks(self) -> None:
        data = model_frame(rows_per_class=5)
        model = build_logistic_regression("C", max_features=50).fit(
            data.drop(columns=["label"]), data["label"]
        )
        features = extract_global_features(model, "C_LOGISTIC_REGRESSION")
        for _, group in features.dropna(subset=["absolute_rank"]).groupby(
            "class_label"
        ):
            self.assertEqual(
                group["absolute_rank"].nunique(), len(group["absolute_rank"])
            )
        selected = select_top_features(features, top_k=4)
        positive = selected.loc[selected["ranking_view"].eq("largest_positive")]
        negative = selected.loc[selected["ranking_view"].eq("largest_negative")]
        self.assertTrue(positive["weight"].gt(0).all())
        self.assertTrue(negative["weight"].lt(0).all())

    def test_zero_importance_tree_features_are_not_reported_as_top(self) -> None:
        data = model_frame(rows_per_class=5)
        model = build_decision_tree("C", max_features=50).fit(
            data.drop(columns=["label"]), data["label"]
        )
        features = extract_global_features(model, "C_DECISION_TREE")
        selected = select_top_features(features, top_k=30)
        self.assertTrue(selected["weight"].gt(0).all())
        self.assertLessEqual(len(selected), 30)


if __name__ == "__main__":
    unittest.main()
