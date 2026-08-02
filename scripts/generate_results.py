"""Generate comparison tables and figures from held-out prediction files."""

from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import yaml

from evaluation.metrics import (
    calculate_metrics,
    paired_stratified_bootstrap,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CONDITIONS = {
    "A_RIDGE",
    "B_RIDGE",
    "C_RIDGE",
    "D_FROZEN_MINILM",
    "E_FINETUNED_BERT",
}


def load_settings() -> dict[str, Any]:
    with (PROJECT_ROOT / "configs/experiment.yaml").open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def load_prediction_files() -> dict[str, pd.DataFrame]:
    files = sorted(
        (PROJECT_ROOT / "results/predictions").glob("*_heldout.csv")
    )
    if not files:
        raise FileNotFoundError("No held-out prediction files were found.")
    results = {
        path.stem.removesuffix("_heldout"): pd.read_csv(path) for path in files
    }
    missing = sorted(EXPECTED_CONDITIONS - set(results))
    unexpected = sorted(set(results) - EXPECTED_CONDITIONS)
    if missing or unexpected:
        raise ValueError(
            "Held-out results are incomplete or unexpected. "
            f"Missing: {missing}; unexpected: {unexpected}."
        )
    required_columns = {"row_index", "true_label", "prediction"}
    reference_name = sorted(results)[0]
    reference = results[reference_name]
    reference_rows = set(reference["row_index"])
    reference_truth = reference.set_index("row_index")["true_label"].sort_index()
    for condition, frame in results.items():
        if not required_columns.issubset(frame.columns):
            raise ValueError(f"{condition} is missing prediction columns.")
        if frame["row_index"].duplicated().any():
            raise ValueError(f"{condition} contains duplicate row indices.")
        if set(frame["row_index"]) != reference_rows:
            raise ValueError("Held-out prediction files cover different videos.")
        truth = frame.set_index("row_index")["true_label"].sort_index()
        if not truth.equals(reference_truth):
            raise ValueError("Held-out prediction files disagree on true labels.")
    return results


def save_confusion_figure(
    condition: str,
    matrix: list[list[int]],
) -> None:
    figure_directory = PROJECT_ROOT / "results/figures"
    figure_directory.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots(figsize=(5, 4))
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=[1, 2, 3, 4],
        yticklabels=[1, 2, 3, 4],
        ax=axis,
    )
    axis.set_xlabel("Predicted label")
    axis.set_ylabel("True label")
    axis.set_title(condition)
    figure.tight_layout()
    figure.savefig(figure_directory / f"{condition}_confusion.png", dpi=200)
    plt.close(figure)


def main() -> None:
    settings = load_settings()
    prediction_sets = load_prediction_files()
    summaries: list[dict[str, object]] = []
    full_metrics: dict[str, object] = {}

    for condition, predictions in prediction_sets.items():
        metrics = calculate_metrics(
            predictions["true_label"],
            predictions["prediction"],
        )
        full_metrics[condition] = metrics
        summaries.append(
            {
                "condition": condition,
                "quadratic_weighted_kappa": metrics[
                    "quadratic_weighted_kappa"
                ],
                "accuracy": metrics["accuracy"],
                "weighted_f1": metrics["weighted_f1"],
                "mean_absolute_error": metrics["mean_absolute_error"],
            }
        )
        save_confusion_figure(condition, metrics["confusion_matrix"])

    comparisons: list[dict[str, object]] = []
    for first_name, second_name in itertools.combinations(prediction_sets, 2):
        first = prediction_sets[first_name]
        second = prediction_sets[second_name]
        aligned = first[["row_index", "true_label", "prediction"]].merge(
            second[["row_index", "true_label", "prediction"]],
            on="row_index",
            suffixes=("_a", "_b"),
            validate="one_to_one",
        )
        if not aligned["true_label_a"].equals(aligned["true_label_b"]):
            raise ValueError("Compared prediction files disagree on true labels.")
        comparison = paired_stratified_bootstrap(
            aligned["true_label_a"],
            aligned["prediction_a"],
            aligned["prediction_b"],
            resamples=int(settings["evaluation"]["bootstrap_resamples"]),
            seed=int(settings["seed"]),
        )
        comparisons.append(
            {
                "condition_a": first_name,
                "condition_b": second_name,
                **comparison,
            }
        )

    tables_directory = PROJECT_ROOT / "results/tables"
    metrics_directory = PROJECT_ROOT / "results/metrics"
    tables_directory.mkdir(parents=True, exist_ok=True)
    metrics_directory.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(summaries).sort_values(
        "quadratic_weighted_kappa",
        ascending=False,
    ).to_csv(tables_directory / "heldout_summary.csv", index=False)
    pd.DataFrame(comparisons).to_csv(
        tables_directory / "bootstrap_comparisons.csv",
        index=False,
    )
    (metrics_directory / "heldout_full_metrics.json").write_text(
        json.dumps(full_metrics, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
