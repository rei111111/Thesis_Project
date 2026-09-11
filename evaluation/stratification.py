"""Shared label and platform stratification helpers."""

from __future__ import annotations

from collections.abc import Iterable, Iterator

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedGroupKFold


def joint_stratification_labels(
    data: pd.DataFrame,
    labels: Iterable[object],
    columns: tuple[str, ...] = (),
) -> pd.Series:
    """Combine non-predictive audit strata with the supervised label."""
    label_values = list(labels)
    if len(label_values) != len(data):
        raise ValueError("Stratification labels and rows must have equal length.")
    label_series = pd.Series(label_values, index=data.index, dtype=object).astype(str)
    if not columns:
        return label_series
    missing = [column for column in columns if column not in data.columns]
    if missing:
        raise ValueError(f"Stratification columns are missing: {missing}")
    parts: list[pd.Series] = []
    for column in columns:
        values = data[column].fillna("").astype(str).str.strip()
        if values.eq("").any():
            raise ValueError(f"Stratification column {column} contains blanks.")
        parts.append(values)
    parts.append(label_series)
    result = parts[0]
    for part in parts[1:]:
        result = result + "\x1f" + part
    return result


def check_group_fold_counts(
    strata: pd.Series,
    groups: np.ndarray,
    folds: int,
    context: str,
) -> None:
    """Require enough distinct content groups in every requested stratum."""
    frame = pd.DataFrame(
        {"stratum": strata.reset_index(drop=True), "group": groups}
    )
    if frame.empty:
        raise ValueError(f"{context} cannot split an empty population.")
    counts = frame.drop_duplicates(["group", "stratum"])[
        "stratum"
    ].value_counts()
    minimum = int(counts.min())
    if minimum < folds:
        raise ValueError(
            f"{context} needs at least {folds} content groups per stratum; "
            f"found {minimum}."
        )


class StratifiedGroupKFoldByColumns:
    """GridSearchCV-compatible joint platform/label grouped splitter."""

    def __init__(
        self,
        n_splits: int = 5,
        shuffle: bool = True,
        random_state: int | None = None,
        stratification_columns: tuple[str, ...] = (),
    ) -> None:
        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state
        self.stratification_columns = stratification_columns

    def split(
        self,
        data: pd.DataFrame,
        labels: Iterable[object],
        groups: Iterable[object] | None = None,
    ) -> Iterator[tuple[np.ndarray, np.ndarray]]:
        if not isinstance(data, pd.DataFrame):
            raise TypeError(
                "Joint platform/label stratification requires a DataFrame."
            )
        if groups is None:
            raise ValueError("Content groups are required for grouped splitting.")
        group_values = np.asarray(list(groups), dtype=object)
        if len(group_values) != len(data):
            raise ValueError("Content groups and rows must have equal length.")
        strata = joint_stratification_labels(
            data.reset_index(drop=True),
            pd.Series(labels).reset_index(drop=True),
            tuple(self.stratification_columns),
        )
        check_group_fold_counts(
            strata,
            group_values,
            int(self.n_splits),
            "Grouped CV",
        )
        splitter = StratifiedGroupKFold(
            n_splits=int(self.n_splits),
            shuffle=bool(self.shuffle),
            random_state=self.random_state,
        )
        splits = list(splitter.split(data, strata, group_values))
        expected = set(strata.unique())
        for training, validation in splits:
            if set(strata.iloc[training].unique()) != expected or set(strata.iloc[validation].unique()) != expected:
                raise ValueError(
                    "Grouped CV could not represent every requested stratum "
                    "in both partitions; revise the fold count before training."
                )
        yield from splits

    def get_n_splits(
        self,
        data: object = None,
        labels: object = None,
        groups: object = None,
    ) -> int:
        return int(self.n_splits)
