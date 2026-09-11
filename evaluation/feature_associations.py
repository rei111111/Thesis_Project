"""Descriptive associations for the six named non-TF--IDF features."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kruskal, spearmanr

from evaluation.metrics import validate_label_array
from evaluation.resampling import bootstrap_indices
from features.content_groups import content_group_ids
from features.linguistic_features import calculate_linguistic_scores
from features.metadata_features import (
    ENGAGEMENT_COLUMNS,
    WithinPlatformPercentileTransformer,
    transformer_feature_names,
)


NAMED_FEATURES = (
    "certainty_score",
    "hedge_score",
    "log1p_likes",
    "log1p_comments",
    "log1p_views",
    "log1p_duration_sec",
)


def named_features_for_transform(engagement_transform: str) -> tuple[str, ...]:
    """Return report-column names aligned with the active feature pipeline."""
    if engagement_transform == "log1p":
        return NAMED_FEATURES
    if engagement_transform == "within_platform_percentile":
        return transformer_feature_names(engagement_transform)
    raise ValueError(f"Unknown engagement transform: {engagement_transform}")


def derive_named_features(
    data: pd.DataFrame,
    certainty_terms: Iterable[str],
    hedge_terms: Iterable[str],
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
) -> pd.DataFrame:
    """Create an auditable row-level table without modifying the source CSV."""
    required = {"label", *text_columns, *ENGAGEMENT_COLUMNS}
    if engagement_transform == "within_platform_percentile":
        required.add(platform_column)
    missing = sorted(required - set(data.columns))
    if missing:
        raise ValueError(f"Named-feature analysis is missing columns: {missing}")
    combined = data.loc[:, list(text_columns)].fillna("").astype(str).agg(
        " ".join, axis=1
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
            "label": validate_label_array(data["label"], "Association labels"),
            "certainty_score": scores[:, 0],
            "hedge_score": scores[:, 1],
        }
    )
    if engagement_transform == "log1p":
        for column in ENGAGEMENT_COLUMNS:
            values = pd.to_numeric(data[column], errors="raise").to_numpy(dtype=float)
            if not np.isfinite(values).all() or np.any(values < 0):
                raise ValueError(f"{column} must contain finite non-negative values.")
            result[f"log1p_{column}"] = np.log1p(values)
    elif engagement_transform == "within_platform_percentile":
        transformer = WithinPlatformPercentileTransformer(
            platform_column=platform_column,
            value_columns=ENGAGEMENT_COLUMNS,
        ).fit(data[[platform_column, *ENGAGEMENT_COLUMNS]])
        transformed = transformer.transform(
            data[[platform_column, *ENGAGEMENT_COLUMNS]]
        )
        for index, column in enumerate(transformer.get_feature_names_out()):
            result[str(column)] = transformed[:, index]
    else:
        raise ValueError(f"Unknown engagement transform: {engagement_transform}")
    if platform_column in data.columns:
        for column in ("record_id", platform_column):
            if column in data.columns:
                result[column] = data[column].astype(str).to_numpy()
        result["content_group"] = content_group_ids(data)
    return result


def class_descriptives(
    features: pd.DataFrame,
    population: str,
    feature_names: tuple[str, ...] = NAMED_FEATURES,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for label, label_data in features.groupby("label", sort=True):
        for feature in feature_names:
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
    groups: object = None,
) -> tuple[float, float, int]:
    if np.unique(values).size < 2:
        return float("nan"), float("nan"), 0
    samples = np.full(resamples, np.nan, dtype=float)
    for iteration, sampled in enumerate(bootstrap_indices(labels, resamples, seed, groups)):
        if np.unique(labels[sampled]).size > 1 and np.unique(values[sampled]).size > 1:
            samples[iteration] = float(spearmanr(labels[sampled], values[sampled]).statistic)
    tail = (1.0 - confidence_level) / 2.0
    finite = samples[np.isfinite(samples)]
    if finite.size == 0:
        return float("nan"), float("nan"), 0
    return (
        float(np.quantile(finite, tail)),
        float(np.quantile(finite, 1.0 - tail)),
        int(finite.size),
    )


def association_statistics(
    features: pd.DataFrame,
    population: str,
    bootstrap_resamples: int,
    seed: int,
    confidence_level: float = 0.95,
    feature_names: tuple[str, ...] = NAMED_FEATURES,
) -> pd.DataFrame:
    """Report ordinal monotonic and omnibus association statistics."""
    if not isinstance(bootstrap_resamples, (int, np.integer)) or isinstance(
        bootstrap_resamples, bool
    ) or int(bootstrap_resamples) < 1:
        raise ValueError("bootstrap_resamples must be a positive integer.")
    if not 0 < confidence_level < 1:
        raise ValueError("confidence_level must be between zero and one.")
    bootstrap_resamples = int(bootstrap_resamples)
    labels = validate_label_array(features["label"], "Association labels")
    bootstrap_groups = features["content_group"].to_numpy() if "content_group" in features else None
    dependent_rows = bootstrap_groups is not None and pd.Series(bootstrap_groups).duplicated().any()
    rows: list[dict[str, object]] = []
    for offset, feature in enumerate(feature_names):
        values = features[feature].to_numpy(dtype=float)
        if not np.isfinite(values).all():
            raise ValueError(f"Association feature {feature} is non-finite.")
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
        # Rank epsilon-squared is the between-group share of total rank
        # variance, H / (N - 1). (H - k + 1) / (N - k) instead estimates
        # rank eta-squared and must not be reported under the epsilon name.
        epsilon_squared = (
            float(np.clip(omnibus_statistic / (len(values) - 1), 0.0, 1.0))
            if np.isfinite(omnibus_statistic)
            else float("nan")
        )
        ci_low, ci_high, valid_resamples = _stratified_bootstrap_spearman(
            labels,
            values,
            resamples=bootstrap_resamples,
            seed=seed + offset,
            confidence_level=confidence_level,
            groups=bootstrap_groups,
        )
        if dependent_rows:
            spearman_p_value = omnibus_p_value = float("nan")
        rows.append(
            {
                "population": population,
                "feature": feature,
                "spearman_rho_with_increasing_severity": spearman_statistic,
                "spearman_p_value": spearman_p_value,
                "spearman_ci_low": ci_low,
                "spearman_ci_high": ci_high,
                "bootstrap_resamples_requested": bootstrap_resamples,
                "bootstrap_valid_resamples": valid_resamples,
                "bootstrap_confidence_level": confidence_level,
                "bootstrap_seed": seed + offset,
                "resampling_unit": "content_group" if bootstrap_groups is not None else "label_stratified_row",
                "association_status": "constant_feature" if np.unique(values).size < 2 else "estimated",
                "p_value_assumption": "independent_rows",
                "p_values_suppressed_for_cluster_dependence": bool(dependent_rows),
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
    text_columns: tuple[str, ...] = ("title", "transcript"),
    engagement_transform: str = "log1p",
    platform_column: str = "platform",
) -> dict[str, int]:
    """Save full-sample descriptives and training-only inferential views."""
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    full_features = derive_named_features(
        full_labelled_data,
        certainty_terms,
        hedge_terms,
        text_columns=text_columns,
        engagement_transform=engagement_transform,
        platform_column=platform_column,
    )
    training_features = derive_named_features(
        training_data,
        certainty_terms,
        hedge_terms,
        text_columns=text_columns,
        engagement_transform=engagement_transform,
        platform_column=platform_column,
    )
    feature_names = named_features_for_transform(engagement_transform)
    full_features.to_csv(directory / "named_features_full_labelled.csv", index=False)
    training_features.to_csv(directory / "named_features_training_only.csv", index=False)
    descriptives = pd.concat(
        [
            class_descriptives(
                full_features, "full_labelled_sample", feature_names
            ),
            class_descriptives(training_features, "training_only", feature_names),
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
        feature_names=feature_names,
    )
    associations.to_csv(directory / "named_feature_associations.csv", index=False)
    return {
        "full_labelled_rows": len(full_features),
        "training_rows": len(training_features),
        "descriptive_rows": len(descriptives),
        "association_rows": len(associations),
    }
