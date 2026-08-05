from __future__ import annotations

import unittest

import numpy as np
import pandas as pd
import yaml
from pathlib import Path

from features.linguistic_features import (
    DERIVED_LINGUISTIC_FEATURES,
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
    LinguisticFeatureExtractor,
    score_per_100_tokens,
    validate_lexicons,
)
from features.metadata_features import MetadataScaler, TRANSFORMER_FEATURE_NAMES
from features.text_features import build_ridge_preprocessor


def sample_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "title": ["Clear claim", "Uncertain claim", "Another claim", "Last"],
            "transcript": [
                "This definitely works",
                "This may work",
                "Evidence suggests a result",
                "This will help",
            ],
            "likes": [0, 10, 20, 30],
            "comments": [0, 1, 2, 3],
            "views": [10, 100, 1000, 10000],
            "duration_sec": [20, 30, 40, 50],
        }
    )


class FeatureTests(unittest.TestCase):
    def test_fallback_lexicons_match_the_versioned_yaml(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        values = yaml.safe_load(
            (project_root / "configs/linguistic_lexicons.yaml").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(tuple(values["certainty_terms"]), DEFAULT_CERTAINTY_TERMS)
        self.assertEqual(tuple(values["hedge_terms"]), DEFAULT_HEDGE_TERMS)

    def test_lexicon_matching_uses_word_boundaries(self) -> None:
        self.assertEqual(score_per_100_tokens("may", ["may"]), 100.0)
        self.assertEqual(score_per_100_tokens("mayonnaise", ["may"]), 0.0)

    def test_linguistic_scores_are_derived_without_mutating_data(self) -> None:
        data = sample_frame()
        original_columns = tuple(data.columns)
        values = LinguisticFeatureExtractor().fit_transform(
            data[["title", "transcript"]]
        )
        self.assertEqual(values.shape, (4, 2))
        self.assertGreater(values[0, 0], 0)
        self.assertGreater(values[1, 1], 0)
        self.assertEqual(tuple(data.columns), original_columns)

    def test_shared_transformer_metadata_has_six_values(self) -> None:
        self.assertEqual(len(TRANSFORMER_FEATURE_NAMES), 6)
        transformed = MetadataScaler().fit_transform(sample_frame())
        self.assertEqual(transformed.shape, (4, 6))
        self.assertTrue(np.isfinite(transformed).all())

    def test_only_certainty_and_hedge_are_derived_linguistic_features(self) -> None:
        self.assertEqual(
            DERIVED_LINGUISTIC_FEATURES,
            ("certainty_score", "hedge_score"),
        )

    def test_lexicon_validation_rejects_overlapping_terms(self) -> None:
        with self.assertRaisesRegex(ValueError, "overlap"):
            validate_lexicons(("always", "maybe"), ("maybe", "may"))

    def test_ridge_feature_sets_expand_in_order(self) -> None:
        data = sample_frame()
        dimensions = []
        for feature_set in ("A", "B", "C"):
            matrix = build_ridge_preprocessor(
                feature_set,
                max_features=30,
            ).fit_transform(data)
            dimensions.append(matrix.shape[1])
        self.assertLess(dimensions[0], dimensions[1])
        self.assertLess(dimensions[1], dimensions[2])


if __name__ == "__main__":
    unittest.main()
