"""Stable content groups used to prevent duplicate-text leakage."""

from __future__ import annotations

import hashlib
import re
import unicodedata

import numpy as np
import pandas as pd


WHITESPACE_PATTERN = re.compile(r"\s+")


def normalize_transcript(text: object) -> str:
    """Normalize transcript text only for duplicate-content grouping."""
    value = "" if text is None or pd.isna(text) else str(text)
    value = unicodedata.normalize("NFKC", value).casefold().strip()
    return WHITESPACE_PATTERN.sub(" ", value)


def content_group_ids(data: pd.DataFrame) -> np.ndarray:
    """Return a stable SHA-256 group id for each normalized transcript."""
    if "transcript" not in data.columns:
        raise ValueError("transcript is required to construct content groups.")
    return data["transcript"].map(
        lambda value: hashlib.sha256(
            normalize_transcript(value).encode("utf-8")
        ).hexdigest()
    ).to_numpy(dtype=object)


def validate_group_labels(
    data: pd.DataFrame,
    target_column: str = "label",
) -> None:
    """Reject identical transcripts assigned conflicting supervised labels."""
    groups = content_group_ids(data)
    frame = pd.DataFrame(
        {
            "group": groups,
            "label": pd.to_numeric(data[target_column], errors="coerce"),
        }
    ).dropna(subset=["label"])
    conflicts = frame.groupby("group")["label"].nunique()
    if (conflicts > 1).any():
        raise ValueError(
            "Identical transcripts have conflicting labels and cannot be "
            "evaluated without leakage."
        )


def duplicate_group_count(data: pd.DataFrame) -> int:
    """Count normalized-transcript groups containing more than one row."""
    counts = pd.Series(content_group_ids(data)).value_counts()
    return int((counts > 1).sum())
