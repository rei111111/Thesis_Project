"""Paired row or content-cluster resampling without splitting related rows."""

from collections.abc import Iterator

import numpy as np
import pandas as pd


def bootstrap_indices(
    labels: np.ndarray,
    resamples: int,
    seed: int,
    groups: object = None,
) -> Iterator[np.ndarray]:
    """Sample rows within labels, or whole clusters with replacement.

    Cluster sampling lets class/platform proportions vary. A cluster spanning
    platforms or labels stays intact, including every repeated member.
    """
    generator = np.random.default_rng(seed)
    if groups is None:
        parts = [np.flatnonzero(labels == value) for value in np.unique(labels)]
        for _ in range(resamples):
            yield np.concatenate([
                generator.choice(indices, size=len(indices), replace=True)
                for indices in parts
            ])
        return
    values = np.asarray(groups, dtype=object)
    if values.ndim != 1 or len(values) != len(labels) or pd.isna(values).any():
        raise ValueError("Bootstrap groups must align with every labelled row.")
    codes, unique = pd.factorize(values, sort=True)
    if len(unique) < 2:
        raise ValueError("Cluster uncertainty needs at least two content groups.")
    members = [np.flatnonzero(codes == index) for index in range(len(unique))]
    for _ in range(resamples):
        drawn = generator.integers(0, len(members), size=len(members))
        yield np.concatenate([members[index] for index in drawn])
