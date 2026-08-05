"""Complement Naive Bayes for non-negative feature configurations A--C."""

from __future__ import annotations

from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline

from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)
from features.text_features import (
    NonNegativeClipper,
    build_interpretable_preprocessor,
)


def build_complement_naive_bayes(
    feature_set: str,
    alpha: float = 1.0,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
) -> Pipeline:
    """Create a leakage-safe CNB pipeline with guaranteed non-negative input."""
    preprocessor = build_interpretable_preprocessor(
        feature_set=feature_set,
        numeric_scaling="minmax",
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words=stop_words,
        certainty_terms=certainty_terms,
        hedge_terms=hedge_terms,
    )
    return Pipeline(
        [
            ("features", preprocessor),
            ("nonnegative", NonNegativeClipper()),
            ("classifier", ComplementNB(alpha=alpha)),
        ]
    )


def complement_nb_parameter_grid(alphas: list[float]) -> dict[str, list[float]]:
    """Return namespaced candidates for nested model selection."""
    return {"classifier__alpha": alphas}
