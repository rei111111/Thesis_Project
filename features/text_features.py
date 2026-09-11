"""Leakage-safe feature-set construction for all interpretable models."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, MinMaxScaler, StandardScaler

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
NUMERIC_SCALING_MODES = ("standard", "minmax", "none")


class TextColumnCombiner(BaseEstimator, TransformerMixin):
    """Combine one or more preselected text columns without corpus statistics."""

    def fit(self, values: object, target: object = None) -> "TextColumnCombiner":
        return self

    def transform(self, values: object) -> np.ndarray:
        if isinstance(values, pd.DataFrame):
            if values.shape[1] < 1:
                raise ValueError("TextColumnCombiner needs at least one text column.")
            combined = values.fillna("").astype(str).agg(" ".join, axis=1)
        else:
            array = np.asarray(values, dtype=object)
            if array.ndim != 2 or array.shape[1] < 1:
                raise ValueError(
                    "TextColumnCombiner expects one or more text columns."
                )
            combined = pd.DataFrame(array).fillna("").astype(str).agg(" ".join, axis=1)
        # A literal "[SEP]" becomes the ordinary TF--IDF token "sep" and
        # consumes one of the 300 vocabulary slots. A space preserves the word
        # boundary without injecting an undocumented predictor.
        return combined.to_numpy(dtype=object)

    def get_feature_names_out(self, input_features: object = None) -> np.ndarray:
        return np.asarray(["combined_text"], dtype=object)


class NonNegativeClipper(BaseEstimator, TransformerMixin):
    """Enforce the numeric contract required by Complement Naive Bayes."""

    def fit(self, values: object, target: object = None) -> "NonNegativeClipper":
        return self

    def transform(self, values: object) -> object:
        if sparse.issparse(values):
            result = values.copy()
            result.data = np.maximum(result.data, 0.0)
            result.eliminate_zeros()
            return result
        return np.maximum(np.asarray(values, dtype=float), 0.0)

    def get_feature_names_out(self, input_features: object = None) -> np.ndarray:
        if input_features is None:
            raise ValueError("input_features are required for pass-through names.")
        return np.asarray(input_features, dtype=object)


def _numeric_scaler(mode: str) -> object:
    if mode == "standard":
        return StandardScaler()
    if mode == "minmax":
        # Validation or held-out values can fall outside the training range.
        # Clipping guarantees the non-negative contract required by CNB.
        return MinMaxScaler(clip=True)
    if mode == "none":
        return FunctionTransformer(feature_names_out="one-to-one")
    raise ValueError(f"numeric_scaling must be one of {NUMERIC_SCALING_MODES}")


def build_interpretable_preprocessor(
    feature_set: str,
    numeric_scaling: str = "standard",
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
) -> ColumnTransformer:
    """Build feature set A, B, or C inside a fitted model pipeline.

    ``standard`` is used by Logistic Regression and Ridge, ``minmax`` by
    Complement Naive Bayes, and ``none`` by the Decision Tree. TF--IDF is
    non-negative in every configuration. The two named linguistic scores and
    four engagement/format variables are derived only when their feature set
    requires them.
    """
    normalized_set = feature_set.upper()
    if normalized_set not in FEATURE_SETS:
        raise ValueError(f"feature_set must be one of {FEATURE_SETS}")
    if numeric_scaling not in NUMERIC_SCALING_MODES:
        raise ValueError(
            f"numeric_scaling must be one of {NUMERIC_SCALING_MODES}"
        )
    if not text_columns or len(set(text_columns)) != len(text_columns):
        raise ValueError("text_columns must contain unique column names.")

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
        ("text", text_pipeline, list(text_columns))
    ]

    if normalized_set in ("B", "C"):
        linguistic_pipeline = Pipeline(
            [
                (
                    "derive",
                    LinguisticFeatureExtractor(certainty_terms, hedge_terms),
                ),
                ("scaler", _numeric_scaler(numeric_scaling)),
            ]
        )
        transformers.append(
            ("linguistic", linguistic_pipeline, list(text_columns))
        )

    if normalized_set == "C":
        if engagement_transform == "within_platform_percentile":
            from features.metadata_features import WithinPlatformPercentileTransformer

            engagement_pipeline = WithinPlatformPercentileTransformer(
                platform_column=platform_column,
                value_columns=ENGAGEMENT_COLUMNS,
            )
            engagement_columns = [platform_column, *ENGAGEMENT_COLUMNS]
        elif engagement_transform == "log1p":
            engagement_pipeline = Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    (
                        "log1p",
                        FunctionTransformer(
                            safe_log1p, feature_names_out="one-to-one"
                        ),
                    ),
                    ("scaler", _numeric_scaler(numeric_scaling)),
                ]
            )
            engagement_columns = list(ENGAGEMENT_COLUMNS)
        else:
            raise ValueError(
                "engagement_transform must be 'log1p' or "
                "'within_platform_percentile'."
            )
        transformers.append(("engagement", engagement_pipeline, engagement_columns))

    return ColumnTransformer(
        transformers,
        remainder="drop",
        sparse_threshold=1.0,
    )


def build_ridge_preprocessor(
    feature_set: str,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
) -> ColumnTransformer:
    """Backward-compatible standard-scaled preprocessor used by Ridge."""
    return build_interpretable_preprocessor(
        feature_set=feature_set,
        numeric_scaling="standard",
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words=stop_words,
        certainty_terms=certainty_terms,
        hedge_terms=hedge_terms,
        text_columns=text_columns,
        engagement_transform=engagement_transform,
        platform_column=platform_column,
    )
