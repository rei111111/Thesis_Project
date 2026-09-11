"""Run the pre-specified analysis excluding videos with two eligible claims."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/experiment.yaml")
    parser.add_argument("--bert-config", default="configs/bert.yaml")
    parser.add_argument("--run-name", default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite-heldout", action="store_true")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    settings = yaml.safe_load(
        (PROJECT_ROOT / arguments.config).read_text(encoding="utf-8")
    )
    run_name = arguments.run_name or str(settings["sensitivity"]["run_name"])
    exclusions = [
        str(int(value)) for value in settings["sensitivity"]["exclude_total_claims"]
    ]
    training_command = [
        sys.executable,
        "-m",
        "scripts.train_models",
        "--model",
        "all",
        "--run-name",
        run_name,
        "--config",
        arguments.config,
        "--bert-config",
        arguments.bert_config,
        "--exclude-total-claims",
        *exclusions,
    ]
    if arguments.device:
        training_command.extend(["--device", arguments.device])
    if arguments.overwrite_heldout:
        training_command.append("--overwrite-heldout")
    subprocess.run(training_command, check=True)
    subprocess.run(
        [
            sys.executable,
            "-m",
            "scripts.generate_results",
            "--run-name",
            run_name,
            "--config",
            arguments.config,
            "--bert-config",
            arguments.bert_config,
            "--exclude-total-claims",
            *exclusions,
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
