# ADHD Misinformation Classification — YouTube + TikTok

This project evaluates six model families across fourteen experimental conditions
and two baselines. Every model trains on YouTube and TikTok together, using the
transcript as its text input. Use `configs/experiment_multiplatform.yaml` for
every experiment command below.

## Setup

Run commands from the project root. If your working environment is already
installed, activate it and skip installation. These activation commands are for
Windows Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
export PYTHONUTF8=1
```

On Linux/macOS, activate with `source .venv/bin/activate`. Set
`PYTHONUTF8=1` in each new shell so child Python processes also use UTF-8.
The commands below additionally specify `-X utf8` to read lexicon punctuation
consistently, including on Windows.

MiniLM and BERT download pretrained checkpoints unless already cached. CPU
execution is supported; append `--device cuda` to training if your installed
PyTorch supports CUDA. Dependencies, downloaded checkpoints, fitted models, and
interpretability outputs can occupy several gigabytes. Keep the environment
used for a completed experiment; its package versions are recorded in receipts.

## Run the pooled experiment

For a fresh experiment, run these steps in order. If your experiment is already
complete, replacing this documentation does not require preparing, training, or
generating results again.

**1. Validate both datasets and the frozen pooled split.**

```bash
python -X utf8 -m scripts.multiplatform_data --config configs/experiment_multiplatform.yaml
```

Expected population: **392 training records, 99 held-out records, and seven
unassigned records excluded from modelling**.

**2. Check the implementation.**

```bash
python -X utf8 -m unittest discover -s testing -v
```

Tests cover data and label arithmetic, feature isolation, grouped partitions,
models, metrics, interpretability, and saved evidence. Optional transformer
tests can skip when their dependencies are unavailable; a skip does not verify
that functionality. Test results are software checks, not thesis model scores.

**3. Train all fourteen conditions and both baselines.**

```bash
python -X utf8 -m scripts.train_models --config configs/experiment_multiplatform.yaml --model all
```

To train a particular family, replace `all` with `logistic`, `ridge`, `cnb`,
`tree`, `minilm`, `bert`, or `baselines`. The four classical choices each train
their A, B, and C conditions. A failed or incomplete condition must be completed
before producing the full report; an `all` command is not an automatic resume.

**4. Generate RQ1–RQ3 tables and figures after training finishes.**

```bash
python -X utf8 -m scripts.generate_results --config configs/experiment_multiplatform.yaml
```

**5. Validate the complete results.**

Use the project-root validator supplied with the Windows correction:

```bash
python -X utf8 validate_pooled_results.py --config configs/experiment_multiplatform.yaml
```

Keep `validate_pooled_results.py` in the project root alongside this README.
It handles Windows path separators while retaining artifact, prediction,
metric, and provenance checks. UTF-8 execution also avoids differing lexicon
interpretations when feature-association tables are recalculated.

Primary outputs are under `results/pooled_multiplatform_reannotated/`.
Successful report generation is followed by completion validation; it does not
replace that final check.

## Dataset and labels

| Input | Source records | Labelled | Training | Held out |
|---|---:|---:|---:|---:|
| `data/dataset.csv` — YouTube | 250 | 243 | 194 | 49 |
| `data/adhd_misinformation_tiktok.csv` — TikTok | 248 | 248 | 198 | 50 |
| **Total** | **498** | **491** | **392** | **99** |

Both sources use this schema:

```text
title,transcript,likes,comments,views,duration_sec,total_claims,false_claims,label
```

`data/adhd_misinformation_dataset.csv` is a matching YouTube copy checked by the
tests; it is not a third input dataset. Keep its parsed values consistent with
`data/dataset.csv`. The copies can have different line endings.

Labels require at least two eligible claims:

```text
supported_ratio = (total_claims - false_claims) / total_claims
```

| Supported ratio | Label |
|---|---|
| 0.80–1.00 | 1 — Accurate |
| 0.60–less than 0.80 | 2 — Slightly misleading |
| 0.16–less than 0.60 | 3 — Moderately misleading |
| 0.00–less than 0.16 | 4 — Highly misleading |

The seven unassigned YouTube source indices are `57, 103, 112, 115, 141, 198,
207` (zero-based). They remain in the CSV and exclusion audit. Preparation
does not renumber, translate, relabel, or deduplicate source records. TikTok
begins at pooled index 250; identifiers and platform fields are derived for
alignment without rewriting the raw CSVs.

Transcript language, title placeholders, source-identity findings, and content
judgements are author-controlled observations. They are advisory and do not
introduce a manual-review file or approval gate. The repeated YouTube source
entries at zero-based pairs `79/177` and `129/246` remain included. Structural
checks still reject invalid numeric inputs, inconsistent claim counts/labels,
stale evidence, and evaluation leakage. The code does not fact-check claims.

## Model inputs and evaluation

| Configuration | Features | Models |
|---|---|---|
| A | Transcript TF–IDF | Logistic Regression, Ridge, Complement Naive Bayes, Decision Tree |
| B | A + certainty and hedge rates | Same four models |
| C | B + within-platform percentiles of likes, comments, views, and duration | Same four models |
| D | Frozen MiniLM + the six auxiliary features | Logistic Regression |
| E | Fine-tuned BERT + the six auxiliary features | Neural classification head |

Titles are excluded from every text and linguistic pipeline, so TikTok's title
placeholder `video` is not a predictor. Actual words in transcripts remain
ordinary text. Claim counts, labels, and record identifiers cannot be features.
Platform routes metadata normalisation and supports stratification/reporting;
it is not emitted as a predictor.

TF–IDF uses up to 300 unigrams/bigrams. Linguistic rates count the longest
non-overlapping lexicon matches per 100 word tokens, using
`configs/linguistic_lexicons.yaml`. MiniLM produces 384-dimensional embeddings;
both transformers use a 256-token limit. BERT settings are in
`configs/bert.yaml`. Requested and resolved checkpoint revisions are recorded.

The frozen split and CV partitions group exact/near-duplicate transcript
content and stratify by platform and label. A–D use five outer and three inner
folds; BERT uses grouped training-only early stopping and the median selected
epoch for final fitting. Vocabularies, scaling, metadata reference distributions,
and model selection are fitted on training data only.

QWK uses the fixed ordinal scale 1–4. Accuracy, weighted F1, MAE, per-class
metrics, and confusion matrices provide complementary evidence. Paired
held-out intervals resample whole content groups; feature-association intervals
also respect these groups. Unsupported independent-row association p-values
are omitted when related records are present. RQ1 Wilson intervals are nominal
record-level summaries. Interpretability exports contain named coefficients,
tree rules, local contributions, and fold stability; embedding dimensions are
not treated as named linguistic explanations.

## Results to keep

All paths below are inside `results/pooled_multiplatform_reannotated/`.

| Path | Purpose |
|---|---|
| `tables/` | RQ1 distributions, model comparisons, ablations, platform summaries, and error analyses |
| `metrics/` | CV/held-out metrics and analysis-population records |
| `predictions/` | Aligned fold and held-out predictions |
| `feature_associations/` | Named features, class descriptives, and associations |
| `figures/` | Confusion matrices and other report figures |
| `interpretability/` | Detailed model explanations and stability evidence; can be large |
| `models/` | Fitted estimators and transformer artifacts; can be large |
| `reproducibility/` | Per-condition receipts, inputs, code hashes, environment, and checkpoint identities |
| `results_manifest.json` | Required artifacts and checksums |
| `study_completion_report.json` | Completion validator outcome |

Use the completed, validated output files for the thesis. Keep the full result
tree for validation even when sharing only its smaller tables and figures.
Deleting required models or interpretability artifacts makes complete output
validation fail. No stored historical thesis score is a target for this project.

## Dataset changes and intentional reruns

The active split files are in `data/multiplatform/`: `train_indices.csv`,
`test_indices.csv`, `excluded_indices.csv`, `split_manifest.json`, and
`validation_report.json`.

After an intentional source or split-protocol change, regenerate these together:

```bash
python -X utf8 -m scripts.multiplatform_data --config configs/experiment_multiplatform.yaml --overwrite-split
```

Configured source counts include unassigned rows. Do not edit exclusion indices
or checksums manually. Changed model inputs require retraining and regeneration
of dependent results. A stale-report error should be resolved against the
intended source files, not bypassed by weakening validation.

For a deliberate full rerun that replaces existing held-out outputs:

```bash
python -X utf8 -m scripts.train_models --config configs/experiment_multiplatform.yaml --model all --overwrite-heldout
python -X utf8 -m scripts.generate_results --config configs/experiment_multiplatform.yaml
python -X utf8 validate_pooled_results.py --config configs/experiment_multiplatform.yaml
```

`--overwrite-split` regenerates split evidence; `--overwrite-heldout` permits
replacement of saved held-out predictions. Neither is needed for README edits.



