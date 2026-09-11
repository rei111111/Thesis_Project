"""Multinomial Logistic Regression for feature configurations A, B, and C."""

from __future__ import annotations

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)
from features.text_features import build_interpretable_preprocessor


def build_logistic_regression(
    feature_set: str,
    c_value: float = 1.0,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    max_iter: int = 2000,
    random_state: int = 42,
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
) -> Pipeline:
    """Create a balanced, leakage-safe Logistic Regression pipeline."""
    preprocessor = build_interpretable_preprocessor(
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
    classifier = LogisticRegression(
        C=c_value,
        class_weight="balanced",
        max_iter=max_iter,
        random_state=random_state,
        solver="lbfgs",
    )
    return Pipeline([("features", preprocessor), ("classifier", classifier)])


def logistic_parameter_grid(c_values: list[float]) -> dict[str, list[float]]:
    """Return namespaced candidates for nested model selection."""
    return {"classifier__C": c_values}
