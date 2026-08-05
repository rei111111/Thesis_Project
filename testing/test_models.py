from __future__ import annotations

import importlib.util
import types
import unittest

import numpy as np
import pandas as pd

from models.frozen_minilm import FrozenMiniLMClassifier
from models.logistic_regression import build_logistic_regression
from models.complement_naive_bayes import build_complement_naive_bayes
from models.decision_tree import build_decision_tree
from models.condition_registry import CONDITION_NAMES
from scripts.train_models import (
    ensure_iterative_estimator_converged,
    ensure_no_prohibited_predictors,
)
from models.ridge_classifier import build_ridge_classifier


def model_frame(rows_per_class: int = 4) -> pd.DataFrame:
    rows = []
    for label in range(1, 5):
        for index in range(rows_per_class):
            rows.append(
                {
                    "row_index": len(rows),
                    "title": f"Class {label}",
                    "transcript": (
                        f"classword{label} information example number {index}"
                    ),
                    "likes": 10 * label + index,
                    "comments": label + index,
                    "views": 100 * label + index,
                    "duration_sec": 20 + label,
                    "label": label,
                }
            )
    return pd.DataFrame(rows)


class FakeSentenceEncoder:
    def encode(self, texts: list[str], **_: object) -> np.ndarray:
        embeddings = np.zeros((len(texts), 384), dtype=np.float32)
        for index, text in enumerate(texts):
            embeddings[index, 0] = len(text)
            embeddings[index, 1] = sum(character.isdigit() for character in text)
            embeddings[index, 2 + (index % 4)] = 1.0
        return embeddings


class ModelTests(unittest.TestCase):
    def test_registry_contains_exactly_fourteen_experimental_conditions(self) -> None:
        self.assertEqual(len(CONDITION_NAMES), 14)
        self.assertEqual(len(set(CONDITION_NAMES)), 14)

    def test_nonconverged_iterative_fit_is_rejected(self) -> None:
        estimator = types.SimpleNamespace(
            classifier_=types.SimpleNamespace(n_iter_=np.asarray([2000]), max_iter=2000)
        )
        with self.assertRaisesRegex(RuntimeError, "without a confirmed"):
            ensure_iterative_estimator_converged(estimator, "TEST")

    def test_fitted_pipeline_contains_no_annotation_leakage(self) -> None:
        data = model_frame()
        model = build_logistic_regression("C", max_features=50).fit(
            data.drop(columns=["label"]), data["label"]
        )
        ensure_no_prohibited_predictors(model, "C_LOGISTIC_REGRESSION")

    def test_all_twelve_interpretable_conditions_fit_and_predict(self) -> None:
        data = model_frame()
        builders = (
            build_logistic_regression,
            build_ridge_classifier,
            build_complement_naive_bayes,
            build_decision_tree,
        )
        for builder in builders:
            for feature_set in ("A", "B", "C"):
                model = builder(feature_set, max_features=50)
                model.fit(data.drop(columns=["label"]), data["label"])
                predictions = model.predict(data.drop(columns=["label"]))
                self.assertEqual(len(predictions), len(data))
                self.assertTrue(set(predictions).issubset({1, 2, 3, 4}))

    def test_ridge_fits_and_predicts_all_feature_sets(self) -> None:
        data = model_frame()
        for feature_set in ("A", "B", "C"):
            model = build_ridge_classifier(feature_set, max_features=50)
            model.fit(data.drop(columns=["label"]), data["label"])
            predictions = model.predict(data.drop(columns=["label"]))
            self.assertEqual(len(predictions), len(data))
            self.assertTrue(set(predictions).issubset({1, 2, 3, 4}))
            ensure_iterative_estimator_converged(model, f"{feature_set}_RIDGE")

    def test_frozen_minilm_derives_six_features_from_raw_csv_inputs(self) -> None:
        data = model_frame()
        model = FrozenMiniLMClassifier(encoder=FakeSentenceEncoder())
        model.fit(data.drop(columns=["label"]), data["label"])
        predictions = model.predict(data.drop(columns=["label"]))
        self.assertEqual(model.embedding_dimension_, 384)
        self.assertEqual(model.auxiliary_dimension_, 6)
        self.assertEqual(len(predictions), len(data))

    @unittest.skipUnless(
        importlib.util.find_spec("torch") is not None,
        "torch is not installed in this lightweight test environment",
    )
    def test_bert_head_outputs_four_logits(self) -> None:
        import torch

        from models.finetuned_bert import BertMetadataClassifier

        class FakeBert(torch.nn.Module):
            def __init__(self) -> None:
                super().__init__()
                self.config = types.SimpleNamespace(hidden_size=8)

            def forward(self, input_ids: object, **_: object) -> object:
                batch_size = input_ids.shape[0]
                pooled = torch.ones((batch_size, 8), dtype=torch.float32)
                return types.SimpleNamespace(pooler_output=pooled)

        model = BertMetadataClassifier(encoder=FakeBert())
        output = model(
            input_ids=torch.ones((3, 5), dtype=torch.long),
            attention_mask=torch.ones((3, 5), dtype=torch.long),
            metadata=torch.ones((3, 6), dtype=torch.float32),
        )
        self.assertEqual(tuple(output["logits"].shape), (3, 4))


if __name__ == "__main__":
    unittest.main()
