"""Deterministic lexical certainty and hedging features derived from text.

These features are computed inside each model pipeline. They are never expected
or written as columns in the author-annotated CSV.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


# Versioned operational lexicons used in every condition. These fallback values
# mirror configs/linguistic_lexicons.yaml exactly. Changing either tuple defines
# a new experiment and must be reported.
DEFAULT_CERTAINTY_TERMS = (
    "absolutely",
    "actually"
    "always"
    "believe"
    "believed"
    "believes"
    "beyond doubt"
    "certain"
    "certainly"
    "clear"
     "clearly"
     "conclusively"
     "decidedly"
     "definite"
     "definitely"
     "demonstrate"
     "demonstrated"
     "demonstrates"
     "doubtless"
     "establish"
     "established"
     "evident"
     "evidently"
     "find"
     "finds"
     "found"
     "in fact"
     "incontestable"
     "incontestably"
     "incontrovertible"
     "incontrovertibly"
     "indeed"
     "indisputable"
     "indisputably"
     "know"
     "known"
     "never"
     "no doubt"
     "obvious"
     "obviously"
     "of course"
     "prove"
     "proved"
     "proves"
     "realize"
     "realized"
     "realizes"
     "really"
     "show"
     "showed"
     "shown"
     "shows"
     "sure"
     "surely"
     "think"
     "thinks"
     "thought"
     "truly"
     "undeniable"
     "undeniably"
     "undisputedly"
     "undoubtedly"
     "without doubt"
)

DEFAULT_HEDGE_TERMS = (
    "about",
    "almost",
    "apparent",
    "apparently",
    "appear",
    "appeared",
    "appears",
    "approximately",
    "argue",
    "argued",
    "argues",
    "around",
    "assume",
    "assumed",
    "broadly",
    "certain amount",
    "certain extent",
    "certain level",
    "claim",
    "claimed",
    "claims",
    "could",
    "couldn’t",
    "doubt",
    "doubtful",
    "essentially",
    "estimate",
    "estimated",
    "fairly",
    "feel",
    "feels",
    "felt",
    "frequently",
    "from my perspective",
    "from our perspective",
    "from this perspective",
    "generally",
    "guess",
    "indicate",
    "indicated",
    "indicates",
    "in general",
    "in most cases",
    "in most instances",
    "in my opinon",
    "in my view",
    "in this view",
    "in our opinion",
    "in our view",
    "largely",
    "likely",
    "mainly",
    "may",
    "maybe",
    "might",
    "mostly",
    "often",
    "on the whole",
    "ought",
    "perhaps",
    "plausible",
    "plausibly",
    "possible",
    "possibly",
    "postulate",
    "postulated",
    "postulates",
    "presumable",
    "presumably",
    "probable",
    "probably",
    "quite",
    "rather x",
    "relatively",
    "roughly",
    "seems",
    "should",
    "sometimes",
    "somewhat",
    "suggest",
    "suggested",
    "suggests",
    "suppose",
    "supposed",
    "supposes",
    "suspect",
    "suspects",
    "tend to",
    "tended to",
    "tends to",
    "to my knowledge",
    "typical",
    "typically",
    "uncertain",
    "uncertainly",
    "unclear",
    "unclearly",
    "unlikely",
    "usually",
    "would",
    "wouldn’t",
)

DERIVED_LINGUISTIC_FEATURES = ("certainty_rate", "hedge_rate")

TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def tokenize(text: object) -> list[str]:
    """Return lowercase word tokens from a possibly missing value."""
    if text is None or pd.isna(text):
        return []
    normalized = str(text).lower().replace("’", "'").replace("‘", "'")
    return TOKEN_PATTERN.findall(normalized)


def count_lexicon_matches(tokens: list[str], terms: Iterable[str]) -> int:
    """Count exact single-word and multi-word lexicon matches."""
    total = 0
    for term in terms:
        term_tokens = tokenize(term)
        width = len(term_tokens)
        if width == 0:
            continue
        for index in range(len(tokens) - width + 1):
            if tokens[index : index + width] == term_tokens:
                total += 1
    return total


def score_per_100_tokens(text: object, terms: Iterable[str]) -> float:
    """Calculate lexicon matches per 100 tokens."""
    tokens = tokenize(text)
    if not tokens:
        return 0.0
    matches = count_lexicon_matches(tokens, terms)
    return 100.0 * matches / len(tokens)


def calculate_linguistic_scores(
    text: object,
    certainty_terms: Iterable[str] = DEFAULT_CERTAINTY_TERMS,
    hedge_terms: Iterable[str] = DEFAULT_HEDGE_TERMS,
) -> tuple[float, float]:
    """Return certainty and hedge scores for one text."""
    certainty = score_per_100_tokens(text, certainty_terms)
    hedge = score_per_100_tokens(text, hedge_terms)
    return certainty, hedge


class LinguisticFeatureExtractor(BaseEstimator, TransformerMixin):
    """Create two lexical rates from raw title/transcript columns."""

    def __init__(
        self,
        certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
        hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    ) -> None:
        self.certainty_terms = certainty_terms
        self.hedge_terms = hedge_terms

    def fit(
        self,
        values: object,
        target: object = None,
    ) -> "LinguisticFeatureExtractor":
        return self

    def transform(self, values: object) -> np.ndarray:
        if isinstance(values, pd.DataFrame):
            title = values.iloc[:, 0].fillna("").astype(str)
            transcript = values.iloc[:, 1].fillna("").astype(str)
        else:
            array = np.asarray(values, dtype=object)
            if array.ndim != 2 or array.shape[1] != 2:
                raise ValueError(
                    "LinguisticFeatureExtractor expects title and transcript."
                )
            title = pd.Series(array[:, 0]).fillna("").astype(str)
            transcript = pd.Series(array[:, 1]).fillna("").astype(str)
        combined = title + " " + transcript
        scores = [
            calculate_linguistic_scores(
                text,
                self.certainty_terms,
                self.hedge_terms,
            )
            for text in combined
        ]
        return np.asarray(scores, dtype=np.float32)

    def get_feature_names_out(self, input_features: object = None) -> np.ndarray:
        return np.asarray(DERIVED_LINGUISTIC_FEATURES, dtype=object)
