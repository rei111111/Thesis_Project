"""Fail unless every non-LaTeX artifact required by the study is complete."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

from models.condition_registry import CONDITION_NAMES
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


def verify_artifact_manifest(root: Path) -> dict[str, Any]:
    manifest = load_json(root / "results_manifest.json")
    if manifest.get("condition_count") != 14:
        raise ValueError(f"{root} does not contain fourteen conditions.")
    if tuple(manifest.get("complete_experimental_conditions", [])) != CONDITION_NAMES:
        raise ValueError(f"{root} condition registry is incomplete or reordered.")
    for artifact in manifest.get("artifacts", []):
        path = root / artifact["path"]
        if not path.exists():
            raise FileNotFoundError(f"Manifest artifact is missing: {path}")
        if path.stat().st_size != artifact["bytes"]:
            raise ValueError(f"Manifest byte size changed for {path}.")
        if file_sha256(path) != artifact["sha256"]:
            raise ValueError(f"Manifest checksum changed for {path}.")
    return manifest


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--primary-run", default="results")
    parser.add_argument(
        "--sensitivity-run",
        default="results/sensitivity_no_two_claims",
    )
    parser.add_argument("--output", default="results/study_completion_report.json")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    with (PROJECT_ROOT / arguments.config).open("r", encoding="utf-8") as file:
        settings = yaml.safe_load(file)
    data_path = PROJECT_ROOT / settings["data"]["dataset_path"]
    data = pd.read_csv(data_path)
    if tuple(data.columns) != CSV_COLUMNS:
        raise ValueError("The final source CSV no longer matches the nine-column schema.")
    expected_rows = settings["data"].get("expected_rows")
    if expected_rows is not None and len(data) != int(expected_rows):
        raise ValueError(
            f"The final source has {len(data)} rows; expected {expected_rows}."
        )

    primary_root = PROJECT_ROOT / arguments.primary_run
    sensitivity_root = PROJECT_ROOT / arguments.sensitivity_run
    primary = verify_artifact_manifest(primary_root)
    sensitivity = verify_artifact_manifest(sensitivity_root)
    expected_exclusion = list(settings["sensitivity"]["exclude_total_claims"])
    if sensitivity.get("excluded_total_claims") != expected_exclusion:
        raise ValueError(
            "Sensitivity output does not use the configured total-claim exclusion."
        )
    report = {
        "complete": True,
        "source_rows": len(data),
        "source_columns": list(data.columns),
        "experimental_conditions": len(CONDITION_NAMES),
        "primary_manifest_artifacts": len(primary.get("artifacts", [])),
        "sensitivity_manifest_artifacts": len(sensitivity.get("artifacts", [])),
        "primary_results_manifest": str(
            (primary_root / "results_manifest.json").relative_to(PROJECT_ROOT)
        ),
        "sensitivity_results_manifest": str(
            (sensitivity_root / "results_manifest.json").relative_to(PROJECT_ROOT)
        ),
    }
    output = PROJECT_ROOT / arguments.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("Study output validation complete: every required code artifact is present.")


if __name__ == "__main__":
    main()
