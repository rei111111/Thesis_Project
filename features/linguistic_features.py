"""Deterministic lexical certainty and hedging features derived from text.

These features are computed inside each model pipeline. They are never expected
or written as columns in the author-annotated CSV.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from functools import lru_cache

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


# Versioned operational lexicons used in every condition. These fallback values
# mirror configs/linguistic_lexicons.yaml exactly. Changing either tuple defines
# a new experiment and must be reported.
DEFAULT_CERTAINTY_TERMS = (
    "actually",
    "always",
    "believe",
    "believed",
    "believes",
    "beyond doubt",
    "certain",
    "certainly",
    "clear",
    "clearly",
    "conclusively",
    "decidedly",
    "definite",
    "definitely",
    "demonstrate",
    "demonstrated",
    "demonstrates",
    "doubtless",
    "establish",
    "established",
    "evident",
    "evidently",
    "find",
    "finds",
    "found",
    "in fact",
    "incontestable",
    "incontestably",
    "incontrovertible",
    "incontrovertibly",
    "indeed",
    "indisputable",
    "indisputably",
    "know",
    "known",
    "must",
    "never",
    "no doubt",
    "obvious",
    "obviously",
    "of course",
    "prove",
    "proved",
    "proves",
    "realize",
    "realized",
    "realizes",
    "really",
    "show",
    "showed",
    "shown",
    "shows",
    "sure",
    "surely",
    "think",
    "thinks",
    "thought",
    "truly",
    "undeniable",
    "undeniably",
    "undisputedly",
    "undoubtedly",
    "without doubt",
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
    "in my opinion",
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
    "rather",
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

DERIVED_LINGUISTIC_FEATURES = ("certainty_score", "hedge_score")

TOKEN_PATTERN = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def tokenize(text: object) -> list[str]:
    """Return lowercase word tokens from a possibly missing value."""
    if text is None or pd.isna(text):
        return []
    normalized = str(text).lower().replace("’", "'").replace("‘", "'")
    return TOKEN_PATTERN.findall(normalized)


@lru_cache(maxsize=32)
def _tokenized_terms(terms: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(tuple(tokenize(term)) for term in terms)


def _normalised_term_tuple(terms: Iterable[str]) -> tuple[str, ...]:
    return tuple(str(term).strip().lower() for term in terms)


def count_lexicon_matches(tokens: list[str], terms: Iterable[str]) -> int:
    """Count longest, non-overlapping exact token-sequence matches."""
    sequences = sorted(
        (value for value in _tokenized_terms(_normalised_term_tuple(terms)) if value),
        key=lambda value: (-len(value), value),
    )
    matches = 0
    index = 0
    while index < len(tokens):
        matched_width = next(
            (
                len(sequence)
                for sequence in sequences
                if tuple(tokens[index : index + len(sequence)]) == sequence
            ),
            0,
        )
        if matched_width:
            matches += 1
            index += matched_width
        else:
            index += 1
    return matches


@lru_cache(maxsize=32)
def _linguistic_candidate_index(
    certainty_terms: tuple[str, ...], hedge_terms: tuple[str, ...]
) -> dict[str, tuple[tuple[tuple[str, ...], int], ...]]:
    """Index fixed lexicon sequences by first token; no corpus values are fitted."""
    candidates = [
        (sequence, category)
        for category, terms in enumerate((certainty_terms, hedge_terms))
        for sequence in _tokenized_terms(terms)
        if sequence
    ]
    candidates.sort(key=lambda item: (-len(item[0]), item[0], item[1]))
    by_first: dict[str, list[tuple[tuple[str, ...], int]]] = {}
    for sequence, category in candidates:
        by_first.setdefault(sequence[0], []).append((sequence, category))
    return {first: tuple(values) for first, values in by_first.items()}


def count_linguistic_matches(
    tokens: list[str],
    certainty_terms: Iterable[str],
    hedge_terms: Iterable[str],
) -> tuple[int, int]:
    """Count longest non-overlapping matches across both named lexicons.

    Resolving both lists together prevents nested expressions such as
    ``no doubt`` from being counted simultaneously as certainty (the phrase)
    and hedging (the nested word ``doubt``).
    """
    candidates = _linguistic_candidate_index(
        _normalised_term_tuple(certainty_terms), _normalised_term_tuple(hedge_terms)
    )
    counts = [0, 0]
    index = 0
    while index < len(tokens):
        match = next(
            (
                (sequence, category)
                for sequence, category in candidates.get(tokens[index], ())
                if tuple(tokens[index : index + len(sequence)]) == sequence
            ),
            None,
        )
        if match is None:
            index += 1
            continue
        sequence, category = match
        counts[category] += 1
        index += len(sequence)
    return counts[0], counts[1]


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
    tokens = tokenize(text)
    if not tokens:
        return 0.0, 0.0
    certainty_matches, hedge_matches = count_linguistic_matches(
        tokens,
        certainty_terms,
        hedge_terms,
    )
    denominator = len(tokens)
    return (
        100.0 * certainty_matches / denominator,
        100.0 * hedge_matches / denominator,
    )


def validate_lexicons(
    certainty_terms: Iterable[str],
    hedge_terms: Iterable[str],
) -> dict[str, object]:
    """Validate and describe the two versioned operational lexicons.

    A term occurring in both lists would be counted once as certainty and once
    as hedging, which would make the two named features needlessly ambiguous.
    The experiment therefore rejects overlaps instead of silently double
    counting them.
    """
    certainty = _normalised_term_tuple(certainty_terms)
    hedge = _normalised_term_tuple(hedge_terms)
    if not certainty or not hedge:
        raise ValueError("Both linguistic lexicons must contain terms.")
    if any(not term for term in certainty + hedge):
        raise ValueError("Linguistic lexicons cannot contain blank terms.")
    certainty_tokenized = _tokenized_terms(certainty)
    hedge_tokenized = _tokenized_terms(hedge)
    if any(not tokens for tokens in certainty_tokenized + hedge_tokenized):
        raise ValueError("Every linguistic lexicon term must contain word tokens.")
    certainty_duplicates = sorted(
        " ".join(tokens)
        for tokens in set(certainty_tokenized)
        if certainty_tokenized.count(tokens) > 1
    )
    hedge_duplicates = sorted(
        " ".join(tokens)
        for tokens in set(hedge_tokenized)
        if hedge_tokenized.count(tokens) > 1
    )
    overlap = sorted(
        " ".join(tokens)
        for tokens in set(certainty_tokenized) & set(hedge_tokenized)
    )
    if certainty_duplicates or hedge_duplicates or overlap:
        raise ValueError(
            "Linguistic lexicons must be disjoint and duplicate-free. "
            f"certainty duplicates={certainty_duplicates}; "
            f"hedge duplicates={hedge_duplicates}; overlap={overlap}."
        )
    return {
        "certainty_term_count": len(certainty),
        "hedge_term_count": len(hedge),
        "overlap": overlap,
        "unit": "matches_per_100_word_tokens",
        "matching_rule": "longest_non_overlapping_across_both_lexicons",
        "feature_names": list(DERIVED_LINGUISTIC_FEATURES),
    }


class LinguisticFeatureExtractor(BaseEstimator, TransformerMixin):
    """Create two lexical rates from one or more preselected text columns."""

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
        validate_lexicons(self.certainty_terms, self.hedge_terms)
        return self

    def transform(self, values: object) -> np.ndarray:
        if isinstance(values, pd.DataFrame):
            if values.shape[1] < 1:
                raise ValueError(
                    "LinguisticFeatureExtractor needs at least one text column."
                )
            combined = values.fillna("").astype(str).agg(" ".join, axis=1)
        else:
            array = np.asarray(values, dtype=object)
            if array.ndim != 2 or array.shape[1] < 1:
                raise ValueError(
                    "LinguisticFeatureExtractor expects one or more text columns."
                )
            combined = pd.DataFrame(array).fillna("").astype(str).agg(" ".join, axis=1)
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
