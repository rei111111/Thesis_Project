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


def transformer_feature_names(engagement_transform: str = "log1p") -> tuple[str, ...]:
    """Return the six named auxiliary outputs for one experiment profile."""
    if engagement_transform == "log1p":
        engagement = ENGAGEMENT_COLUMNS
    elif engagement_transform == "within_platform_percentile":
        engagement = tuple(
            f"{column}_within_platform_percentile"
            for column in ENGAGEMENT_COLUMNS
        )
    else:
        raise ValueError(
            "engagement_transform must be 'log1p' or "
            "'within_platform_percentile'."
        )
    return DERIVED_LINGUISTIC_FEATURES + engagement


class WithinPlatformPercentileTransformer(BaseEstimator, TransformerMixin):
    """Map numeric values to training-fold empirical percentiles by platform.

    The platform column is routing context only: it selects the appropriate
    training reference distribution and is never emitted as a model feature.
    """

    def __init__(
        self,
        platform_column: str = "platform",
        value_columns: tuple[str, ...] = ENGAGEMENT_COLUMNS,
    ) -> None:
        self.platform_column = platform_column
        self.value_columns = value_columns

    def _frame(self, values: object) -> pd.DataFrame:
        columns = [self.platform_column, *self.value_columns]
        if isinstance(values, pd.DataFrame):
            missing = [column for column in columns if column not in values.columns]
            if missing:
                raise ValueError(
                    f"Platform-percentile inputs are missing columns: {missing}"
                )
            return values.loc[:, columns].reset_index(drop=True).copy()
        array = np.asarray(values, dtype=object)
        if array.ndim != 2 or array.shape[1] != len(columns):
            raise ValueError(
                "Platform-percentile inputs must contain platform followed by "
                f"{list(self.value_columns)}."
            )
        return pd.DataFrame(array, columns=columns)

    def _validated(self, values: object) -> pd.DataFrame:
        frame = self._frame(values)
        platform = frame[self.platform_column].fillna("").astype(str).str.strip()
        if platform.eq("").any():
            raise ValueError("Platform routing values cannot be blank.")
        frame[self.platform_column] = platform
        for column in self.value_columns:
            numeric = pd.to_numeric(frame[column], errors="coerce")
            if (
                numeric.isna().any()
                or not np.isfinite(numeric.to_numpy(dtype=float)).all()
                or (numeric < 0).any()
            ):
                raise ValueError(
                    f"{column} must contain finite non-negative values."
                )
            frame[column] = numeric.astype(float)
        return frame

    def fit(
        self,
        values: object,
        target: object = None,
    ) -> "WithinPlatformPercentileTransformer":
        frame = self._validated(values)
        self.platforms_ = tuple(sorted(frame[self.platform_column].unique()))
        self.reference_values_ = {
            platform: {
                column: np.sort(
                    selected[column].to_numpy(dtype=float), kind="stable"
                )
                for column in self.value_columns
            }
            for platform, selected in frame.groupby(self.platform_column, sort=True)
        }
        return self

    def transform(self, values: object) -> np.ndarray:
        if not hasattr(self, "reference_values_"):
            raise RuntimeError(
                "WithinPlatformPercentileTransformer must be fitted first."
            )
        frame = self._validated(values)
        unknown = sorted(
            set(frame[self.platform_column].unique()) - set(self.platforms_)
        )
        if unknown:
            raise ValueError(
                "Validation data contains platforms absent from the training "
                f"fold: {unknown}."
            )
        result = np.empty((len(frame), len(self.value_columns)), dtype=np.float32)
        for row_position, row in frame.iterrows():
            references = self.reference_values_[str(row[self.platform_column])]
            for column_position, column in enumerate(self.value_columns):
                ordered = references[column]
                value = float(row[column])
                left = np.searchsorted(ordered, value, side="left")
                right = np.searchsorted(ordered, value, side="right")
                result[row_position, column_position] = (
                    float(left + right) / (2.0 * len(ordered))
                )
        return result

    def get_feature_names_out(self, input_features: object = None) -> np.ndarray:
        return np.asarray(
            [
                f"{column}_within_platform_percentile"
                for column in self.value_columns
            ],
            dtype=object,
        )


def safe_log1p(values: object) -> np.ndarray:
    """Apply log(1+x) after rejecting negative values."""
    array = np.asarray(values, dtype=float)
    if not np.isfinite(array).all():
        raise ValueError("Engagement and duration values must be finite.")
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
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
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
    if engagement_transform == "log1p":
        engagement_pipeline: object = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                (
                    "log1p",
                    FunctionTransformer(safe_log1p, feature_names_out="one-to-one"),
                ),
                ("scaler", StandardScaler()),
            ]
        )
        engagement_columns = list(ENGAGEMENT_COLUMNS)
    elif engagement_transform == "within_platform_percentile":
        engagement_pipeline = WithinPlatformPercentileTransformer(
            platform_column=platform_column,
            value_columns=ENGAGEMENT_COLUMNS,
        )
        engagement_columns = [platform_column, *ENGAGEMENT_COLUMNS]
    else:
        raise ValueError(
            "engagement_transform must be 'log1p' or "
            "'within_platform_percentile'."
        )
    return ColumnTransformer(
        [
            ("linguistic", linguistic_pipeline, list(text_columns)),
            ("engagement", engagement_pipeline, engagement_columns),
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
        text_columns: tuple[str, ...] = ("title", "transcript"),
        engagement_transform: str = "log1p",
        platform_column: str = "platform",
    ) -> None:
        self.certainty_terms = certainty_terms
        self.hedge_terms = hedge_terms
        self.text_columns = text_columns
        self.engagement_transform = engagement_transform
        self.platform_column = platform_column

    def fit(self, data: pd.DataFrame, target: object = None) -> "MetadataScaler":
        required = tuple(self.text_columns) + ENGAGEMENT_COLUMNS
        if self.engagement_transform == "within_platform_percentile":
            required = required + (self.platform_column,)
        validate_raw_auxiliary_columns(data, required)
        self.preprocessor_ = build_metadata_preprocessor(
            self.certainty_terms,
            self.hedge_terms,
            text_columns=self.text_columns,
            engagement_transform=self.engagement_transform,
            platform_column=self.platform_column,
        )
        self.preprocessor_.fit(data)
        return self

    def transform(self, data: pd.DataFrame) -> np.ndarray:
        if not hasattr(self, "preprocessor_"):
            raise RuntimeError("MetadataScaler must be fitted before transform.")
        required = tuple(self.text_columns) + ENGAGEMENT_COLUMNS
        if self.engagement_transform == "within_platform_percentile":
            required = required + (self.platform_column,)
        validate_raw_auxiliary_columns(data, required)
        values = self.preprocessor_.transform(data)
        return np.asarray(values, dtype=np.float32)

    def get_feature_names_out(self) -> np.ndarray:
        return np.asarray(
            transformer_feature_names(self.engagement_transform), dtype=object
        )
