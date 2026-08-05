"""Run the pre-specified analysis excluding videos with two eligible claims."""

from __future__ import annotations

import argparse
import subprocess
import sys


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-name", default="sensitivity_no_two_claims")
    parser.add_argument("--device", default=None)
    parser.add_argument("--overwrite-heldout", action="store_true")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    training_command = [
        sys.executable,
        "-m",
        "scripts.train_models",
        "--model",
        "all",
        "--run-name",
        arguments.run_name,
        "--exclude-total-claims",
        "2",
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
            arguments.run_name,
            "--exclude-total-claims",
            "2",
        ],
        check=True,
    )


if __name__ == "__main__":
    main()
