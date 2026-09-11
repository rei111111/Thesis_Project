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
from evaluation.reproducibility import (
    scientific_code_manifest,
    validate_training_run_receipts,
)
from features.content_groups import content_group_ids
from evaluation.stratification import StratifiedGroupKFoldByColumns
from features.linguistic_features import validate_lexicons
from features.metadata_features import transformer_feature_names
from models.condition_registry import (
    BASELINE_NAMES,
    CONDITION_BY_NAME,
    CONDITION_NAMES,
    ablation_pairs,
)
from scripts.multiplatform_data import (
    is_multiplatform,
    load_multiplatform_saved_split,
    source_input_files,
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


def required_training_outputs(
    root: Path,
    settings: dict[str, Any],
) -> dict[str, list[Path]]:
    """List the trained evidence that each condition's receipt must cover."""
    requirements: dict[str, list[Path]] = {}
    for condition in expected_names(settings):
        paths = [
            root / "metrics" / f"{condition}_cv.csv",
            root / "metrics" / f"{condition}_heldout.json",
            root / "predictions" / f"{condition}_cv.csv",
            root / "predictions" / f"{condition}_heldout.csv",
        ]
        model_root = root / "models" / condition
        if condition != "E_FINETUNED_BERT":
            paths.extend(
                [
                    model_root / "estimator.joblib",
                    model_root / "selected_parameters.json",
                ]
            )
        if condition in CONDITION_BY_NAME and CONDITION_BY_NAME[condition].interpretable:
            interpretation = root / "interpretability"
            paths.extend(
                [
                    interpretation / f"{condition}_all_features.csv",
                    interpretation / f"{condition}_top_features.csv",
                    interpretation / f"{condition}_fold_features.csv",
                    interpretation / f"{condition}_feature_stability.csv",
                    interpretation / f"{condition}_summary.json",
                ]
            )
            if condition.endswith(("LOGISTIC_REGRESSION", "RIDGE")):
                paths.append(interpretation / f"{condition}_intercepts.csv")
            if condition.endswith("DECISION_TREE"):
                paths.extend(
                    [
                        interpretation / f"{condition}_rules.txt",
                        interpretation / f"{condition}_nodes.csv",
                        interpretation / f"{condition}_heldout_paths.csv",
                        interpretation / f"{condition}_tree.png",
                    ]
                )
            else:
                paths.append(
                    interpretation / f"{condition}_heldout_contributions.csv"
                )
        elif condition == "D_FROZEN_MINILM":
            interpretation = root / "interpretability"
            paths.extend(
                [
                    model_root / "checkpoint_metadata.json",
                    interpretation / f"{condition}_named_auxiliary_features.csv",
                    interpretation / f"{condition}_named_auxiliary_fold_features.csv",
                    interpretation / f"{condition}_named_auxiliary_stability.csv",
                    interpretation
                    / f"{condition}_heldout_named_auxiliary_contributions.csv",
                    interpretation / f"{condition}_summary.json",
                ]
            )
        elif condition == "E_FINETUNED_BERT":
            paths.extend(
                [
                    model_root / "model_state.pt",
                    model_root / "metadata_scaler.joblib",
                    model_root / "training_settings.joblib",
                    model_root / "training_settings.json",
                    model_root / "training_history.csv",
                    model_root / "checkpoint_metadata.json",
                    model_root / "tokenizer" / "tokenizer_config.json",
                    model_root / "encoder_config" / "config.json",
                ]
            )
            vocabulary = model_root / "tokenizer" / "tokenizer.json"
            if not vocabulary.is_file():
                vocabulary = model_root / "tokenizer" / "vocab.txt"
            paths.append(vocabulary)
            paths.extend(
                path for path in (model_root / "tokenizer").rglob("*") if path.is_file()
            )
            for fold in range(1, int(settings["evaluation"]["outer_folds"]) + 1):
                fold_root = model_root / "outer_folds" / f"fold_{fold}"
                paths.extend(
                    [
                        fold_root / "training_history.csv",
                        fold_root / "fold_training_record.json",
                    ]
                )
        requirements[condition] = paths
    return requirements


def training_input_files(
    settings: dict[str, Any],
    experiment_config: str,
    bert_config: str,
) -> dict[str, Path]:
    data_settings = settings["data"]
    result = {
        "experiment_config": PROJECT_ROOT / experiment_config,
        "bert_config": PROJECT_ROOT / bert_config,
        "linguistic_lexicons": PROJECT_ROOT
        / settings["features"]["linguistic_lexicon_path"],
        "train_indices": PROJECT_ROOT / data_settings["train_indices_path"],
        "test_indices": PROJECT_ROOT / data_settings["test_indices_path"],
        "excluded_indices": PROJECT_ROOT / data_settings["excluded_indices_path"],
        "split_manifest": PROJECT_ROOT / data_settings["split_manifest_path"],
    }
    if is_multiplatform(settings):
        result.update(source_input_files(PROJECT_ROOT, data_settings))
    else:
        result["dataset"] = PROJECT_ROOT / data_settings["dataset_path"]
    return result


def expected_names(settings: dict[str, Any]) -> tuple[str, ...]:
    include_baselines = bool(settings.get("reporting", {}).get("include_baselines", True))
    if not include_baselines:
        raise ValueError(
            "The thesis result contract requires both contextual baselines."
        )
    return CONDITION_NAMES + BASELINE_NAMES


def _assert_metric_payload_matches(
    observed: object,
    expected: object,
    context: str,
) -> None:
    """Compare persisted metric JSON with values recalculated from predictions."""
    if isinstance(expected, dict):
        if not isinstance(observed, dict) or set(observed) != set(expected):
            raise ValueError(f"{context} has missing or unexpected metric fields.")
        for key in expected:
            _assert_metric_payload_matches(
                observed[key], expected[key], f"{context}.{key}"
            )
        return
    if isinstance(expected, list):
        if not isinstance(observed, list) or len(observed) != len(expected):
            raise ValueError(f"{context} has a mismatched metric array.")
        for index, (observed_value, expected_value) in enumerate(
            zip(observed, expected, strict=True)
        ):
            _assert_metric_payload_matches(
                observed_value, expected_value, f"{context}[{index}]"
            )
        return
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if (
            isinstance(observed, bool)
            or not isinstance(observed, (int, float))
            or not np.isfinite(float(observed))
        ):
            raise ValueError(f"{context} is not a finite numeric metric.")
        if not np.isclose(
            float(observed), float(expected), rtol=1e-10, atol=1e-12
        ):
            raise ValueError(f"{context} does not match saved predictions.")
        return
    if observed != expected:
        raise ValueError(f"{context} does not match saved predictions.")


def load_prediction_files(
    root: Path,
    settings: dict[str, Any],
    expected_heldout: pd.DataFrame | None = None,
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
    validated: dict[str, pd.DataFrame] = {}
    recalculated_metrics: dict[str, dict[str, object]] = {}
    for condition, raw_frame in observed.items():
        frame = raw_frame.copy()
        if not required_columns.issubset(frame.columns):
            raise ValueError(f"{condition} is missing prediction columns.")
        for column in required_columns:
            numeric = pd.to_numeric(frame[column], errors="coerce")
            if (
                numeric.isna().any()
                or not np.isfinite(numeric.to_numpy(dtype=float)).all()
                or not np.equal(numeric, np.floor(numeric)).all()
            ):
                raise ValueError(f"{condition} has a non-integer {column} value.")
            frame[column] = numeric.astype(int)
        if frame["row_index"].duplicated().any():
            raise ValueError(f"{condition} contains duplicate row indices.")
        if expected_heldout is not None and "platform" in expected_heldout.columns:
            required_identity = {"record_id", "platform"}
            if not required_identity.issubset(frame.columns):
                raise ValueError(
                    f"{condition} is missing pooled identity columns: "
                    f"{sorted(required_identity - set(frame.columns))}."
                )
        if "condition" in frame.columns and not frame["condition"].eq(condition).all():
            raise ValueError(
                f"{condition} contains a mismatched internal condition name."
            )
        probability_columns = [
            f"probability_{label}" for label in (1, 2, 3, 4)
        ]
        present_probabilities = [
            column for column in probability_columns if column in frame.columns
        ]
        if present_probabilities:
            if present_probabilities != probability_columns:
                raise ValueError(
                    f"{condition} contains an incomplete probability vector."
                )
            probabilities = frame[probability_columns].apply(
                pd.to_numeric, errors="coerce"
            ).to_numpy(dtype=float)
            if (
                not np.isfinite(probabilities).all()
                or np.any(probabilities < 0)
                or np.any(probabilities > 1)
                or not np.allclose(
                    probabilities.sum(axis=1), 1.0, rtol=1e-6, atol=1e-6
                )
                or not np.array_equal(
                    probabilities.argmax(axis=1) + 1,
                    frame["prediction"].to_numpy(dtype=int),
                )
            ):
                raise ValueError(
                    f"{condition} contains invalid or prediction-inconsistent "
                    "class probabilities."
                )
        recalculated_metrics[condition] = calculate_metrics(
            frame["true_label"], frame["prediction"]
        )
        validated[condition] = frame

    if expected_heldout is not None:
        expected_truth = (
            expected_heldout[["row_index", "label"]]
            .rename(columns={"label": "true_label"})
            .astype({"row_index": int, "true_label": int})
            .sort_values("row_index")
            .set_index("row_index")["true_label"]
        )
    else:
        reference = validated[expected[0]]
        expected_truth = (
            reference.set_index("row_index")["true_label"].sort_index()
        )
    reference_rows = set(expected_truth.index)
    for condition, frame in validated.items():
        if set(frame["row_index"]) != reference_rows:
            raise ValueError("Held-out prediction files cover different videos.")
        truth = frame.set_index("row_index")["true_label"].sort_index()
        if not truth.equals(expected_truth):
            raise ValueError(
                "Held-out predictions do not match the frozen held-out rows "
                "and labels."
            )
        if expected_heldout is not None and "platform" in expected_heldout.columns:
            expected_identity = (
                expected_heldout[["row_index", "record_id", "platform"]]
                .astype({"row_index": int, "record_id": str, "platform": str})
                .sort_values("row_index")
                .reset_index(drop=True)
            )
            observed_identity = (
                frame[["row_index", "record_id", "platform"]]
                .astype({"row_index": int, "record_id": str, "platform": str})
                .sort_values("row_index")
                .reset_index(drop=True)
            )
            if not observed_identity.equals(expected_identity):
                raise ValueError(
                    f"{condition} pooled identities do not match the frozen split."
                )
    for condition in expected:
        metric_path = root / "metrics" / f"{condition}_heldout.json"
        if not metric_path.exists():
            raise FileNotFoundError(f"Missing held-out metrics: {metric_path}")
        try:
            stored_metrics = json.loads(metric_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Held-out metric JSON is invalid: {metric_path}") from exc
        _assert_metric_payload_matches(
            stored_metrics,
            recalculated_metrics[condition],
            f"{condition} held-out metrics",
        )
    return {name: validated[name].sort_values("row_index") for name in expected}


def load_cv_files(
    root: Path,
    settings: dict[str, Any],
    expected_training: pd.DataFrame | None = None,
) -> dict[str, pd.DataFrame]:
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
        fold_values = pd.to_numeric(frame["fold"], errors="coerce")
        if (
            fold_values.isna().any()
            or not np.isfinite(fold_values.to_numpy(dtype=float)).all()
            or not np.equal(fold_values, np.floor(fold_values)).all()
        ):
            raise ValueError(f"{condition} has a non-integer CV fold value.")
        frame["fold"] = fold_values.astype(int)
        if (
            len(frame) != expected_folds
            or set(frame["fold"]) != set(range(1, expected_folds + 1))
        ):
            raise ValueError(f"{condition} does not contain {expected_folds} folds.")
        if not np.isfinite(frame[list(METRIC_NAMES)].to_numpy(dtype=float)).all():
            raise ValueError(f"{condition} contains a non-finite CV metric.")
        prediction_path = root / "predictions" / f"{condition}_cv.csv"
        if not prediction_path.exists():
            raise FileNotFoundError(f"Missing outer-CV predictions: {prediction_path}")
        predictions = pd.read_csv(prediction_path)
        prediction_columns = {"row_index", "fold", "true_label", "prediction"}
        if not prediction_columns.issubset(predictions.columns):
            raise ValueError(f"{prediction_path} is missing CV prediction columns.")
        for column in prediction_columns:
            numeric = pd.to_numeric(predictions[column], errors="coerce")
            if (
                numeric.isna().any()
                or not np.isfinite(numeric.to_numpy(dtype=float)).all()
                or not np.equal(numeric, np.floor(numeric)).all()
            ):
                raise ValueError(f"{condition} has a non-integer CV {column} value.")
            predictions[column] = numeric.astype(int)
        if predictions["row_index"].duplicated().any():
            raise ValueError(f"{condition} repeats rows across outer folds.")
        if expected_training is not None and "platform" in expected_training.columns:
            required_identity = {"record_id", "platform"}
            if not required_identity.issubset(predictions.columns):
                raise ValueError(
                    f"{condition} CV predictions omit pooled identity columns."
                )
            expected_identity = (
                expected_training[["row_index", "record_id", "platform"]]
                .astype({"row_index": int, "record_id": str, "platform": str})
                .sort_values("row_index")
                .reset_index(drop=True)
            )
            observed_identity = (
                predictions[["row_index", "record_id", "platform"]]
                .astype({"row_index": int, "record_id": str, "platform": str})
                .sort_values("row_index")
                .reset_index(drop=True)
            )
            if not observed_identity.equals(expected_identity):
                raise ValueError(
                    f"{condition} CV identities do not match the frozen "
                    "pooled training rows."
                )
        if not set(predictions["fold"]).issubset(range(1, expected_folds + 1)):
            raise ValueError(f"{condition} contains an invalid outer-fold number.")
        calculate_metrics(predictions["true_label"], predictions["prediction"])

        for fold in range(1, expected_folds + 1):
            fold_predictions = predictions.loc[predictions["fold"].eq(fold)]
            if fold_predictions.empty:
                raise ValueError(f"{condition} has no predictions for fold {fold}.")
            recalculated = calculate_metrics(
                fold_predictions["true_label"],
                fold_predictions["prediction"],
            )
            metric_row = frame.loc[frame["fold"].eq(fold)].iloc[0]
            for metric in METRIC_NAMES:
                if not np.isclose(
                    float(metric_row[metric]),
                    float(recalculated[metric]),
                    rtol=1e-10,
                    atol=1e-12,
                ):
                    raise ValueError(
                        f"{condition} fold {fold} stored {metric} does not "
                        "match its saved predictions."
                    )
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
    if expected_training is not None:
        if reference_assignment is None:
            raise ValueError("No outer-fold assignments were loaded.")
        expected_assignment = (
            expected_training[["row_index", "label"]]
            .rename(columns={"label": "true_label"})
            .astype({"row_index": int, "true_label": int})
            .sort_values("row_index")
            .reset_index(drop=True)
        )
        observed_truth = reference_assignment[["row_index", "true_label"]]
        if not observed_truth.equals(expected_assignment):
            raise ValueError(
                "Outer-CV predictions do not match the frozen training rows "
                "and labels."
            )
        group_frame = expected_training[["row_index"]].copy()
        group_frame["content_group"] = content_group_ids(expected_training)
        group_assignments = reference_assignment[["row_index", "fold"]].merge(
            group_frame,
            on="row_index",
            validate="one_to_one",
        )
        groups_split_across_folds = (
            group_assignments.groupby("content_group")["fold"].nunique().gt(1)
        )
        if groups_split_across_folds.any():
            raise ValueError(
                "Outer-CV assignments split exact or near-duplicate transcript "
                "content across folds."
            )
        if "seed" in settings:
            ordered = expected_training.reset_index(drop=True)
            splitter = StratifiedGroupKFoldByColumns(
                n_splits=expected_folds, random_state=int(settings["seed"]),
                stratification_columns=tuple(
                    settings.get("split", {}).get("stratification_columns", ())
                ),
            )
            fold_numbers = np.zeros(len(ordered), dtype=int)
            for fold, (_, validation) in enumerate(
                splitter.split(ordered, ordered["label"], content_group_ids(ordered)), 1
            ):
                fold_numbers[validation] = fold
            expected_fold_rows = ordered[["row_index"]].assign(fold=fold_numbers)
            expected_fold_rows = expected_fold_rows.sort_values("row_index").reset_index(drop=True)
            if not reference_assignment[["row_index", "fold"]].equals(expected_fold_rows):
                raise ValueError("Outer-CV assignments do not replay the configured splitter.")
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
    figure_directory: Path | None,
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
        if figure_directory is not None:
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


def save_rq1_platform_distribution(
    data: pd.DataFrame,
    tables_directory: Path,
    confidence_level: float,
    excluded_total_claims: tuple[int, ...],
) -> pd.DataFrame:
    """Save descriptive label distributions separately for each platform."""
    if "platform" not in data.columns:
        raise ValueError("Platform-specific RQ1 output requires a platform column.")
    labelled = data.loc[data["label"].notna()].copy()
    if excluded_total_claims:
        labelled = labelled.loc[
            ~labelled["total_claims"].isin(excluded_total_claims)
        ]
    rows: list[pd.DataFrame] = []
    for platform, selected in labelled.groupby("platform", sort=True):
        distribution = pd.DataFrame(
            class_distribution_table(selected["label"], confidence_level)
        )
        distribution.insert(0, "platform", str(platform))
        distribution.insert(2, "category", distribution["label"].map(LABEL_NAMES))
        rows.append(distribution)
    result = pd.concat(rows, ignore_index=True)
    result.to_csv(
        tables_directory / "rq1_class_distribution_by_platform.csv",
        index=False,
    )
    return result


def save_error_cases(
    prediction_sets: dict[str, pd.DataFrame],
    data: pd.DataFrame,
    tables_directory: Path,
) -> pd.DataFrame:
    source = data.reset_index(drop=True).copy()
    if "row_index" not in source.columns:
        source.insert(0, "row_index", np.arange(len(source), dtype=int))
    rows: list[pd.DataFrame] = []
    for condition, predictions in prediction_sets.items():
        source_columns = [
            column
            for column in (
                "row_index",
                "record_id",
                "platform",
                "title",
                "transcript",
                "total_claims",
                "false_claims",
            )
            if column in source.columns
        ]
        merged = predictions[["row_index", "true_label", "prediction"]].merge(
            source[source_columns],
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
    engagement_transform: str = "log1p",
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
    prohibited = {
        "row_index",
        "record_id",
        "source_row",
        "platform",
        "total_claims",
        "false_claims",
        "label",
    }
    nontext_features = all_features.loc[
        all_features["feature_group"].ne("textual"), "feature"
    ].astype(str)
    leaked = sorted(set(nontext_features) & prohibited)
    if leaked:
        raise ValueError(f"Interpretability exports reveal prohibited predictors: {leaked}")
    all_features.to_csv(tables_directory / "all_interpretable_model_features.csv", index=False)
    all_stability.to_csv(tables_directory / "all_feature_stability.csv", index=False)

    c_features = all_features.loc[all_features["condition"].str.startswith("C_")]
    expected_named = set(
        transformer_feature_names(engagement_transform)
    )
    named = c_features.loc[
        c_features["feature_group"].isin(
            ["handcrafted_linguistic", "engagement_or_format"]
        )
        & c_features["feature"].isin(expected_named)
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
        & c_features["absolute_weight"].gt(0)
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


def platform_heldout_tables(
    prediction_sets: dict[str, pd.DataFrame],
    heldout: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Calculate platform-specific and equally weighted platform summaries."""
    identity = heldout[["row_index", "platform"]].copy()
    rows: list[dict[str, object]] = []
    for condition, predictions in prediction_sets.items():
        aligned = predictions[["row_index", "true_label", "prediction"]].merge(
            identity,
            on="row_index",
            validate="one_to_one",
        )
        for platform, selected in aligned.groupby("platform", sort=True):
            metrics = calculate_metrics(
                selected["true_label"], selected["prediction"]
            )
            rows.append(
                {
                    "condition": condition,
                    "platform": str(platform),
                    "rows": len(selected),
                    **{name: metrics[name] for name in METRIC_NAMES},
                }
            )
    by_platform = pd.DataFrame(rows)
    macro = (
        by_platform.groupby("condition", as_index=False)[list(METRIC_NAMES)]
        .mean()
        .rename(columns={name: f"platform_macro_{name}" for name in METRIC_NAMES})
    )
    return by_platform, macro


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
    experiment_config: str,
    bert_config: str,
    training_receipts: list[Path],
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
        "reported_condition_count": len(CONDITION_NAMES) + len(BASELINE_NAMES),
        "random_seed": int(settings["seed"]),
        "data_mode": settings["data"].get("mode", "youtube_only"),
        "text_columns": list(
            settings["features"].get(
                "text_columns", ("title", "transcript")
            )
        ),
        "engagement_transform": settings["features"].get(
            "engagement_transform", "log1p"
        ),
        "stratification_columns": list(
            settings["split"].get("stratification_columns", ())
        ),
        "platform_reporting": bool(
            settings.get("reporting", {}).get("report_by_platform", False)
        ),
        "expected_outer_folds": int(settings["evaluation"]["outer_folds"]),
        "expected_inner_folds": int(settings["evaluation"]["inner_folds"]),
        "primary_metric": str(settings["evaluation"]["primary_metric"]),
        "bootstrap_resamples": int(settings["evaluation"]["bootstrap_resamples"]),
        "bootstrap_unit": "content_group" if is_multiplatform(settings) else "label_stratified_row",
        "association_bootstrap_resamples": int(
            settings["reporting"]["association_bootstrap_resamples"]
        ),
        "confidence_level": float(settings["reporting"]["confidence_level"]),
        "excluded_total_claims": list(excluded_total_claims),
        "scientific_code_sha256": scientific_code_manifest(PROJECT_ROOT)["sha256"],
        "source_inputs": {
            name: {
                "path": str(path.relative_to(PROJECT_ROOT)),
                "sha256": sha256(path),
            }
            for name, path in training_input_files(
                settings, experiment_config, bert_config
            ).items()
        },
        "training_run_receipts": [
            {
                "path": str(path.relative_to(PROJECT_ROOT)),
                "sha256": sha256(path),
            }
            for path in training_receipts
        ],
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
    parser.add_argument("--bert-config", default="configs/bert.yaml")
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--exclude-total-claims", nargs="*", type=int, default=[])
    parser.add_argument("--bootstrap-resamples", type=int, default=None)
    parser.add_argument("--association-bootstrap-resamples", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    settings = load_settings(arguments.config)
    bert_settings = load_settings(arguments.bert_config)
    arguments.run_name = arguments.run_name or str(
        settings.get("reporting", {}).get("default_run_name", "primary")
    )
    exclusions = tuple(sorted(set(arguments.exclude_total_claims)))
    sensitivity_name = str(settings["sensitivity"]["run_name"])
    configured_sensitivity_exclusions = tuple(
        sorted(set(int(value) for value in settings["sensitivity"]["exclude_total_claims"]))
    )
    primary_run_name = str(
        settings.get("reporting", {}).get("default_run_name", "primary")
    )
    if arguments.run_name == primary_run_name and exclusions:
        raise ValueError("The primary analysis cannot exclude labelled rows.")
    if (
        arguments.run_name == sensitivity_name
        and exclusions != configured_sensitivity_exclusions
    ):
        raise ValueError(
            "The named sensitivity run must use the exclusions in experiment.yaml."
        )
    certified_run = arguments.run_name in {primary_run_name, sensitivity_name}
    if certified_run and (
        arguments.bootstrap_resamples is not None
        or arguments.association_bootstrap_resamples is not None
    ):
        raise ValueError(
            "Certified primary/sensitivity runs must use the configured resample counts."
        )
    if arguments.bootstrap_resamples is not None:
        settings["evaluation"]["bootstrap_resamples"] = arguments.bootstrap_resamples
    if arguments.association_bootstrap_resamples is not None:
        settings["reporting"][
            "association_bootstrap_resamples"
        ] = arguments.association_bootstrap_resamples
    data_settings = settings["data"]
    if is_multiplatform(settings):
        training, heldout, data = load_multiplatform_saved_split(
            PROJECT_ROOT, settings
        )
    else:
        dataset_path = PROJECT_ROOT / data_settings["dataset_path"]
        data = pd.read_csv(dataset_path)
        training, heldout = load_saved_split(
            dataset_path,
            PROJECT_ROOT / data_settings["train_indices_path"],
            PROJECT_ROOT / data_settings["test_indices_path"],
            PROJECT_ROOT / data_settings["excluded_indices_path"],
            PROJECT_ROOT / data_settings["split_manifest_path"],
            split_settings=settings["split"],
            data_contract=data_settings,
        )
    if exclusions:
        training = training.loc[
            ~training["total_claims"].isin(exclusions)
        ].reset_index(drop=True)
        heldout = heldout.loc[
            ~heldout["total_claims"].isin(exclusions)
        ].reset_index(drop=True)

    root = run_root(arguments.run_name)
    training_receipts = validate_training_run_receipts(
        PROJECT_ROOT,
        root,
        expected_names(settings),
        training_input_files(settings, arguments.config, arguments.bert_config),
        exclusions={"total_claims": list(exclusions)},
        required_outputs=required_training_outputs(root, settings),
        checkpoint_names={
            "frozen_sentence_transformer": settings["minilm"]["model_name"],
            "fine_tuned_transformer": bert_settings["model_name"],
        },
    )
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

    prediction_sets = load_prediction_files(root, settings, heldout)
    cv_results = load_cv_files(root, settings, training)
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
    platform_summary: pd.DataFrame | None = None
    if is_multiplatform(settings):
        platform_summary, platform_macro = platform_heldout_tables(
            prediction_sets, heldout
        )
        platform_summary.to_csv(
            tables_directory / "heldout_summary_by_platform.csv", index=False
        )
        platform_macro.to_csv(
            tables_directory / "heldout_platform_macro_summary.csv", index=False
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
        groups=(
            content_group_ids(heldout.sort_values("row_index"))
            if is_multiplatform(settings) else None
        ),
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

    distribution = save_rq1_distribution(
        data,
        tables_directory,
        figures_directory,
        float(settings["reporting"]["confidence_level"]),
        exclusions,
    )
    if is_multiplatform(settings):
        save_rq1_platform_distribution(
            data,
            tables_directory,
            float(settings["reporting"]["confidence_level"]),
            exclusions,
        )
    full_labelled = data.loc[data["label"].notna()].copy()
    if "row_index" not in full_labelled.columns:
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
        text_columns=tuple(
            settings["features"].get("text_columns", ("title", "transcript"))
        ),
        engagement_transform=str(
            settings["features"].get("engagement_transform", "log1p")
        ),
        platform_column=str(
            settings["features"].get("platform_column", "platform")
        ),
    )
    save_error_cases(prediction_sets, data, tables_directory)
    save_interpretability_synthesis(
        root,
        heldout_summary,
        tables_directory,
        top_k=int(settings["interpretability"]["top_features_per_class"]),
        engagement_transform=str(
            settings["features"].get("engagement_transform", "log1p")
        ),
    )

    summary = {
        "data_mode": data_settings.get("mode", "youtube_only"),
        "source_rows": len(data),
        "labelled_rows_in_rq1": int(distribution["count"].sum()),
        "training_rows_in_analysis": len(training),
        "heldout_rows_in_analysis": len(heldout),
        "source_columns": list(data.columns),
        "source_has_video_id": "video_id" in data.columns,
        "source_has_platform": "platform" in data.columns,
        "text_columns_used_by_models": list(
            settings["features"].get(
                "text_columns", ("title", "transcript")
            )
        ),
        "engagement_transform": settings["features"].get(
            "engagement_transform", "log1p"
        ),
        "platform_distribution": (
            {
                str(key): int(value)
                for key, value in data["platform"]
                .value_counts()
                .sort_index()
                .items()
            }
            if "platform" in data.columns
            else None
        ),
        "platform_heldout_metrics_reported": platform_summary is not None,
        "derived_linguistic_features": ["certainty_score", "hedge_score"],
        "experimental_condition_count": len(CONDITION_NAMES),
        "conditions": list(CONDITION_NAMES),
        "excluded_total_claims": list(exclusions),
    }
    (metrics_directory / "analysis_population.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    write_results_manifest(
        root,
        settings,
        exclusions,
        arguments.config,
        arguments.bert_config,
        training_receipts,
    )
    print(
        f"Generated complete RQ1--RQ3 outputs for {len(CONDITION_NAMES)} "
        f"experimental conditions in {root}."
    )


if __name__ == "__main__":
    main()
