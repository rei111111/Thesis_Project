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
from collections.abc import Iterable
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
SCIENTIFIC_SOURCE_DIRECTORIES = ("evaluation", "features", "models", "scripts")


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


def scientific_code_manifest(project_root: str | Path) -> dict[str, object]:
    """Hash the executable scientific Python source, even outside Git."""
    root = Path(project_root).resolve()
    files = sorted(
        path
        for directory in SCIENTIFIC_SOURCE_DIRECTORIES
        for path in (root / directory).rglob("*.py")
        if path.is_file()
    )
    aggregate = hashlib.sha256()
    records: list[dict[str, object]] = []
    for path in files:
        relative = str(path.relative_to(root))
        digest = sha256_file(path)
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
        records.append(
            {"path": relative, "bytes": path.stat().st_size, "sha256": digest}
        )
    if not records:
        raise FileNotFoundError("No scientific Python source files were found.")
    return {"sha256": aggregate.hexdigest(), "files": records}


def file_manifest(
    project_root: str | Path,
    paths: Iterable[str | Path],
) -> list[dict[str, object]]:
    """Create stable project-relative checksum records for existing files."""
    root = Path(project_root).resolve()
    resolved = sorted({Path(path).resolve() for path in paths})
    records: list[dict[str, object]] = []
    for path in resolved:
        if not path.is_file():
            raise FileNotFoundError(f"Run output is missing: {path}")
        try:
            relative = path.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Run artifact is outside the project root: {path}") from exc
        records.append(
            {
                "path": str(relative),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return records


def validate_training_run_receipts(
    project_root: str | Path,
    result_root: str | Path,
    expected_conditions: Iterable[str],
    input_files: dict[str, str | Path],
    exclusions: dict[str, object],
    required_outputs: dict[str, Iterable[str | Path]],
    checkpoint_names: dict[str, str],
) -> list[Path]:
    """Prove every condition is covered by compatible, untampered run receipts."""
    root = Path(project_root).resolve()
    result = Path(result_root).resolve()
    receipt_paths = sorted((result / "reproducibility").glob("run_*.json"))
    if not receipt_paths:
        raise FileNotFoundError("No training run receipts were found.")
    expected_inputs = {
        name: sha256_file(path) for name, path in input_files.items()
    }
    current_code_hash = str(scientific_code_manifest(root)["sha256"])
    conditions = tuple(expected_conditions)
    candidates: dict[str, list[tuple[Path, str]]] = {
        condition: [] for condition in conditions
    }
    for receipt_path in receipt_paths:
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if receipt.get("exclusions", {}) != exclusions:
            continue
        if receipt.get("checkpoint_names", {}) != checkpoint_names:
            continue
        if receipt.get("scientific_code", {}).get("sha256") != current_code_hash:
            continue
        recorded_inputs = receipt.get("input_files", {})
        if any(
            recorded_inputs.get(name, {}).get("sha256") != digest
            for name, digest in expected_inputs.items()
        ):
            continue
        output_records = {
            record.get("path"): record
            for record in receipt.get("output_files", [])
            if isinstance(record, dict)
        }
        package_signature = json.dumps(
            receipt.get("package_versions", {}), sort_keys=True
        )
        completed = set(receipt.get("completed_conditions", []))
        for condition in set(conditions) & completed:
            required = [Path(path).resolve() for path in required_outputs[condition]]
            valid = True
            for path in required:
                try:
                    relative = str(path.relative_to(root))
                except ValueError:
                    valid = False
                    break
                record = output_records.get(relative)
                if (
                    record is None
                    or not path.is_file()
                    or path.stat().st_size != record.get("bytes")
                    or sha256_file(path) != record.get("sha256")
                ):
                    valid = False
                    break
            if valid:
                candidates[condition].append((receipt_path, package_signature))
    missing = [condition for condition, values in candidates.items() if not values]
    if missing:
        raise ValueError(
            "No current-code, current-input training receipt covers conditions: "
            f"{missing}. Rerun those conditions before generating results."
        )
    signatures = {
        signature for values in candidates.values() for _, signature in values
    }
    compatible = [
        signature
        for signature in signatures
        if all(
            any(candidate_signature == signature for _, candidate_signature in values)
            for values in candidates.values()
        )
    ]
    if not compatible:
        raise ValueError(
            "Conditions were produced under incompatible package environments; "
            "a single environment must cover the complete comparison."
        )
    selected_signature = sorted(compatible)[-1]
    return sorted(
        {
            path
            for values in candidates.values()
            for path, signature in values
            if signature == selected_signature
        }
    )


def build_run_manifest(
    project_root: str | Path,
    command: list[str],
    run_name: str,
    requested_model: str,
    seed: int,
    input_files: dict[str, str | Path],
    exclusions: dict[str, object] | None = None,
    extra: dict[str, Any] | None = None,
    completed_conditions: Iterable[str] = (),
    output_files: Iterable[str | Path] = (),
    checkpoint_names: dict[str, str] | None = None,
) -> dict[str, object]:
    root = Path(project_root)
    missing_inputs = [name for name, path in input_files.items() if not Path(path).is_file()]
    if missing_inputs:
        raise FileNotFoundError(f"Run inputs are missing: {missing_inputs}")
    hashes = {
        name: {
            "path": str(Path(path).resolve().relative_to(root.resolve())),
            "sha256": sha256_file(path),
        }
        for name, path in input_files.items()
    }
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "run_name": run_name,
        "requested_model": requested_model,
        "command": command,
        "random_seed": seed,
        "input_files": hashes,
        "scientific_code": scientific_code_manifest(root),
        "completed_conditions": list(completed_conditions),
        "output_files": file_manifest(root, output_files),
        "exclusions": exclusions or {},
        "package_versions": package_versions(),
        "hardware": hardware_information(),
        "git_commit": git_commit(root),
        "checkpoint_names": checkpoint_names or {},
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
