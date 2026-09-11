"""Frozen MiniLM embeddings followed by Logistic Regression."""

from __future__ import annotations

from typing import Any
import re

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.linear_model import LogisticRegression
from sklearn.utils.validation import check_is_fitted

from features.metadata_features import MetadataScaler
from features.linguistic_features import (
    DEFAULT_CERTAINTY_TERMS,
    DEFAULT_HEDGE_TERMS,
)
from features.transformer_features import encode_minilm, load_minilm_encoder


class FrozenMiniLMClassifier(ClassifierMixin, BaseEstimator):
    """Scikit-learn estimator for thesis Configuration D."""

    def __init__(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        revision: str | None = None,
        c_value: float = 1.0,
        batch_size: int = 32,
        expected_embedding_dimension: int = 384,
        expected_max_sequence_length: int = 256,
        max_iter: int = 2000,
        random_state: int = 42,
        device: str | None = None,
        encoder: Any = None,
        certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
        hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
        text_columns: tuple[str, ...] = ("title", "transcript"),
        engagement_transform: str = "log1p",
        platform_column: str = "platform",
    ) -> None:
        self.model_name = model_name
        self.revision = revision
        self.c_value = c_value
        self.batch_size = batch_size
        self.expected_embedding_dimension = expected_embedding_dimension
        self.expected_max_sequence_length = expected_max_sequence_length
        self.max_iter = max_iter
        self.random_state = random_state
        self.device = device
        self.encoder = encoder
        self.certainty_terms = certainty_terms
        self.hedge_terms = hedge_terms
        self.text_columns = text_columns
        self.engagement_transform = engagement_transform
        self.platform_column = platform_column

    def __getstate__(self) -> dict[str, Any]:
        """Exclude lazily loaded Hub objects from persisted sklearn artifacts."""
        state = self.__dict__.copy()
        state.pop("encoder_", None)
        return state

    def _active_encoder(self) -> Any:
        if hasattr(self, "encoder_"):
            return self.encoder_
        if self.encoder is not None:
            active = self.encoder
        else:
            resolved_revision = getattr(self, "model_revision_", None)
            active = load_minilm_encoder(
                self.model_name,
                self.device,
                resolved_revision or self.revision,
            )
        self.encoder_ = active
        return active

    def _build_matrix(self, data: pd.DataFrame, fit_scaler: bool) -> np.ndarray:
        active_encoder = self._active_encoder()
        observed_max_length = getattr(active_encoder, "max_seq_length", None)
        if observed_max_length is None:
            raise ValueError("MiniLM encoder does not expose max_seq_length.")
        if int(observed_max_length) != int(self.expected_max_sequence_length):
            raise ValueError(
                "MiniLM maximum sequence length does not match the configured "
                f"contract: expected {self.expected_max_sequence_length}, "
                f"found {observed_max_length}."
            )
        if fit_scaler:
            self.max_sequence_length_ = int(observed_max_length)
            first_module = None
            if hasattr(active_encoder, "_first_module"):
                first_module = active_encoder._first_module()
            auto_model = getattr(first_module, "auto_model", None)
            config = getattr(auto_model, "config", None)
            self.model_revision_ = (
                getattr(config, "_commit_hash", None) or self.revision
            )
            if (
                isinstance(self.revision, str)
                and re.fullmatch(r"[0-9a-f]{40}", self.revision)
                and self.model_revision_ != self.revision
            ):
                raise RuntimeError("MiniLM resolved a different checkpoint from the requested revision.")
        embeddings = encode_minilm(
            data=data,
            model_name=self.model_name,
            batch_size=self.batch_size,
            device=self.device,
            revision=getattr(self, "model_revision_", None) or self.revision,
            encoder=active_encoder,
            text_columns=self.text_columns,
        )
        if not np.isfinite(embeddings).all():
            raise ValueError("MiniLM returned non-finite embedding values.")
        embedding_dimension = int(embeddings.shape[1])
        if fit_scaler and embedding_dimension != int(
            self.expected_embedding_dimension
        ):
            raise ValueError(
                "MiniLM embedding dimension does not match the configured "
                f"checkpoint contract: expected {self.expected_embedding_dimension}, "
                f"found {embedding_dimension}."
            )
        if not fit_scaler and embedding_dimension != int(self.embedding_dimension_):
            raise ValueError(
                "MiniLM embedding dimension changed after the estimator was fitted."
            )
        if fit_scaler:
            self.metadata_scaler_ = MetadataScaler(
                self.certainty_terms,
                self.hedge_terms,
                text_columns=self.text_columns,
                engagement_transform=self.engagement_transform,
                platform_column=self.platform_column,
            ).fit(data)
        metadata = self.metadata_scaler_.transform(data)
        matrix = np.hstack((embeddings, metadata))
        if not np.isfinite(matrix).all():
            raise ValueError("MiniLM model inputs contain non-finite values.")
        return matrix

    def fit(
        self,
        data: pd.DataFrame,
        target: object,
    ) -> "FrozenMiniLMClassifier":
        # A refit must use the current constructor parameters, including a
        # changed model, revision, device or explicitly supplied encoder.
        for name in tuple(vars(self)):
            if name.endswith("_"):
                delattr(self, name)
        matrix = self._build_matrix(data, fit_scaler=True)
        self.classifier_ = LogisticRegression(
            C=self.c_value,
            class_weight="balanced",
            max_iter=self.max_iter,
            random_state=self.random_state,
        )
        self.classifier_.fit(matrix, target)
        self.classes_ = self.classifier_.classes_
        self.auxiliary_dimension_ = len(
            self.metadata_scaler_.get_feature_names_out()
        )
        self.embedding_dimension_ = matrix.shape[1] - self.auxiliary_dimension_
        return self

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, ("classifier_", "metadata_scaler_"))
        matrix = self._build_matrix(data, fit_scaler=False)
        return self.classifier_.predict(matrix)

    def predict_proba(self, data: pd.DataFrame) -> np.ndarray:
        check_is_fitted(self, ("classifier_", "metadata_scaler_"))
        matrix = self._build_matrix(data, fit_scaler=False)
        return self.classifier_.predict_proba(matrix)


def minilm_parameter_grid(c_values: list[float]) -> dict[str, list[float]]:
    """Return the Logistic Regression search space."""
    return {"c_value": c_values}
