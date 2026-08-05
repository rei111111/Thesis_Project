"""Depth-constrained Decision Tree for feature configurations A, B, and C."""

from __future__ import annotations

from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier

from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)
from features.text_features import build_interpretable_preprocessor


def build_decision_tree(
    feature_set: str,
    max_depth: int = 5,
    min_samples_leaf: int = 5,
    max_features: int = 300,
    ngram_range: tuple[int, int] = (1, 2),
    stop_words: str | None = "english",
    random_state: int = 42,
    certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
) -> Pipeline:
    """Create an unstandardised, class-balanced, inspectable tree pipeline."""
    preprocessor = build_interpretable_preprocessor(
        feature_set=feature_set,
        numeric_scaling="none",
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words=stop_words,
        certainty_terms=certainty_terms,
        hedge_terms=hedge_terms,
    )
    classifier = DecisionTreeClassifier(
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        class_weight="balanced",
        random_state=random_state,
    )
    return Pipeline([("features", preprocessor), ("classifier", classifier)])


def decision_tree_parameter_grid(
    max_depths: list[int],
    min_samples_leaf: list[int],
) -> dict[str, list[int]]:
    """Return namespaced candidates for nested model selection."""
    return {
        "classifier__max_depth": max_depths,
        "classifier__min_samples_leaf": min_samples_leaf,
    }
