"""Predeclared non-experimental baselines used to contextualise performance."""

from __future__ import annotations

from sklearn.dummy import DummyClassifier


def build_most_frequent_baseline(random_state: int = 42) -> DummyClassifier:
    return DummyClassifier(strategy="most_frequent", random_state=random_state)


def build_stratified_random_baseline(random_state: int = 42) -> DummyClassifier:
    return DummyClassifier(strategy="stratified", random_state=random_state)
