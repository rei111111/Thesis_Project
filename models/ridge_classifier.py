"""Ridge Classifier for feature configurations A, B, and C."""

from __future__ import annotations

from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline

from features.text_features import build_ridge_preprocessor
from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)


def build_ridge_classifier(
    feature_set: str,
    alpha: float = 1.0,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
) -> Pipeline:
    """Create a leakage-safe Ridge pipeline for one feature set."""
    preprocessor = build_ridge_preprocessor(
        feature_set=feature_set,
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words=stop_words,
        certainty_terms=certainty_terms,
        hedge_terms=hedge_terms,
    )
    classifier = RidgeClassifier(alpha=alpha, class_weight="balanced")
    return Pipeline(
        [
            ("features", preprocessor),
            ("classifier", classifier),
        ]
    )


def ridge_parameter_grid(alphas: list[float]) -> dict[str, list[float]]:
    """Return namespaced parameters for GridSearchCV."""
    return {"classifier__alpha": alphas}
