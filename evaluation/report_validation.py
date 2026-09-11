"""Recalculate scientific report tables from frozen rows and saved predictions."""

import io
import json
from pathlib import Path
import tempfile

import pandas as pd
import yaml

from evaluation.feature_associations import save_named_feature_reports
from evaluation.metrics import bootstrap_many_conditions, class_distribution_table
from features.content_groups import content_group_ids
from models.condition_registry import ablation_pairs


def check_table(path: Path, expected: pd.DataFrame) -> None:
    """Compare full values/schema after the same CSV round trip as the report."""
    canonical = pd.read_csv(io.StringIO(expected.to_csv(index=False)))
    observed = pd.read_csv(path)
    try:
        pd.testing.assert_frame_equal(
            observed, canonical, check_dtype=False, rtol=1e-9, atol=1e-11
        )
    except AssertionError as exc:
        raise ValueError(f"{path.name} does not match recalculated evidence.") from exc


def verify_report_tables(
    project_root: Path,
    root: Path,
    settings: dict,
    data: pd.DataFrame,
    training: pd.DataFrame,
    heldout: pd.DataFrame,
    prediction_sets: dict,
    cv_results: dict,
    exclusions: tuple[int, ...],
) -> None:
    from scripts.generate_results import (
        LABEL_NAMES, _assert_metric_payload_matches, add_condition_metadata,
        add_metric_ranks, cv_tables, heldout_tables, save_error_cases,
        save_interpretability_synthesis, save_rq1_platform_distribution,
    )

    tables = root / "tables"
    confidence = float(settings["reporting"]["confidence_level"])
    pooled = bool(settings["data"].get("sources"))
    labelled = data.loc[data["label"].notna()].copy()
    if "row_index" not in labelled:
        labelled.insert(0, "row_index", labelled.index.astype(int))
    if exclusions:
        labelled = labelled.loc[~labelled["total_claims"].isin(exclusions)]
    rq1 = pd.DataFrame(class_distribution_table(labelled["label"], confidence))
    rq1.insert(1, "category", rq1["label"].map(LABEL_NAMES))
    check_table(tables / "rq1_class_distribution.csv", rq1)

    summary, per_class, metrics, errors = heldout_tables(prediction_sets, None)
    summary = add_condition_metadata(add_metric_ranks(summary))
    check_table(tables / "heldout_summary.csv", summary)
    check_table(tables / "heldout_per_class_metrics.csv", per_class)
    check_table(tables / "heldout_ordinal_error_summary.csv", errors)
    _assert_metric_payload_matches(
        json.loads((root / "metrics/heldout_full_metrics.json").read_text()),
        metrics, "heldout_full_metrics.json",
    )
    for name, values in metrics.items():
        matrix = pd.read_csv(root / "figures" / f"{name}_confusion.csv", index_col=0)
        if matrix.shape != (4, 4) or matrix.to_numpy().tolist() != values["confusion_matrix"]:
            raise ValueError(f"{name} confusion matrix does not match predictions.")
    cv_summary, cv_differences = cv_tables(cv_results)
    check_table(tables / "cv_summary.csv", add_condition_metadata(
        add_metric_ranks(cv_summary, suffix="_mean")
    ))
    check_table(tables / "cv_paired_differences.csv", cv_differences)

    reference = next(iter(prediction_sets.values())).sort_values("row_index")
    intervals, differences = bootstrap_many_conditions(
        reference["true_label"],
        {name: frame.sort_values("row_index")["prediction"] for name, frame in prediction_sets.items()},
        resamples=int(settings["evaluation"]["bootstrap_resamples"]),
        seed=int(settings["seed"]), confidence_level=confidence,
        groups=content_group_ids(heldout.sort_values("row_index")) if pooled else None,
    )
    differences = pd.DataFrame(differences)
    check_table(tables / "heldout_bootstrap_metric_intervals.csv", pd.DataFrame(intervals))
    check_table(tables / "heldout_bootstrap_pairwise_differences.csv", differences)
    for filename, source in (
        ("rq2_cv_ablation_differences.csv", cv_differences),
        ("rq2_heldout_ablation_bootstrap.csv", differences),
    ):
        parts = []
        for first, second, contrast in ablation_pairs():
            selected = source.loc[source["condition_a"].eq(first) & source["condition_b"].eq(second)].copy()
            selected.insert(0, "ablation_contrast", contrast)
            parts.append(selected)
        check_table(tables / filename, pd.concat(parts, ignore_index=True))

    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        if pooled:
            save_rq1_platform_distribution(data, temporary, confidence, exclusions)
        save_error_cases(prediction_sets, data, temporary)
        save_interpretability_synthesis(
            root, summary, temporary,
            top_k=int(settings["interpretability"]["top_features_per_class"]),
            engagement_transform=settings["features"].get("engagement_transform", "log1p"),
        )
        for expected_file in temporary.glob("*.csv"):
            check_table(tables / expected_file.name, pd.read_csv(expected_file))

        lexicons = yaml.safe_load((project_root / settings["features"]["linguistic_lexicon_path"]).read_text())
        associations = temporary / "associations"
        save_named_feature_reports(
            labelled, training,
            tuple(str(value).strip().lower() for value in lexicons["certainty_terms"]),
            tuple(str(value).strip().lower() for value in lexicons["hedge_terms"]),
            associations,
            bootstrap_resamples=int(settings["reporting"]["association_bootstrap_resamples"]),
            seed=int(settings["seed"]), confidence_level=confidence,
            text_columns=tuple(settings["features"].get("text_columns", ("title", "transcript"))),
            engagement_transform=settings["features"].get("engagement_transform", "log1p"),
            platform_column=settings["features"].get("platform_column", "platform"),
        )
        for expected_file in associations.glob("*.csv"):
            check_table(root / "feature_associations" / expected_file.name, pd.read_csv(expected_file))
