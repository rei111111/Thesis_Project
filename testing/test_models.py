from __future__ import annotations

import importlib.util
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

import joblib
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
    run_bert,
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
    max_seq_length = 256

    def encode(self, texts: list[str], **_: object) -> np.ndarray:
        embeddings = np.zeros((len(texts), 384), dtype=np.float32)
        for index, text in enumerate(texts):
            embeddings[index, 0] = len(text)
            embeddings[index, 1] = sum(character.isdigit() for character in text)
            embeddings[index, 2 + (index % 4)] = 1.0
        return embeddings


class FakeRevisionedSentenceEncoder(FakeSentenceEncoder):
    def _first_module(self) -> object:
        return types.SimpleNamespace(
            auto_model=types.SimpleNamespace(
                config=types.SimpleNamespace(_commit_hash="f" * 40)
            )
        )


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

    def test_text_token_named_label_is_not_mistaken_for_source_leakage(self) -> None:
        data = model_frame()
        data["transcript"] = data["transcript"] + " label"
        model = build_logistic_regression("A", max_features=100).fit(
            data.drop(columns=["label"]), data["label"]
        )
        self.assertIn(
            "text__label",
            set(model.named_steps["features"].get_feature_names_out()),
        )
        ensure_no_prohibited_predictors(model, "A_LOGISTIC_REGRESSION")

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

    def test_saved_minilm_reloads_the_resolved_checkpoint_revision(self) -> None:
        data = model_frame()
        initial_encoder = FakeRevisionedSentenceEncoder()
        with patch(
            "models.frozen_minilm.load_minilm_encoder",
            return_value=initial_encoder,
        ):
            model = FrozenMiniLMClassifier().fit(
                data.drop(columns=["label"]), data["label"]
            )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "estimator.joblib"
            joblib.dump(model, path)
            restored = joblib.load(path)
            reloaded_encoder = FakeRevisionedSentenceEncoder()
            with patch(
                "models.frozen_minilm.load_minilm_encoder",
                return_value=reloaded_encoder,
            ) as loader:
                restored.predict(data.drop(columns=["label"]))
        self.assertEqual(loader.call_args.args[2], "f" * 40)

    def test_bert_run_checks_revisions_and_saves_heldout_predictions(self) -> None:
        data = model_frame(rows_per_class=1)
        training = data.copy()
        heldout = data.copy()
        settings = {"seed": 42, "evaluation": {"outer_folds": 2}}
        bert_settings = {"model_name": "bert-base-uncased", "resolved_revision": "a" * 40}
        lexicons = {"certainty_terms": ("clearly",), "hedge_terms": ("may",)}
        revision = "a" * 40

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            metrics = root / "metrics"
            predictions = root / "predictions"
            models = root / "models"
            interpretability = root / "interpretability"
            for path in (metrics, predictions, models, interpretability):
                path.mkdir()

            def fake_outer_cv(**kwargs: object) -> object:
                output = Path(str(kwargs["output_directory"]))
                for fold in (1, 2):
                    fold_directory = output / f"fold_{fold}"
                    fold_directory.mkdir(parents=True)
                    (fold_directory / "fold_training_record.json").write_text(
                        '{"encoder_commit_hash":"'
                        + revision
                        + '","tokenizer_commit_hash":"'
                        + revision
                        + '"}',
                        encoding="utf-8",
                    )
                return types.SimpleNamespace(best_epochs=[1, 2])

            def fake_final_bert(**kwargs: object) -> pd.DataFrame:
                output = Path(str(kwargs["output_directory"]))
                output.mkdir(parents=True, exist_ok=True)
                (output / "checkpoint_metadata.json").write_text(
                    '{"encoder_commit_hash":"'
                    + revision
                    + '","tokenizer_commit_hash":"'
                    + revision
                    + '"}',
                    encoding="utf-8",
                )
                return pd.DataFrame(
                    {
                        "row_index": heldout["row_index"],
                        "condition": "E_FINETUNED_BERT",
                        "true_label": heldout["label"],
                        "prediction": heldout["label"],
                    }
                )

            with (
                patch(
                    "scripts.train_models.result_paths",
                    return_value=(metrics, predictions, models, interpretability),
                ),
                patch(
                    "scripts.train_models.run_bert_outer_cross_validation",
                    side_effect=fake_outer_cv,
                ),
                patch("scripts.train_models.save_cross_validation_result"),
                patch(
                    "scripts.train_models.fit_final_bert",
                    side_effect=fake_final_bert,
                ),
                patch("scripts.train_models.save_heldout_predictions") as save,
            ):
                run_bert(
                    training,
                    heldout,
                    settings,
                    bert_settings,
                    lexicons,
                    overwrite=False,
                    device=None,
                    run_name="primary",
                )

        save.assert_called_once()

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
