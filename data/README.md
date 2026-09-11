# Data Files

`dataset.csv` is the canonical source for the original YouTube-only profile.
The additive pooled profile uses both `dataset.csv` and
`adhd_misinformation_tiktok.csv` in one run. Neither profile edits a source CSV.

`adhd_misinformation_dataset.csv` is a legacy copy retained from the uploaded
archive. It is currently semantically identical to `dataset.csv` but uses
different line-ending bytes, so it does not share the canonical checksum. Do
not switch the configured path or edit one copy independently. The test suite
fails if the two files diverge semantically.

`train_indices.csv`, `test_indices.csv`, and `excluded_indices.csv` contain
strictly increasing zero-based source row positions. Their checksums,
population summaries, and deterministic reconstruction protocol are recorded
in `split_manifest.json`.

Both YouTube CSV copies include the supplied English transcript replacements
and reviewed claim counts/labels. Videos 130 and 247 have identical transcripts
and now both have three total claims, three false claims and Label 4.
Their rows and all other metadata are retained.

There are 243 labelled YouTube rows. Seven rows have blank labels under the
two-claim minimum: zero-based indices `57, 103, 112, 115, 141, 198, 207`
(Videos 58, 104, 113, 116, 142, 199 and 208). The YouTube-only split has
194 training and 49 held-out rows. Excluded rows are kept in the source file
and exclusion audit, without changing anyone else's source index.

`validation_report.json` currently records no low-Latin-script flags following
the supplied English replacements. This heuristic does not infer language or
eligibility, and no manual-review CSV is required. Transcript and inclusion
decisions remain the author's responsibility.

## Pooled multi-platform files

`adhd_misinformation_tiktok.csv` is the immutable 248-row TikTok source. Its
`title` cells retain the author-supplied placeholder `video`; the pooled feature
policy excludes the complete title column from all models rather than changing
or manufacturing titles.

`multiplatform/train_indices.csv`, `test_indices.csv`, and
`excluded_indices.csv` address the deterministic in-memory concatenation of
YouTube first and TikTok second. Stable `record_id` values include the platform
and original source-row position, so the same local row number on two platforms
cannot be confused.

`multiplatform/split_manifest.json` freezes source hashes, joint
platform/label distributions, selected grouped fold, and index hashes. The
current split contains 392 labelled training rows, 99 labelled held-out rows,
and the seven unassigned YouTube rows in the excluded audit file. All 498
source rows keep their original positions: TikTok starts at global index 250.
The configured source counts remain 250 and 248; they count all source rows,
including rows without labels.

Both profiles' three index files, split manifest and validation report were
regenerated together after the annotation update. If either source CSV changes
again, regenerate the affected profile before training. Do not edit excluded
indices alone or renumber source rows to remove gaps.

`multiplatform/validation_report.json` records source-specific validation,
placeholder counts, pooled class counts, and exact/near-duplicate grouping
diagnostics. These diagnostics are evidence about the supplied files, not
instructions to rewrite or exclude rows.

The row-ordered source-URL list is
`YT_Shorts_wm222dk_transcription/collection_of_all_links.txt`. Its current hash
and audit are recorded in `validation_report.json`, but it is not a model input
or frozen-split prerequisite. It currently contains two repeated YouTube
video IDs (zero-based row pairs 79/177 and 129/246), so it has 248 unique IDs
for 250 records. This is an author-review warning and does not block training,
result generation, or output validation.
