from __future__ import annotations

import unittest
import json
from pathlib import Path

import numpy as np
import pandas as pd

from features.content_groups import content_group_ids
from scripts.prepare_data import (
    CSV_COLUMNS,
    label_from_claims,
    validate_dataset,
)


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
    def test_label_boundaries(self) -> None:
        calculated = label_from_claims(
            np.full(6, 100),
            np.asarray([20, 21, 40, 41, 84, 85]),
        )
        np.testing.assert_array_equal(calculated, [1, 2, 2, 3, 3, 4])

    def test_validation_rejects_inconsistent_label(self) -> None:
        data = pd.DataFrame([valid_row(label=1)])
        with self.assertRaisesRegex(ValueError, "claim counts"):
            validate_dataset(data)

    def test_unassigned_rows_require_fewer_than_two_claims(self) -> None:
        data = pd.DataFrame(
            [
                valid_row(total_claims=0, false_claims=0, label=np.nan),
                valid_row(
                    title="One claim",
                    transcript="A different transcript",
                    total_claims=1,
                    false_claims=1,
                    label=np.nan,
                ),
            ]
        )
        summary = validate_dataset(data)
        self.assertEqual(summary["modelled_rows"], 0)
        self.assertEqual(summary["excluded_unassigned_rows"], 2)

    def test_derived_feature_columns_are_rejected_in_source_csv(self) -> None:
        data = pd.DataFrame([valid_row()])
        data["certainty_score"] = 0.0
        with self.assertRaisesRegex(ValueError, "exactly"):
            validate_dataset(data)

    def test_removed_identifier_and_grouping_columns_are_rejected(self) -> None:
        for column in ("video_id", "platform"):
            data = pd.DataFrame([valid_row()])
            data[column] = "not part of the source schema"
            with self.assertRaisesRegex(ValueError, "exactly"):
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

    def test_frozen_split_keeps_duplicate_content_together(self) -> None:
        data = pd.read_csv(PROJECT_ROOT / "data/dataset.csv")
        train = set(
            pd.read_csv(PROJECT_ROOT / "data/train_indices.csv")["row_index"]
        )
        heldout = set(
            pd.read_csv(PROJECT_ROOT / "data/test_indices.csv")["row_index"]
        )
        groups = content_group_ids(data)
        duplicate_rows = pd.Series(groups).groupby(groups).groups
        duplicated = [set(rows) for rows in duplicate_rows.values() if len(rows) > 1]
        self.assertTrue(duplicated)
        for rows in duplicated:
            self.assertFalse(bool(rows & train) and bool(rows & heldout))

    def test_frozen_split_matches_the_active_thesis_design(self) -> None:
        manifest = json.loads(
            (PROJECT_ROOT / "data/split_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["seed"], 42)
        self.assertEqual(manifest["heldout_fold"], 4)
        self.assertEqual(manifest["heldout_fold_setting"], "auto")
        self.assertEqual(manifest["training_rows"], 196)
        self.assertEqual(manifest["heldout_rows"], 50)
        self.assertIn("train_indices_sha256", manifest)
        self.assertIn("test_indices_sha256", manifest)


if __name__ == "__main__":
    unittest.main()
