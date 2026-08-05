"""Frozen MiniLM embeddings followed by Logistic Regression."""

from __future__ import annotations

from typing import Any

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
        c_value: float = 1.0,
        batch_size: int = 32,
        max_iter: int = 2000,
        random_state: int = 42,
        device: str | None = None,
        encoder: Any = None,
        certainty_terms: tuple[str, ...] = DEFAULT_CERTAINTY_TERMS,
        hedge_terms: tuple[str, ...] = DEFAULT_HEDGE_TERMS,
    ) -> None:
        self.model_name = model_name
        self.c_value = c_value
        self.batch_size = batch_size
        self.max_iter = max_iter
        self.random_state = random_state
        self.device = device
        self.encoder = encoder
        self.certainty_terms = certainty_terms
        self.hedge_terms = hedge_terms

    def _build_matrix(self, data: pd.DataFrame, fit_scaler: bool) -> np.ndarray:
        active_encoder = self.encoder or load_minilm_encoder(
            self.model_name,
            self.device,
        )
        if fit_scaler:
            first_module = None
            if hasattr(active_encoder, "_first_module"):
                first_module = active_encoder._first_module()
            auto_model = getattr(first_module, "auto_model", None)
            config = getattr(auto_model, "config", None)
            self.model_revision_ = getattr(config, "_commit_hash", None)
        embeddings = encode_minilm(
            data=data,
            model_name=self.model_name,
            batch_size=self.batch_size,
            device=self.device,
            encoder=active_encoder,
        )
        if fit_scaler:
            self.metadata_scaler_ = MetadataScaler(
                self.certainty_terms,
                self.hedge_terms,
            ).fit(data)
        metadata = self.metadata_scaler_.transform(data)
        return np.hstack((embeddings, metadata))

    def fit(
        self,
        data: pd.DataFrame,
        target: object,
    ) -> "FrozenMiniLMClassifier":
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
