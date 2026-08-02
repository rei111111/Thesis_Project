"""Train and evaluate Ridge, frozen MiniLM, and fine-tuned BERT."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
from typing import Any

import joblib
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
from models.frozen_minilm import FrozenMiniLMClassifier, minilm_parameter_grid
from models.ridge_classifier import build_ridge_classifier, ridge_parameter_grid


PROJECT_ROOT = Path(__file__).resolve().parents[1]


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
    if not certainty or not hedge or any(not term for term in certainty + hedge):
        raise ValueError("Both linguistic lexicons must contain nonblank terms.")
    return {"certainty_terms": certainty, "hedge_terms": hedge}


def result_paths() -> tuple[Path, Path, Path]:
    return (
        PROJECT_ROOT / "results/metrics",
        PROJECT_ROOT / "results/predictions",
        PROJECT_ROOT / "results/models",
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


def run_ridge(
    training: Any,
    heldout: Any,
    settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
) -> None:
    metrics_directory, predictions_directory, model_directory = result_paths()
    evaluation = settings["evaluation"]
    tfidf = settings["features"]["tfidf"]
    ngram_range = tuple(tfidf["ngram_range"])

    for feature_set in ("A", "B", "C"):
        condition = f"{feature_set}_RIDGE"
        output = predictions_directory / f"{condition}_heldout.csv"
        ensure_heldout_write_allowed(output, overwrite)
        estimator = build_ridge_classifier(
            feature_set=feature_set,
            max_features=int(tfidf["max_features"]),
            ngram_range=ngram_range,
            stop_words=tfidf.get("stop_words"),
            **lexicons,
        )
        grid = ridge_parameter_grid(settings["ridge"]["alphas"])
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
        final_estimator, selected = fit_selected_estimator(
            estimator,
            grid,
            training,
            folds=int(evaluation["outer_folds"]),
            seed=int(settings["seed"]),
            n_jobs=int(evaluation.get("n_jobs", 1)),
        )
        _save_estimator(final_estimator, selected, condition, model_directory)
        predictions = predict_selected_estimator(
            final_estimator,
            heldout,
            condition,
        )
        save_heldout_predictions(predictions, output)


def run_minilm(
    training: Any,
    heldout: Any,
    settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
) -> None:
    metrics_directory, predictions_directory, model_directory = result_paths()
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
    final_estimator, selected = fit_selected_estimator(
        estimator,
        grid,
        training,
        folds=int(evaluation["outer_folds"]),
        seed=int(settings["seed"]),
        n_jobs=1,
    )
    _save_estimator(final_estimator, selected, condition, model_directory)
    predictions = predict_selected_estimator(
        final_estimator,
        heldout,
        condition,
    )
    save_heldout_predictions(predictions, output)


def run_bert(
    training: Any,
    heldout: Any,
    settings: dict[str, Any],
    bert_settings: dict[str, Any],
    lexicons: dict[str, tuple[str, ...]],
    overwrite: bool,
    device: str | None,
) -> None:
    metrics_directory, predictions_directory, model_directory = result_paths()
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


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        choices=("ridge", "minilm", "bert", "all"),
        required=True,
    )
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--bert-config", default="configs/bert.yaml")
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite-heldout", action="store_true")
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

    if arguments.model in ("ridge", "all"):
        run_ridge(
            training,
            heldout,
            settings,
            lexicons,
            arguments.overwrite_heldout,
        )
    if arguments.model in ("minilm", "all"):
        run_minilm(
            training,
            heldout,
            settings,
            lexicons,
            arguments.overwrite_heldout,
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
        )


if __name__ == "__main__":
    main()
