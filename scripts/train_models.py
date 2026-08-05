"""Train all fourteen thesis conditions and two contextual baselines."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import yaml

from evaluation.cross_validation import (
    run_bert_outer_cross_validation,
    run_nested_cross_validation,
    save_cross_validation_result,
)
from evaluation.final_evaluation import (
    fit_final_bert,
    fit_selected_estimator,
    load_saved_split,
    predict_selected_estimator,
    save_heldout_predictions,
)
from evaluation.reproducibility import build_run_manifest, save_run_manifest
from features.linguistic_features import validate_lexicons
from models.baselines import (
    build_most_frequent_baseline,
    build_stratified_random_baseline,
)
from models.complement_naive_bayes import (
    build_complement_naive_bayes,
    complement_nb_parameter_grid,
)
from models.condition_registry import INTERPRETABLE_MODEL_FAMILIES
from models.decision_tree import build_decision_tree, decision_tree_parameter_grid
from models.frozen_minilm import FrozenMiniLMClassifier, minilm_parameter_grid
from models.logistic_regression import (
    build_logistic_regression,
    logistic_parameter_grid,
)
from models.ridge_classifier import build_ridge_classifier, ridge_parameter_grid


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_CHOICES = (
    "logistic",
    "ridge",
    "cnb",
    "tree",
    "interpretable",
    "baselines",
    "minilm",
    "bert",
    "all",
)
CLI_TO_FAMILY = {
    "logistic": "LOGISTIC_REGRESSION",
    "ridge": "RIDGE",
    "cnb": "COMPLEMENT_NB",
    "tree": "DECISION_TREE",
}
PROHIBITED_PREDICTORS = {"row_index", "total_claims", "false_claims", "label"}


def check_optional_dependencies(model: str) -> None:
    """Fail before training if the requested transformer stack is absent."""
    required: dict[str, str] = {}
    if model in ("minilm", "all"):
        required["sentence_transformers"] = "sentence-transformers"
    if model in ("bert", "all"):
        required["torch"] = "torch"
        required["transformers"] = "transformers"
    missing = [
        package_name
        for module_name, package_name in required.items()
        if importlib.util.find_spec(module_name) is None
    ]
    if missing:
        raise ImportError(
            "Missing dependencies for the requested model(s): "
            f"{missing}. Install requirements.txt before training."
        )


def load_yaml(relative_path: str) -> dict[str, Any]:
    with (PROJECT_ROOT / relative_path).open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_lexicons(settings: dict[str, Any]) -> dict[str, tuple[str, ...]]:
    path = settings["features"]["linguistic_lexicon_path"]
    values = load_yaml(path)
    certainty = tuple(str(term).strip().lower() for term in values["certainty_terms"])
    hedge = tuple(str(term).strip().lower() for term in values["hedge_terms"])
    validate_lexicons(certainty, hedge)
    return {"certainty_terms": certainty, "hedge_terms": hedge}


def run_root(run_name: str) -> Path:
    if not run_name or any(part in run_name for part in ("/", "\\", "..")):
        raise ValueError("run_name must be one safe directory name.")
    return PROJECT_ROOT / "results" if run_name == "primary" else PROJECT_ROOT / "results" / run_name


def result_paths(run_name: str) -> tuple[Path, Path, Path, Path]:
    root = run_root(run_name)
    return (
        root / "metrics",
        root / "predictions",
        root / "models",
        root / "interpretability",
    )


def ensure_heldout_write_allowed(path: Path, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(
            f"{path} already exists. Do not repeat held-out evaluation unless "
            "the reason is documented; pass --overwrite-heldout if justified."
        )


def _save_estimator(
    estimator: Any,
    parameters: dict[str, Any],
    condition: str,
    model_directory: Path,
) -> None:
    output = model_directory / condition
    output.mkdir(parents=True, exist_ok=True)
    joblib.dump(estimator, output / "estimator.joblib")
    (output / "selected_parameters.json").write_text(
        json.dumps(parameters, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def ensure_iterative_estimator_converged(estimator: Any, condition: str) -> None:
    """Reject a silently maxed-out Logistic Regression fit."""
    if hasattr(estimator, "named_steps"):
        classifier = estimator.named_steps.get("classifier")
    else:
        classifier = getattr(estimator, "classifier_", None)
    if classifier is None or not hasattr(classifier, "n_iter_"):
        return
    maximum_value = getattr(classifier, "max_iter", None)
    iteration_values = getattr(classifier, "n_iter_", None)
    if maximum_value is None or iteration_values is None:
        return
    maximum = int(maximum_value)
    observed = int(np.max(np.asarray(iteration_values, dtype=int)))
    if maximum and observed >= maximum:
        raise RuntimeError(
            f"{condition} reached max_iter={maximum} without a confirmed "
            "converged fit. Increase the pre-specified limit and rerun every "
            "affected condition before using its held-out result."
        )


def ensure_no_prohibited_predictors(estimator: Any, condition: str) -> None:
    """Prove that annotation-derived and audit fields cannot enter a model."""
    names: set[str] = set()
    if hasattr(estimator, "named_steps") and "features" in estimator.named_steps:
        raw_names = estimator.named_steps["features"].get_feature_names_out()
        names = {str(value).split("__")[-1] for value in raw_names}
    elif hasattr(estimator, "metadata_scaler_"):
        names = {
            str(value)
            for value in estimator.metadata_scaler_.get_feature_names_out()
        }
    overlap = sorted(names & PROHIBITED_PREDICTORS)
    if overlap:
        raise RuntimeError(
            f"{condition} contains prohibited leakage features: {overlap}."
        )


def _interpretable_estimator_and_grid(
    family: str,
    feature_set: str,
    settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
) -> tuple[Any, dict[str, list[Any]]]:
    tfidf = settings["features"]["tfidf"]
    common = {
        "feature_set": feature_set,
        "max_features": int(tfidf["max_features"]),
        "ngram_range": tuple(tfidf["ngram_range"]),
        "stop_words": tfidf.get("stop_words"),
        **lexicons,
    }
    if family == "LOGISTIC_REGRESSION":
        model_settings = settings["logistic_regression"]
        estimator = build_logistic_regression(
            max_iter=int(model_settings["max_iter"]),
            random_state=int(settings["seed"]),
            **common,
        )
        grid = logistic_parameter_grid(model_settings["c_values"])
    elif family == "RIDGE":
        estimator = build_ridge_classifier(**common)
        grid = ridge_parameter_grid(settings["ridge"]["alphas"])
    elif family == "COMPLEMENT_NB":
        estimator = build_complement_naive_bayes(**common)
        grid = complement_nb_parameter_grid(
            settings["complement_naive_bayes"]["alphas"]
        )
    elif family == "DECISION_TREE":
        model_settings = settings["decision_tree"]
        estimator = build_decision_tree(
            random_state=int(settings["seed"]),
            **common,
        )
        grid = decision_tree_parameter_grid(
            model_settings["max_depths"],
            model_settings["min_samples_leaf"],
        )
    else:
        raise ValueError(f"Unknown interpretable family: {family}")
    return estimator, grid


def run_interpretable_family(
    family: str,
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
    run_name: str,
    export_interpretability: bool = True,
) -> None:
    metrics_directory, predictions_directory, model_directory, interpretation_directory = result_paths(run_name)
    evaluation = settings["evaluation"]
    interpretation = settings["interpretability"]
    for feature_set in ("A", "B", "C"):
        condition = f"{feature_set}_{family}"
        output = predictions_directory / f"{condition}_heldout.csv"
        ensure_heldout_write_allowed(output, overwrite)
        estimator, grid = _interpretable_estimator_and_grid(
            family,
            feature_set,
            settings,
            lexicons,
        )
        cross_validation = run_nested_cross_validation(
            estimator=estimator,
            parameter_grid=grid,
            data=training,
            outer_folds=int(evaluation["outer_folds"]),
            inner_folds=int(evaluation["inner_folds"]),
            seed=int(settings["seed"]),
            n_jobs=int(evaluation.get("n_jobs", 1)),
        )
        save_cross_validation_result(
            cross_validation,
            condition,
            metrics_directory,
            predictions_directory,
        )
        for fold_estimator in cross_validation.fitted_estimators:
            ensure_iterative_estimator_converged(fold_estimator, condition)
        final_estimator, selected = fit_selected_estimator(
            estimator,
            grid,
            training,
            folds=int(evaluation["outer_folds"]),
            seed=int(settings["seed"]),
            n_jobs=int(evaluation.get("n_jobs", 1)),
        )
        ensure_iterative_estimator_converged(final_estimator, condition)
        ensure_no_prohibited_predictors(final_estimator, condition)
        _save_estimator(final_estimator, selected, condition, model_directory)
        predictions = predict_selected_estimator(
            final_estimator,
            heldout,
            condition,
        )
        save_heldout_predictions(predictions, output)
        if export_interpretability:
            from evaluation.interpretability import save_interpretability_artifacts

            summary = save_interpretability_artifacts(
                final_estimator=final_estimator,
                fold_estimators=cross_validation.fitted_estimators,
                heldout_data=heldout,
                condition=condition,
                output_directory=interpretation_directory,
                top_k=int(interpretation["top_features_per_class"]),
                local_top_k=int(
                    interpretation["local_features_per_prediction"]
                ),
            )
            (interpretation_directory / f"{condition}_summary.json").write_text(
                json.dumps(summary, indent=2),
                encoding="utf-8",
            )


def run_baselines(
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    settings: dict[str, Any],
    overwrite: bool,
    run_name: str,
) -> None:
    metrics_directory, predictions_directory, model_directory, _ = result_paths(run_name)
    evaluation = settings["evaluation"]
    builders = {
        "BASELINE_MOST_FREQUENT": build_most_frequent_baseline,
        "BASELINE_STRATIFIED_RANDOM": build_stratified_random_baseline,
    }
    for condition, builder in builders.items():
        output = predictions_directory / f"{condition}_heldout.csv"
        ensure_heldout_write_allowed(output, overwrite)
        estimator = builder(int(settings["seed"]))
        cross_validation = run_nested_cross_validation(
            estimator=estimator,
            parameter_grid={},
            data=training,
            outer_folds=int(evaluation["outer_folds"]),
            inner_folds=int(evaluation["inner_folds"]),
            seed=int(settings["seed"]),
            n_jobs=1,
        )
        save_cross_validation_result(
            cross_validation,
            condition,
            metrics_directory,
            predictions_directory,
        )
        fitted, selected = fit_selected_estimator(
            estimator,
            {},
            training,
            folds=int(evaluation["outer_folds"]),
            seed=int(settings["seed"]),
            n_jobs=1,
        )
        _save_estimator(fitted, selected, condition, model_directory)
        predictions = predict_selected_estimator(fitted, heldout, condition)
        save_heldout_predictions(predictions, output)


def run_minilm(
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
    run_name: str,
) -> None:
    metrics_directory, predictions_directory, model_directory, _ = result_paths(run_name)
    evaluation = settings["evaluation"]
    model_settings = settings["minilm"]
    condition = "D_FROZEN_MINILM"
    output = predictions_directory / f"{condition}_heldout.csv"
    ensure_heldout_write_allowed(output, overwrite)
    estimator = FrozenMiniLMClassifier(
        model_name=model_settings["model_name"],
        batch_size=int(model_settings["batch_size"]),
        random_state=int(settings["seed"]),
        **lexicons,
    )
    grid = minilm_parameter_grid(model_settings["c_values"])
    cross_validation = run_nested_cross_validation(
        estimator=estimator,
        parameter_grid=grid,
        data=training,
        outer_folds=int(evaluation["outer_folds"]),
        inner_folds=int(evaluation["inner_folds"]),
        seed=int(settings["seed"]),
        n_jobs=1,
    )
    save_cross_validation_result(
        cross_validation,
        condition,
        metrics_directory,
        predictions_directory,
    )
    for fold_estimator in cross_validation.fitted_estimators:
        ensure_iterative_estimator_converged(fold_estimator, condition)
    final_estimator, selected = fit_selected_estimator(
        estimator,
        grid,
        training,
        folds=int(evaluation["outer_folds"]),
        seed=int(settings["seed"]),
        n_jobs=1,
    )
    ensure_iterative_estimator_converged(final_estimator, condition)
    ensure_no_prohibited_predictors(final_estimator, condition)
    _save_estimator(final_estimator, selected, condition, model_directory)
    minilm_model_path = model_directory / condition
    (minilm_model_path / "checkpoint_metadata.json").write_text(
        json.dumps(
            {
                "model_name": final_estimator.model_name,
                "model_commit_hash": getattr(
                    final_estimator,
                    "model_revision_",
                    None,
                ),
                "embedding_dimension": int(final_estimator.embedding_dimension_),
                "named_auxiliary_features": final_estimator.metadata_scaler_
                .get_feature_names_out()
                .tolist(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    predictions = predict_selected_estimator(final_estimator, heldout, condition)
    save_heldout_predictions(predictions, output)
    from evaluation.interpretability import save_minilm_auxiliary_artifacts

    summary = save_minilm_auxiliary_artifacts(
        final_estimator,
        cross_validation.fitted_estimators,
        heldout.drop(columns=["label"]),
        result_paths(run_name)[3],
    )
    interpretation_path = result_paths(run_name)[3]
    (interpretation_path / f"{condition}_summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )


def run_bert(
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    settings: dict[str, Any],
    bert_settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
    device: str | None,
    run_name: str,
) -> None:
    metrics_directory, predictions_directory, model_directory, _ = result_paths(run_name)
    evaluation = settings["evaluation"]
    condition = "E_FINETUNED_BERT"
    output = predictions_directory / f"{condition}_heldout.csv"
    ensure_heldout_write_allowed(output, overwrite)
    active_bert_settings = dict(bert_settings)
    active_bert_settings["linguistic_lexicons"] = {
        key: list(value) for key, value in lexicons.items()
    }
    cross_validation = run_bert_outer_cross_validation(
        data=training,
        settings=active_bert_settings,
        outer_folds=int(evaluation["outer_folds"]),
        seed=int(settings["seed"]),
        output_directory=model_directory / condition / "outer_folds",
        device=device,
    )
    save_cross_validation_result(
        cross_validation,
        condition,
        metrics_directory,
        predictions_directory,
    )
    predictions = fit_final_bert(
        training_data=training,
        heldout_data=heldout,
        settings=active_bert_settings,
        outer_best_epochs=cross_validation.best_epochs,
        output_directory=model_directory / condition,
        device=device,
    )
    save_heldout_predictions(predictions, output)


def apply_sensitivity_exclusions(
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    excluded_total_claims: tuple[int, ...],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if not excluded_total_claims:
        return training, heldout
    for value in excluded_total_claims:
        if value < 0:
            raise ValueError("Excluded total-claim values cannot be negative.")
    filtered_training = training.loc[
        ~training["total_claims"].isin(excluded_total_claims)
    ].reset_index(drop=True)
    filtered_heldout = heldout.loc[
        ~heldout["total_claims"].isin(excluded_total_claims)
    ].reset_index(drop=True)
    for name, frame in (("training", filtered_training), ("held-out", filtered_heldout)):
        missing = sorted(set((1, 2, 3, 4)) - set(frame["label"].astype(int)))
        if missing:
            raise ValueError(
                f"Sensitivity exclusion removes classes {missing} from {name} data."
            )
    return filtered_training, filtered_heldout


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=MODEL_CHOICES, required=True)
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--bert-config", default="configs/bert.yaml")
    parser.add_argument("--device", default=None)
    parser.add_argument("--run-name", default="primary")
    parser.add_argument("--exclude-total-claims", nargs="*", type=int, default=[])
    parser.add_argument("--overwrite-heldout", action="store_true")
    parser.add_argument("--skip-interpretability", action="store_true")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    check_optional_dependencies(arguments.model)
    settings = load_yaml(arguments.config)
    bert_settings = load_yaml(arguments.bert_config)
    lexicons = load_lexicons(settings)
    data_settings = settings["data"]
    training, heldout = load_saved_split(
        PROJECT_ROOT / data_settings["dataset_path"],
        PROJECT_ROOT / data_settings["train_indices_path"],
        PROJECT_ROOT / data_settings["test_indices_path"],
        PROJECT_ROOT / data_settings["excluded_indices_path"],
        PROJECT_ROOT / data_settings["split_manifest_path"],
    )
    exclusions = tuple(sorted(set(arguments.exclude_total_claims)))
    training, heldout = apply_sensitivity_exclusions(training, heldout, exclusions)

    if arguments.model in CLI_TO_FAMILY:
        families = (CLI_TO_FAMILY[arguments.model],)
    elif arguments.model in ("interpretable", "all"):
        families = INTERPRETABLE_MODEL_FAMILIES
    else:
        families = ()
    for family in families:
        run_interpretable_family(
            family,
            training,
            heldout,
            settings,
            lexicons,
            arguments.overwrite_heldout,
            arguments.run_name,
            export_interpretability=not arguments.skip_interpretability,
        )
    if arguments.model in ("baselines", "all"):
        run_baselines(
            training,
            heldout,
            settings,
            arguments.overwrite_heldout,
            arguments.run_name,
        )
    if arguments.model in ("minilm", "all"):
        run_minilm(
            training,
            heldout,
            settings,
            lexicons,
            arguments.overwrite_heldout,
            arguments.run_name,
        )
    if arguments.model in ("bert", "all"):
        run_bert(
            training,
            heldout,
            settings,
            bert_settings,
            lexicons,
            arguments.overwrite_heldout,
            arguments.device,
            arguments.run_name,
        )

    input_files = {
        "dataset": PROJECT_ROOT / data_settings["dataset_path"],
        "experiment_config": PROJECT_ROOT / arguments.config,
        "bert_config": PROJECT_ROOT / arguments.bert_config,
        "linguistic_lexicons": PROJECT_ROOT
        / settings["features"]["linguistic_lexicon_path"],
        "train_indices": PROJECT_ROOT / data_settings["train_indices_path"],
        "test_indices": PROJECT_ROOT / data_settings["test_indices_path"],
        "excluded_indices": PROJECT_ROOT / data_settings["excluded_indices_path"],
        "split_manifest": PROJECT_ROOT / data_settings["split_manifest_path"],
    }
    manifest = build_run_manifest(
        PROJECT_ROOT,
        command=[sys.executable, "-m", "scripts.train_models", *sys.argv[1:]],
        run_name=arguments.run_name,
        requested_model=arguments.model,
        seed=int(settings["seed"]),
        input_files=input_files,
        exclusions={"total_claims": list(exclusions)},
        extra={
            "training_rows_used": len(training),
            "heldout_rows_used": len(heldout),
            "interpretability_exported": not arguments.skip_interpretability,
        },
    )
    save_run_manifest(manifest, run_root(arguments.run_name) / "reproducibility")


if __name__ == "__main__":
    main()
