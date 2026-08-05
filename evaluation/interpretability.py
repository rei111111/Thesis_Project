"""Global, fold-stability, rule, and local explanation exports.

Only Configurations A--C are handled here. MiniLM dimensions are unnamed and
fine-tuned BERT is opaque under the approved study design, so neither is
presented as a source of substantive feature associations.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.naive_bayes import ComplementNB
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree


def _normalise_feature_name(name: object) -> tuple[str, str]:
    value = str(name)
    if "__" in value:
        branch, clean = value.split("__", maxsplit=1)
    else:
        branch, clean = "unknown", value
    group = {
        "text": "textual",
        "linguistic": "handcrafted_linguistic",
        "engagement": "engagement_or_format",
    }.get(branch, branch)
    return clean, group


def feature_names(estimator: Any) -> tuple[np.ndarray, np.ndarray]:
    """Return clean feature names and their substantive groups."""
    if not hasattr(estimator, "named_steps") or "features" not in estimator.named_steps:
        raise TypeError("Interpretability export requires a fitted feature pipeline.")
    raw = estimator.named_steps["features"].get_feature_names_out()
    parsed = [_normalise_feature_name(value) for value in raw]
    return (
        np.asarray([value[0] for value in parsed], dtype=object),
        np.asarray([value[1] for value in parsed], dtype=object),
    )


def _classifier(estimator: Any) -> Any:
    try:
        return estimator.named_steps["classifier"]
    except (AttributeError, KeyError) as exc:
        raise TypeError("Expected a fitted Pipeline with a classifier step.") from exc


def extract_global_features(
    estimator: Any,
    condition: str,
    fold: int | None = None,
) -> pd.DataFrame:
    """Export every fitted named weight or global tree importance."""
    names, groups = feature_names(estimator)
    classifier = _classifier(estimator)
    common = {
        "condition": condition,
        "fold": fold if fold is not None else "final_training_fit",
    }
    rows: list[dict[str, object]] = []

    if isinstance(classifier, DecisionTreeClassifier):
        for index, (name, group, weight) in enumerate(
            zip(names, groups, classifier.feature_importances_, strict=True)
        ):
            rows.append(
                {
                    **common,
                    "class_label": "all",
                    "feature_index": index,
                    "feature": name,
                    "feature_group": group,
                    "weight_type": "gini_importance",
                    "weight": float(weight),
                }
            )
    elif isinstance(classifier, ComplementNB):
        for class_index, class_label in enumerate(classifier.classes_):
            for index, (name, group, weight) in enumerate(
                zip(
                    names,
                    groups,
                    classifier.feature_log_prob_[class_index],
                    strict=True,
                )
            ):
                rows.append(
                    {
                        **common,
                        "class_label": int(class_label),
                        "feature_index": index,
                        "feature": name,
                        "feature_group": group,
                        "weight_type": "complement_log_weight",
                        "weight": float(weight),
                    }
                )
    elif hasattr(classifier, "coef_"):
        coefficients = np.asarray(classifier.coef_, dtype=float)
        classes = np.asarray(classifier.classes_)
        if coefficients.ndim != 2 or coefficients.shape[1] != len(names):
            raise ValueError("Classifier coefficients do not align with features.")
        if coefficients.shape[0] != len(classes):
            raise ValueError("Classifier coefficients do not align with classes.")
        for class_index, class_label in enumerate(classes):
            for index, (name, group, weight) in enumerate(
                zip(names, groups, coefficients[class_index], strict=True)
            ):
                rows.append(
                    {
                        **common,
                        "class_label": int(class_label),
                        "feature_index": index,
                        "feature": name,
                        "feature_group": group,
                        "weight_type": "coefficient",
                        "weight": float(weight),
                    }
                )
    else:
        raise TypeError(f"Unsupported interpretable classifier: {type(classifier)}")

    frame = pd.DataFrame(rows)
    frame["absolute_weight"] = frame["weight"].abs()
    frame["direction"] = np.select(
        [frame["weight"] > 0, frame["weight"] < 0],
        ["positive", "negative"],
        default="zero",
    )
    frame["absolute_rank"] = (
        frame.groupby("class_label", dropna=False)["absolute_weight"]
        .rank(method="min", ascending=False)
        .astype(int)
    )
    frame["positive_rank"] = (
        frame.groupby("class_label", dropna=False)["weight"]
        .rank(method="min", ascending=False)
        .astype(int)
    )
    frame["negative_rank"] = (
        frame.groupby("class_label", dropna=False)["weight"]
        .rank(method="min", ascending=True)
        .astype(int)
    )
    return frame.sort_values(
        ["class_label", "absolute_rank", "feature"],
        kind="stable",
    ).reset_index(drop=True)


def select_top_features(frame: pd.DataFrame, top_k: int) -> pd.DataFrame:
    """Select transparent top-weight views without discarding the full table."""
    if top_k < 1:
        raise ValueError("top_k must be positive.")
    output: list[pd.DataFrame] = []
    for _, group in frame.groupby("class_label", dropna=False, sort=False):
        weight_type = str(group["weight_type"].iloc[0])
        if weight_type == "coefficient":
            positive = group.nsmallest(top_k, "positive_rank").copy()
            positive["ranking_view"] = "largest_positive"
            negative = group.nsmallest(top_k, "negative_rank").copy()
            negative["ranking_view"] = "largest_negative"
            output.extend([positive, negative])
        else:
            strongest = group.nsmallest(top_k, "absolute_rank").copy()
            strongest["ranking_view"] = "strongest_weight"
            output.append(strongest)
    return pd.concat(output, ignore_index=True) if output else frame.iloc[0:0]


def extract_intercepts(estimator: Any, condition: str) -> pd.DataFrame:
    classifier = _classifier(estimator)
    if not hasattr(classifier, "intercept_"):
        return pd.DataFrame(columns=["condition", "class_label", "intercept"])
    return pd.DataFrame(
        {
            "condition": condition,
            "class_label": np.asarray(classifier.classes_, dtype=int),
            "intercept": np.asarray(classifier.intercept_, dtype=float),
        }
    )


def aggregate_fold_stability(
    fold_features: pd.DataFrame,
    fold_count: int,
    top_k: int,
) -> pd.DataFrame:
    """Aggregate fold weights while treating absent fold vocabulary as zero."""
    if fold_count < 2:
        raise ValueError("At least two fitted folds are required for stability.")
    if fold_features.empty:
        return fold_features.copy()
    key_columns = [
        "condition",
        "class_label",
        "feature",
        "feature_group",
        "weight_type",
    ]
    unique_keys = fold_features[key_columns].drop_duplicates().copy()
    folds = pd.DataFrame({"fold": np.arange(1, fold_count + 1, dtype=int)})
    unique_keys["_join"] = 1
    folds["_join"] = 1
    complete = unique_keys.merge(folds, on="_join").drop(columns="_join")
    values = fold_features[key_columns + ["fold", "weight", "absolute_rank"]]
    complete = complete.merge(
        values,
        on=key_columns + ["fold"],
        how="left",
        validate="one_to_one",
    )
    complete["present"] = complete["weight"].notna()
    complete["in_fold_top_k"] = complete["absolute_rank"].le(top_k).fillna(False)
    complete["weight"] = complete["weight"].fillna(0.0)
    complete["absolute_weight"] = complete["weight"].abs()
    complete["positive"] = complete["weight"].gt(0)
    complete["negative"] = complete["weight"].lt(0)

    rows: list[dict[str, object]] = []
    for key, group in complete.groupby(key_columns, dropna=False, sort=False):
        nonzero = int((group["weight"] != 0).sum())
        positive = int(group["positive"].sum())
        negative = int(group["negative"].sum())
        sign_consistency = (
            float(max(positive, negative) / nonzero) if nonzero else 0.0
        )
        rows.append(
            {
                **dict(zip(key_columns, key, strict=True)),
                "mean_weight_missing_as_zero": float(group["weight"].mean()),
                "sample_std_weight_missing_as_zero": float(group["weight"].std(ddof=1)),
                "median_weight_missing_as_zero": float(group["weight"].median()),
                "mean_absolute_weight_missing_as_zero": float(
                    group["absolute_weight"].mean()
                ),
                "minimum_weight": float(group["weight"].min()),
                "maximum_weight": float(group["weight"].max()),
                "fold_presence_count": int(group["present"].sum()),
                "fold_presence_fraction": float(group["present"].mean()),
                "nonzero_fold_count": nonzero,
                "positive_fold_fraction": float(positive / fold_count),
                "negative_fold_fraction": float(negative / fold_count),
                "sign_consistency_nonzero": sign_consistency,
                "top_k_fold_count": int(group["in_fold_top_k"].sum()),
                "top_k_fold_fraction": float(group["in_fold_top_k"].mean()),
            }
        )
    result = pd.DataFrame(rows)
    return result.sort_values(
        ["class_label", "top_k_fold_fraction", "mean_absolute_weight_missing_as_zero"],
        ascending=[True, False, False],
        kind="stable",
    ).reset_index(drop=True)


def tree_rule_text(estimator: Any) -> str:
    classifier = _classifier(estimator)
    if not isinstance(classifier, DecisionTreeClassifier):
        raise TypeError("Readable rules are available only for Decision Trees.")
    names, _ = feature_names(estimator)
    return export_text(
        classifier,
        feature_names=list(names),
        decimals=5,
        show_weights=True,
    )


def _tree_depths(classifier: DecisionTreeClassifier) -> np.ndarray:
    tree = classifier.tree_
    depths = np.zeros(tree.node_count, dtype=int)
    stack = [(0, 0)]
    while stack:
        node, depth = stack.pop()
        depths[node] = depth
        left = tree.children_left[node]
        right = tree.children_right[node]
        if left != right:
            stack.append((left, depth + 1))
            stack.append((right, depth + 1))
    return depths


def tree_node_table(estimator: Any, condition: str) -> pd.DataFrame:
    classifier = _classifier(estimator)
    if not isinstance(classifier, DecisionTreeClassifier):
        raise TypeError("Node export is available only for Decision Trees.")
    names, groups = feature_names(estimator)
    tree = classifier.tree_
    depths = _tree_depths(classifier)
    rows: list[dict[str, object]] = []
    for node in range(tree.node_count):
        feature_index = int(tree.feature[node])
        is_leaf = tree.children_left[node] == tree.children_right[node]
        class_weights = np.asarray(tree.value[node]).reshape(-1)
        predicted_index = int(np.argmax(class_weights))
        rows.append(
            {
                "condition": condition,
                "node_id": node,
                "depth": int(depths[node]),
                "is_leaf": bool(is_leaf),
                "feature_index": None if is_leaf else feature_index,
                "feature": None if is_leaf else str(names[feature_index]),
                "feature_group": None if is_leaf else str(groups[feature_index]),
                "threshold": None if is_leaf else float(tree.threshold[node]),
                "left_child": None if is_leaf else int(tree.children_left[node]),
                "right_child": None if is_leaf else int(tree.children_right[node]),
                "impurity": float(tree.impurity[node]),
                "weighted_samples": float(tree.weighted_n_node_samples[node]),
                "predicted_class": int(classifier.classes_[predicted_index]),
                "class_weights": "|".join(f"{value:.8g}" for value in class_weights),
            }
        )
    return pd.DataFrame(rows)


def _transformed_matrix(estimator: Any, data: pd.DataFrame) -> object:
    matrix = estimator.named_steps["features"].transform(data)
    if "nonnegative" in estimator.named_steps:
        matrix = estimator.named_steps["nonnegative"].transform(matrix)
    return matrix


def local_linear_contributions(
    estimator: Any,
    data: pd.DataFrame,
    condition: str,
    top_k: int,
) -> pd.DataFrame:
    """Export top named contributions for each predicted held-out class."""
    classifier = _classifier(estimator)
    if isinstance(classifier, DecisionTreeClassifier) or not (
        hasattr(classifier, "coef_") or isinstance(classifier, ComplementNB)
    ):
        raise TypeError("Linear contribution export needs LR, Ridge, or CNB.")
    names, groups = feature_names(estimator)
    matrix = _transformed_matrix(estimator, data.drop(columns=["label"], errors="ignore"))
    predictions = np.asarray(
        estimator.predict(data.drop(columns=["label"], errors="ignore")),
        dtype=int,
    )
    if isinstance(classifier, ComplementNB):
        weights = np.asarray(classifier.feature_log_prob_, dtype=float)
        weight_type = "input_times_complement_log_weight"
    else:
        weights = np.asarray(classifier.coef_, dtype=float)
        weight_type = "input_times_coefficient"
    class_to_index = {
        int(class_label): index for index, class_label in enumerate(classifier.classes_)
    }
    rows: list[dict[str, object]] = []
    row_indices = (
        data["row_index"].astype(int).to_numpy()
        if "row_index" in data.columns
        else np.arange(len(data), dtype=int)
    )
    for position, (row_index, prediction) in enumerate(
        zip(row_indices, predictions, strict=True)
    ):
        values = (
            matrix.getrow(position).toarray().ravel()
            if sparse.issparse(matrix)
            else np.asarray(matrix[position]).ravel()
        )
        class_index = class_to_index[int(prediction)]
        contributions = values * weights[class_index]
        candidates = np.flatnonzero(values)
        if len(candidates) == 0:
            continue
        order = candidates[np.argsort(np.abs(contributions[candidates]))[::-1]][:top_k]
        for rank, feature_index in enumerate(order, start=1):
            rows.append(
                {
                    "condition": condition,
                    "row_index": int(row_index),
                    "predicted_class": int(prediction),
                    "rank": rank,
                    "feature": str(names[feature_index]),
                    "feature_group": str(groups[feature_index]),
                    "transformed_value": float(values[feature_index]),
                    "model_weight": float(weights[class_index, feature_index]),
                    "contribution": float(contributions[feature_index]),
                    "contribution_type": weight_type,
                }
            )
    return pd.DataFrame(rows)


def local_tree_paths(
    estimator: Any,
    data: pd.DataFrame,
    condition: str,
) -> pd.DataFrame:
    """Export the exact named rule path followed by every held-out row."""
    classifier = _classifier(estimator)
    if not isinstance(classifier, DecisionTreeClassifier):
        raise TypeError("Tree paths require a Decision Tree estimator.")
    names, groups = feature_names(estimator)
    predictors = data.drop(columns=["label"], errors="ignore")
    matrix = _transformed_matrix(estimator, predictors)
    paths = classifier.decision_path(matrix)
    leaves = classifier.apply(matrix)
    predictions = classifier.predict(matrix)
    depths = _tree_depths(classifier)
    row_indices = (
        data["row_index"].astype(int).to_numpy()
        if "row_index" in data.columns
        else np.arange(len(data), dtype=int)
    )
    rows: list[dict[str, object]] = []
    for position, row_index in enumerate(row_indices):
        start, stop = paths.indptr[position], paths.indptr[position + 1]
        for node in paths.indices[start:stop]:
            if node == leaves[position]:
                rows.append(
                    {
                        "condition": condition,
                        "row_index": int(row_index),
                        "predicted_class": int(predictions[position]),
                        "node_id": int(node),
                        "depth": int(depths[node]),
                        "is_leaf": True,
                        "feature": None,
                        "feature_group": None,
                        "transformed_value": None,
                        "operator": "leaf",
                        "threshold": None,
                    }
                )
                continue
            feature_index = int(classifier.tree_.feature[node])
            value = float(matrix[position, feature_index])
            threshold = float(classifier.tree_.threshold[node])
            rows.append(
                {
                    "condition": condition,
                    "row_index": int(row_index),
                    "predicted_class": int(predictions[position]),
                    "node_id": int(node),
                    "depth": int(depths[node]),
                    "is_leaf": False,
                    "feature": str(names[feature_index]),
                    "feature_group": str(groups[feature_index]),
                    "transformed_value": value,
                    "operator": "<=" if value <= threshold else ">",
                    "threshold": threshold,
                }
            )
    return pd.DataFrame(rows)


def save_tree_figure(
    estimator: Any,
    condition: str,
    output_path: str | Path,
) -> None:
    classifier = _classifier(estimator)
    if not isinstance(classifier, DecisionTreeClassifier):
        raise TypeError("Tree figure requires a Decision Tree estimator.")
    names, _ = feature_names(estimator)
    figure, axis = plt.subplots(figsize=(26, 14))
    plot_tree(
        classifier,
        feature_names=list(names),
        class_names=[str(value) for value in classifier.classes_],
        filled=True,
        rounded=True,
        impurity=True,
        proportion=True,
        fontsize=7,
        ax=axis,
    )
    axis.set_title(condition)
    figure.tight_layout()
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(figure)


def save_interpretability_artifacts(
    final_estimator: Any,
    fold_estimators: list[Any],
    heldout_data: pd.DataFrame,
    condition: str,
    output_directory: str | Path,
    top_k: int = 20,
    local_top_k: int = 10,
) -> dict[str, int]:
    """Persist all interpretability evidence for one A--C condition."""
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    global_frame = extract_global_features(final_estimator, condition)
    global_frame.to_csv(directory / f"{condition}_all_features.csv", index=False)
    top_frame = select_top_features(global_frame, top_k)
    top_frame.to_csv(directory / f"{condition}_top_features.csv", index=False)
    intercepts = extract_intercepts(final_estimator, condition)
    if not intercepts.empty:
        intercepts.to_csv(directory / f"{condition}_intercepts.csv", index=False)

    fold_frames = [
        extract_global_features(estimator, condition, fold=fold)
        for fold, estimator in enumerate(fold_estimators, start=1)
    ]
    fold_features = pd.concat(fold_frames, ignore_index=True)
    fold_features.to_csv(directory / f"{condition}_fold_features.csv", index=False)
    stability = aggregate_fold_stability(fold_features, len(fold_estimators), top_k)
    stability.to_csv(directory / f"{condition}_feature_stability.csv", index=False)

    classifier = _classifier(final_estimator)
    if isinstance(classifier, DecisionTreeClassifier):
        (directory / f"{condition}_rules.txt").write_text(
            tree_rule_text(final_estimator),
            encoding="utf-8",
        )
        nodes = tree_node_table(final_estimator, condition)
        nodes.to_csv(directory / f"{condition}_nodes.csv", index=False)
        paths = local_tree_paths(final_estimator, heldout_data, condition)
        paths.to_csv(directory / f"{condition}_heldout_paths.csv", index=False)
        save_tree_figure(
            final_estimator,
            condition,
            directory / f"{condition}_tree.png",
        )
        local_rows = len(paths)
    else:
        local = local_linear_contributions(
            final_estimator,
            heldout_data,
            condition,
            top_k=local_top_k,
        )
        local.to_csv(
            directory / f"{condition}_heldout_contributions.csv",
            index=False,
        )
        local_rows = len(local)

    return {
        "global_feature_rows": len(global_frame),
        "top_feature_rows": len(top_frame),
        "fold_feature_rows": len(fold_features),
        "stability_rows": len(stability),
        "local_explanation_rows": local_rows,
    }


def extract_minilm_auxiliary_features(
    estimator: Any,
    condition: str = "D_FROZEN_MINILM",
    fold: int | None = None,
) -> pd.DataFrame:
    """Export only MiniLM's six named auxiliary coefficients.

    The preceding embedding dimensions remain intentionally absent because
    they have no direct linguistic interpretation.
    """
    required = ("classifier_", "metadata_scaler_", "embedding_dimension_")
    if any(not hasattr(estimator, attribute) for attribute in required):
        raise TypeError("Expected a fitted FrozenMiniLMClassifier.")
    names = estimator.metadata_scaler_.get_feature_names_out()
    coefficients = np.asarray(estimator.classifier_.coef_, dtype=float)
    auxiliary = coefficients[:, int(estimator.embedding_dimension_) :]
    if auxiliary.shape[1] != len(names):
        raise ValueError("MiniLM auxiliary coefficients do not align with names.")
    rows: list[dict[str, object]] = []
    for class_index, class_label in enumerate(estimator.classifier_.classes_):
        for feature_index, (name, weight) in enumerate(
            zip(names, auxiliary[class_index], strict=True)
        ):
            rows.append(
                {
                    "condition": condition,
                    "fold": fold if fold is not None else "final_training_fit",
                    "class_label": int(class_label),
                    "feature_index": int(estimator.embedding_dimension_)
                    + feature_index,
                    "feature": str(name),
                    "feature_group": (
                        "handcrafted_linguistic"
                        if str(name) in {"certainty_score", "hedge_score"}
                        else "engagement_or_format"
                    ),
                    "weight_type": "auxiliary_coefficient",
                    "weight": float(weight),
                }
            )
    frame = pd.DataFrame(rows)
    frame["absolute_weight"] = frame["weight"].abs()
    frame["direction"] = np.select(
        [frame["weight"] > 0, frame["weight"] < 0],
        ["positive", "negative"],
        default="zero",
    )
    frame["absolute_rank"] = (
        frame.groupby("class_label")["absolute_weight"]
        .rank(method="min", ascending=False)
        .astype(int)
    )
    frame["positive_rank"] = (
        frame.groupby("class_label")["weight"]
        .rank(method="min", ascending=False)
        .astype(int)
    )
    frame["negative_rank"] = (
        frame.groupby("class_label")["weight"]
        .rank(method="min", ascending=True)
        .astype(int)
    )
    return frame.sort_values(["class_label", "absolute_rank"]).reset_index(drop=True)


def local_minilm_auxiliary_contributions(
    estimator: Any,
    data: pd.DataFrame,
    condition: str = "D_FROZEN_MINILM",
) -> pd.DataFrame:
    """Explain the named auxiliary portion without interpreting embeddings."""
    names = estimator.metadata_scaler_.get_feature_names_out()
    values = estimator.metadata_scaler_.transform(data)
    auxiliary = np.asarray(estimator.classifier_.coef_, dtype=float)[
        :, int(estimator.embedding_dimension_) :
    ]
    predictions = estimator.predict(data)
    class_to_index = {
        int(class_label): index
        for index, class_label in enumerate(estimator.classifier_.classes_)
    }
    row_indices = (
        data["row_index"].astype(int).to_numpy()
        if "row_index" in data.columns
        else np.arange(len(data), dtype=int)
    )
    rows: list[dict[str, object]] = []
    for position, (row_index, prediction) in enumerate(
        zip(row_indices, predictions, strict=True)
    ):
        class_index = class_to_index[int(prediction)]
        contributions = values[position] * auxiliary[class_index]
        order = np.argsort(np.abs(contributions))[::-1]
        for rank, feature_index in enumerate(order, start=1):
            rows.append(
                {
                    "condition": condition,
                    "row_index": int(row_index),
                    "predicted_class": int(prediction),
                    "rank": rank,
                    "feature": str(names[feature_index]),
                    "feature_group": (
                        "handcrafted_linguistic"
                        if str(names[feature_index])
                        in {"certainty_score", "hedge_score"}
                        else "engagement_or_format"
                    ),
                    "transformed_value": float(values[position, feature_index]),
                    "model_weight": float(auxiliary[class_index, feature_index]),
                    "contribution": float(contributions[feature_index]),
                    "contribution_type": "named_auxiliary_only",
                }
            )
    return pd.DataFrame(rows)


def save_minilm_auxiliary_artifacts(
    final_estimator: Any,
    fold_estimators: list[Any],
    heldout_data: pd.DataFrame,
    output_directory: str | Path,
) -> dict[str, int]:
    directory = Path(output_directory)
    directory.mkdir(parents=True, exist_ok=True)
    condition = "D_FROZEN_MINILM"
    final_features = extract_minilm_auxiliary_features(final_estimator)
    final_features.to_csv(
        directory / f"{condition}_named_auxiliary_features.csv",
        index=False,
    )
    fold_features = pd.concat(
        [
            extract_minilm_auxiliary_features(estimator, fold=fold)
            for fold, estimator in enumerate(fold_estimators, start=1)
        ],
        ignore_index=True,
    )
    fold_features.to_csv(
        directory / f"{condition}_named_auxiliary_fold_features.csv",
        index=False,
    )
    stability = aggregate_fold_stability(
        fold_features,
        fold_count=len(fold_estimators),
        top_k=len(final_estimator.metadata_scaler_.get_feature_names_out()),
    )
    stability.to_csv(
        directory / f"{condition}_named_auxiliary_stability.csv",
        index=False,
    )
    local = local_minilm_auxiliary_contributions(final_estimator, heldout_data)
    local.to_csv(
        directory / f"{condition}_heldout_named_auxiliary_contributions.csv",
        index=False,
    )
    return {
        "named_auxiliary_feature_rows": len(final_features),
        "named_auxiliary_fold_rows": len(fold_features),
        "named_auxiliary_stability_rows": len(stability),
        "named_auxiliary_local_rows": len(local),
        "unnamed_embedding_dimensions_excluded": int(
            final_estimator.embedding_dimension_
        ),
    }
