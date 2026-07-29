# Thesis Project



This repository contains Wamiq and Raime's implementation of:



- Ridge Classifier with feature configurations A, B, and C;
- frozen `all-MiniLM-L6-v2` embeddings with Logistic Regression;
- fine-tuned `bert-base-uncased` with six auxiliary features.


and the other 3 classical classifiers.



## Expected CSV columns

```text
title, transcript, likes, comments, views, duration_sec, total_claims, false_claims, label, certainty_score, hedge_score
```

`certainty_score` and `hedge_score` are optional during preparation. If they are absent, `scripts/prepare_data.py` creates them with the placeholder word lists in `features/linguistic_features.py`. Replace those lists with the final approved thesis lexicons before the official experiments.

`total_claims` and `false_claims` are used only for label validation and are never passed to a model.

The CSV row order is frozen during preparation. The split and prediction files use an internally generated `row_index`; `row_index` is not required in the input CSV.

## Setup

Run all commands from the `Thesis_Project` directory:

```bash
python -m venv .venv
```

Activate the environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Validate the CSV, create missing linguistic scores, and freeze the split:

```bash
python -m scripts.prepare_data --data data/dataset.csv
```

Run one model family:

```bash
python -m scripts.train_models --model ridge

python -m scripts.train_models --model minilm

python -m scripts.train_models --model bert
```

Run all three:

```bash
python -m scripts.train_models --model all
```

Generate summary tables and confusion matrices from saved held-out predictions:

```bash
python -m scripts.generate_results
```

Run the lightweight tests:

```bash
python -m unittest discover -s testing -v
```

Transformer downloads and fine-tuning require internet access and substantially more time than the lightweight tests. The supplied `data/dataset.csv` is synthetic placeholder data and must be replaced before the thesis experiments.
