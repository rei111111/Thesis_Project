"""TF--IDF and feature-set construction for Ridge Classifier."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler

from features.metadata_features import (
    ENGAGEMENT_COLUMNS,
    safe_log1p,
)
from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
    LinguisticFeatureExtractor,
)


FEATURE_SETS = ("A", "B", "C")


class TextColumnCombiner(BaseEstimator, TransformerMixin):
    """Combine title and transcript without fitting corpus statistics."""

    def fit(self, values: object, target: object = None) -> "TextColumnCombiner":
        return self

    def transform(self, values: object) -> np.ndarray:
        if isinstance(values, pd.DataFrame):
            title = values.iloc[:, 0].fillna("").astype(str)
            transcript = values.iloc[:, 1].fillna("").astype(str)
        else:
            array = np.asarray(values, dtype=object)
            title = pd.Series(array[:, 0]).fillna("").astype(str)
            transcript = pd.Series(array[:, 1]).fillna("").astype(str)
        return (title + " [SEP] " + transcript).to_numpy(dtype=object)

    def get_feature_names_out(self, input_features: object = None) -> np.ndarray:
        return np.asarray(["combined_text"], dtype=object)


def build_ridge_preprocessor(
    feature_set: str,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
) -> ColumnTransformer:
    """Build A, B, or C with all fitted steps inside the model pipeline."""
    normalized_set = feature_set.upper()
    if normalized_set not in FEATURE_SETS:
        raise ValueError(f"feature_set must be one of {FEATURE_SETS}")

    text_pipeline = Pipeline(
        [
            ("combine", TextColumnCombiner()),
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    max_features=max_features,
                    ngram_range=ngram_range,
                    stop_words=stop_words,
                ),
            ),
        ]
    )
    transformers: list[tuple[str, object, list[str]]] = [
        ("text", text_pipeline, ["title", "transcript"])
    ]

    if normalized_set in ("B", "C"):
        linguistic_pipeline = Pipeline(
            [
                (
                    "derive",
                    LinguisticFeatureExtractor(certainty_terms, hedge_terms),
                ),
                ("scaler", StandardScaler()),
            ]
        )
        transformers.append(
            ("linguistic", linguistic_pipeline, ["title", "transcript"])
        )

    if normalized_set == "C":
        engagement_pipeline = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                (
                    "log1p",
                    FunctionTransformer(safe_log1p, feature_names_out="one-to-one"),
                ),
                ("scaler", StandardScaler()),
            ]
        )
        transformers.append(
            ("engagement", engagement_pipeline, list(ENGAGEMENT_COLUMNS))
        )

    return ColumnTransformer(
        transformers,
        remainder="drop",
        sparse_threshold=0.3,
    )
