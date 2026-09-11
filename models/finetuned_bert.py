"""Fine-tuned BERT with six scaled auxiliary features."""

from __future__ import annotations

import copy
import json
import random
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from evaluation.metrics import quadratic_weighted_kappa

from features.metadata_features import MetadataScaler
from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)
from features.transformer_features import BertVideoDataset

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as functional
    from torch.utils.data import DataLoader
except ImportError:
    torch = None
    nn = None
    functional = None
    DataLoader = None

try:
    from transformers import (
        AutoConfig,
        AutoModel,
        AutoTokenizer,
        get_linear_schedule_with_warmup,
    )
except ImportError:
    AutoConfig = None
    AutoModel = None
    AutoTokenizer = None
    get_linear_schedule_with_warmup = None


TorchModule = nn.Module if nn is not None else object


def require_torch() -> None:
    if torch is None or nn is None or DataLoader is None:
        raise ImportError("Install torch before running fine-tuned BERT.")


def require_transformers() -> None:
    if AutoConfig is None or AutoModel is None or AutoTokenizer is None:
        raise ImportError("Install transformers before running fine-tuned BERT.")


def resolve_bert_settings(settings: dict[str, Any]) -> dict[str, Any]:
    """Pin encoder and tokenizer to one immutable commit before any fits."""
    active = dict(settings)
    revision = active.get("resolved_revision")
    if revision is None:
        require_transformers()
        config = AutoConfig.from_pretrained(
            active["model_name"], revision=active.get("revision")
        )
        revision = getattr(config, "_commit_hash", None) or active.get("revision")
    if not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{40}", revision) is None:
        raise ValueError("BERT requires a resolved immutable checkpoint commit.")
    requested = active.get("revision")
    if isinstance(requested, str) and re.fullmatch(r"[0-9a-f]{40}", requested) and requested != revision:
        raise ValueError("BERT resolved a different commit from the requested revision.")
    active["resolved_revision"] = revision
    return active


def set_random_seed(seed: int) -> None:
    """Set the repeatable parts of the Python, NumPy, and PyTorch state."""
    random.seed(seed)
    np.random.seed(seed)
    if torch is not None:
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        if hasattr(torch.backends, "cudnn"):
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False


class BertMetadataClassifier(TorchModule):
    """BERT pooled representation concatenated with derived auxiliary values."""

    def __init__(
        self,
        model_name: str = "bert-base-uncased",
        revision: str | None = None,
        metadata_dimension: int = 6,
        num_labels: int = 4,
        dropout: float = 0.1,
        encoder: Any = None,
    ) -> None:
        require_torch()
        super().__init__()
        if encoder is None:
            require_transformers()
            arguments = {"revision": revision} if revision else {}
            encoder = AutoModel.from_pretrained(model_name, **arguments)
        self.bert = encoder
        hidden_size = int(self.bert.config.hidden_size)
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_size + metadata_dimension, num_labels)

    def forward(
        self,
        input_ids: Any,
        attention_mask: Any,
        metadata: Any,
        token_type_ids: Any = None,
        labels: Any = None,
        class_weights: Any = None,
    ) -> dict[str, Any]:
        encoder_arguments = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
        }
        if token_type_ids is not None:
            encoder_arguments["token_type_ids"] = token_type_ids
        outputs = self.bert(**encoder_arguments)
        pooled = getattr(outputs, "pooler_output", None)
        if pooled is None:
            pooled = outputs.last_hidden_state[:, 0, :]
        combined = torch.cat((pooled, metadata.float()), dim=1)
        logits = self.classifier(self.dropout(combined))

        loss = None
        if labels is not None:
            loss = functional.cross_entropy(
                logits,
                labels,
                weight=class_weights,
            )
        return {"loss": loss, "logits": logits}


@dataclass
class BertTrainingResult:
    model: BertMetadataClassifier
    tokenizer: Any
    metadata_scaler: MetadataScaler
    best_epoch: int
    history: list[dict[str, float]]
    settings: dict[str, Any]


def calculate_class_weights(labels: pd.Series, num_labels: int = 4) -> Any:
    """Return balanced weights for labels encoded as 1 through 4."""
    require_torch()
    numeric = pd.to_numeric(labels, errors="coerce").to_numpy(dtype=float)
    if (
        numeric.ndim != 1
        or numeric.size == 0
        or not np.isfinite(numeric).all()
        or not np.equal(numeric, np.floor(numeric)).all()
    ):
        raise ValueError("BERT labels must be finite whole numbers.")
    integral = numeric.astype(np.int64)
    if not set(np.unique(integral)).issubset(range(1, num_labels + 1)):
        raise ValueError("BERT labels fall outside the configured label range.")
    zero_based = integral - 1
    counts = np.bincount(zero_based, minlength=num_labels)
    if np.any(counts == 0):
        raise ValueError("Every class must occur in the current training rows.")
    weights = len(zero_based) / (num_labels * counts)
    return torch.tensor(weights, dtype=torch.float32)


def resolve_device(requested: str | None = None) -> Any:
    require_torch()
    if requested:
        return torch.device(requested)
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _make_loader(
    data: pd.DataFrame,
    tokenizer: Any,
    metadata: np.ndarray,
    max_length: int,
    batch_size: int,
    include_labels: bool,
    shuffle: bool,
    text_columns: tuple[str, ...] = ("title", "transcript"),
) -> Any:
    dataset = BertVideoDataset(
        data=data,
        tokenizer=tokenizer,
        metadata=metadata,
        max_length=max_length,
        include_labels=include_labels,
        text_columns=text_columns,
    )
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)


def _model_inputs(batch: dict[str, Any], device: Any) -> dict[str, Any]:
    keys = {"input_ids", "attention_mask", "token_type_ids", "metadata", "labels"}
    return {
        key: value.to(device)
        for key, value in batch.items()
        if key in keys
    }


def _require_finite_logits(logits: Any) -> None:
    if not bool(torch.isfinite(logits).all()):
        raise FloatingPointError("BERT produced non-finite logits; predictions are invalid.")


def _weighted_loss_parts(loss: Any, labels: Any, class_weights: Any) -> tuple[float, float]:
    """Recover the weighted loss numerator and its true reduction denominator."""
    value = float(loss.detach().item())
    if not np.isfinite(value):
        raise FloatingPointError("BERT produced non-finite loss; training cannot continue.")
    denominator = (
        float(labels.numel()) if class_weights is None
        else float(class_weights[labels].detach().double().sum().item())
    )
    if not np.isfinite(denominator) or denominator <= 0:
        raise ValueError("BERT weighted loss requires a positive finite denominator.")
    return value * denominator, denominator


def _validation_predictions(
    model: BertMetadataClassifier,
    loader: Any,
    device: Any,
    class_weights: Any,
) -> tuple[np.ndarray, np.ndarray, float]:
    model.eval()
    labels: list[int] = []
    predictions: list[int] = []
    loss_sum = loss_weight = 0.0
    with torch.no_grad():
        for batch in loader:
            arguments = _model_inputs(batch, device)
            output = model(**arguments, class_weights=class_weights)
            _require_finite_logits(output["logits"])
            numerator, denominator = _weighted_loss_parts(
                output["loss"], arguments["labels"], class_weights
            )
            loss_sum += numerator
            loss_weight += denominator
            labels.extend((arguments["labels"] + 1).cpu().tolist())
            predictions.extend((output["logits"].argmax(dim=1) + 1).cpu().tolist())
    return (
        np.asarray(labels, dtype=int),
        np.asarray(predictions, dtype=int),
        loss_sum / loss_weight,
    )


def train_bert_model(
    train_data: pd.DataFrame,
    validation_data: pd.DataFrame | None,
    settings: dict[str, Any],
    fixed_epochs: int | None = None,
    output_directory: str | Path | None = None,
    tokenizer: Any = None,
    encoder: Any = None,
    device: str | None = None,
) -> BertTrainingResult:
    """Train with early stopping, or for fixed epochs when validation is absent."""
    require_torch()
    settings = dict(settings)
    if tokenizer is None or encoder is None:
        settings = resolve_bert_settings(settings)
    if int(settings.get("num_labels", 4)) != 4:
        raise ValueError("The thesis BERT condition requires exactly four labels.")
    if int(settings.get("max_length", 0)) < 2:
        raise ValueError("BERT max_length must be at least two tokens.")
    if int(settings.get("batch_size", 0)) < 1:
        raise ValueError("BERT batch_size must be positive.")
    if fixed_epochs is not None and int(fixed_epochs) < 1:
        raise ValueError("fixed_epochs must be positive when supplied.")
    if validation_data is not None and validation_data.empty:
        raise ValueError("BERT validation_data cannot be empty.")
    if tokenizer is None:
        require_transformers()
        tokenizer_arguments = (
            {"revision": settings["resolved_revision"]}
            if settings.get("resolved_revision")
            else {}
        )
        tokenizer = AutoTokenizer.from_pretrained(
            settings["model_name"],
            **tokenizer_arguments,
        )

    seed = int(settings.get("seed", 42))
    set_random_seed(seed)
    active_device = resolve_device(device)

    lexicons = settings.get("linguistic_lexicons", {})
    certainty_terms = tuple(
        lexicons.get("certainty_terms", DEFAULT_CERTAINTY_TERMS)
    )
    hedge_terms = tuple(lexicons.get("hedge_terms", DEFAULT_HEDGE_TERMS))
    text_columns = tuple(settings.get("text_columns", ("title", "transcript")))
    engagement_transform = str(settings.get("engagement_transform", "log1p"))
    platform_column = str(settings.get("platform_column", "platform"))
    scaler = MetadataScaler(
        certainty_terms,
        hedge_terms,
        text_columns=text_columns,
        engagement_transform=engagement_transform,
        platform_column=platform_column,
    ).fit(train_data)
    train_metadata = scaler.transform(train_data)
    train_loader = _make_loader(
        train_data,
        tokenizer,
        train_metadata,
        int(settings["max_length"]),
        int(settings["batch_size"]),
        include_labels=True,
        shuffle=True,
        text_columns=text_columns,
    )

    validation_loader = None
    if validation_data is not None:
        validation_metadata = scaler.transform(validation_data)
        validation_loader = _make_loader(
            validation_data,
            tokenizer,
            validation_metadata,
            int(settings["max_length"]),
            int(settings["batch_size"]),
            include_labels=True,
            shuffle=False,
            text_columns=text_columns,
        )

    model = BertMetadataClassifier(
        model_name=settings["model_name"],
        revision=settings.get("resolved_revision") or settings.get("revision"),
        metadata_dimension=len(scaler.get_feature_names_out()),
        num_labels=int(settings.get("num_labels", 4)),
        dropout=float(settings.get("dropout", 0.1)),
        encoder=encoder,
    ).to(active_device)
    hidden_size = int(model.bert.config.hidden_size)
    expected_hidden_size = int(settings.get("expected_hidden_size", hidden_size))
    if hidden_size != expected_hidden_size:
        raise ValueError(
            "BERT hidden size does not match the configured checkpoint contract: "
            f"expected {expected_hidden_size}, found {hidden_size}."
        )
    if len(scaler.get_feature_names_out()) != 6:
        raise ValueError("The thesis BERT condition requires six auxiliary features.")
    encoder_revision = getattr(model.bert.config, "_commit_hash", None)
    tokenizer_revision = getattr(tokenizer, "init_kwargs", {}).get("_commit_hash")
    pinned_revision = settings.get("resolved_revision")
    if pinned_revision and any(
        value and value != pinned_revision
        for value in (encoder_revision, tokenizer_revision)
    ):
        raise RuntimeError("BERT checkpoint differs from the pinned revision.")
    if encoder_revision and tokenizer_revision and encoder_revision != tokenizer_revision:
        raise RuntimeError(
            "BERT encoder and tokenizer resolved to different checkpoint revisions."
        )

    class_weights = calculate_class_weights(
        train_data["label"],
        int(settings.get("num_labels", 4)),
    ).to(active_device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(settings["learning_rate"]),
        weight_decay=float(settings.get("weight_decay", 0.01)),
    )

    epoch_limit = int(
        fixed_epochs if fixed_epochs is not None else settings.get("max_epochs", 5)
    )
    if epoch_limit < 1:
        raise ValueError("BERT epoch limit must be positive.")
    total_steps = max(1, epoch_limit * len(train_loader))
    if get_linear_schedule_with_warmup is None:
        scheduler = None
    else:
        warmup_steps = int(total_steps * float(settings.get("warmup_fraction", 0.1)))
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps=total_steps,
        )

    best_score = float("-inf")
    best_epoch = epoch_limit
    best_state = None
    stale_epochs = 0
    patience = int(settings.get("early_stopping_patience", 2))
    if patience < 1:
        raise ValueError("BERT early-stopping patience must be positive.")
    history: list[dict[str, float]] = []

    for epoch in range(1, epoch_limit + 1):
        model.train()
        training_loss_sum = training_loss_weight = 0.0
        for batch in train_loader:
            optimizer.zero_grad(set_to_none=True)
            arguments = _model_inputs(batch, active_device)
            output = model(**arguments, class_weights=class_weights)
            loss = output["loss"]
            _require_finite_logits(output["logits"])
            numerator, denominator = _weighted_loss_parts(
                loss, arguments["labels"], class_weights
            )
            loss.backward()
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                float(settings.get("gradient_clip", 1.0)),
                error_if_nonfinite=True,
            )
            optimizer.step()
            if scheduler is not None:
                scheduler.step()
            training_loss_sum += numerator
            training_loss_weight += denominator

        record = {
            "epoch": float(epoch),
            "training_loss": training_loss_sum / training_loss_weight,
        }
        if validation_loader is not None:
            labels, predictions, validation_loss = _validation_predictions(
                model,
                validation_loader,
                active_device,
                class_weights,
            )
            score = quadratic_weighted_kappa(labels, predictions)
            record["validation_loss"] = validation_loss
            record["validation_qwk"] = score
            if np.isfinite(score) and score > best_score:
                best_score = score
                best_epoch = epoch
                best_state = copy.deepcopy(model.state_dict())
                stale_epochs = 0
            else:
                stale_epochs += 1
                if stale_epochs >= patience:
                    history.append(record)
                    break
        history.append(record)

    if best_state is not None:
        model.load_state_dict(best_state)
    elif validation_loader is not None:
        raise RuntimeError(
            "BERT early stopping produced no finite validation QWK; the fold "
            "cannot be used as a valid model-selection result."
        )

    result = BertTrainingResult(
        model=model,
        tokenizer=tokenizer,
        metadata_scaler=scaler,
        best_epoch=best_epoch,
        history=history,
        settings=dict(settings),
    )
    if output_directory is not None:
        save_bert_artifacts(result, output_directory)
    return result


def predict_bert(
    result: BertTrainingResult,
    data: pd.DataFrame,
    device: str | None = None,
) -> pd.DataFrame:
    """Predict labels and class probabilities while preserving identifiers."""
    require_torch()
    active_device = resolve_device(device)
    model = result.model.to(active_device)
    metadata = result.metadata_scaler.transform(data)
    loader = _make_loader(
        data,
        result.tokenizer,
        metadata,
        int(result.settings["max_length"]),
        int(result.settings["batch_size"]),
        include_labels=False,
        shuffle=False,
        text_columns=tuple(
            result.settings.get("text_columns", ("title", "transcript"))
        ),
    )

    row_indices: list[int] = []
    predictions: list[int] = []
    probabilities: list[list[float]] = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            row_indices.extend(batch["row_index"].cpu().tolist())
            arguments = _model_inputs(batch, active_device)
            output = model(**arguments)
            _require_finite_logits(output["logits"])
            batch_probabilities = torch.softmax(output["logits"], dim=1)
            predictions.extend((batch_probabilities.argmax(dim=1) + 1).cpu().tolist())
            probabilities.extend(batch_probabilities.cpu().tolist())

    frame = pd.DataFrame(
        {
            "row_index": row_indices,
            "prediction": predictions,
        }
    )
    for class_index in range(4):
        frame[f"probability_{class_index + 1}"] = [
            row[class_index] for row in probabilities
        ]
    return frame


def save_bert_artifacts(
    result: BertTrainingResult,
    output_directory: str | Path,
) -> None:
    """Save the trained head, scaler, tokenizer, and training history."""
    require_torch()
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    torch.save(result.model.state_dict(), directory / "model_state.pt")
    joblib.dump(result.metadata_scaler, directory / "metadata_scaler.joblib")
    result.tokenizer.save_pretrained(directory / "tokenizer")
    encoder_config_directory = directory / "encoder_config"
    if not hasattr(result.model.bert.config, "save_pretrained"):
        raise TypeError("BERT encoder configuration cannot be persisted.")
    result.model.bert.config.save_pretrained(encoder_config_directory)
    pd.DataFrame(result.history).to_csv(directory / "training_history.csv", index=False)
    joblib.dump(result.settings, directory / "training_settings.joblib")
    (directory / "training_settings.json").write_text(
        json.dumps(result.settings, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    tokenizer_revision = getattr(result.tokenizer, "init_kwargs", {}).get(
        "_commit_hash"
    )
    encoder_revision = getattr(result.model.bert.config, "_commit_hash", None)
    resolved_encoder_revision = encoder_revision or result.settings.get("resolved_revision")
    resolved_tokenizer_revision = tokenizer_revision or result.settings.get("resolved_revision")
    metadata_dimension = len(result.metadata_scaler.get_feature_names_out())
    hidden_size = int(result.model.bert.config.hidden_size)
    num_labels = int(result.model.classifier.out_features)
    metadata = {
        "model_name": result.settings.get("model_name"),
        "requested_revision": result.settings.get("revision"),
        "encoder_commit_hash": resolved_encoder_revision,
        "tokenizer_commit_hash": resolved_tokenizer_revision,
        "checkpoint_identity_resolved": bool(
            resolved_encoder_revision and resolved_tokenizer_revision
        ),
        "hidden_size": hidden_size,
        "metadata_dimension": metadata_dimension,
        "classifier_input_dimension": int(result.model.classifier.in_features),
        "num_labels": num_labels,
        "maximum_sequence_length": int(result.settings["max_length"]),
        "best_epoch": result.best_epoch,
        "auxiliary_feature_names": result.metadata_scaler.get_feature_names_out().tolist(),
        "auxiliary_feature_count": metadata_dimension,
    }
    (directory / "checkpoint_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )


def load_bert_artifacts(
    input_directory: str | Path,
    device: str | None = None,
) -> BertTrainingResult:
    """Reconstruct a saved BERT condition without downloading mutable files."""
    require_torch()
    require_transformers()
    directory = Path(input_directory)
    settings = json.loads(
        (directory / "training_settings.json").read_text(encoding="utf-8")
    )
    metadata = json.loads(
        (directory / "checkpoint_metadata.json").read_text(encoding="utf-8")
    )
    tokenizer = AutoTokenizer.from_pretrained(
        directory / "tokenizer", local_files_only=True
    )
    encoder_config = AutoConfig.from_pretrained(
        directory / "encoder_config", local_files_only=True
    )
    encoder = AutoModel.from_config(encoder_config)
    scaler = joblib.load(directory / "metadata_scaler.joblib")
    model = BertMetadataClassifier(
        model_name=settings["model_name"],
        revision=metadata.get("encoder_commit_hash"),
        metadata_dimension=int(metadata["metadata_dimension"]),
        num_labels=int(metadata["num_labels"]),
        dropout=float(settings.get("dropout", 0.1)),
        encoder=encoder,
    )
    active_device = resolve_device(device)
    try:
        state = torch.load(
            directory / "model_state.pt",
            map_location=active_device,
            weights_only=True,
        )
    except TypeError:
        state = torch.load(directory / "model_state.pt", map_location=active_device)
    model.load_state_dict(state, strict=True)
    model.to(active_device)
    history_path = directory / "training_history.csv"
    history = pd.read_csv(history_path).to_dict(orient="records")
    return BertTrainingResult(
        model=model,
        tokenizer=tokenizer,
        metadata_scaler=scaler,
        best_epoch=int(metadata["best_epoch"]),
        history=history,
        settings=settings,
    )
