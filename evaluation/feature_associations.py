"""Descriptive associations for the six named non-TF--IDF features."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kruskal, spearmanr

from features.linguistic_features import calculate_linguistic_scores
from features.metadata_features import ENGAGEMENT_COLUMNS


NAMED_FEATURES = (
    "certainty_score",
    "hedge_score",
    "log1p_likes",
    "log1p_comments",
    "log1p_views",
    "log1p_duration_sec",
)


def derive_named_features(
    data: pd.DataFrame,
    certainty_terms: Iterable[str],
    hedge_terms: Iterable[str],
) -> pd.DataFrame:
    """Create an auditable row-level table without modifying the source CSV."""
    required = {"title", "transcript", "label", *ENGAGEMENT_COLUMNS}
    missing = sorted(required - set(data.columns))
    if missing:
        raise ValueError(f"Named-feature analysis is missing columns: {missing}")
    combined = (
        data["title"].fillna("").astype(str)
        + " "
        + data["transcript"].fillna("").astype(str)
    )
    scores = np.asarray(
        [
            calculate_linguistic_scores(text, certainty_terms, hedge_terms)
            for text in combined
        ],
        dtype=float,
    )
    result = pd.DataFrame(
        {
            "row_index": (
                data["row_index"].astype(int).to_numpy()
                if "row_index" in data.columns
                else data.index.to_numpy(dtype=int)
            ),
            "label": pd.to_numeric(data["label"]).astype(int).to_numpy(),
            "certainty_score": scores[:, 0],
            "hedge_score": scores[:, 1],
        }
    )
    for column in ENGAGEMENT_COLUMNS:
        values = pd.to_numeric(data[column], errors="raise").to_numpy(dtype=float)
        if np.any(values < 0):
            raise ValueError(f"{column} contains negative values.")
        result[f"log1p_{column}"] = np.log1p(values)
    return result


def class_descriptives(features: pd.DataFrame, population: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for label, label_data in features.groupby("label", sort=True):
        for feature in NAMED_FEATURES:
            values = label_data[feature].to_numpy(dtype=float)
            rows.append(
                {
                    "population": population,
                    "label": int(label),
                    "feature": feature,
                    "count": len(values),
                    "mean": float(np.mean(values)),
                    "sample_std": float(np.std(values, ddof=1)) if len(values) > 1 else 0.0,
                    "minimum": float(np.min(values)),
                    "q1": float(np.quantile(values, 0.25)),
                    "median": float(np.median(values)),
                    "q3": float(np.quantile(values, 0.75)),
                    "maximum": float(np.max(values)),
                }
            )
    return pd.DataFrame(rows)


def _holm_adjust(p_values: np.ndarray) -> np.ndarray:
    """Holm-adjust a finite vector while preserving original order."""
    finite = np.isfinite(p_values)
    adjusted = np.full_like(p_values, np.nan, dtype=float)
    finite_indices = np.flatnonzero(finite)
    order = finite_indices[np.argsort(p_values[finite])]
    running = 0.0
    count = len(order)
    for rank, index in enumerate(order):
        candidate = min(1.0, (count - rank) * float(p_values[index]))
        running = max(running, candidate)
        adjusted[index] = running
    return adjusted


def _stratified_bootstrap_spearman(
    labels: np.ndarray,
    values: np.ndarray,
    resamples: int,
    seed: int,
    confidence_level: float,
) -> tuple[float, float]:
    generator = np.random.default_rng(seed)
    if np.unique(values).size < 2:
        return float("nan"), float("nan")
    indices_by_class = [np.flatnonzero(labels == value) for value in np.unique(labels)]
    samples = np.empty(resamples, dtype=float)
    for iteration in range(resamples):
        sampled = np.concatenate(
            [
                generator.choice(indices, size=len(indices), replace=True)
                for indices in indices_by_class
            ]
        )
        samples[iteration] = float(spearmanr(labels[sampled], values[sampled]).statistic)
    tail = (1.0 - confidence_level) / 2.0
    return (
        float(np.nanquantile(samples, tail)),
        float(np.nanquantile(samples, 1.0 - tail)),
    )


def association_statistics(
    features: pd.DataFrame,
    population: str,
    bootstrap_resamples: int,
    seed: int,
    confidence_level: float = 0.95,
) -> pd.DataFrame:
    """Report ordinal monotonic and omnibus association statistics."""
    labels = features["label"].to_numpy(dtype=int)
    rows: list[dict[str, object]] = []
    for offset, feature in enumerate(NAMED_FEATURES):
        values = features[feature].to_numpy(dtype=float)
        if np.unique(values).size < 2:
            spearman_statistic = float("nan")
            spearman_p_value = float("nan")
        else:
            spearman = spearmanr(labels, values)
            spearman_statistic = float(spearman.statistic)
            spearman_p_value = float(spearman.pvalue)
        groups = [
            values[labels == label]
            for label in sorted(np.unique(labels))
        ]
        if np.unique(values).size < 2:
            omnibus_statistic = float("nan")
            omnibus_p_value = float("nan")
        else:
            omnibus = kruskal(*groups)
            omnibus_statistic = float(omnibus.statistic)
            omnibus_p_value = float(omnibus.pvalue)
        class_count = len(groups)
        epsilon_squared = (
            max(
                0.0,
                float(
                    (omnibus_statistic - class_count + 1)
                    / (len(values) - class_count)
                ),
            )
            if np.isfinite(omnibus_statistic)
            else float("nan")
        )
        ci_low, ci_high = _stratified_bootstrap_spearman(
            labels,
            values,
            resamples=bootstrap_resamples,
            seed=seed + offset,
            confidence_level=confidence_level,
        )
        rows.append(
            {
                "population": population,
                "feature": feature,
                "spearman_rho_with_increasing_severity": spearman_statistic,
                "spearman_p_value": spearman_p_value,
                "spearman_ci_low": ci_low,
                "spearman_ci_high": ci_high,
                "kruskal_h": omnibus_statistic,
                "kruskal_p_value": omnibus_p_value,
                "kruskal_epsilon_squared": epsilon_squared,
            }
        )
    result = pd.DataFrame(rows)
    result["spearman_p_holm"] = _holm_adjust(
        result["spearman_p_value"].to_numpy(dtype=float)
    )
    result["kruskal_p_holm"] = _holm_adjust(
        result["kruskal_p_value"].to_numpy(dtype=float)
    )
    result["absolute_spearman_rank"] = result[
        "spearman_rho_with_increasing_severity"
    ].abs().rank(method="min", ascending=False, na_option="bottom").astype(int)
    return result.sort_values("absolute_spearman_rank", kind="stable")


def save_named_feature_reports(
    full_labelled_data: pd.DataFrame,
    training_data: pd.DataFrame,
    certainty_terms: Iterable[str],
    hedge_terms: Iterable[str],
    output_directory: str | Path,
    bootstrap_resamples: int,
    seed: int,
    confidence_level: float = 0.95,
) -> dict[str, int]:
    """Save full-sample descriptives and training-only inferential views."""
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    full_features = derive_named_features(
        full_labelled_data,
        certainty_terms,
        hedge_terms,
    )
    training_features = derive_named_features(
        training_data,
        certainty_terms,
        hedge_terms,
    )
    full_features.to_csv(directory / "named_features_full_labelled.csv", index=False)
    training_features.to_csv(directory / "named_features_training_only.csv", index=False)
    descriptives = pd.concat(
        [
            class_descriptives(full_features, "full_labelled_sample"),
            class_descriptives(training_features, "training_only"),
        ],
        ignore_index=True,
    )
    descriptives.to_csv(directory / "named_feature_class_descriptives.csv", index=False)
    associations = association_statistics(
        training_features,
        "training_only",
        bootstrap_resamples=bootstrap_resamples,
        seed=seed,
        confidence_level=confidence_level,
    )
    associations.to_csv(directory / "named_feature_associations.csv", index=False)
    return {
        "full_labelled_rows": len(full_features),
        "training_rows": len(training_features),
        "descriptive_rows": len(descriptives),
        "association_rows": len(associations),
    }
