"""Regression tests for the additive pooled YouTube/TikTok experiment."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
import json
import shutil
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd
import yaml

from evaluation.stratification import StratifiedGroupKFoldByColumns
from evaluation.metrics import calculate_metrics
from evaluation.cross_validation import _grouped_early_stopping_split
from features.content_groups import content_group_ids
from features.linguistic_features import LinguisticFeatureExtractor
from features.metadata_features import WithinPlatformPercentileTransformer
from features.transformer_features import BertVideoDataset, encode_minilm
from models.complement_naive_bayes import build_complement_naive_bayes
from models.decision_tree import build_decision_tree
from models.logistic_regression import build_logistic_regression
from models.frozen_minilm import FrozenMiniLMClassifier
from models.ridge_classifier import build_ridge_classifier
from scripts.multiplatform_data import (
    load_multiplatform_data,
    load_multiplatform_saved_split,
    validate_multiplatform_experiment,
    verify_multiplatform_split,
)
from scripts.generate_results import (
    load_cv_files,
    platform_heldout_tables,
    training_input_files,
)
from scripts.prepare_data import file_sha256


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "configs/experiment_multiplatform.yaml"


def load_settings() -> dict[str, object]:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def synthetic_pooled_data() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    class_words = {1: "accurate", 2: "slight", 3: "moderate", 4: "severe"}
    for index in range(32):
        label = index % 4 + 1
        platform = "youtube" if (index // 4) % 2 == 0 else "tiktok"
        rows.append(
            {
                "row_index": index,
                "record_id": f"{platform}:{index:06d}",
                "platform": platform,
                "source_row": index,
                "title": "titleonlysentinel",
                "transcript": (
                    f"{class_words[label]} transcript evidence sample number {index}"
                ),
                "total_claims": 4,
                "false_claims": label - 1,
                "likes": 10 + index * (2 if platform == "youtube" else 20),
                "comments": 2 + index,
                "views": 100 + index * (10 if platform == "youtube" else 100),
                "duration_sec": 20 + index,
                "label": label,
            }
        )
    return pd.DataFrame(rows)


class MultiPlatformTests(unittest.TestCase):
    def test_both_source_csvs_remain_byte_identical_during_loading(self) -> None:
        settings = load_settings()
        source_paths = [
            PROJECT_ROOT / str(source["path"])
            for source in settings["data"]["sources"]
        ]
        before = {path: file_sha256(path) for path in source_paths}
        data, report = load_multiplatform_data(PROJECT_ROOT, settings["data"])
        after = {path: file_sha256(path) for path in source_paths}
        self.assertEqual(before, after)
        self.assertEqual(len(data), settings["data"]["expected_rows"])
        self.assertEqual(report["modelled_rows"], int(data["label"].notna().sum()))
        self.assertFalse(report["raw_csvs_modified"])
        offset = 0
        for source, path in zip(settings["data"]["sources"], source_paths):
            raw = pd.read_csv(path)
            pooled = data.iloc[offset:offset + len(raw)]
            self.assertEqual(
                pooled["record_id"].tolist(),
                [f"{source['name']}:{row:06d}" for row in range(len(raw))],
            )
            self.assertEqual(pooled["source_row"].tolist(), list(range(len(raw))))
            self.assertEqual(pooled["row_index"].tolist(), list(range(offset, offset + len(raw))))
            offset += len(raw)

    def test_tiktok_placeholder_titles_are_declared_but_not_rewritten(self) -> None:
        settings = load_settings()
        raw = pd.read_csv(PROJECT_ROOT / "data/adhd_misinformation_tiktok.csv")
        source = next(item for item in settings["data"]["sources"] if item["name"] == "tiktok")
        self.assertEqual(len(raw), source["expected_rows"])
        self.assertEqual(set(raw["title"].str.strip().str.casefold()), {"video"})
        _, report = load_multiplatform_data(PROJECT_ROOT, settings["data"])
        audits = {
            item["source"]: item for item in report["title_placeholder_audit"]
        }
        self.assertEqual(audits["tiktok"]["placeholder_rows"], len(raw))
        self.assertTrue(audits["tiktok"]["excluded_from_pooled_text"])

    def test_pooled_config_requires_transcript_only(self) -> None:
        settings = load_settings()
        validate_multiplatform_experiment(settings)
        changed = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
        changed["features"]["text_columns"] = ["title", "transcript"]
        with self.assertRaisesRegex(ValueError, "sole text column"):
            validate_multiplatform_experiment(changed)

    def test_training_receipts_bind_both_source_files(self) -> None:
        settings = load_settings()
        files = training_input_files(
            settings,
            "configs/experiment_multiplatform.yaml",
            "configs/bert.yaml",
        )
        self.assertIn("dataset_youtube", files)
        self.assertIn("dataset_tiktok", files)
        self.assertNotIn("dataset", files)

    def test_frozen_pooled_split_replays_and_contains_both_platforms(self) -> None:
        settings = load_settings()
        verify_multiplatform_split(PROJECT_ROOT, settings)
        training, heldout, full = load_multiplatform_saved_split(
            PROJECT_ROOT, settings
        )
        manifest = json.loads(
            (PROJECT_ROOT / settings["data"]["split_manifest_path"]).read_text(encoding="utf-8")
        )
        self.assertEqual(len(full), settings["data"]["expected_rows"])
        self.assertEqual(len(training) + len(heldout), int(full["label"].notna().sum()))
        train_rows = set(training["row_index"])
        test_rows = set(heldout["row_index"])
        self.assertFalse(train_rows & test_rows)
        self.assertEqual(train_rows | test_rows, set(full.loc[full["label"].notna(), "row_index"]))
        excluded = pd.read_csv(PROJECT_ROOT / settings["data"]["excluded_indices_path"])
        self.assertEqual(set(excluded["row_index"]), set(full.loc[full["label"].isna(), "row_index"]))
        for name, subset in (("training", training), ("heldout", heldout)):
            self.assertEqual(manifest[f"{name}_rows"], len(subset))
            self.assertEqual(set(subset["platform"]), set(full["platform"]))
            self.assertEqual(set(subset["label"]), {1, 2, 3, 4})
            self.assertEqual(manifest[f"{name}_platform_distribution"], subset["platform"].value_counts().to_dict())
        groups = dict(zip(full["row_index"], content_group_ids(full)))
        train_groups = {groups[row] for row in train_rows}
        test_groups = {groups[row] for row in test_rows}
        self.assertFalse(train_groups & test_groups)

    def test_pooled_loader_rejects_a_stale_validation_report(self) -> None:
        settings = load_settings()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data/multiplatform").mkdir(parents=True)
            for relative in (
                "data/dataset.csv",
                "data/adhd_misinformation_tiktok.csv",
                "data/multiplatform/train_indices.csv",
                "data/multiplatform/test_indices.csv",
                "data/multiplatform/excluded_indices.csv",
                "data/multiplatform/split_manifest.json",
                "data/multiplatform/validation_report.json",
            ):
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(PROJECT_ROOT / relative, target)
            report_path = root / "data/multiplatform/validation_report.json"
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report["source_rows"] = 999
            report_path.write_text(json.dumps(report), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "validation report is stale"):
                verify_multiplatform_split(root, settings)

    def test_within_platform_percentiles_are_fold_local_and_platform_is_not_output(self) -> None:
        training = pd.DataFrame(
            {
                "platform": ["youtube", "youtube", "tiktok", "tiktok"],
                "likes": [0, 10, 100, 200],
                "comments": [0, 10, 100, 200],
                "views": [0, 10, 100, 200],
                "duration_sec": [0, 10, 100, 200],
            }
        )
        validation = pd.DataFrame(
            {
                "platform": ["youtube", "tiktok"],
                "likes": [5, 150],
                "comments": [5, 150],
                "views": [5, 150],
                "duration_sec": [5, 150],
            }
        )
        transformer = WithinPlatformPercentileTransformer().fit(training)
        observed = transformer.transform(validation)
        np.testing.assert_allclose(observed, np.full((2, 4), 0.5))
        self.assertNotIn("platform", transformer.get_feature_names_out())

    def test_all_classical_conditions_ignore_title_placeholders(self) -> None:
        data = synthetic_pooled_data()
        predictors = data.drop(columns="label")
        builders = (
            build_logistic_regression,
            build_ridge_classifier,
            build_complement_naive_bayes,
            build_decision_tree,
        )
        for builder in builders:
            for feature_set in ("A", "B", "C"):
                with self.subTest(builder=builder.__name__, feature_set=feature_set):
                    model = builder(
                        feature_set,
                        max_features=40,
                        stop_words=None,
                        text_columns=("transcript",),
                        engagement_transform="within_platform_percentile",
                        platform_column="platform",
                    )
                    model.fit(predictors, data["label"])
                    predictions = model.predict(predictors)
                    self.assertEqual(len(predictions), len(data))
                    vocabulary = model.named_steps["features"].named_transformers_[
                        "text"
                    ].named_steps["tfidf"].vocabulary_
                    self.assertNotIn("titleonlysentinel", vocabulary)

    def test_linguistic_features_use_transcript_only(self) -> None:
        frame = pd.DataFrame(
            {
                "title": ["definitely maybe titleonlysentinel"],
                "transcript": ["plain transcript words"],
            }
        )
        extractor = LinguisticFeatureExtractor(
            certainty_terms=("definitely",), hedge_terms=("maybe",)
        )
        observed = extractor.fit_transform(frame[["transcript"]])
        np.testing.assert_array_equal(observed, np.zeros((1, 2)))

    def test_minilm_receives_only_transcripts(self) -> None:
        class RecordingEncoder:
            def encode(self, texts: list[str], **kwargs: object) -> np.ndarray:
                self.texts = texts
                return np.zeros((len(texts), 384), dtype=np.float32)

        encoder = RecordingEncoder()
        frame = synthetic_pooled_data().iloc[:2]
        values = encode_minilm(
            frame,
            "unused",
            encoder=encoder,
            text_columns=("transcript",),
        )
        self.assertEqual(values.shape, (2, 384))
        self.assertEqual(encoder.texts, frame["transcript"].tolist())
        self.assertTrue(all("titleonlysentinel" not in text for text in encoder.texts))

    def test_pooled_minilm_fits_with_platform_percentile_metadata(self) -> None:
        class RecordingEncoder:
            max_seq_length = 256

            def _first_module(self) -> SimpleNamespace:
                config = SimpleNamespace(_commit_hash="fixed-test-revision")
                return SimpleNamespace(auto_model=SimpleNamespace(config=config))

            def encode(self, texts: list[str], **kwargs: object) -> np.ndarray:
                self.texts = texts
                values = np.zeros((len(texts), 384), dtype=np.float32)
                values[:, 0] = np.arange(len(texts), dtype=np.float32)
                return values

        encoder = RecordingEncoder()
        data = synthetic_pooled_data()
        model = FrozenMiniLMClassifier(
            encoder=encoder,
            revision="fixed-test-revision",
            text_columns=("transcript",),
            engagement_transform="within_platform_percentile",
            platform_column="platform",
        ).fit(data.drop(columns="label"), data["label"])
        self.assertEqual(len(model.predict(data.drop(columns="label"))), len(data))
        self.assertEqual(
            model.metadata_scaler_.get_feature_names_out().tolist(),
            [
                "certainty_score",
                "hedge_score",
                "likes_within_platform_percentile",
                "comments_within_platform_percentile",
                "views_within_platform_percentile",
                "duration_sec_within_platform_percentile",
            ],
        )
        self.assertTrue(all("titleonlysentinel" not in text for text in encoder.texts))

    def test_bert_tokenizer_receives_one_transcript_sequence(self) -> None:
        class RecordingTokenizer:
            def __call__(self, *args: object, **kwargs: object) -> dict[str, np.ndarray]:
                self.args = args
                self.kwargs = kwargs
                return {
                    "input_ids": np.asarray([[1, 2]]),
                    "attention_mask": np.asarray([[1, 1]]),
                }

        fake_torch = SimpleNamespace(
            float32=np.float32,
            long=np.int64,
            tensor=lambda values, dtype=None: np.asarray(values, dtype=dtype),
        )
        tokenizer = RecordingTokenizer()
        frame = synthetic_pooled_data().iloc[:1]
        with patch("features.transformer_features.torch", fake_torch):
            dataset = BertVideoDataset(
                frame,
                tokenizer,
                np.zeros((1, 6), dtype=np.float32),
                max_length=256,
                text_columns=("transcript",),
            )
            dataset[0]
        self.assertEqual(tokenizer.args, (frame.iloc[0]["transcript"],))
        self.assertTrue(tokenizer.kwargs["truncation"])
        self.assertNotIn("titleonlysentinel", tokenizer.args)

    def test_joint_cv_stratifies_platform_and_label_while_grouping(self) -> None:
        data = synthetic_pooled_data()
        groups = content_group_ids(data)
        splitter = StratifiedGroupKFoldByColumns(
            n_splits=4,
            shuffle=True,
            random_state=42,
            stratification_columns=("platform",),
        )
        expected = {
            (platform, label)
            for platform in ("youtube", "tiktok")
            for label in (1, 2, 3, 4)
        }
        for training, validation in splitter.split(data, data["label"], groups):
            validation_strata = set(
                zip(
                    data.iloc[validation]["platform"],
                    data.iloc[validation]["label"],
                )
            )
            self.assertEqual(validation_strata, expected)
            self.assertFalse(set(groups[training]) & set(groups[validation]))

    def test_bert_early_stopping_contains_every_platform_label_stratum(self) -> None:
        data = synthetic_pooled_data()
        fitting, stopping = _grouped_early_stopping_split(
            data,
            requested_fraction=0.20,
            seed=42,
            stratification_columns=("platform",),
        )
        expected = {
            (platform, label)
            for platform in ("youtube", "tiktok")
            for label in (1, 2, 3, 4)
        }
        for selected in (fitting, stopping):
            self.assertEqual(
                set(zip(selected["platform"], selected["label"])), expected
            )
        self.assertFalse(
            set(content_group_ids(fitting)) & set(content_group_ids(stopping))
        )

    def test_cv_loader_rejects_a_wrong_platform_identity_in_any_condition(self) -> None:
        training = synthetic_pooled_data().iloc[:8].copy()
        assignments = pd.DataFrame(
            {
                "row_index": training["row_index"],
                "record_id": training["record_id"],
                "platform": training["platform"],
                "fold": np.repeat([1, 2], 4),
                "true_label": training["label"],
                "prediction": training["label"],
            }
        )
        assignments.loc[0, "platform"] = "wrong-platform"
        metric_rows: list[dict[str, object]] = []
        for fold in (1, 2):
            selected = assignments.loc[assignments["fold"].eq(fold)]
            metrics = calculate_metrics(
                selected["true_label"], selected["prediction"]
            )
            metric_rows.append(
                {
                    "fold": fold,
                    **{
                        name: metrics[name]
                        for name in (
                            "quadratic_weighted_kappa",
                            "accuracy",
                            "weighted_f1",
                            "mean_absolute_error",
                        )
                    },
                }
            )
        settings = {
            "reporting": {"include_baselines": True},
            "evaluation": {"outer_folds": 2},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "metrics").mkdir()
            (root / "predictions").mkdir()
            name = "A_RIDGE"
            assignments.to_csv(root / "predictions" / f"{name}_cv.csv", index=False)
            pd.DataFrame(metric_rows).to_csv(
                root / "metrics" / f"{name}_cv.csv", index=False
            )
            with (
                patch("scripts.generate_results.expected_names", return_value=(name,)),
                self.assertRaisesRegex(ValueError, "identities"),
            ):
                load_cv_files(root, settings, training)

    def test_platform_metrics_are_reported_separately_and_equally_weighted(self) -> None:
        heldout = synthetic_pooled_data().iloc[:8].copy()
        predictions = pd.DataFrame(
            {
                "row_index": heldout["row_index"],
                "true_label": heldout["label"],
                "prediction": heldout["label"],
            }
        )
        by_platform, macro = platform_heldout_tables(
            {"perfect": predictions}, heldout
        )
        self.assertEqual(set(by_platform["platform"]), {"youtube", "tiktok"})
        self.assertEqual(by_platform["rows"].sum(), len(heldout))
        self.assertTrue(by_platform["quadratic_weighted_kappa"].eq(1.0).all())
        self.assertEqual(
            float(macro.iloc[0]["platform_macro_quadratic_weighted_kappa"]),
            1.0,
        )


if __name__ == "__main__":
    unittest.main()
