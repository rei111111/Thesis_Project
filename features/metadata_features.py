"""Fold-local derivation and scaling of the six auxiliary features."""

from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler

from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
    DERIVED_LINGUISTIC_FEATURES,
    LinguisticFeatureExtractor,
)

ENGAGEMENT_COLUMNS = ("likes", "comments", "views", "duration_sec")
RAW_AUXILIARY_COLUMNS = ("title", "transcript") + ENGAGEMENT_COLUMNS
TRANSFORMER_FEATURE_NAMES = DERIVED_LINGUISTIC_FEATURES + ENGAGEMENT_COLUMNS


def safe_log1p(values: object) -> np.ndarray:
    """Apply log(1+x) after rejecting negative values."""
    array = np.asarray(values, dtype=float)
    if np.any(array < 0):
        raise ValueError("Engagement and duration values cannot be negative.")
    return np.log1p(array)


def validate_raw_auxiliary_columns(
    data: pd.DataFrame,
    columns: tuple[str, ...] = RAW_AUXILIARY_COLUMNS,
) -> None:
    """Raise a clear error when raw inputs for auxiliary features are absent."""
    missing = [column for column in columns if column not in data.columns]
    if missing:
        raise ValueError(f"Missing raw auxiliary inputs: {missing}")


def build_metadata_preprocessor(
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
) -> ColumnTransformer:
    """Derive two text rates and transform four raw metadata values."""
    linguistic_pipeline = Pipeline(
        [
            (
                "derive",
                LinguisticFeatureExtractor(certainty_terms, hedge_terms),
            ),
            ("scaler", StandardScaler()),
        ]
    )
    engagement_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("log1p", FunctionTransformer(safe_log1p, feature_names_out="one-to-one")),
            ("scaler", StandardScaler()),
        ]
    )
    return ColumnTransformer(
        [
            ("linguistic", linguistic_pipeline, ["title", "transcript"]),
            ("engagement", engagement_pipeline, list(ENGAGEMENT_COLUMNS)),
        ],
        remainder="drop",
        verbose_feature_names_out=False,
    )


class MetadataScaler(BaseEstimator, TransformerMixin):
    """Scikit-learn compatible wrapper used by both transformer models."""

    def __init__(
        self,
        certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
        hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    ) -> None:
        self.certainty_terms = certainty_terms
        self.hedge_terms = hedge_terms

    def fit(self, data: pd.DataFrame, target: object = None) -> "MetadataScaler":
        validate_raw_auxiliary_columns(data)
        self.preprocessor_ = build_metadata_preprocessor(
            self.certainty_terms,
            self.hedge_terms,
        )
        self.preprocessor_.fit(data)
        return self

    def transform(self, data: pd.DataFrame) -> np.ndarray:
        if not hasattr(self, "preprocessor_"):
            raise RuntimeError("MetadataScaler must be fitted before transform.")
        validate_raw_auxiliary_columns(data)
        values = self.preprocessor_.transform(data)
        return np.asarray(values, dtype=np.float32)

    def get_feature_names_out(self) -> np.ndarray:
        return np.asarray(TRANSFORMER_FEATURE_NAMES, dtype=object)
