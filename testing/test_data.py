from __future__ import annotations

import unittest
import json
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

from features.content_groups import content_group_ids, duplicate_group_count
from evaluation.final_evaluation import load_saved_split
from scripts.prepare_data import (
    CSV_COLUMNS,
    audit_source_links,
    create_or_validate_split,
    file_sha256,
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

    def test_label_function_enforces_two_claim_minimum_and_whole_counts(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least 2"):
            label_from_claims([1], [1])
        with self.assertRaisesRegex(ValueError, "whole"):
            label_from_claims([2.5], [1])

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

    def test_one_claim_cannot_receive_an_assigned_label(self) -> None:
        data = pd.DataFrame(
            [valid_row(total_claims=1, false_claims=1, label=4)]
        )
        with self.assertRaisesRegex(ValueError, "at least 2"):
            validate_dataset(data)

    def test_duration_limit_matches_the_collection_protocol(self) -> None:
        data = pd.DataFrame([valid_row(duration_sec=181)])
        with self.assertRaisesRegex(ValueError, "180-second"):
            validate_dataset(data)

    def test_validation_rejects_nonfinite_numeric_values(self) -> None:
        data = pd.DataFrame([valid_row(views=np.inf)])
        with self.assertRaisesRegex(ValueError, "non-numeric or missing"):
            validate_dataset(data)

    def test_validation_rejects_even_nearly_integral_source_values(self) -> None:
        for override in (
            {"total_claims": 5.000000001},
            {"label": 4.000000001},
        ):
            with self.subTest(override=override):
                data = pd.DataFrame([valid_row(**override)])
                with self.assertRaisesRegex(ValueError, "whole"):
                    validate_dataset(data)

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
        self.assertEqual(summary["modelled_rows"], int(data["label"].notna().sum()))
        self.assertEqual(
            summary["excluded_unassigned_rows"], int(data["label"].isna().sum())
        )
        self.assertEqual(
            summary["class_distribution"],
            {str(label): int(data["label"].eq(label).sum()) for label in range(1, 5)},
        )
        self.assertEqual(summary["exact_duplicate_transcript_groups"], 1)
        self.assertEqual(summary["duplicate_or_near_duplicate_content_groups"], 4)
        self.assertEqual(
            summary["transcript_language_warnings"]["zero_based_rows"],
            [],
        )
        self.assertTrue(summary["transcript_language_warnings"]["advisory_only"])

    def test_legacy_dataset_copy_has_not_diverged_semantically(self) -> None:
        canonical = pd.read_csv(PROJECT_ROOT / "data/dataset.csv")
        legacy = pd.read_csv(
            PROJECT_ROOT / "data/adhd_misinformation_dataset.csv"
        )
        pd.testing.assert_frame_equal(canonical, legacy)

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
        self.assertEqual(duplicate_group_count(data), 4)

    def test_frozen_split_matches_the_current_dataset_and_protocol(self) -> None:
        manifest = json.loads(
            (PROJECT_ROOT / "data/split_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["seed"], 42)
        self.assertIn(manifest["heldout_fold"], range(manifest["heldout_folds"]))
        self.assertEqual(manifest["heldout_fold_setting"], "auto")
        data_path = PROJECT_ROOT / "data/dataset.csv"
        data = pd.read_csv(data_path)
        train_rows = pd.read_csv(PROJECT_ROOT / "data/train_indices.csv")["row_index"]
        test_rows = pd.read_csv(PROJECT_ROOT / "data/test_indices.csv")["row_index"]
        excluded_rows = pd.read_csv(PROJECT_ROOT / "data/excluded_indices.csv")["row_index"]
        self.assertEqual(manifest["dataset_sha256"], file_sha256(data_path))
        self.assertEqual(manifest["source_rows"], len(data))
        self.assertEqual(manifest["modelled_rows"], int(data["label"].notna().sum()))
        self.assertEqual(manifest["excluded_rows"], len(excluded_rows))
        self.assertEqual(set(excluded_rows), set(data.index[data["label"].isna()]))
        self.assertFalse(set(train_rows) & set(test_rows))
        self.assertEqual(
            set(train_rows) | set(test_rows), set(data.index[data["label"].notna()])
        )
        for name, rows in (("training", train_rows), ("heldout", test_rows)):
            self.assertEqual(manifest[f"{name}_rows"], len(rows))
            self.assertEqual(
                manifest[f"{name}_class_distribution"],
                {str(label): int(data.loc[rows, "label"].eq(label).sum()) for label in range(1, 5)},
            )
        self.assertEqual(manifest["minimum_claims_for_assigned_label"], 2)
        self.assertEqual(manifest["near_duplicate_minimum_tokens"], 20)
        self.assertEqual(
            manifest["split_generation_grouping"],
            "exact_normalized_transcript_sha256",
        )
        self.assertIn("leakage_audit_group_method", manifest)
        self.assertIn("train_indices_sha256", manifest)
        self.assertIn("test_indices_sha256", manifest)
        self.assertNotIn("source_links_sha256", manifest)

    def test_frozen_split_can_be_recreated_exactly(self) -> None:
        data_path = PROJECT_ROOT / "data/dataset.csv"
        data = pd.read_csv(data_path)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            created = create_or_validate_split(
                data,
                root / "train.csv",
                root / "test.csv",
                root / "excluded.csv",
                root / "manifest.json",
                heldout_folds=5,
                heldout_fold="auto",
                seed=42,
                dataset_sha256=file_sha256(data_path),
                generation_grouping="exact_normalized_transcript_sha256",
            )
            recreated_train = set(pd.read_csv(root / "train.csv")["row_index"])
            recreated_test = set(pd.read_csv(root / "test.csv")["row_index"])
        frozen_train = set(
            pd.read_csv(PROJECT_ROOT / "data/train_indices.csv")["row_index"]
        )
        frozen_test = set(
            pd.read_csv(PROJECT_ROOT / "data/test_indices.csv")["row_index"]
        )
        self.assertEqual(recreated_train, frozen_train)
        self.assertEqual(recreated_test, frozen_test)
        frozen_manifest = json.loads(
            (PROJECT_ROOT / "data/split_manifest.json").read_text(encoding="utf-8")
        )
        self.assertEqual(created["heldout_fold"], frozen_manifest["heldout_fold"])

    def test_saved_split_rejects_nonreproducible_row_assignments(self) -> None:
        data_path = PROJECT_ROOT / "data/dataset.csv"
        data = pd.read_csv(data_path)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            train_path = root / "train.csv"
            test_path = root / "test.csv"
            excluded_path = root / "excluded.csv"
            manifest_path = root / "manifest.json"
            arguments = {
                "data": data,
                "train_indices_path": train_path,
                "test_indices_path": test_path,
                "excluded_indices_path": excluded_path,
                "manifest_path": manifest_path,
                "heldout_folds": 5,
                "heldout_fold": "auto",
                "seed": 42,
                "dataset_sha256": file_sha256(data_path),
                "generation_grouping": "exact_normalized_transcript_sha256",
            }
            create_or_validate_split(**arguments)
            train = pd.read_csv(train_path)
            test = pd.read_csv(test_path)
            train.loc[0, "row_index"], test.loc[0, "row_index"] = (
                int(test.loc[0, "row_index"]),
                int(train.loc[0, "row_index"]),
            )
            train.sort_values("row_index").to_csv(train_path, index=False)
            test.sort_values("row_index").to_csv(test_path, index=False)
            with self.assertRaisesRegex(ValueError, "cannot be recreated"):
                create_or_validate_split(**arguments)

    def test_source_link_audit_detects_duplicate_video_ids(self) -> None:
        audit = audit_source_links(
            PROJECT_ROOT
            / "YT_Shorts_wm222dk_transcription/collection_of_all_links.txt",
            expected_rows=250,
        )
        self.assertEqual(audit["unique_source_id_count"], 248)
        self.assertEqual(audit["duplicate_source_id_count"], 2)
        self.assertTrue(audit["has_duplicate_source_ids"])
        self.assertTrue(audit["warnings"])

    def test_language_flags_are_advisory_and_need_no_manifest(self) -> None:
        data = pd.DataFrame([valid_row(transcript="यह एक परीक्षण प्रतिलेख है।")])
        audit = validate_dataset(data)["transcript_language_warnings"]
        self.assertEqual(
            audit["zero_based_rows"],
            [0],
        )
        self.assertTrue(audit["advisory_only"])
        self.assertEqual(
            {path.name for path in (PROJECT_ROOT / "data").glob("*.csv")},
            {
                "adhd_misinformation_tiktok.csv",
                "adhd_misinformation_dataset.csv",
                "dataset.csv",
                "excluded_indices.csv",
                "test_indices.csv",
                "train_indices.csv",
            },
        )

    def test_saved_split_loads_despite_advisory_source_warnings(self) -> None:
        training, heldout = load_saved_split(
            PROJECT_ROOT / "data/dataset.csv",
            PROJECT_ROOT / "data/train_indices.csv",
            PROJECT_ROOT / "data/test_indices.csv",
            PROJECT_ROOT / "data/excluded_indices.csv",
            PROJECT_ROOT / "data/split_manifest.json",
            split_settings={
                "heldout_folds": 5,
                "heldout_fold": "auto",
                "seed": 42,
                "generation_grouping": "exact_normalized_transcript_sha256",
            },
            data_contract={
                "expected_rows": 250,
                "minimum_claims_for_assigned_label": 2,
                "unassigned_allowed_below_claims": 2,
                "maximum_duration_seconds": 180,
            },
        )
        data = pd.read_csv(PROJECT_ROOT / "data/dataset.csv")
        self.assertEqual(len(training) + len(heldout), int(data["label"].notna().sum()))
        self.assertTrue(training["label"].notna().all())
        self.assertTrue(heldout["label"].notna().all())


if __name__ == "__main__":
    unittest.main()
