"""Behavioral regressions from the pooled-project validity audit."""

import importlib.util
import json
import shutil
import sys
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
import warnings
from unittest.mock import patch

import joblib
import numpy as np
import pandas as pd

from evaluation.feature_associations import association_statistics
from evaluation.metrics import bootstrap_many_conditions, calculate_metrics, metric_function
from evaluation.report_validation import check_table
from evaluation.resampling import bootstrap_indices
from evaluation.stratification import StratifiedGroupKFoldByColumns
from features.content_groups import content_group_ids, validate_group_labels
from models.condition_registry import BASELINE_NAMES, CONDITION_NAMES
from models.finetuned_bert import resolve_bert_settings
from scripts.generate_results import load_cv_files, required_training_outputs
from testing.test_multiplatform import PROJECT_ROOT, load_settings, synthetic_pooled_data


HAS_TRANSFORMERS = all(importlib.util.find_spec(name) for name in ("torch", "transformers"))
HAS_SENTENCE_TRANSFORMERS = HAS_TRANSFORMERS and importlib.util.find_spec("sentence_transformers") is not None


class PooledAuditTests(unittest.TestCase):
    def test_qwk_preserves_missing_ordinal_category_spacing(self):
        truth, predicted = np.array([1, 3, 4, 4]), np.array([3, 3, 4, 1])
        observed = np.mean((truth - predicted) ** 2)
        expected = np.mean((truth[:, None] - predicted[None, :]) ** 2)
        self.assertAlmostEqual(calculate_metrics(truth, predicted)["quadratic_weighted_kappa"], 1 - observed / expected)
        self.assertAlmostEqual(1 - observed / expected, -2 / 11)

    def test_fast_bootstrap_matches_scalar_metrics_for_every_replicate(self):
        truth = np.array([1, 3, 4, 4, 1, 3, 4, 4])
        first = np.array([3, 3, 4, 1, 1, 4, 4, 3])
        second = truth.copy()
        for groups in (None, np.array(["mixed", "b", "mixed", "d", "e", "f", "g", "h"])):
            intervals, differences = bootstrap_many_conditions(
                truth, {"first": first, "second": second}, resamples=40, seed=51, groups=groups
            )
            for row in intervals:
                calculate = metric_function(row["metric"])
                pred = first if row["condition"] == "first" else second
                values = [calculate(truth[index], pred[index]) for index in bootstrap_indices(truth, 40, 51, groups)]
                self.assertAlmostEqual(row["bootstrap_mean"], np.mean(values))
                np.testing.assert_allclose([row["ci_low"], row["ci_high"]], np.quantile(values, [.025, .975]), atol=1e-12)
            self.assertEqual(len(differences), 4)

    def test_cluster_draws_keep_mixed_platform_and_label_members_together(self):
        labels = np.array([1, 4, 2, 3, 1, 4])
        groups = np.array(["cross_platform", "cross_platform", "b", "c", "d", "e"])
        varied = False
        for selected in bootstrap_indices(labels, 30, 4, groups):
            counts = np.bincount(selected, minlength=6)
            self.assertEqual(counts[0], counts[1])
            varied |= len(selected) != len(labels)
        self.assertTrue(varied)

    def test_constant_association_is_explicit_and_cluster_pvalues_are_suppressed(self):
        frame = pd.DataFrame({"label": [1, 1, 2, 2, 3, 3, 4, 4], "varying": range(8), "constant": 0, "content_group": ["a", "a", "b", "c", "d", "e", "f", "g"]})
        result = association_statistics(frame, "training_only", 20, 8, feature_names=("varying", "constant"))
        constant = result.set_index("feature").loc["constant"]
        self.assertEqual(constant["association_status"], "constant_feature")
        self.assertEqual(constant["bootstrap_valid_resamples"], 0)
        self.assertTrue(result["spearman_p_value"].isna().all())
        self.assertTrue(result["resampling_unit"].eq("content_group").all())

    def test_exact_transcript_label_conflicts_are_advisory(self):
        frame = pd.DataFrame({"transcript": ["same", "same"], "label": [1, 4]})
        # Capture locally: assertWarnsRegex scans every imported module's
        # warning registry and can trigger unrelated optional lazy imports.
        with warnings.catch_warnings(record=True) as captured:
            warnings.simplefilter("always", UserWarning)
            validate_group_labels(frame)
        self.assertTrue(
            any(
                issubclass(item.category, UserWarning)
                and "execution is not blocked" in str(item.message)
                for item in captured
            ),
            "Expected the non-blocking conflicting-label UserWarning.",
        )
        self.assertEqual(len(set(content_group_ids(frame))), 1)
        self.assertEqual(frame["label"].tolist(), [1, 4])

    def test_bert_revision_resolves_before_tokenizer_and_stays_pinned(self):
        config = SimpleNamespace(_commit_hash="b" * 40)
        with patch("models.finetuned_bert.require_transformers"), patch("models.finetuned_bert.AutoConfig") as loader:
            loader.from_pretrained.return_value = config
            active = resolve_bert_settings({"model_name": "bert-base-uncased", "revision": None})
            again = resolve_bert_settings(active)
        self.assertEqual(active["resolved_revision"], "b" * 40)
        self.assertEqual(active, again)
        self.assertIsNone(active["revision"])
        loader.from_pretrained.assert_called_once()

    def test_bert_tokenizer_assets_are_required_beyond_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            tokenizer = root / "models/E_FINETUNED_BERT/tokenizer"
            tokenizer.mkdir(parents=True)
            (tokenizer / "tokenizer_config.json").write_text("{}")
            settings = {"evaluation": {"outer_folds": 2}, "reporting": {"include_baselines": True}}
            required = required_training_outputs(root, settings)["E_FINETUNED_BERT"]
            self.assertIn(tokenizer / "vocab.txt", required)

    def test_cv_loader_rejects_consistently_swapped_fold_numbers(self):
        frame = synthetic_pooled_data()
        settings = {"seed": 42, "split": {"stratification_columns": ["platform"]}, "evaluation": {"outer_folds": 2}, "reporting": {"include_baselines": True}}
        cv = StratifiedGroupKFoldByColumns(n_splits=2, random_state=42, stratification_columns=("platform",))
        assigned = np.zeros(len(frame), dtype=int)
        for fold, (_, validation) in enumerate(cv.split(frame, frame.label, content_group_ids(frame)), 1):
            assigned[validation] = 3 - fold
        predictions = frame[["row_index", "record_id", "platform"]].assign(fold=assigned, true_label=frame.label, prediction=frame.label)
        metrics = []
        for fold in (1, 2):
            selected = predictions.loc[predictions.fold.eq(fold)]
            values = calculate_metrics(selected.true_label, selected.prediction)
            metrics.append({"fold": fold, **{k: v for k, v in values.items() if k not in ("per_class", "confusion_matrix")}})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "predictions").mkdir(); (root / "metrics").mkdir()
            for condition in (*CONDITION_NAMES, *BASELINE_NAMES):
                predictions.to_csv(root / "predictions" / f"{condition}_cv.csv", index=False)
                pd.DataFrame(metrics).to_csv(root / "metrics" / f"{condition}_cv.csv", index=False)
            with self.assertRaisesRegex(ValueError, "replay"):
                load_cv_files(root, settings, frame)

    def test_changed_class_counts_with_the_same_total_are_rejected(self):
        expected = pd.DataFrame({"label": [1, 2, 3, 4], "count": [10, 20, 30, 40]})
        altered = expected.copy(); altered.loc[0, "count"] += 1; altered.loc[1, "count"] -= 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rq1.csv"
            altered.to_csv(path, index=False)
            with self.assertRaisesRegex(ValueError, "recalculated"):
                check_table(path, expected)

    def test_unused_blank_titles_do_not_block_pooled_loading(self):
        from scripts.multiplatform_data import load_multiplatform_data

        settings = load_settings()
        settings["data"]["sources"][1]["require_all_titles_placeholder"] = True
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            for source in settings["data"]["sources"]:
                data = pd.read_csv(PROJECT_ROOT / source["path"])
                data["title"] = ""
                data.to_csv(root / source["path"], index=False)
            with warnings.catch_warnings(record=True) as captured:
                warnings.simplefilter("always", UserWarning)
                combined, report = load_multiplatform_data(root, settings["data"])
            self.assertTrue(
                any(
                    issubclass(item.category, UserWarning)
                    and "Titles are excluded" in str(item.message)
                    for item in captured
                ),
                "Expected the excluded-title UserWarning.",
            )
            self.assertEqual(len(combined), settings["data"]["expected_rows"])
            self.assertEqual(report["modelled_rows"], int(combined["label"].notna().sum()))
            self.assertTrue(combined["title"].isna().all())

    def test_actual_grouped_partitions_must_cover_all_strata(self):
        data = synthetic_pooled_data()
        # Feasibility counts alone cannot guarantee the heuristic's output.
        first = np.flatnonzero(data.platform.eq("youtube"))
        second = np.flatnonzero(data.platform.eq("tiktok"))
        splitter = StratifiedGroupKFoldByColumns(n_splits=2, stratification_columns=("platform",))
        with patch("evaluation.stratification.StratifiedGroupKFold.split", return_value=iter([(first, second), (second, first)])):
            with self.assertRaisesRegex(ValueError, "represent every requested stratum"):
                list(splitter.split(data, data.label, content_group_ids(data)))

    def test_bert_rejects_a_conflicting_pinned_commit(self):
        with self.assertRaisesRegex(ValueError, "different commit"):
            resolve_bert_settings({"model_name": "local", "revision": "a" * 40, "resolved_revision": "b" * 40})

    def test_completed_condition_receipt_survives_a_later_training_failure(self):
        from scripts import train_models
        from evaluation.reproducibility import sha256_file

        original_cv = train_models.run_nested_cross_validation
        calls = 0

        def fail_second_condition(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise RuntimeError("simulated later condition failure")
            return original_cv(*args, **kwargs)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            shutil.copytree(
                PROJECT_ROOT,
                root,
                ignore=shutil.ignore_patterns(
                    "__pycache__", "*.pyc", "results", ".venv", "venv", ".git"
                ),
            )
            with patch.object(train_models, "PROJECT_ROOT", root), patch.object(sys, "argv", ["train_models", "--config", "configs/experiment_multiplatform.yaml", "--model", "baselines"]), patch.object(train_models, "run_nested_cross_validation", side_effect=fail_second_condition):
                with self.assertRaisesRegex(RuntimeError, "simulated later"):
                    train_models.main()
            run_name = load_settings()["reporting"]["default_run_name"]
            receipts = list((root / "results" / run_name / "reproducibility").glob("run_*.json"))
            self.assertEqual(len(receipts), 1)
            receipt = json.loads(receipts[0].read_text())
            self.assertEqual(receipt["completed_conditions"], ["BASELINE_MOST_FREQUENT"])
            self.assertTrue(receipt["output_files"])
            for record in receipt["output_files"]:
                self.assertEqual(sha256_file(root / record["path"]), record["sha256"])

    @unittest.skipUnless(HAS_TRANSFORMERS, "Requires PyTorch and Transformers")
    def test_real_bert_training_save_and_offline_reload(self):
        import torch
        from transformers import BertConfig, BertModel, BertTokenizerFast
        from models.finetuned_bert import train_bert_model, predict_bert, load_bert_artifacts

        torch.set_num_threads(1)
        data = synthetic_pooled_data()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vocabulary = root / "vocab.txt"
            vocabulary.write_text("[PAD]\n[UNK]\n[CLS]\n[SEP]\n[MASK]\ntranscript\naccurate\nslight\nmoderate\nsevere\nevidence\n")
            tokenizer = BertTokenizerFast(vocab_file=str(vocabulary))
            encoder = BertModel(BertConfig(vocab_size=11, hidden_size=12, num_hidden_layers=1, num_attention_heads=3, intermediate_size=24))
            encoder.config._commit_hash = "b" * 40
            settings = {"model_name": "local-test-encoder", "revision": None, "resolved_revision": "b" * 40, "expected_hidden_size": 12, "max_length": 16, "batch_size": 8, "learning_rate": .001, "max_epochs": 1, "seed": 42, "text_columns": ["transcript"], "engagement_transform": "within_platform_percentile"}
            fitted = train_bert_model(data, None, settings, fixed_epochs=1, output_directory=root / "saved", tokenizer=tokenizer, encoder=encoder, device="cpu")
            original = predict_bert(fitted, data, device="cpu")
            self.assertNotIn("_commit_hash", tokenizer.init_kwargs)
            meta = json.loads((root / "saved/checkpoint_metadata.json").read_text())
            self.assertEqual(meta["tokenizer_commit_hash"], "b" * 40)
            restored = load_bert_artifacts(root / "saved", device="cpu")
            replayed = predict_bert(restored, data, device="cpu")
            pd.testing.assert_frame_equal(original, replayed, atol=1e-7, rtol=1e-7)
            self.assertTrue(np.isfinite(pd.DataFrame(fitted.history).to_numpy()).all())

    @unittest.skipUnless(HAS_SENTENCE_TRANSFORMERS, "Requires Sentence Transformers")
    def test_real_sentence_transformer_classifier_save_and_reload(self):
        import torch
        from transformers import BertConfig, BertModel, BertTokenizerFast
        from sentence_transformers import SentenceTransformer, models
        from features.transformer_features import load_minilm_encoder
        from models.frozen_minilm import FrozenMiniLMClassifier

        torch.set_num_threads(1)
        data = synthetic_pooled_data()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            vocab = root / "vocab.txt"
            vocab.write_text("[PAD]\n[UNK]\n[CLS]\n[SEP]\n[MASK]\ntranscript\naccurate\nslight\nmoderate\nsevere\n")
            BertTokenizerFast(vocab_file=str(vocab)).save_pretrained(root / "encoder")
            BertModel(BertConfig(vocab_size=10, hidden_size=12, num_hidden_layers=1, num_attention_heads=3, intermediate_size=24)).save_pretrained(root / "encoder")
            transformer = models.Transformer(str(root / "encoder"), max_seq_length=16)
            SentenceTransformer(modules=[transformer, models.Pooling(12)], device="cpu").save(str(root / "sentence"))
            fitted = FrozenMiniLMClassifier(model_name=str(root / "sentence"), revision="b" * 40, expected_embedding_dimension=12, expected_max_sequence_length=16, device="cpu", text_columns=("transcript",), engagement_transform="within_platform_percentile").fit(data, data.label)
            before = fitted.predict_proba(data)
            joblib.dump(fitted, root / "model.joblib")
            load_minilm_encoder.cache_clear()
            restored = joblib.load(root / "model.joblib")
            np.testing.assert_allclose(before, restored.predict_proba(data), atol=1e-7)
            np.testing.assert_allclose(before[:1], restored.predict_proba(data.iloc[:1]), atol=1e-7)


if __name__ == "__main__":
    unittest.main()
