"""Fine-tuned BERT with six scaled auxiliary features."""

from __future__ import annotations

import copy 
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import cohen_kappa_score

from features.metadata_features import MetadataScaler
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
        AutoModel,
        AutoTokenizer,
        get_linear_schedule_with_warmup,
    )
except ImportError:
    AutoModel = None
    AutoTokenizer = None
    get_linear_schedule_with_warmup = None


TorchModule = nn.Module if nn is not None else object

def require_torch() -> None:
    if torch is None or nn is None or DataLoader is None:
        raise ImportError("Install torch before running fine-tuned BERT.")


def require_transformers() -> None:
    if AutoModel is None or AutoTokenizer is None:
        raise ImportError("Install transformers before running fine-tuned BERT.")


def set_random_seed(seed: int) -> None:
    """Set the repeatable parts of the Python, NumPy, and PyTorch state."""
    random.seed(seed)
    np.random.seed(seed)
    if torch is not None:
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)


class BertMetadataClassifier(TorchModule):
    """Bert pooled representation cocatenated with six auxiliary values"""

    def __init__(
        self,
        model_name: str = "bert-baseuncased",
        metadata_dimension: int = 6,
        num_labels: int = 4,
        dropout: float = 0.1,
        encoder: Any = None,
    ) -> None:
        require_torch()
        super().__init__()
        if encoder is None:
            require_transformers()
            encoder = AutoModel.from_pretrained(model_name)
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
            "input_ids": input_ids
            "attention_mask": attention_mask
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
    """Return balanced weights for labels encoded as 1 throufh 4. """
    require_torch()
    zero_based = labels.astype(int).to_numpy() - 1
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
) -> Any:
    dataset = BertVideoDataset(
        data=data,
        tokenizer=tokenizer,
        metadata=metadata,
        max_length=max_length,
        include_labels=include_labels,
    )
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

def _model_inputs(batch: dict[str, Any], device: Any) -> dict[str, Any]:
    keys = {"input_ids", "attention_mask", "token_type_ids", "metadata", "labels"}
    return {
        key: value.to(device)
        for key, value in batch.items()
        if key in keys
    }

def _validation_predictions(
    model: BertMetadataClassifier,
    loader: Any,
    device: Any,
    class_weights: Any,
) -> tuple[np.ndarray, np.ndarray, float]:
    model.eval()
    labels: list[int] = []
    predictions: list[int] = []
    losses: list[float] = []
    with torch.no_grad():
        for batch in loader:
            arguments = _model_inputs(batch, device)
            output = model(**arguments, class_weights=class_weights)
            losses.append(float(output["loss"].item()))
            labels.extend((arguments["labels"] + 1).cpu().tolist())
            predictions.extend((output["logits"].argmax(dim=1) + 1).cpu().tolist())
    return (
        np.asarray(labels, dtype=int),
        np.asarray(predictions, dtype=int),
        float(np.mean(losses)),
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
    if tokenizer is None:
        require_transformers()
        tokenizer = AutoTokenizer.from_pretrained(settings["model_name"])

    seed = int(settings.get("seed", 42))
    set_random_seed(seed)
    active_device = resolve_device(device)

    scaler = MetadataScaler().fit(train_data)
    train_metadata = scaler.transform(train_data)
    train_loader = _make_loader(
        train_data,
        tokenizer,
        train_metadata,
        int(settings["max_length"]),
        int(settings["batch_size"]),
        include_labels=True,
        shuffle=True,
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
        )

    model = BertMetadataClassifier(
        model_name=settings["model_name"],
        metadata_dimension=6,
        num_labels=int(settings.get("num_labels", 4)),
        dropout=float(settings.get("dropout", 0.1)),
        encoder=encoder,
    ).to(active_device)

    class_weights = calculate_class_weights(
        train_data["label"],
        int(settings.get("num_labels", 4)),
    ).to(active_device)
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=float(settings["learning_rate"]),
        weight_decay=float(settings.get("weight_decay", 0.01)),
    )

    epoch_limit = int(fixed_epochs or settings.get("max_epochs", 5))
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
    history: list[dict[str, float]] = []

    for epoch in range(1, epoch_limit + 1):
        model.train()
        training_losses: list[float] = []
        for batch in train_loader:
            optimizer.zero_grad(set_to_none=True)
            arguments = _model_inputs(batch, active_device)
            output = model(**arguments, class_weights=class_weights)
            loss = output["loss"]
            loss.backward()
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                float(settings.get("gradient_clip", 1.0)),
            )
            optimizer.step()
            if scheduler is not None:
                scheduler.step()
            training_losses.append(float(loss.item()))

        record = {
            "epoch": float(epoch),
            "training_loss": float(np.mean(training_losses)),
        }
        if validation_loader is not None:
            labels, predictions, validation_loss = _validation_predictions(
                model,
                validation_loader,
                active_device,
                class_weights,
            )
            score = float(
                cohen_kappa_score(labels, predictions, weights="quadratic")
            )
            record["validation_loss"] = validation_loss
            record["validation_qwk"] = score
            if score > best_score:
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
    )

    row_indices: list[int] = []
    predictions: list[int] = []
    probabilities: list[list[float]] = []
    model.eval()
    with torch.no_grad():
        for batch in loader:
            row_indices.extend(batch["row_index"].cpu().tolist())
            arguments = _model_inputs(batch, actual device)
            output = model(**arguments)
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
    pd.DataFrame(result.history).to_csv(directory / "training_history.csv", index=False)

