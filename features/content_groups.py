"""Stable content groups used to prevent duplicate-text leakage.

Exact hashing alone misses transcripts that differ only through punctuation,
minor transcription corrections, or a short added introduction.  The study
therefore groups both exact duplicates and highly similar token sequences.
The similarity rule is label-blind and is used only to keep related videos in
the same data partition; it is never supplied to a classifier as a feature.
"""

from __future__ import annotations

import hashlib
from difflib import SequenceMatcher
from functools import lru_cache
import re
import unicodedata
import warnings

import numpy as np
import pandas as pd


WHITESPACE_PATTERN = re.compile(r"\s+")
TOKEN_PATTERN = re.compile(r"\w+(?:'\w+)?", flags=re.UNICODE)

# Frozen grouping protocol for the corrected leakage audit and grouped CV. The
# length/Jaccard checks are conservative pre-filters; SequenceMatcher makes the
# final decision. Changing these values defines a new CV/audit protocol and
# requires rerunning every condition.
NEAR_DUPLICATE_SEQUENCE_THRESHOLD = 0.80
NEAR_DUPLICATE_MINIMUM_TOKENS = 20
NEAR_DUPLICATE_MINIMUM_LENGTH_RATIO = 0.70
NEAR_DUPLICATE_MINIMUM_TOKEN_JACCARD = 0.50
CONTENT_GROUP_METHOD = (
    "connected components of token-sequence similarity >= 0.80 for texts "
    "with >= 20 tokens, after length-ratio >= 0.70 and token-Jaccard >= 0.50 "
    "prefilters"
)
EXACT_CONTENT_GROUP_METHOD = "sha256 of NFKC-casefolded whitespace-normalized transcript"


def normalize_transcript(text: object) -> str:
    """Normalize transcript text only for duplicate-content grouping."""
    value = "" if text is None or pd.isna(text) else str(text)
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    return WHITESPACE_PATTERN.sub(" ", value)


def _tokens(value: str) -> tuple[str, ...]:
    return tuple(TOKEN_PATTERN.findall(value))


def _is_near_duplicate(
    first: tuple[str, ...],
    second: tuple[str, ...],
) -> bool:
    """Apply the frozen, label-blind near-duplicate rule to two transcripts."""
    if not first or not second:
        return False
    if first == second:
        return True
    if min(len(first), len(second)) < NEAR_DUPLICATE_MINIMUM_TOKENS:
        return False
    length_ratio = min(len(first), len(second)) / max(len(first), len(second))
    if length_ratio < NEAR_DUPLICATE_MINIMUM_LENGTH_RATIO:
        return False
    first_set = set(first)
    second_set = set(second)
    union = first_set | second_set
    jaccard = len(first_set & second_set) / len(union) if union else 1.0
    if jaccard < NEAR_DUPLICATE_MINIMUM_TOKEN_JACCARD:
        return False
    return (
        SequenceMatcher(None, first, second, autojunk=False).ratio()
        >= NEAR_DUPLICATE_SEQUENCE_THRESHOLD
    )


@lru_cache(maxsize=128)
def _component_representatives(
    normalized_texts: tuple[str, ...],
) -> tuple[str, ...]:
    """Return the canonical transcript for each near-duplicate component."""
    tokenized = tuple(_tokens(value) for value in normalized_texts)
    parents = list(range(len(normalized_texts)))

    def find(index: int) -> int:
        while parents[index] != index:
            parents[index] = parents[parents[index]]
            index = parents[index]
        return index

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root != second_root:
            parents[max(first_root, second_root)] = min(first_root, second_root)

    for first_index in range(len(normalized_texts)):
        for second_index in range(first_index + 1, len(normalized_texts)):
            if (
                normalized_texts[first_index] == normalized_texts[second_index]
                or _is_near_duplicate(
                    tokenized[first_index],
                    tokenized[second_index],
                )
            ):
                union(first_index, second_index)

    members: dict[int, list[str]] = {}
    for index, value in enumerate(normalized_texts):
        members.setdefault(find(index), []).append(value)
    canonical = {
        root: min(values)
        for root, values in members.items()
    }
    return tuple(canonical[find(index)] for index in range(len(normalized_texts)))


def exact_content_group_ids(data: pd.DataFrame) -> np.ndarray:
    """Return transcript hashes used for exact-duplicate diagnostics."""
    if "transcript" not in data.columns:
        raise ValueError("transcript is required to construct content groups.")
    return data["transcript"].map(
        lambda value: hashlib.sha256(
            normalize_transcript(value).encode("utf-8")
        ).hexdigest()
    ).to_numpy(dtype=object)


def content_group_ids(data: pd.DataFrame) -> np.ndarray:
    """Return group ids for exact and operationally near-duplicate content."""
    if "transcript" not in data.columns:
        raise ValueError("transcript is required to construct content groups.")
    normalized = tuple(data["transcript"].map(normalize_transcript))
    representatives = _component_representatives(normalized)
    return np.asarray(
        [
            hashlib.sha256(value.encode("utf-8")).hexdigest()
            for value in representatives
        ],
        dtype=object,
    )


def validate_group_labels(
    data: pd.DataFrame,
    target_column: str = "label",
) -> None:
    """Report author-controlled label conflicts without removing any rows."""
    # Conflicting labels do not cause leakage when the content group remains
    # intact. The author owns their adjudication; grouping applies either way.
    groups = exact_content_group_ids(data)
    frame = pd.DataFrame(
        {
            "group": groups,
            "label": pd.to_numeric(data[target_column], errors="coerce"),
        }
    ).dropna(subset=["label"])
    conflicts = frame.groupby("group")["label"].nunique()
    if (conflicts > 1).any():
        warnings.warn(
            "Identical transcripts have conflicting labels. Review the "
            "author-controlled annotations; all rows remain included and "
            "grouped, and execution is not blocked.",
            UserWarning,
            stacklevel=2,
        )


def duplicate_group_count(data: pd.DataFrame) -> int:
    """Count exact-or-near-duplicate groups containing more than one row."""
    counts = pd.Series(content_group_ids(data)).value_counts()
    return int((counts > 1).sum())


def exact_duplicate_group_count(data: pd.DataFrame) -> int:
    """Count exact normalized-transcript groups containing multiple rows."""
    counts = pd.Series(exact_content_group_ids(data)).value_counts()
    return int((counts > 1).sum())
