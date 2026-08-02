from __future__ import annotations

import unittest
from pathlib import Path

import numpy as np
import pandas as pd

from evaluation.final_evaluation import load_saved_split
from scripts.prepare_data import CSV_COLUMNS, validate_dataset


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def valid_row(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "title": "Example",
        "transcript": "Example transcript",
        "likes": 1,
        "comments": 1,
        "views": 10,
        "duration_sec": 30,
        "total_claims": 5,
        "false_claims": 5,
        "label": 4,
    }
    row.update(overrides)
    return row


class DataTests(unittest.TestCase):
    def test_validation_trusts_author_label_and_claim_counts(self) -> None:
        data = pd.DataFrame([valid_row(label=1, false_claims=5)])
        summary = validate_dataset(data)
        self.assertEqual(summary["modelled_rows"], 1)
        self.assertFalse(summary["author_annotations_recalculated"])

    def test_any_blank_label_is_retained_but_not_modelled(self) -> None:
        data = pd.DataFrame(
            [valid_row(total_claims=5, false_claims=5, label=np.nan)]
        )
        summary = validate_dataset(data)
        self.assertEqual(summary["modelled_rows"], 0)
        self.assertEqual(summary["excluded_unassigned_rows"], 1)

    def test_derived_feature_columns_are_rejected_in_source_csv(self) -> None:
        data = pd.DataFrame([valid_row()])
        data["certainty_score"] = 0.0
        with self.assertRaisesRegex(ValueError, "exactly"):
            validate_dataset(data)

    def test_invalid_model_metadata_is_rejected(self) -> None:
        data = pd.DataFrame([valid_row(views="not a number")])
        with self.assertRaisesRegex(ValueError, "views"):
            validate_dataset(data)

    def test_final_dataset_matches_the_250_video_schema(self) -> None:
        data = pd.read_csv(PROJECT_ROOT / "data/dataset.csv")
        self.assertEqual(tuple(data.columns), CSV_COLUMNS)
        summary = validate_dataset(data, expected_rows=250)
        self.assertEqual(summary["source_rows"], 250)
        self.assertEqual(summary["modelled_rows"], 246)
        self.assertEqual(summary["excluded_unassigned_rows"], 4)
        self.assertEqual(
            summary["class_distribution"],
            {"1": 116, "2": 41, "3": 71, "4": 18},
        )

    def test_saved_split_covers_every_source_row_once(self) -> None:
        data = pd.read_csv(PROJECT_ROOT / "data/dataset.csv")
        train = set(
            pd.read_csv(PROJECT_ROOT / "data/train_indices.csv")["row_index"]
        )
        heldout = set(
            pd.read_csv(PROJECT_ROOT / "data/test_indices.csv")["row_index"]
        )
        excluded = set(
            pd.read_csv(PROJECT_ROOT / "data/excluded_indices.csv")["row_index"]
        )
        self.assertFalse(train & heldout)
        self.assertFalse(train & excluded)
        self.assertFalse(heldout & excluded)
        self.assertEqual(train | heldout | excluded, set(range(len(data))))
        self.assertEqual((len(train), len(heldout), len(excluded)), (196, 50, 4))

    def test_saved_split_loader_recovers_labelled_rows(self) -> None:
        training, heldout = load_saved_split(
            PROJECT_ROOT / "data/dataset.csv",
            PROJECT_ROOT / "data/train_indices.csv",
            PROJECT_ROOT / "data/test_indices.csv",
            PROJECT_ROOT / "data/excluded_indices.csv",
            PROJECT_ROOT / "data/split_manifest.json",
        )
        self.assertEqual((len(training), len(heldout)), (196, 50))
        self.assertFalse(training["label"].isna().any())
        self.assertFalse(heldout["label"].isna().any())


if __name__ == "__main__":
    unittest.main()
