# ADHD Short-Video Misinformation Classification

This repository contains the authors' YouTube Shorts material and the complete
machine-learning pipeline for the current 250-video ADHD dataset. Run commands
from the repository root (`Thesis_Project`).

## Implemented model families

1. **Ridge Classifier**, evaluated under three feature conditions:
   - A: TF-IDF text only;
   - B: TF-IDF plus internally derived certainty and hedge rates;
   - C: condition B plus engagement metadata and video duration.
2. **Frozen MiniLM** (`sentence-transformers/all-MiniLM-L6-v2`): a frozen
   384-dimensional sentence embedding joined to six auxiliary features and
   classified with balanced multinomial Logistic Regression.
3. **Fine-tuned BERT** (`bert-base-uncased`): the transformer is fine-tuned end
   to end, and its pooled text representation is joined to the same six
   auxiliary features before a four-class neural classification head.

These are three model families and five reported experimental conditions:
`A_RIDGE`, `B_RIDGE`, `C_RIDGE`, `D_FROZEN_MINILM`, and
`E_FINETUNED_BERT`.

## Canonical dataset

`data/dataset.csv` is the file read by every training command. In this package,
the uploaded 250-video file has replaced the former 40-row mock dataset.
`data/adhd_misinformation_dataset.csv` is retained because it was part of the
uploaded project; it is currently byte-for-byte identical to `dataset.csv` but
is not read by the model pipeline.

The canonical CSV has exactly these nine author-provided columns, in order:

```text
title,transcript,likes,comments,views,duration_sec,total_claims,false_claims,label
```

| Columns | Role |
|---|---|
| `title`, `transcript` | Raw text predictors |
| `likes`, `comments`, `views`, `duration_sec` | Raw numeric predictors for conditions C, D, and E |
| `total_claims`, `false_claims` | Author annotation/audit fields; never predictors |
| `label` | Supervised target; never a predictor |

`certainty_score` and `hedge_score` are deliberately absent from the CSV. The
code derives `certainty_rate` and `hedge_rate` from `title + transcript` inside
the fitted feature pipelines. The fixed operational lists are stored in
`configs/linguistic_lexicons.yaml`, and matching fallback lists are stored in
`features/linguistic_features.py`.

## Author-owned annotation correctness

The preparation code trusts the authors' annotations. It does **not**:

- recalculate a label from `total_claims` and `false_claims`;
- alter, repair, deduplicate, reorder, or rewrite source rows;
- detect or group repeated transcripts;
- add derived feature columns to the CSV.

It checks only the runtime contract needed by the models: exact columns, the
expected row count, nonblank text, usable numeric predictor metadata, and
labels that are either blank or integers 1–4. The current file has 250 source
rows, 246 assigned labels, and four blank labels. The four blank-label rows are
retained in the source CSV and recorded in `data/excluded_indices.csv`, but they
cannot be used for supervised training or evaluation.

The authors will resolve repeated CSV entries before the definitive thesis run.
After any row is added, removed, reordered, or edited, regenerate all split
files before training:

```bash
python -m scripts.prepare_data --overwrite-split
```

## Feature conditions

| Condition | Input representation | Estimator |
|---|---|---|
| A-Ridge | TF-IDF of title + transcript | Balanced Ridge Classifier |
| B-Ridge | A + certainty/hedge rates | Balanced Ridge Classifier |
| C-Ridge | B + log-scaled likes, comments, views, duration | Balanced Ridge Classifier |
| D | Frozen MiniLM embedding + six auxiliary values | Balanced Logistic Regression |
| E | Fine-tuned BERT representation + six auxiliary values | Four-output neural head |

The six auxiliary values used by D and E are the two internally derived lexical
rates plus the four raw numeric fields. Their scalers are fitted only on the
current training portion of each split or fold.

## Splitting and evaluation

- The 246 labelled rows are divided with an ordinary label-stratified 80/20
  split using seed 42: 196 training rows and 50 held-out rows.
- Split files contain stable zero-based row positions from `dataset.csv`.
- Duplicate-content handling is intentionally not implemented. If repeated
  rows remain, ordinary stratification may place them in different subsets.
- Ridge and MiniLM use five-fold outer stratified cross-validation on the
  training set. Three-fold inner stratified cross-validation selects their
  hyperparameters.
- BERT uses five-fold outer stratified cross-validation. Within each outer
  training fold, a label-stratified training-only subset controls early
  stopping. The median selected epoch is used for the final fit.
- TF-IDF vocabularies, metadata scalers, feature scalers, class weights, and
  hyperparameter searches are fitted without access to their evaluation rows.
- The final held-out set is evaluated once per condition.
- Metrics include quadratic weighted Cohen's kappa, accuracy, weighted F1,
  mean absolute error, per-class precision/recall/F1, and a four-class
  confusion matrix.
- Pairwise model comparisons use aligned, label-stratified bootstrap intervals.

## Setup

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

MiniLM and BERT download pretrained weights on first use. Fine-tuned BERT is
practical on a CUDA-capable GPU; CPU execution is supported but can be slow.

## Execution workflow

### 1. Check the CSV and create or verify split files

```bash
python -m scripts.prepare_data
```

If `dataset.csv` intentionally changed:

```bash
python -m scripts.prepare_data --overwrite-split
```

### 2. Run automated tests

```bash
python -m unittest discover -s testing -v
```

### 3. Train one family or all families

```bash
python -m scripts.train_models --model ridge
python -m scripts.train_models --model minilm
python -m scripts.train_models --model bert --device cuda
python -m scripts.train_models --model all --device cuda
```

Held-out prediction files are write-once by default. A justified rerun requires
`--overwrite-heldout`; do not use that flag merely to tune against the held-out
set.

### 4. Build final tables and figures

After all five condition prediction files exist:

```bash
python -m scripts.generate_results
```

## Generated outputs

| Location | Contents |
|---|---|
| `data/validation_report.json` | Source schema, row, and class summary |
| `data/split_manifest.json` | Dataset checksum, split method, seed, and counts |
| `data/train_indices.csv` | 196 training row positions |
| `data/test_indices.csv` | 50 held-out row positions |
| `data/excluded_indices.csv` | Four unassigned row positions |
| `results/metrics/` | Cross-validation and held-out metrics |
| `results/predictions/` | Row-aligned CV and held-out predictions |
| `results/models/` | Fitted estimators, BERT state, tokenizer, and scalers |
| `results/tables/` | Final performance and bootstrap-comparison tables |
| `results/figures/` | Confusion-matrix figures |

No trained model, held-out prediction, or claimed thesis performance result is
prepackaged. Those artifacts are produced only when the authors run the
documented training commands.

## Project layout

```text
Thesis_Project/
├── YT_Shorts_wm222dk_transcription/  authors' source and fact-check material
├── raime_transcription/              second-author source area
├── configs/                          experiment, BERT, and lexicon settings
├── data/                             canonical CSV and saved row splits
├── features/                         text, linguistic, metadata, transformer input
├── models/                           Ridge, frozen MiniLM, fine-tuned BERT
├── evaluation/                       cross-validation, metrics, final evaluation
├── scripts/                          command-line workflow
├── testing/                          dependency-light automated tests
└── results/                          generated models, metrics, predictions, tables
```
