"""Canonical names and ordering for the fourteen thesis conditions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConditionSpec:
    name: str
    configuration: str
    model_family: str
    feature_set: str | None
    interpretable: bool
    display_name: str


INTERPRETABLE_MODEL_FAMILIES = (
    "LOGISTIC_REGRESSION",
    "RIDGE",
    "COMPLEMENT_NB",
    "DECISION_TREE",
)

CONDITION_SPECS = tuple(
    ConditionSpec(
        name=f"{feature_set}_{model_family}",
        configuration=feature_set,
        model_family=model_family,
        feature_set=feature_set,
        interpretable=True,
        display_name=f"{feature_set}: {model_family.replace('_', ' ').title()}",
    )
    for feature_set in ("A", "B", "C")
    for model_family in INTERPRETABLE_MODEL_FAMILIES
) + (
    ConditionSpec(
        name="D_FROZEN_MINILM",
        configuration="D",
        model_family="FROZEN_MINILM",
        feature_set=None,
        interpretable=False,
        display_name="D: Frozen MiniLM + Logistic Regression",
    ),
    ConditionSpec(
        name="E_FINETUNED_BERT",
        configuration="E",
        model_family="FINETUNED_BERT",
        feature_set=None,
        interpretable=False,
        display_name="E: Fine-tuned BERT",
    ),
)

CONDITION_NAMES = tuple(spec.name for spec in CONDITION_SPECS)
CONDITION_BY_NAME = {spec.name: spec for spec in CONDITION_SPECS}
BASELINE_NAMES = ("BASELINE_MOST_FREQUENT", "BASELINE_STRATIFIED_RANDOM")


def ablation_pairs() -> tuple[tuple[str, str, str], ...]:
    """Return A--B and B--C comparisons for each interpretable family."""
    pairs: list[tuple[str, str, str]] = []
    for family in INTERPRETABLE_MODEL_FAMILIES:
        pairs.append((f"A_{family}", f"B_{family}", "A_minus_B"))
        pairs.append((f"B_{family}", f"C_{family}", "B_minus_C"))
    return tuple(pairs)
