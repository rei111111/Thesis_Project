"""Generate every RQ1--RQ3 table, statistic, audit file, and figure."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yaml

from evaluation.feature_associations import save_named_feature_reports
from evaluation.final_evaluation import load_saved_split
from evaluation.metrics import (
    bootstrap_many_conditions,
    calculate_metrics,
    class_distribution_table,
    ordinal_error_summary,
)
from features.linguistic_features import validate_lexicons
from models.condition_registry import (
    BASELINE_NAMES,
    CONDITION_BY_NAME,
    CONDITION_NAMES,
    ablation_pairs,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
METRIC_NAMES = (
    "quadratic_weighted_kappa",
    "accuracy",
    "weighted_f1",
    "mean_absolute_error",
)
LABEL_NAMES = {
    1: "Accurate",
    2: "Slightly misleading",
    3: "Moderately misleading",
    4: "Highly misleading",
}


def load_settings(relative_path: str) -> dict[str, Any]:
    with (PROJECT_ROOT / relative_path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def run_root(run_name: str) -> Path:
    if not run_name or any(part in run_name for part in ("/", "\\", "..")):
        raise ValueError("run_name must be one safe directory name.")
    return PROJECT_ROOT / "results" if run_name == "primary" else PROJECT_ROOT / "results" / run_name


def expected_names(settings: dict[str, Any]) -> tuple[str, ...]:
    include_baselines = bool(settings.get("reporting", {}).get("include_baselines", True))
    return CONDITION_NAMES + (BASELINE_NAMES if include_baselines else ())


def load_prediction_files(
    root: Path,
    settings: dict[str, Any],
) -> dict[str, pd.DataFrame]:
    files = sorted((root / "predictions").glob("*_heldout.csv"))
    if not files:
        raise FileNotFoundError("No held-out prediction files were found.")
    observed = {
        path.stem.removesuffix("_heldout"): pd.read_csv(path) for path in files
    }
    expected = expected_names(settings)
    missing = sorted(set(expected) - set(observed))
    unexpected = sorted(set(observed) - set(expected))
    if missing or unexpected:
        raise ValueError(
            "Held-out results are incomplete or unexpected. "
            f"Missing: {missing}; unexpected: {unexpected}."
        )
    required_columns = {"row_index", "true_label", "prediction"}
    reference = observed[expected[0]]
    reference_rows = set(reference["row_index"])
    reference_truth = reference.set_index("row_index")["true_label"].sort_index()
    for condition, frame in observed.items():
        if not required_columns.issubset(frame.columns):
            raise ValueError(f"{condition} is missing prediction columns.")
        if frame["row_index"].duplicated().any():
            raise ValueError(f"{condition} contains duplicate row indices.")
        if "condition" in frame.columns and not frame["condition"].eq(condition).all():
            raise ValueError(
                f"{condition} contains a mismatched internal condition name."
            )
        if set(frame["row_index"]) != reference_rows:
            raise ValueError("Held-out prediction files cover different videos.")
        truth = frame.set_index("row_index")["true_label"].sort_index()
        if not truth.equals(reference_truth):
            raise ValueError("Held-out prediction files disagree on true labels.")
    return {name: observed[name].sort_values("row_index") for name in expected}


def load_cv_files(root: Path, settings: dict[str, Any]) -> dict[str, pd.DataFrame]:
    results: dict[str, pd.DataFrame] = {}
    reference_assignment: pd.DataFrame | None = None
    expected_folds = int(settings["evaluation"]["outer_folds"])
    required = {"fold", *METRIC_NAMES}
    for condition in expected_names(settings):
        path = root / "metrics" / f"{condition}_cv.csv"
        if not path.exists():
            raise FileNotFoundError(f"Missing outer-CV metrics: {path}")
        frame = pd.read_csv(path)
        if not required.issubset(frame.columns):
            raise ValueError(f"{path} is missing required CV metric columns.")
        if len(frame) != expected_folds or frame["fold"].nunique() != expected_folds:
            raise ValueError(f"{condition} does not contain {expected_folds} folds.")
        prediction_path = root / "predictions" / f"{condition}_cv.csv"
        if not prediction_path.exists():
            raise FileNotFoundError(f"Missing outer-CV predictions: {prediction_path}")
        predictions = pd.read_csv(prediction_path)
        prediction_columns = {"row_index", "fold", "true_label", "prediction"}
        if not prediction_columns.issubset(predictions.columns):
            raise ValueError(f"{prediction_path} is missing CV prediction columns.")
        if predictions["row_index"].duplicated().any():
            raise ValueError(f"{condition} repeats rows across outer folds.")
        assignment = predictions[["row_index", "fold", "true_label"]].sort_values(
            "row_index"
        ).reset_index(drop=True)
        if reference_assignment is None:
            reference_assignment = assignment
        elif not assignment.equals(reference_assignment):
            raise ValueError(
                "Outer-fold row assignments differ across conditions; paired "
                "fold comparisons would be invalid."
            )
        results[condition] = frame.sort_values("fold").reset_index(drop=True)
    return results


def save_confusion_figure(
    condition: str,
    matrix: list[list[int]],
    figure_directory: Path,
) -> None:
    figure_directory.mkdir(parents=True, exist_ok=True)
    matrix_frame = pd.DataFrame(matrix, index=(1, 2, 3, 4), columns=(1, 2, 3, 4))
    matrix_frame.index.name = "true_label"
    matrix_frame.columns.name = "predicted_label"
    matrix_frame.to_csv(figure_directory / f"{condition}_confusion.csv")
    figure, axis = plt.subplots(figsize=(5, 4))
    sns.heatmap(
        matrix_frame,
        annot=True,
        fmt="d",
        cmap="Blues",
        ax=axis,
    )
    axis.set_xlabel("Predicted label")
    axis.set_ylabel("True label")
    axis.set_title(condition)
    figure.tight_layout()
    figure.savefig(figure_directory / f"{condition}_confusion.png", dpi=200)
    plt.close(figure)


def heldout_tables(
    prediction_sets: dict[str, pd.DataFrame],
    figure_directory: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object], pd.DataFrame]:
    summary_rows: list[dict[str, object]] = []
    class_rows: list[dict[str, object]] = []
    error_rows: list[dict[str, object]] = []
    full_metrics: dict[str, object] = {}
    for condition, predictions in prediction_sets.items():
        metrics = calculate_metrics(
            predictions["true_label"],
            predictions["prediction"],
        )
        full_metrics[condition] = metrics
        summary_rows.append(
            {
                "condition": condition,
                **{name: metrics[name] for name in METRIC_NAMES},
            }
        )
        for label, values in metrics["per_class"].items():
            class_rows.append(
                {
                    "condition": condition,
                    "label": int(label),
                    **values,
                }
            )
        error_rows.append(
            {
                "condition": condition,
                **ordinal_error_summary(
                    predictions["true_label"], predictions["prediction"]
                ),
            }
        )
        save_confusion_figure(
            condition,
            metrics["confusion_matrix"],
            figure_directory,
        )
    return (
        pd.DataFrame(summary_rows),
        pd.DataFrame(class_rows),
        full_metrics,
        pd.DataFrame(error_rows),
    )


def cv_tables(
    cv_results: dict[str, pd.DataFrame],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    summary_rows: list[dict[str, object]] = []
    for condition, frame in cv_results.items():
        row: dict[str, object] = {"condition": condition, "folds": len(frame)}
        for metric in METRIC_NAMES:
            row[f"{metric}_mean"] = float(frame[metric].mean())
            row[f"{metric}_sample_std"] = float(frame[metric].std(ddof=1))
            row[f"{metric}_minimum"] = float(frame[metric].min())
            row[f"{metric}_maximum"] = float(frame[metric].max())
        summary_rows.append(row)

    difference_rows: list[dict[str, object]] = []
    for first, second in itertools.combinations(cv_results, 2):
        merged = cv_results[first][["fold", *METRIC_NAMES]].merge(
            cv_results[second][["fold", *METRIC_NAMES]],
            on="fold",
            suffixes=("_a", "_b"),
            validate="one_to_one",
        )
        for metric in METRIC_NAMES:
            differences = merged[f"{metric}_a"] - merged[f"{metric}_b"]
            higher_is_better = metric != "mean_absolute_error"
            first_wins = differences.gt(0) if higher_is_better else differences.lt(0)
            second_wins = differences.lt(0) if higher_is_better else differences.gt(0)
            difference_rows.append(
                {
                    "condition_a": first,
                    "condition_b": second,
                    "metric": metric,
                    "mean_a_minus_b": float(differences.mean()),
                    "sample_std_a_minus_b": float(differences.std(ddof=1)),
                    "minimum_a_minus_b": float(differences.min()),
                    "maximum_a_minus_b": float(differences.max()),
                    "condition_a_fold_wins": int(first_wins.sum()),
                    "condition_b_fold_wins": int(second_wins.sum()),
                    "ties": int(differences.eq(0).sum()),
                    "higher_is_better": higher_is_better,
                    "inferential_test_performed": False,
                }
            )
    return pd.DataFrame(summary_rows), pd.DataFrame(difference_rows)


def add_metric_ranks(frame: pd.DataFrame, suffix: str = "") -> pd.DataFrame:
    result = frame.copy()
    for metric in METRIC_NAMES:
        column = f"{metric}{suffix}"
        if column in result.columns:
            result[f"{metric}_rank"] = (
                result[column]
                .rank(
                    method="min",
                    ascending=metric == "mean_absolute_error",
                )
                .astype(int)
            )
    return result


def add_condition_metadata(frame: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for condition in frame["condition"]:
        if condition in CONDITION_BY_NAME:
            spec = CONDITION_BY_NAME[condition]
            rows.append(
                {
                    "condition": condition,
                    "configuration": spec.configuration,
                    "model_family": spec.model_family,
                    "feature_set": spec.feature_set,
                    "experimental_condition": True,
                }
            )
        else:
            rows.append(
                {
                    "condition": condition,
                    "configuration": "baseline",
                    "model_family": condition.removeprefix("BASELINE_"),
                    "feature_set": None,
                    "experimental_condition": False,
                }
            )
    return pd.DataFrame(rows).merge(
        frame,
        on="condition",
        validate="one_to_one",
    )


def save_rq1_distribution(
    data: pd.DataFrame,
    tables_directory: Path,
    figures_directory: Path,
    confidence_level: float,
    excluded_total_claims: tuple[int, ...],
) -> pd.DataFrame:
    labelled = data.loc[data["label"].notna()].copy()
    if excluded_total_claims:
        labelled = labelled.loc[
            ~labelled["total_claims"].isin(excluded_total_claims)
        ]
    distribution = pd.DataFrame(
        class_distribution_table(labelled["label"], confidence_level)
    )
    distribution.insert(1, "category", distribution["label"].map(LABEL_NAMES))
    distribution.to_csv(tables_directory / "rq1_class_distribution.csv", index=False)
    figure, axis = plt.subplots(figsize=(7, 4.5))
    axis.bar(
        distribution["category"],
        distribution["percentage"],
        color="#4472C4",
    )
    axis.set_ylabel("Percentage of labelled videos")
    axis.set_xlabel("Severity category")
    axis.set_ylim(0, max(5.0, float(distribution["percentage"].max()) * 1.2))
    axis.tick_params(axis="x", rotation=20)
    for index, row in distribution.iterrows():
        axis.text(index, row["percentage"] + 0.5, f"{row['percentage']:.1f}%", ha="center")
    figure.tight_layout()
    figure.savefig(figures_directory / "rq1_class_distribution.png", dpi=200)
    plt.close(figure)
    return distribution


def save_error_cases(
    prediction_sets: dict[str, pd.DataFrame],
    data: pd.DataFrame,
    tables_directory: Path,
) -> pd.DataFrame:
    source = data.reset_index(drop=True).copy()
    source.insert(0, "row_index", np.arange(len(source), dtype=int))
    rows: list[pd.DataFrame] = []
    for condition, predictions in prediction_sets.items():
        merged = predictions[["row_index", "true_label", "prediction"]].merge(
            source[["row_index", "title", "transcript", "total_claims", "false_claims"]],
            on="row_index",
            validate="one_to_one",
        )
        merged.insert(0, "condition", condition)
        merged["signed_error"] = merged["prediction"] - merged["true_label"]
        merged["absolute_error"] = merged["signed_error"].abs()
        merged["error_direction"] = np.select(
            [merged["signed_error"] < 0, merged["signed_error"] > 0],
            ["underestimates_severity", "overestimates_severity"],
            default="correct",
        )
        rows.append(merged)
    result = pd.concat(rows, ignore_index=True)
    result.to_csv(tables_directory / "heldout_prediction_cases.csv", index=False)
    result.loc[result["absolute_error"] > 0].to_csv(
        tables_directory / "heldout_error_cases_only.csv",
        index=False,
    )
    return result


def save_interpretability_synthesis(
    root: Path,
    heldout_summary: pd.DataFrame,
    tables_directory: Path,
    top_k: int,
) -> None:
    interpretation_directory = root / "interpretability"
    all_frames: list[pd.DataFrame] = []
    stability_frames: list[pd.DataFrame] = []
    minilm_auxiliary: pd.DataFrame | None = None
    minilm_stability: pd.DataFrame | None = None
    coverage_rows: list[dict[str, object]] = []
    for condition in CONDITION_NAMES:
        spec = CONDITION_BY_NAME[condition]
        if spec.interpretable:
            feature_path = interpretation_directory / f"{condition}_all_features.csv"
            stability_path = interpretation_directory / f"{condition}_feature_stability.csv"
            if not feature_path.exists() or not stability_path.exists():
                raise FileNotFoundError(
                    f"Interpretability output is incomplete for {condition}."
                )
            features = pd.read_csv(feature_path)
            stability = pd.read_csv(stability_path)
            all_frames.append(features)
            stability_frames.append(stability)
            coverage_rows.append(
                {
                    "condition": condition,
                    "interpretability_level": "inherent_named_features",
                    "named_feature_rows": len(features),
                    "fold_stability_rows": len(stability),
                    "substantive_feature_ranking_allowed": True,
                    "named_auxiliary_inspection_allowed": True,
                }
            )
        elif condition == "D_FROZEN_MINILM":
            feature_path = (
                interpretation_directory
                / f"{condition}_named_auxiliary_features.csv"
            )
            stability_path = (
                interpretation_directory
                / f"{condition}_named_auxiliary_stability.csv"
            )
            if not feature_path.exists() or not stability_path.exists():
                raise FileNotFoundError(
                    "MiniLM's named auxiliary interpretability output is incomplete."
                )
            minilm_auxiliary = pd.read_csv(feature_path)
            minilm_stability = pd.read_csv(stability_path)
            coverage_rows.append(
                {
                    "condition": condition,
                    "interpretability_level": (
                        "named_auxiliary_coefficients_with_unnamed_text_embedding"
                    ),
                    "named_feature_rows": len(minilm_auxiliary),
                    "fold_stability_rows": len(minilm_stability),
                    "substantive_feature_ranking_allowed": False,
                    "named_auxiliary_inspection_allowed": True,
                }
            )
        else:
            coverage_rows.append(
                {
                    "condition": condition,
                    "interpretability_level": (
                        "linear_head_over_unnamed_embedding_dimensions"
                        if condition == "D_FROZEN_MINILM"
                        else "opaque_end_to_end_transformer"
                    ),
                    "named_feature_rows": 0,
                    "fold_stability_rows": 0,
                    "substantive_feature_ranking_allowed": False,
                    "named_auxiliary_inspection_allowed": False,
                }
            )
    all_features = pd.concat(all_frames, ignore_index=True)
    all_stability = pd.concat(stability_frames, ignore_index=True)
    prohibited = {"row_index", "total_claims", "false_claims", "label"}
    leaked = sorted(set(all_features["feature"].astype(str)) & prohibited)
    if leaked:
        raise ValueError(f"Interpretability exports reveal prohibited predictors: {leaked}")
    all_features.to_csv(tables_directory / "all_interpretable_model_features.csv", index=False)
    all_stability.to_csv(tables_directory / "all_feature_stability.csv", index=False)

    c_features = all_features.loc[all_features["condition"].str.startswith("C_")]
    named = c_features.loc[
        c_features["feature"].isin(
            ["certainty_score", "hedge_score", "likes", "comments", "views", "duration_sec"]
        )
    ].copy()
    if minilm_auxiliary is not None:
        named = pd.concat([named, minilm_auxiliary], ignore_index=True)
        minilm_auxiliary.to_csv(
            tables_directory / "rq2_minilm_named_auxiliary_weights.csv",
            index=False,
        )
    if minilm_stability is not None:
        minilm_stability.to_csv(
            tables_directory / "rq2_minilm_named_auxiliary_stability.csv",
            index=False,
        )
    named.to_csv(tables_directory / "rq2_named_feature_model_weights.csv", index=False)

    class_specific = c_features.loc[
        c_features["feature_group"].eq("textual")
        & c_features["class_label"].ne("all")
        & c_features["absolute_rank"].le(top_k)
    ].copy()
    if not class_specific.empty:
        class_specific["reciprocal_rank"] = 1.0 / class_specific["absolute_rank"]
        consensus = (
            class_specific.groupby(["class_label", "feature"], as_index=False)
            .agg(
                models_in_top_k=("condition", "nunique"),
                mean_reciprocal_rank=("reciprocal_rank", "mean"),
                mean_absolute_weight=("absolute_weight", "mean"),
                positive_model_count=("direction", lambda values: int((values == "positive").sum())),
                negative_model_count=("direction", lambda values: int((values == "negative").sum())),
                contributing_conditions=("condition", lambda values: "|".join(sorted(set(values)))),
            )
            .sort_values(
                ["class_label", "models_in_top_k", "mean_reciprocal_rank"],
                ascending=[True, False, False],
            )
        )
    else:
        consensus = class_specific
    consensus.to_csv(tables_directory / "rq2_textual_feature_consensus.csv", index=False)
    c_features.loc[
        c_features["condition"].eq("C_DECISION_TREE")
        & c_features["absolute_rank"].le(top_k)
    ].to_csv(tables_directory / "rq2_decision_tree_top_features.csv", index=False)

    coverage = pd.DataFrame(coverage_rows).merge(
        heldout_summary,
        on="condition",
        how="left",
        validate="one_to_one",
    )
    coverage.to_csv(
        tables_directory / "rq3_performance_interpretability_tradeoff.csv",
        index=False,
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_results_manifest(
    root: Path,
    settings: dict[str, Any],
    excluded_total_claims: tuple[int, ...],
) -> None:
    artifact_directories = (
        "metrics",
        "predictions",
        "models",
        "interpretability",
        "feature_associations",
        "tables",
        "figures",
        "reproducibility",
    )
    files = sorted(
        path
        for directory in artifact_directories
        for path in (root / directory).rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    )
    manifest = {
        "complete_experimental_conditions": list(CONDITION_NAMES),
        "contextual_baselines": list(BASELINE_NAMES),
        "condition_count": len(CONDITION_NAMES),
        "expected_outer_folds": int(settings["evaluation"]["outer_folds"]),
        "bootstrap_resamples": int(settings["evaluation"]["bootstrap_resamples"]),
        "excluded_total_claims": list(excluded_total_claims),
        "artifacts": [
            {
                "path": str(path.relative_to(root)),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in files
        ],
    }
    (root / "results_manifest.json").write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--run-name", default="primary")
    parser.add_argument("--exclude-total-claims", nargs="*", type=int, default=[])
    parser.add_argument("--bootstrap-resamples", type=int, default=None)
    parser.add_argument("--association-bootstrap-resamples", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    settings = load_settings(arguments.config)
    if arguments.bootstrap_resamples is not None:
        settings["evaluation"]["bootstrap_resamples"] = arguments.bootstrap_resamples
    if arguments.association_bootstrap_resamples is not None:
        settings["reporting"][
            "association_bootstrap_resamples"
        ] = arguments.association_bootstrap_resamples
    root = run_root(arguments.run_name)
    tables_directory = root / "tables"
    metrics_directory = root / "metrics"
    figures_directory = root / "figures"
    association_directory = root / "feature_associations"
    for directory in (
        tables_directory,
        metrics_directory,
        figures_directory,
        association_directory,
    ):
        directory.mkdir(parents=True, exist_ok=True)

    prediction_sets = load_prediction_files(root, settings)
    cv_results = load_cv_files(root, settings)
    heldout_summary, per_class, full_metrics, errors = heldout_tables(
        prediction_sets,
        figures_directory,
    )
    heldout_summary = add_condition_metadata(add_metric_ranks(heldout_summary))
    heldout_summary.to_csv(tables_directory / "heldout_summary.csv", index=False)
    per_class.to_csv(tables_directory / "heldout_per_class_metrics.csv", index=False)
    errors.to_csv(tables_directory / "heldout_ordinal_error_summary.csv", index=False)
    (metrics_directory / "heldout_full_metrics.json").write_text(
        json.dumps(full_metrics, indent=2),
        encoding="utf-8",
    )

    cv_summary, cv_differences = cv_tables(cv_results)
    cv_summary = add_condition_metadata(
        add_metric_ranks(cv_summary, suffix="_mean")
    )
    cv_summary.to_csv(tables_directory / "cv_summary.csv", index=False)
    cv_differences.to_csv(tables_directory / "cv_paired_differences.csv", index=False)
    cv_ablation_rows: list[pd.DataFrame] = []
    for first, second, contrast in ablation_pairs():
        selected = cv_differences.loc[
            cv_differences["condition_a"].eq(first)
            & cv_differences["condition_b"].eq(second)
        ].copy()
        selected.insert(0, "ablation_contrast", contrast)
        cv_ablation_rows.append(selected)
    pd.concat(cv_ablation_rows, ignore_index=True).to_csv(
        tables_directory / "rq2_cv_ablation_differences.csv",
        index=False,
    )

    reference = next(iter(prediction_sets.values())).sort_values("row_index")
    prediction_map = {
        condition: frame.sort_values("row_index")["prediction"].to_numpy(dtype=int)
        for condition, frame in prediction_sets.items()
    }
    intervals, bootstrap_differences = bootstrap_many_conditions(
        reference["true_label"].to_numpy(dtype=int),
        prediction_map,
        resamples=int(settings["evaluation"]["bootstrap_resamples"]),
        seed=int(settings["seed"]),
        confidence_level=float(settings["reporting"]["confidence_level"]),
    )
    interval_frame = pd.DataFrame(intervals)
    difference_frame = pd.DataFrame(bootstrap_differences)
    interval_frame.to_csv(
        tables_directory / "heldout_bootstrap_metric_intervals.csv",
        index=False,
    )
    difference_frame.to_csv(
        tables_directory / "heldout_bootstrap_pairwise_differences.csv",
        index=False,
    )
    ablation_rows: list[pd.DataFrame] = []
    for first, second, contrast in ablation_pairs():
        selected = difference_frame.loc[
            difference_frame["condition_a"].eq(first)
            & difference_frame["condition_b"].eq(second)
        ].copy()
        selected.insert(0, "ablation_contrast", contrast)
        ablation_rows.append(selected)
    pd.concat(ablation_rows, ignore_index=True).to_csv(
        tables_directory / "rq2_heldout_ablation_bootstrap.csv",
        index=False,
    )

    data_settings = settings["data"]
    dataset_path = PROJECT_ROOT / data_settings["dataset_path"]
    data = pd.read_csv(dataset_path)
    exclusions = tuple(sorted(set(arguments.exclude_total_claims)))
    distribution = save_rq1_distribution(
        data,
        tables_directory,
        figures_directory,
        float(settings["reporting"]["confidence_level"]),
        exclusions,
    )
    training, heldout = load_saved_split(
        dataset_path,
        PROJECT_ROOT / data_settings["train_indices_path"],
        PROJECT_ROOT / data_settings["test_indices_path"],
        PROJECT_ROOT / data_settings["excluded_indices_path"],
        PROJECT_ROOT / data_settings["split_manifest_path"],
    )
    if exclusions:
        training = training.loc[~training["total_claims"].isin(exclusions)].reset_index(drop=True)
        heldout = heldout.loc[~heldout["total_claims"].isin(exclusions)].reset_index(drop=True)
    full_labelled = data.loc[data["label"].notna()].copy()
    full_labelled.insert(0, "row_index", full_labelled.index.astype(int))
    if exclusions:
        full_labelled = full_labelled.loc[
            ~full_labelled["total_claims"].isin(exclusions)
        ].reset_index(drop=True)
    lexicon_values = load_settings(settings["features"]["linguistic_lexicon_path"])
    certainty_terms = tuple(
        str(value).strip().lower() for value in lexicon_values["certainty_terms"]
    )
    hedge_terms = tuple(
        str(value).strip().lower() for value in lexicon_values["hedge_terms"]
    )
    validate_lexicons(certainty_terms, hedge_terms)
    save_named_feature_reports(
        full_labelled,
        training,
        certainty_terms,
        hedge_terms,
        association_directory,
        bootstrap_resamples=int(
            settings["reporting"]["association_bootstrap_resamples"]
        ),
        seed=int(settings["seed"]),
        confidence_level=float(settings["reporting"]["confidence_level"]),
    )
    save_error_cases(prediction_sets, data, tables_directory)
    save_interpretability_synthesis(
        root,
        heldout_summary,
        tables_directory,
        top_k=int(settings["interpretability"]["top_features_per_class"]),
    )

    summary = {
        "source_rows": len(data),
        "labelled_rows_in_rq1": int(distribution["count"].sum()),
        "training_rows_in_analysis": len(training),
        "heldout_rows_in_analysis": len(heldout),
        "source_columns": list(data.columns),
        "source_has_video_id": "video_id" in data.columns,
        "source_has_platform": "platform" in data.columns,
        "derived_linguistic_features": ["certainty_score", "hedge_score"],
        "experimental_condition_count": len(CONDITION_NAMES),
        "conditions": list(CONDITION_NAMES),
        "excluded_total_claims": list(exclusions),
    }
    (metrics_directory / "analysis_population.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    write_results_manifest(root, settings, exclusions)
    print(
        f"Generated complete RQ1--RQ3 outputs for {len(CONDITION_NAMES)} "
        f"experimental conditions in {root}."
    )


if __name__ == "__main__":
    main()
