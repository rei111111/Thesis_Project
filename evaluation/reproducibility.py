"""Machine-readable provenance for data, configuration, hardware, and runs."""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TRACKED_PACKAGES = (
    "numpy",
    "pandas",
    "scipy",
    "scikit-learn",
    "joblib",
    "PyYAML",
    "matplotlib",
    "seaborn",
    "torch",
    "transformers",
    "sentence-transformers",
)


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_versions() -> dict[str, str | None]:
    versions: dict[str, str | None] = {}
    for package in TRACKED_PACKAGES:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return versions


def hardware_information() -> dict[str, object]:
    information: dict[str, object] = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "logical_cpu_count": os.cpu_count(),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
    }
    try:
        import torch

        information.update(
            {
                "torch_cuda_available": bool(torch.cuda.is_available()),
                "torch_cuda_version": torch.version.cuda,
                "torch_cudnn_version": (
                    torch.backends.cudnn.version()
                    if hasattr(torch.backends, "cudnn")
                    else None
                ),
                "gpu_count": int(torch.cuda.device_count()),
                "gpu_names": [
                    torch.cuda.get_device_name(index)
                    for index in range(torch.cuda.device_count())
                ],
            }
        )
    except ImportError:
        information["torch_cuda_available"] = None
    return information


def git_commit(project_root: str | Path) -> str | None:
    root = Path(project_root)
    if not (root / ".git").exists():
        return None
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def build_run_manifest(
    project_root: str | Path,
    command: list[str],
    run_name: str,
    requested_model: str,
    seed: int,
    input_files: dict[str, str | Path],
    exclusions: dict[str, object] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, object]:
    root = Path(project_root)
    hashes = {
        name: {
            "path": str(Path(path).resolve().relative_to(root.resolve())),
            "sha256": sha256_file(path),
        }
        for name, path in input_files.items()
        if Path(path).exists()
    }
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "run_name": run_name,
        "requested_model": requested_model,
        "command": command,
        "random_seed": seed,
        "input_files": hashes,
        "exclusions": exclusions or {},
        "package_versions": package_versions(),
        "hardware": hardware_information(),
        "git_commit": git_commit(root),
        "checkpoint_names": {
            "frozen_sentence_transformer": "sentence-transformers/all-MiniLM-L6-v2",
            "fine_tuned_transformer": "bert-base-uncased",
        },
        "extra": extra or {},
    }


def save_run_manifest(
    manifest: dict[str, object],
    output_directory: str | Path,
) -> Path:
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    timestamp = str(manifest["created_utc"]).replace(":", "-").replace("+", "_")
    path = directory / f"run_{timestamp}.json"
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return path
