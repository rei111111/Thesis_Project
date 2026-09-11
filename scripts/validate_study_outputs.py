"""Fail unless every non-LaTeX artifact required by the study is complete."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from evaluation.final_evaluation import load_saved_split
from evaluation.report_validation import verify_report_tables
from evaluation.reproducibility import (
    scientific_code_manifest,
    validate_training_run_receipts,
)
from features.metadata_features import transformer_feature_names
from models.condition_registry import BASELINE_NAMES, CONDITION_NAMES
from scripts.generate_results import (
    load_cv_files,
    load_prediction_files,
    platform_heldout_tables,
    required_training_outputs,
    run_root,
    training_input_files,
)
from scripts.multiplatform_data import (
    is_multiplatform,
    load_multiplatform_data,
    load_multiplatform_saved_split,
    validate_multiplatform_experiment,
)
from scripts.prepare_data import CSV_COLUMNS


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Required study artifact is missing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _verify_checkpoint_metadata(
    root: Path,
    settings: dict[str, Any],
    bert_settings: dict[str, Any],
) -> None:
    expected_auxiliary_names = list(
        transformer_feature_names(
            str(settings["features"].get("engagement_transform", "log1p"))
        )
    )
    minilm_root = root / "models" / "D_FROZEN_MINILM"
    minilm = load_json(minilm_root / "checkpoint_metadata.json")
    expected_embedding = int(settings["minilm"]["expected_embedding_dimension"])
    expected_max_length = int(settings["minilm"]["expected_max_sequence_length"])
    fold_revisions = minilm.get("outer_fold_model_commit_hashes", [])
    fold_dimensions = minilm.get("outer_fold_embedding_dimensions", [])
    fold_max_lengths = minilm.get("outer_fold_max_sequence_lengths", [])
    expected_fold_count = int(settings["evaluation"]["outer_folds"])
    minilm_revisions = [*fold_revisions, minilm.get("model_commit_hash")]
    if (
        minilm.get("model_name") != settings["minilm"]["model_name"]
        or minilm.get("requested_revision") != settings["minilm"].get("revision")
        or int(minilm.get("embedding_dimension", -1)) != expected_embedding
        or int(minilm.get("expected_embedding_dimension", -1)) != expected_embedding
        or int(minilm.get("max_sequence_length", -1)) != expected_max_length
        or int(minilm.get("expected_max_sequence_length", -1))
        != expected_max_length
        or minilm.get("named_auxiliary_features") != expected_auxiliary_names
        or len(fold_revisions) != expected_fold_count
        or fold_dimensions != [expected_embedding] * expected_fold_count
        or fold_max_lengths != [expected_max_length] * expected_fold_count
        or any(not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{40}", value) is None for value in minilm_revisions)
        or len(set(minilm_revisions)) != 1
    ):
        raise ValueError("MiniLM checkpoint metadata is incomplete or inconsistent.")

    bert_root = root / "models" / "E_FINETUNED_BERT"
    tokenizer_root = bert_root / "tokenizer"
    if (tokenizer_root / "tokenizer.json").is_file():
        tokenizer_state = load_json(tokenizer_root / "tokenizer.json")
        if not tokenizer_state.get("model", {}).get("vocab"):
            raise ValueError("Saved BERT tokenizer vocabulary is empty.")
    elif not (tokenizer_root / "vocab.txt").is_file() or not (
        tokenizer_root / "vocab.txt"
    ).read_text(encoding="utf-8").strip():
        raise ValueError("Saved BERT tokenizer vocabulary is missing.")
    final = load_json(bert_root / "checkpoint_metadata.json")
    final_training_settings = load_json(bert_root / "training_settings.json")
    expected_final_settings = dict(bert_settings)
    expected_final_settings["seed"] = int(settings["seed"])
    expected_final_settings["text_columns"] = list(
        settings["features"].get("text_columns", ("title", "transcript"))
    )
    expected_final_settings["engagement_transform"] = str(
        settings["features"].get("engagement_transform", "log1p")
    )
    expected_final_settings["platform_column"] = str(
        settings["features"].get("platform_column", "platform")
    )
    expected_final_settings["stratification_columns"] = list(
        settings["split"].get("stratification_columns", ())
    )
    with (
        PROJECT_ROOT / settings["features"]["linguistic_lexicon_path"]
    ).open("r", encoding="utf-8") as file:
        lexicon_values = yaml.safe_load(file)
    expected_final_settings["linguistic_lexicons"] = {
        "certainty_terms": [
            str(value).strip().lower()
            for value in lexicon_values["certainty_terms"]
        ],
        "hedge_terms": [
            str(value).strip().lower() for value in lexicon_values["hedge_terms"]
        ],
    }
    mismatched_settings = {
        key: {
            "expected": value,
            "observed": final_training_settings.get(key),
        }
        for key, value in expected_final_settings.items()
        if final_training_settings.get(key) != value
    }
    if mismatched_settings:
        raise ValueError(
            "Final BERT training settings differ from configs/bert.yaml: "
            f"{mismatched_settings}."
        )
    if (
        final.get("model_name") != bert_settings["model_name"]
        or final.get("requested_revision") != bert_settings.get("revision")
        or final_training_settings.get("resolved_revision") != final.get("encoder_commit_hash")
        or not final.get("checkpoint_identity_resolved")
        or int(final.get("hidden_size", -1))
        != int(bert_settings["expected_hidden_size"])
        or int(final.get("metadata_dimension", -1)) != 6
        or int(final.get("classifier_input_dimension", -1))
        != int(bert_settings["expected_hidden_size"]) + 6
        or int(final.get("num_labels", -1)) != 4
        or int(final.get("maximum_sequence_length", -1))
        != int(bert_settings["max_length"])
        or final.get("auxiliary_feature_names") != expected_auxiliary_names
    ):
        raise ValueError("Final BERT checkpoint metadata violates the thesis contract.")
    fold_records = [
        load_json(
            bert_root
            / "outer_folds"
            / f"fold_{fold}"
            / "fold_training_record.json"
        )
        for fold in range(1, int(settings["evaluation"]["outer_folds"]) + 1)
    ]
    revisions = [
        final.get("encoder_commit_hash"),
        final.get("tokenizer_commit_hash"),
    ]
    best_epochs: list[int] = []
    for fold, record in enumerate(fold_records, start=1):
        fold_settings = record.get("settings", {})
        expected_fold_settings = dict(expected_final_settings)
        expected_fold_settings["seed"] = int(settings["seed"]) + fold
        if (
            int(record.get("fold", -1)) != fold
            or fold_settings.get("resolved_revision") != final.get("encoder_commit_hash")
            or int(record.get("hidden_size", -1))
            != int(bert_settings["expected_hidden_size"])
            or int(record.get("metadata_dimension", -1)) != 6
            or int(record.get("num_labels", -1)) != 4
            or any(
                fold_settings.get(key) != value
                for key, value in expected_fold_settings.items()
            )
            or int(record.get("outer_training_rows", 0))
            != int(record.get("fitting_rows", -1))
            + int(record.get("early_stopping_rows", -1))
            or min(
                int(record.get("fitting_rows", 0)),
                int(record.get("early_stopping_rows", 0)),
                int(record.get("outer_validation_rows", 0)),
            )
            < 1
        ):
            raise ValueError(f"BERT outer-fold record {fold} is inconsistent.")
        best_epoch = int(record.get("best_epoch", 0))
        if not 1 <= best_epoch <= int(bert_settings["max_epochs"]):
            raise ValueError(f"BERT outer-fold record {fold} has an invalid epoch.")
        history = pd.read_csv(
            bert_root
            / "outer_folds"
            / f"fold_{fold}"
            / "training_history.csv"
        )
        required_history = {
            "epoch",
            "training_loss",
            "validation_loss",
            "validation_qwk",
        }
        numeric_history = (
            history[list(required_history)].apply(pd.to_numeric, errors="coerce")
            if required_history.issubset(history.columns)
            else pd.DataFrame()
        )
        if (
            history.empty
            or not required_history.issubset(history.columns)
            or numeric_history.empty
            or not pd.notna(numeric_history).all().all()
            or not pd.DataFrame(
                np.isfinite(numeric_history.to_numpy(dtype=float))
            ).all().all()
            or not np.equal(
                numeric_history["epoch"], np.floor(numeric_history["epoch"])
            ).all()
            or numeric_history["epoch"].astype(int).tolist()
            != list(range(1, len(numeric_history) + 1))
            or int(
                numeric_history.loc[
                    numeric_history["validation_qwk"].idxmax(), "epoch"
                ]
            )
            != best_epoch
        ):
            raise ValueError(
                f"BERT outer-fold history {fold} does not support its best epoch."
            )
        best_epochs.append(best_epoch)
        revisions.extend(
            [record.get("encoder_commit_hash"), record.get("tokenizer_commit_hash")]
        )
    if any(not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{40}", value) is None for value in revisions) or len(set(revisions)) != 1:
        raise ValueError("BERT checkpoint revisions are missing or inconsistent.")
    if int(final.get("best_epoch", 0)) != int(pd.Series(best_epochs).median()):
        raise ValueError("Final BERT epoch is not the median outer-fold best epoch.")
    final_history = pd.read_csv(bert_root / "training_history.csv")
    final_epochs = pd.to_numeric(final_history.get("epoch"), errors="coerce")
    final_losses = pd.to_numeric(
        final_history.get("training_loss"), errors="coerce"
    )
    if (
        final_history.empty
        or not {"epoch", "training_loss"}.issubset(final_history.columns)
        or final_epochs is None
        or final_losses is None
        or not np.isfinite(final_epochs.to_numpy(dtype=float)).all()
        or not np.equal(final_epochs, np.floor(final_epochs)).all()
        or not np.isfinite(final_losses.to_numpy(dtype=float)).all()
        or len(final_history) != int(final["best_epoch"])
        or final_epochs.astype(int).tolist()
        != list(range(1, int(final["best_epoch"]) + 1))
    ):
        raise ValueError("Final BERT history does not match its fixed epoch count.")


def verify_artifact_manifest(
    root: Path,
    settings: dict[str, Any],
    bert_settings: dict[str, Any],
    experiment_config: str,
    bert_config: str,
    excluded_total_claims: tuple[int, ...],
) -> dict[str, Any]:
    manifest = load_json(root / "results_manifest.json")
    if manifest.get("condition_count") != 14:
        raise ValueError(f"{root} does not contain fourteen conditions.")
    if tuple(manifest.get("complete_experimental_conditions", [])) != CONDITION_NAMES:
        raise ValueError(f"{root} condition registry is incomplete or reordered.")
    if tuple(manifest.get("contextual_baselines", [])) != BASELINE_NAMES:
        raise ValueError(f"{root} baseline registry is incomplete or reordered.")
    expected_protocol = {
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
    }
    observed_protocol = {key: manifest.get(key) for key in expected_protocol}
    if observed_protocol != expected_protocol:
        raise ValueError(
            f"{root} was not generated under the active thesis protocol."
        )
    artifacts = manifest.get("artifacts", [])
    if not artifacts:
        raise ValueError(f"{root} has an empty artifact manifest.")
    artifact_path_list = [str(artifact["path"]) for artifact in artifacts]
    if len(artifact_path_list) != len(set(artifact_path_list)):
        raise ValueError(f"{root} contains duplicate artifact-manifest paths.")
    artifact_paths = set(artifact_path_list)
    required_paths = {
        "metrics/heldout_full_metrics.json",
        "metrics/analysis_population.json",
        "tables/heldout_summary.csv",
        "tables/cv_summary.csv",
        "tables/rq1_class_distribution.csv",
        "tables/heldout_per_class_metrics.csv",
        "tables/heldout_ordinal_error_summary.csv",
        "tables/cv_paired_differences.csv",
        "tables/rq2_cv_ablation_differences.csv",
        "tables/heldout_bootstrap_metric_intervals.csv",
        "tables/heldout_bootstrap_pairwise_differences.csv",
        "tables/rq2_heldout_ablation_bootstrap.csv",
        "tables/heldout_prediction_cases.csv",
        "tables/heldout_error_cases_only.csv",
        "tables/all_interpretable_model_features.csv",
        "tables/all_feature_stability.csv",
        "tables/rq2_minilm_named_auxiliary_weights.csv",
        "tables/rq2_minilm_named_auxiliary_stability.csv",
        "tables/rq2_named_feature_model_weights.csv",
        "tables/rq2_textual_feature_consensus.csv",
        "tables/rq2_decision_tree_top_features.csv",
        "tables/rq3_performance_interpretability_tradeoff.csv",
        "feature_associations/named_features_full_labelled.csv",
        "feature_associations/named_features_training_only.csv",
        "feature_associations/named_feature_class_descriptives.csv",
        "feature_associations/named_feature_associations.csv",
        "figures/rq1_class_distribution.png",
    }
    if is_multiplatform(settings):
        required_paths.update(
            {
                "tables/rq1_class_distribution_by_platform.csv",
                "tables/heldout_summary_by_platform.csv",
                "tables/heldout_platform_macro_summary.csv",
            }
        )
    training_requirements = required_training_outputs(root, settings)
    for paths in training_requirements.values():
        required_paths.update(str(path.relative_to(root)) for path in paths)
    for condition in (*CONDITION_NAMES, *BASELINE_NAMES):
        required_paths.update(
            {
                f"figures/{condition}_confusion.csv",
                f"figures/{condition}_confusion.png",
            }
        )
    missing_required = sorted(required_paths - artifact_paths)
    if missing_required:
        raise FileNotFoundError(
            f"{root} is missing required study artifacts: {missing_required}"
        )
    if not any(path.startswith("reproducibility/run_") for path in artifact_paths):
        raise FileNotFoundError(f"{root} has no recorded training run manifest.")

    for artifact in artifacts:
        path = root / artifact["path"]
        if path.resolve() != root.resolve() and root.resolve() not in path.resolve().parents:
            raise ValueError(f"Manifest path escapes the result root: {path}")
        if not path.exists():
            raise FileNotFoundError(f"Manifest artifact is missing: {path}")
        if path.stat().st_size != artifact["bytes"]:
            raise ValueError(f"Manifest byte size changed for {path}.")
        if file_sha256(path) != artifact["sha256"]:
            raise ValueError(f"Manifest checksum changed for {path}.")

    tracked_directories = (
        "metrics",
        "predictions",
        "models",
        "interpretability",
        "feature_associations",
        "tables",
        "figures",
        "reproducibility",
    )
    actual_paths = {
        str(path.relative_to(root))
        for directory in tracked_directories
        for path in (root / directory).rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    }
    if actual_paths != artifact_paths:
        raise ValueError(
            f"{root} contains unmanifested or phantom study artifacts."
        )

    inputs = training_input_files(settings, experiment_config, bert_config)
    expected_source_inputs = {
        name: {
            "path": str(path.relative_to(PROJECT_ROOT)),
            "sha256": file_sha256(path),
        }
        for name, path in inputs.items()
    }
    if manifest.get("source_inputs") != expected_source_inputs:
        raise ValueError(f"{root} source-input hashes are stale.")
    checkpoint_names = {
        "frozen_sentence_transformer": settings["minilm"]["model_name"],
        "fine_tuned_transformer": bert_settings["model_name"],
    }
    receipts = validate_training_run_receipts(
        PROJECT_ROOT,
        root,
        (*CONDITION_NAMES, *BASELINE_NAMES),
        inputs,
        exclusions={"total_claims": list(excluded_total_claims)},
        required_outputs=training_requirements,
        checkpoint_names=checkpoint_names,
    )
    expected_receipts = [
        {"path": str(path.relative_to(PROJECT_ROOT)), "sha256": file_sha256(path)}
        for path in receipts
    ]
    if manifest.get("training_run_receipts") != expected_receipts:
        raise ValueError(f"{root} training-receipt references are stale.")
    _verify_checkpoint_metadata(root, settings, bert_settings)
    return manifest


def verify_semantic_results(
    root: Path,
    settings: dict[str, Any],
    excluded_total_claims: tuple[int, ...],
) -> None:
    """Re-run alignment and metric checks against the active frozen split."""
    data_settings = settings["data"]
    if is_multiplatform(settings):
        training, heldout, data = load_multiplatform_saved_split(
            PROJECT_ROOT, settings
        )
    else:
        data = pd.read_csv(PROJECT_ROOT / data_settings["dataset_path"])
        training, heldout = load_saved_split(
            PROJECT_ROOT / data_settings["dataset_path"],
            PROJECT_ROOT / data_settings["train_indices_path"],
            PROJECT_ROOT / data_settings["test_indices_path"],
            PROJECT_ROOT / data_settings["excluded_indices_path"],
            PROJECT_ROOT / data_settings["split_manifest_path"],
            split_settings=settings["split"],
            data_contract=data_settings,
        )
    if excluded_total_claims:
        training = training.loc[
            ~training["total_claims"].isin(excluded_total_claims)
        ].reset_index(drop=True)
        heldout = heldout.loc[
            ~heldout["total_claims"].isin(excluded_total_claims)
        ].reset_index(drop=True)
    prediction_sets = load_prediction_files(root, settings, heldout)
    cv_results = load_cv_files(root, settings, training)
    population = load_json(root / "metrics" / "analysis_population.json")
    expected_population = {
        "data_mode": data_settings.get("mode", "youtube_only"),
        "source_rows": len(data),
        "labelled_rows_in_rq1": len(training) + len(heldout),
        "training_rows_in_analysis": len(training),
        "heldout_rows_in_analysis": len(heldout),
        "experimental_condition_count": len(CONDITION_NAMES),
        "excluded_total_claims": list(excluded_total_claims),
        "text_columns_used_by_models": list(
            settings["features"].get(
                "text_columns", ("title", "transcript")
            )
        ),
        "engagement_transform": settings["features"].get(
            "engagement_transform", "log1p"
        ),
    }
    if any(population.get(key) != value for key, value in expected_population.items()):
        raise ValueError(f"{root} analysis-population record is inconsistent.")
    expected_conditions = set((*CONDITION_NAMES, *BASELINE_NAMES))
    if set(prediction_sets) != expected_conditions:
        raise ValueError(f"{root} does not contain the complete prediction set.")
    if is_multiplatform(settings):
        expected_by_platform, expected_platform_macro = platform_heldout_tables(
            prediction_sets, heldout
        )
        observed_by_platform = pd.read_csv(
            root / "tables" / "heldout_summary_by_platform.csv"
        )
        observed_platform_macro = pd.read_csv(
            root / "tables" / "heldout_platform_macro_summary.csv"
        )
        pd.testing.assert_frame_equal(
            observed_by_platform,
            expected_by_platform,
            check_dtype=False,
            rtol=1e-10,
            atol=1e-12,
        )
        pd.testing.assert_frame_equal(
            observed_platform_macro,
            expected_platform_macro,
            check_dtype=False,
            rtol=1e-10,
            atol=1e-12,
        )
        rq1_by_platform = pd.read_csv(
            root / "tables" / "rq1_class_distribution_by_platform.csv"
        )
        expected_counts = data.loc[data["label"].notna()].copy()
        if excluded_total_claims:
            expected_counts = expected_counts.loc[
                ~expected_counts["total_claims"].isin(excluded_total_claims)
            ]
        observed_counts = (
            rq1_by_platform.groupby("platform")["count"].sum().sort_index()
        )
        true_counts = expected_counts["platform"].value_counts().sort_index()
        if not observed_counts.equals(true_counts):
            raise ValueError("Platform-specific RQ1 counts are inconsistent.")
    verify_report_tables(
        PROJECT_ROOT, root, settings, data, training, heldout,
        prediction_sets, cv_results, excluded_total_claims,
    )


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--bert-config", default="configs/bert.yaml")
    parser.add_argument("--primary-run", default=None)
    parser.add_argument(
        "--sensitivity-run",
        default=None,
    )
    parser.add_argument(
        "--require-sensitivity",
        action="store_true",
        help="Require and validate the optional two-claim sensitivity run.",
    )
    parser.add_argument("--output", default=None)
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    with (PROJECT_ROOT / arguments.config).open("r", encoding="utf-8") as file:
        settings = yaml.safe_load(file)
    with (PROJECT_ROOT / arguments.bert_config).open("r", encoding="utf-8") as file:
        bert_settings = yaml.safe_load(file)
    if is_multiplatform(settings):
        validate_multiplatform_experiment(settings)
        data, _ = load_multiplatform_data(PROJECT_ROOT, settings["data"])
    else:
        data_path = PROJECT_ROOT / settings["data"]["dataset_path"]
        data = pd.read_csv(data_path)
        if tuple(data.columns) != CSV_COLUMNS:
            raise ValueError(
                "The final source CSV no longer matches the nine-column schema."
            )
    expected_rows = settings["data"].get("expected_rows")
    if expected_rows is not None and len(data) != int(expected_rows):
        raise ValueError(
            f"The final source has {len(data)} rows; expected {expected_rows}."
        )
    default_run_name = str(
        settings.get("reporting", {}).get("default_run_name", "primary")
    )
    primary_root = (
        PROJECT_ROOT / arguments.primary_run
        if arguments.primary_run
        else run_root(default_run_name)
    )
    sensitivity_root = (
        PROJECT_ROOT / arguments.sensitivity_run
        if arguments.sensitivity_run
        else run_root(str(settings["sensitivity"]["run_name"]))
    )
    primary_exclusions: tuple[int, ...] = ()
    primary = verify_artifact_manifest(
        primary_root,
        settings,
        bert_settings,
        arguments.config,
        arguments.bert_config,
        primary_exclusions,
    )
    verify_semantic_results(primary_root, settings, primary_exclusions)
    sensitivity: dict[str, Any] | None = None
    sensitivity_manifest_path = sensitivity_root / "results_manifest.json"
    if arguments.require_sensitivity or sensitivity_manifest_path.exists():
        sensitivity_exclusions = tuple(
            sorted(
                set(
                    int(value)
                    for value in settings["sensitivity"]["exclude_total_claims"]
                )
            )
        )
        sensitivity = verify_artifact_manifest(
            sensitivity_root,
            settings,
            bert_settings,
            arguments.config,
            arguments.bert_config,
            sensitivity_exclusions,
        )
        verify_semantic_results(
            sensitivity_root,
            settings,
            sensitivity_exclusions,
        )
    report = {
        "complete": True,
        "source_rows": len(data),
        "source_columns": list(data.columns),
        "experimental_conditions": len(CONDITION_NAMES),
        "primary_manifest_artifacts": len(primary.get("artifacts", [])),
        "sensitivity_checked": sensitivity is not None,
        "sensitivity_manifest_artifacts": (
            len(sensitivity.get("artifacts", []))
            if sensitivity is not None
            else 0
        ),
        "primary_results_manifest": str(
            (primary_root / "results_manifest.json").relative_to(PROJECT_ROOT)
        ),
        "sensitivity_results_manifest": (
            str(sensitivity_manifest_path.relative_to(PROJECT_ROOT))
            if sensitivity is not None
            else None
        ),
    }
    output = (
        PROJECT_ROOT / arguments.output
        if arguments.output
        else primary_root / "study_completion_report.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(
        "Study output validation complete: every required primary artifact is "
        "present and checksum-valid."
    )


if __name__ == "__main__":
    main()
