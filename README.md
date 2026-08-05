# ADHD Short-Video Misinformation Classification

This repository implements the complete computational study needed for RQ1,
RQ2, and RQ3: fourteen experimental conditions, two contextual baselines,
global and local interpretability exports, fold-stability analysis,
paired uncertainty estimates, error analysis, and a pre-specified sensitivity
run.

## Source CSV contract

`data/dataset.csv` contains exactly these nine columns, in this order:

```text
title,transcript,likes,comments,views,duration_sec,total_claims,false_claims,label
```

There is no source `video_id` column and no source `platform` column. The code
inserts a zero-based `row_index` in memory and in split/prediction artifacts so
rows can be audited without expanding the source CSV.

| Field | Modelling role |
|---|---|
| `title`, `transcript` | Raw text predictors |
| `likes`, `comments`, `views`, `duration_sec` | Raw predictors in C--E |
| `total_claims`, `false_claims` | Annotation-audit fields; prohibited predictors |
| `label` | Ordinal target, 1--4 |

The only handcrafted linguistic features are `certainty_score` and
`hedge_score`. They are matches per 100 word tokens, derived from title plus
transcript inside each fitted pipeline. They are not CSV columns. Their fixed,
validated, non-overlapping lexicons are stored in
`configs/linguistic_lexicons.yaml`.

## Label validation

The code checks, but never invents or fact-checks, the manual annotations:

```text
supported_ratio = (total_claims - false_claims) / total_claims
```

| Ratio | Label |
|---|---:|
| 0.80--1.00 | 1, Accurate |
| 0.60--<0.80 | 2, Slightly misleading |
| 0.16--<0.60 | 3, Moderately misleading |
| 0.00--<0.16 | 4, Highly misleading |

The packaged YouTube file currently has 250 rows, 246 assigned labels, and four
retained but unassigned rows. When the separate 250-video contribution is
appended, replace `data/dataset.csv`, set `data.expected_rows` to `500` (or pass
`--expected-rows 500`), review the combined file, and create a new frozen split.
All fourteen conditions must then be rerun together; metrics from separate
250-video runs must not be combined.

The current 250-video subset contains one manual annotation record per video.
It was annotated by one person, so no double-coding or inter-annotator-agreement
workflow is part of this repository.

## Fourteen conditions

| Configuration | Features | Models | Count |
|---|---|---|---:|
| A | TF-IDF title + transcript | Logistic Regression, Ridge, CNB, Decision Tree | 4 |
| B | A + certainty and hedge scores | Same four models | 4 |
| C | B + log-transformed engagement and duration | Same four models | 4 |
| D | Frozen 384-dimensional MiniLM + six named auxiliary values | Logistic Regression | 1 |
| E | Fine-tuned BERT pooled representation + six named auxiliary values | Neural head | 1 |

Logistic Regression and Ridge use standard-scaled named numeric features. CNB
uses fold-local clipped Min--Max scaling so every input remains non-negative.
The Decision Tree receives log-transformed but otherwise unstandardised numeric
features. The two baselines are reported separately and are not experimental
conditions.

## Leakage and evaluation safeguards

- The source checksum and all three split-index checksums are frozen.
- Exact normalised-transcript duplicates remain in one held-out/outer/inner
  group.
- The TF-IDF vocabulary, scalers, class weighting, and model selection are fit
  using training rows only.
- All classical conditions and MiniLM use five grouped outer folds and three
  grouped inner folds, with QWK as the selection metric.
- BERT uses the same five outer folds and a grouped training-only early-stopping
  subset. The median selected epoch is used for final fitting.
- The aligned held-out rows are evaluated once per finalized run.
- Stored held-out files are write-protected unless an intentional rerun uses
  `--overwrite-heldout`.

## Interpretability outputs

Every A--C final fit exports all named model evidence, not just a model label:

- Logistic Regression and Ridge: all class coefficients, positive/negative
  rankings, intercepts, and top per-video feature contributions;
- Complement Naive Bayes: all class complement weights, rankings, and
  per-video weighted contributions;
- Decision Tree: all feature importances, a node table, exact text rules, a
  rendered tree, and the precise rule path for each held-out prediction;
- all four families: outer-fold feature tables and stability summaries that
  count a feature missing from a fold vocabulary as zero;
- Configuration-C cross-model consensus tables for textual and named features;
- MiniLM's six named auxiliary coefficients and their fold stability are
  exported separately, while its 384 unnamed embedding dimensions are excluded
  from substantive ranking;
- a performance/interpretability table that explicitly marks MiniLM dimensions
  as unnamed and fine-tuned BERT as opaque under the approved design.

RQ2 also receives class descriptives and training-only Spearman/Kruskal
association statistics for the two linguistic scores and four log-transformed
metadata values, including bootstrap intervals and Holm-adjusted p-values.

## Installation

Run from the project root:

```bash
python -m venv .venv
```

Activate the environment and install:

```bash
pip install -r requirements.txt
```

then

```bash
python -m pip install --no-cache-dir torch==2.12.1 \
  --index-url https://download.pytorch.org/whl/cu126
```

Transformer downloads require internet access. Fine-tuned BERT is intended to
run on a CUDA-capable GPU.

## Reproducible workflow

Validate the current file and verify the frozen split:

```bash
python -m scripts.prepare_data
```

After an intentional dataset change, create a new split:

```bash
python -m scripts.prepare_data --expected-rows 250 --overwrite-split
```

Train all fourteen conditions and both baselines:

```bash
python -m scripts.train_models --model all --device cuda
```

Families can also be run separately:

```bash
python -m scripts.train_models --model logistic
python -m scripts.train_models --model ridge
python -m scripts.train_models --model cnb
python -m scripts.train_models --model tree
python -m scripts.train_models --model baselines
python -m scripts.train_models --model minilm
python -m scripts.train_models --model bert --device cuda
```

Generate the complete result artifact set only after every prediction file is
present:

```bash
python -m scripts.generate_results
```

# This is useless, do not run this

Run the pre-specified two-claim sensitivity analysis in its own output tree:

```bash
python -m scripts.run_sensitivity --device cuda
```

After the primary and sensitivity outputs both exist, verify the entire
non-LaTeX study artifact set and every recorded checksum:


# This is useless don't run this either

```bash
python -m scripts.validate_study_outputs
```

## Outputs

Primary outputs are written under `results/`:

```text
metrics/                 fold and held-out metrics, population audit
predictions/             aligned outer-fold and held-out predictions
models/                  selected fitted estimators and BERT artifacts
interpretability/        weights, stability, rules, paths, contributions
feature_associations/    named-feature rows, descriptives, statistics
tables/                  RQ1--RQ3 summaries, ablations, errors, bootstraps
figures/                 confusion matrices, class distribution, trees
reproducibility/         commands, hashes, packages, hardware, seeds
results_manifest.json    checksums and completeness contract
```

The generator rejects missing conditions, unexpected stale prediction files,
misaligned rows, inconsistent true labels, missing fold metrics, and missing
interpretability artifacts.

## Verification

Run the dependency-light suite:


# Don't worry if a few things fail

```bash
python -m unittest discover -s testing -v
```

The BERT tensor test activates automatically when PyTorch is installed. See
`VERIFICATION.md` and `IMPLEMENTATION_MANIFEST.md` for the verified state and
the exact file-level change list.
