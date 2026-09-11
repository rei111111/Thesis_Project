"""Text encoding and dataset helpers for MiniLM and BERT."""

from __future__ import annotations

from functools import lru_cache
from typing import Any

import numpy as np
import pandas as pd

try:
    import torch
    from torch.utils.data import Dataset
except ImportError:  # Allows the classical-model modules to run independently.
    torch = None

    class Dataset:  # type: ignore[no-redef]
        pass


def combine_text_columns(
    data: pd.DataFrame,
    text_columns: tuple[str, ...],
) -> list[str]:
    """Return stable combined text from explicitly selected columns."""
    if not text_columns or len(set(text_columns)) != len(text_columns):
        raise ValueError("text_columns must contain unique column names.")
    missing = [column for column in text_columns if column not in data.columns]
    if missing:
        raise ValueError(f"Selected text columns are missing: {missing}")
    # SentenceTransformer receives one text string. Avoid injecting a literal
    # checkpoint-specific special-token spelling into the natural-language
    # input; BERT's paired tokenizer adds its own true separator separately.
    return data.loc[:, list(text_columns)].fillna("").astype(str).agg(
        " ".join, axis=1
    ).tolist()


def combine_title_and_transcript(data: pd.DataFrame) -> list[str]:
    """Backward-compatible title/transcript input for the YouTube profile."""
    return combine_text_columns(data, ("title", "transcript"))


@lru_cache(maxsize=4)
def load_minilm_encoder(
    model_name: str,
    device: str | None = None,
    revision: str | None = None,
) -> Any:
    """Load and reuse a frozen Sentence Transformer encoder."""
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise ImportError(
            "Install sentence-transformers to run the frozen MiniLM model."
        ) from exc
    arguments: dict[str, Any] = {"device": device}
    if revision:
        arguments["revision"] = revision
    encoder = SentenceTransformer(model_name, **arguments)
    return encoder


def encode_minilm(
    data: pd.DataFrame,
    model_name: str,
    batch_size: int = 32,
    device: str | None = None,
    revision: str | None = None,
    encoder: Any = None,
    text_columns: tuple[str, ...] = ("title", "transcript"),
) -> np.ndarray:
    """Encode the configured text columns while keeping the encoder frozen."""
    active_encoder = (
        encoder
        if encoder is not None
        else load_minilm_encoder(model_name, device, revision)
    )
    texts = combine_text_columns(data, text_columns)
    embeddings = active_encoder.encode(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        show_progress_bar=False,
    )
    values = np.asarray(embeddings, dtype=np.float32)
    if values.ndim != 2:
        raise ValueError("MiniLM must return a two-dimensional embedding matrix.")
    return values


class BertVideoDataset(Dataset):
    """Tokenized configured text plus scaled auxiliary features."""

    def __init__(
        self,
        data: pd.DataFrame,
        tokenizer: Any,
        metadata: np.ndarray,
        max_length: int,
        include_labels: bool = True,
        text_columns: tuple[str, ...] = ("title", "transcript"),
    ) -> None:
        if torch is None:
            raise ImportError("Install torch to create BertVideoDataset.")
        if len(data) != len(metadata):
            raise ValueError("Text rows and metadata rows must remain aligned.")
        self.data = data.reset_index(drop=True)
        self.tokenizer = tokenizer
        self.metadata = np.asarray(metadata, dtype=np.float32)
        self.max_length = max_length
        self.include_labels = include_labels
        if len(text_columns) not in (1, 2) or len(set(text_columns)) != len(
            text_columns
        ):
            raise ValueError("BERT requires one or two unique text columns.")
        missing = [column for column in text_columns if column not in self.data]
        if missing:
            raise ValueError(f"BERT text columns are missing: {missing}")
        self.text_columns = text_columns

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> dict[str, Any]:
        row = self.data.iloc[index]
        texts = [
            "" if pd.isna(row[column]) else str(row[column])
            for column in self.text_columns
        ]
        common = {
            "padding": "max_length",
            "max_length": self.max_length,
            "return_tensors": "pt",
        }
        if len(texts) == 1:
            encoded = self.tokenizer(texts[0], truncation=True, **common)
        else:
            encoded = self.tokenizer(
                texts[0], texts[1], truncation="only_second", **common
            )
        item = {
            key: value.squeeze(0)
            for key, value in encoded.items()
            if key in {"input_ids", "attention_mask", "token_type_ids"}
        }
        item["metadata"] = torch.tensor(self.metadata[index], dtype=torch.float32)
        item["row_index"] = int(row["row_index"])
        if self.include_labels:
            item["labels"] = torch.tensor(int(row["label"]) - 1, dtype=torch.long)
        return item
