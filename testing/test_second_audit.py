"""Behavioral regressions from the audit of archive 0921153e."""

import importlib.util
import pickle
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.compose import ColumnTransformer
from sklearn.exceptions import NotFittedError
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.tree import DecisionTreeClassifier

from evaluation.interpretability import local_tree_paths, tree_rule_text
from features.linguistic_features import count_linguistic_matches
from models.frozen_minilm import FrozenMiniLMClassifier
from testing.test_multiplatform import synthetic_pooled_data

HAS_TORCH = importlib.util.find_spec("torch") is not None


class SmallSentenceEncoder:
    max_seq_length = 16

    def __init__(self, revision):
        self.revision = revision

    def _first_module(self):
        return SimpleNamespace(auto_model=SimpleNamespace(config=SimpleNamespace(_commit_hash=self.revision)))

    def encode(self, texts, **kwargs):
        return np.asarray([[len(text), text.count("e")] for text in texts], dtype=np.float32)


def sentence_model():
    return FrozenMiniLMClassifier(
        model_name="old-model", revision="a" * 40,
        expected_embedding_dimension=2, expected_max_sequence_length=16,
        text_columns=("transcript",), engagement_transform="within_platform_percentile",
    )


class SecondAuditTests(unittest.TestCase):
    def test_minilm_refit_uses_new_model_and_revision(self):
        data = synthetic_pooled_data()
        first, second = SmallSentenceEncoder("a" * 40), SmallSentenceEncoder("b" * 40)
        with patch("models.frozen_minilm.load_minilm_encoder", side_effect=[first, second]) as load:
            model = sentence_model().fit(data, data.label)
            model.set_params(model_name="new-model", revision="b" * 40).fit(data, data.label)
            load.assert_called_with("new-model", None, "b" * 40)
        self.assertEqual(model.model_revision_, "b" * 40)
        self.assertIs(model.encoder_, second)

    def test_deserialized_minilm_refit_does_not_pin_to_previous_fit(self):
        data = synthetic_pooled_data()
        with patch("models.frozen_minilm.load_minilm_encoder", return_value=SmallSentenceEncoder("a" * 40)):
            model = sentence_model().fit(data, data.label)
        restored = pickle.loads(pickle.dumps(model))
        with patch("models.frozen_minilm.load_minilm_encoder", return_value=SmallSentenceEncoder("b" * 40)) as load:
            restored.set_params(revision="b" * 40).fit(data, data.label)
            load.assert_called_with("old-model", None, "b" * 40)
        self.assertEqual(restored.model_revision_, "b" * 40)

    def test_failed_refit_cannot_predict_with_stale_classifier(self):
        data = synthetic_pooled_data()
        with patch("models.frozen_minilm.load_minilm_encoder", return_value=SmallSentenceEncoder("a" * 40)):
            model = sentence_model().fit(data, data.label)
        with patch("models.frozen_minilm.load_minilm_encoder", side_effect=RuntimeError("checkpoint unavailable")):
            with self.assertRaisesRegex(RuntimeError, "checkpoint unavailable"):
                model.set_params(model_name="new-model").fit(data, data.label)
        with self.assertRaises(NotFittedError):
            model.predict(data)

    def test_minilm_refuses_a_different_explicit_checkpoint(self):
        data = synthetic_pooled_data()
        with patch("models.frozen_minilm.load_minilm_encoder", return_value=SmallSentenceEncoder("b" * 40)):
            with self.assertRaisesRegex(RuntimeError, "different checkpoint"):
                sentence_model().fit(data, data.label)

    def test_tree_explanation_follows_float32_branch_in_dense_and_sparse_inputs(self):
        for use_sparse in (False, True):
            with self.subTest(sparse=use_sparse):
                transformer = FunctionTransformer(
                    sparse.csr_matrix if use_sparse else None,
                    feature_names_out="one-to-one",
                )
                model = Pipeline([
                    ("features", ColumnTransformer(
                        [("text", transformer, ["x"])],
                        sparse_threshold=1.0 if use_sparse else 0.0,
                    )),
                    ("classifier", DecisionTreeClassifier(max_depth=1, random_state=1)),
                ]).fit(pd.DataFrame({"x": [0., 1.]}), [1, 4])
                data = pd.DataFrame({"row_index": [0], "x": [.50000001]})
                self.assertEqual(sparse.issparse(model.named_steps["features"].transform(data)), use_sparse)
                self.assertEqual(model.predict(data).tolist(), [1])
                path = local_tree_paths(model, data, "tree")
                root = path.loc[path.node_id.eq(0)].iloc[0]
                self.assertEqual(root["operator"], "<=")
                self.assertEqual(root["transformed_value"], .5)
                leaf = int(path.loc[path.is_leaf, "node_id"].iloc[0])
                self.assertEqual(leaf, model.named_steps["classifier"].tree_.children_left[0])

    def test_tree_rules_preserve_threshold_and_feature_identity(self):
        data = pd.DataFrame({"x": [.12345678, .12345698]})
        model = Pipeline([
            ("features", ColumnTransformer([("text", "passthrough", ["x"]), ("engagement", "passthrough", ["x"])])),
            ("classifier", DecisionTreeClassifier(max_depth=1, random_state=1)),
        ]).fit(data, [1, 4])
        tree = model.named_steps["classifier"].tree_
        self.assertEqual(tree.node_count, 3)
        rule = tree_rule_text(model)
        selected_name = model.named_steps["features"].get_feature_names_out()[tree.feature[0]]
        self.assertIn(f"if {selected_name} <= {repr(float(tree.threshold[0]))}:", rule)
        self.assertIn("float32", rule)
        self.assertIn("predict class 1", rule)
        self.assertIn("predict class 4", rule)

    def test_lexicon_index_preserves_longest_match_and_configuration_changes(self):
        tokens = "alpha beta alpha beta gamma alpha".split()
        certainty, hedge = ("alpha beta", "gamma"), ("alpha", "delta")
        self.assertEqual(count_linguistic_matches(tokens, certainty, hedge), (3, 1))
        self.assertEqual(count_linguistic_matches(tokens, hedge, certainty), (1, 3))
        self.assertEqual(count_linguistic_matches(tokens, certainty, hedge), (3, 1))

    @unittest.skipUnless(HAS_TORCH, "Requires PyTorch")
    def test_bert_validation_loss_matches_whole_weighted_population(self):
        import torch
        from models.finetuned_bert import _validation_predictions

        class Fixed(torch.nn.Module):
            def forward(self, input_ids, labels, class_weights):
                return {"logits": input_ids, "loss": torch.nn.functional.cross_entropy(input_ids, labels, weight=class_weights)}

        logits = torch.tensor([[4., 1., 0., 0.], [0., 1., 4., 0.], [0., 1., 0., 4.]])
        labels = torch.tensor([0, 1, 3])
        weights = torch.tensor([1., 5., 2., 3.])
        expected = torch.nn.functional.cross_entropy(logits, labels, weight=weights).item()
        for batch_size in (1, 2, 3):
            loader = [{"input_ids": logits[i:i + batch_size], "labels": labels[i:i + batch_size]} for i in range(0, 3, batch_size)]
            truth, predictions, loss = _validation_predictions(Fixed(), loader, torch.device("cpu"), weights)
            self.assertAlmostEqual(loss, expected, places=6)
            self.assertEqual(truth.tolist(), [1, 2, 4])
            self.assertEqual(predictions.tolist(), [1, 3, 4])

    @unittest.skipUnless(HAS_TORCH, "Requires PyTorch")
    def test_nonfinite_logits_cannot_become_apparently_valid_class_one(self):
        import torch
        from models.finetuned_bert import _validation_predictions

        class Broken(torch.nn.Module):
            def forward(self, input_ids, labels, class_weights):
                return {"logits": torch.full((len(labels), 4), float("nan")), "loss": torch.tensor(0.)}

        with self.assertRaisesRegex(FloatingPointError, "non-finite logits"):
            _validation_predictions(Broken(), [{"input_ids": torch.ones(1, 4), "labels": torch.tensor([0])}], torch.device("cpu"), torch.ones(4))

    @unittest.skipUnless(HAS_TORCH, "Requires PyTorch")
    def test_nonfinite_training_loss_is_rejected(self):
        import torch
        from models.finetuned_bert import _weighted_loss_parts

        with self.assertRaisesRegex(FloatingPointError, "non-finite loss"):
            _weighted_loss_parts(torch.tensor(float("inf")), torch.tensor([0]), torch.ones(4))


if __name__ == "__main__":
    unittest.main()
