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


def combine_title_and_transcript(data: pd.DataFrame) -> list[str]:
    """Return stable combined text for sentence embeddings."""
    title = data["title"].fillna("").astype(str)
    transcript = data["transcript"].fillna("").astype(str)
    return (title + " [SEP] " + transcript).tolist()


@lru_cache(maxsize=4)
def load_minilm_encoder(model_name: str, device: str | None = None) -> Any:
    """Load and reuse a frozen Sentence Transformer encoder."""
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise ImportError(
            "Install sentence-transformers to run the frozen MiniLM model."
        ) from exc
    encoder = SentenceTransformer(model_name, device=device)
    return encoder


def encode_minilm(
    data: pd.DataFrame,
    model_name: str,
    batch_size: int = 32,
    device: str | None = None,
    encoder: Any = None,
) -> np.ndarray:
    """Encode title and transcript while keeping the encoder frozen."""
    active_encoder = encoder or load_minilm_encoder(model_name, device)
    texts = combine_title_and_transcript(data)
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
    """Tokenized title/transcript pairs plus scaled auxiliary features."""

    def __init__(
        self,
        data: pd.DataFrame,
        tokenizer: Any,
        metadata: np.ndarray,
        max_length: int,
        include_labels: bool = True,
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

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> dict[str, Any]:
        row = self.data.iloc[index]
        encoded = self.tokenizer(
            str(row.get("title", "")),
            str(row.get("transcript", "")),
            padding="max_length",
            truncation="only_second",
            max_length=self.max_length,
            return_tensors="pt",
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
