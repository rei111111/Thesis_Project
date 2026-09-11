# Archived Initial Project Plan — Superseded

> **Do not use this file as an implementation specification.** It records an
> abandoned early design (500 videos, a 400/100 split, source `video_id` and
> `platform` columns, an exclamation feature, and seven auxiliary values). The
> authoritative short-form final thesis instead uses 250 source rows, 246
> labelled rows, a frozen 196/50 split, the documented nine-column source CSV,
> and six auxiliary values: certainty, hedge, likes, comments, views, and
> duration. See `README.md`, `configs/`, `VALIDITY_AUDIT.md`, and
> `IMPLEMENTATION_MANIFEST.md` for the active implementation. This historical
> text is retained only to explain project evolution.

# 1. Project Goal

  `Thesis_Project`will contain the complete code and data workflow for the thesis. The repository will:

- combine the separately collected transcripts and fact-checking records;
- validate and prepare the final modelling dataset;
- create the fixed training and held-out test split;
- extract text, linguistic, engagement, and transformer features;
- train four classical models and two transformer models;
- evaluate all fourteen experimental conditions consistently;
- generate the metrics, predictions, tables, and figures required by the thesis.

  This document defines the structure and approach only. Implementation code will be added later.

# Schema of a video's transcription and fact checking

- *Transcription*: blahblahblah
- *Metadata features*: 100k likes, 1 million views, 10k comments, 50 seconds duration
- *Fact Checking Discussion*: Identification of claims, checking wrong and true claims under the already decided criteria, finalizing the calculation of % of false claims ratio for CSV and discussion of claim and what clinical evidence it contradicts.

# 2. Experimental Conditions

    The same four classical models will be evaluated with three feature configurations:

    | Configuration | Features                                                             | Models                                                            | Conditions |
    | ------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------- | ---------: |
    | A             | TF--IDF                                                              | Logistic Regression, Ridge, Complement Naive Bayes, Decision Tree |          4 |
    | B             | A  certainty, hedge, and exclamation features                        | The same four models                                              |          4 |
    | C             | B  likes, comments, views, and duration                              | The same four models                                              |          4 |
    | D             | Frozen àll-MiniLM-L6-v2`embeddings  the same seven non-text features | Logistic Regression                                               |          1 |
    | E             | Fine-tuned `bert-base-uncased` the same seven non-text features      | BERT classification head                                          |          1 |
    |               |                                                                      | **Total**                                                         |     **14** |

    The six model files therefore represent:

    1. Logistic Regression;
    2. Ridge Classifier;
    3. Complement Naive Bayes;
    4. Decision Tree;
    5. frozen MiniLM with Logistic Regression;
    6. fine-tuned BERT.

# 3. Repository Structure

     ```text
     Thesis_Project/
     ├── README.md
     ├── Initial_plan.MD
     ├── requirements.txt
     ├── .gitignore
     │
     ├── wm222dk_transcription/
     │   ├── transcripts/
     │   └── fact_checking/
     │
     ├── raime_transcription/
     │   ├── transcripts/
     │   └── fact_checking/
     │
     ├── configs/
     │   ├── experiment.yaml
     │   └── bert.yaml
     │
     ├── data/
     │   ├── dataset.csv
     │   ├── train_ids.csv
     │   └── test_ids.csv
     │
     ├── features/
     │   ├── text_features.py
     │   ├── linguistic_features.py
     │   ├── metadata_features.py
     │   └── transformer_features.py
     │
     ├── models/
     │   ├── logistic_regression.py
     │   ├── ridge_classifier.py
     │   ├── complement_naive_bayes.py
     │   ├── decision_tree.py
     │   ├── frozen_minilm.py
     │   └── finetuned_bert.py
     │
     ├── evaluation/
     │   ├── cross_validation.py
     │   ├── metrics.py
     │   └── final_evaluation.py
     │
     ├── scripts/
     │   ├── prepare_data.py
     │   ├── train_models.py
     │   └── generate_results.py
     │
     ├── testing/
     │   ├── test_data.py
     │   ├── test_features.py
     │   ├── test_models.py
     │   └── test_evaluation.py
     │
     └── results/
         ├── predictions/
             ├── metrics/
                 ├── tables/
                     └── figures/
                     ```

# 4. Folder and File Responsibilities

 Root files

- `README.md`: explains installation, repository usage, and the order in which scripts are run.
- Ìnitial_plan.MD`: records the agreed structure, methods, and implementation phases.
- `requirements.txt`: pins the Python packages used in the final experiments.
- `.gitignore`: excludes private data, model checkpoints, caches, and generated files that should not be committed.

  Transcription folders

  `wm222dk_transcription/`and `raime_transcription/`contain the original work produced by each author of the study:

- raw transcripts;
- video-level fact-checking;
- claim annotations needed to verify the final label.

  Every transcript and fact-checking record must use the same anonymous `video_id`. These folders are the source records and must not be overwritten by model-processing scripts.

   `data/`

   The `data/`folder contains only data prepared for modelling:

- `dataset.csv`: the merged and validated dataset;
- `train_ids.csv`: the 400 training video identifiers;
- `test_ids.csv`: the 100 permanently held-out video identifiers.

   The raw transcripts and fact-checking records remain in the two contributor folders and are not duplicated here.

   The modelling dataset will contain:

   ```text
   video_id
   platform
   title
   transcript
   likes
   comments
   views
   duration_sec
   total_claims
   false_claims
   label
   ```

   `total_claims`and `false_claims`are used only to audit the labels. They must never be included as model features because they directly determine the target.

    `configs/`

    - èxperiment.yaml`stores shared settings: seed 42, paths, feature configurations, classical-model search spaces, cross-validation folds, metrics, and bootstrap count.
    - `bert.yaml`stores the BERT-specific settings: checkpoint, sequence length, batch size, learning rate, epochs, dropout, warm-up, weight decay, clipping, and early stopping.

    Settings should be changed in the configuration files rather than copied across scripts.

     `features/`

     - `text_features.py`: combines title and transcript and creates fold-fitted TF--IDF unigram and bigram features.
     - `linguistic_features.py`: calculates certainty, hedge, and exclamation features.
     - `metadata_features.py`: transforms likes, comments, views, and duration and applies model-appropriate scaling.
     - `transformer_features.py`: creates frozen MiniLM embeddings and prepares title/transcript pairs for BERT tokenization.

     All fitted feature processing must use training rows only.

      `models/`

      - `logistic_regression.py`: Logistic Regression for Configurations A, B, and C.
      - `ridge_classifier.py`: Ridge Classifier for Configurations A, B, and C.
      - `complement_naive_bayes.py`: Complement Naive Bayes for Configurations A, B, and C.
      - `decision_tree.py`: depth-constrained Decision Tree for Configurations A, B, and C.
      - `frozen_minilm.py`: Configuration D, using frozen 384-dimensional àll-MiniLM-L6-v2`embeddings, seven non-text features, and Logistic Regression.
      - `finetuned_bert.py`: Configuration E, fine-tuning `bert-base-uncased`and combining its 768-dimensional pooled text representation with the same seven non-text features before four-class classification.

      Each file contains the construction and training behaviour of its model. Shared evaluation logic does not belong inside the model files.

       èvaluation/`

       - `cross_validation.py`: runs nested five-outer/three-inner stratified cross-validation for A--D and the outer-fold/internal-early-stopping procedure for E.
       - `metrics.py`: calculates quadratic weighted Cohen's kappa, accuracy, weighted F1, mean absolute error, per-class scores, and confusion matrices.
       - `final_evaluation.py`: trains the final models on the 400 training videos, evaluates them once on the 100 held-out videos, and performs paired bootstrap comparisons.

        `scripts/`

        - `prepare_data.py`: merges contributor records, validates the dataset, checks labels, and creates or loads the fixed split.
        - `train_models.py`: runs cross-validation and trains the final versions of all fourteen conditions.
        - `generate_results.py`: evaluates saved predictions and produces thesis-ready tables and figures.

        These files are short entry points. The main logic stays inside `features/`, `models/`, and èvaluation/`.

         `testing/`

         - `test_data.py`: tests schema, labels, duplicate identifiers, and split separation.
         - `test_features.py`: tests feature groups, transformations, dimensions, and training-only fitting.
         - `test_models.py`: smoke-tests all six model implementations.
         - `test_evaluation.py`: tests metrics, fold separation, prediction alignment, and test-set protection.

          `results/`

          Stores generated:

          - per-video predictions;
          - cross-validation and held-out metrics;
          - comparison tables;
          - confusion matrices and other figures.

          Each result must record the condition name, seed, configuration, and dataset version that produced it.

# 5. Data and Training Flow

           1. Store each contributor's transcripts and fact-checking records in their own folder.
           2. Match records by `video_id`.
           3. Merge them into `data/dataset.csv`.
           4. Validate required fields, claim counts, labels, class values, and the expected 500 videos.
           5. Create the stratified 400/100 split once with seed 42 and save the identifiers.
           6. Fit feature processing only on the current training data.
           7. Run model selection and cross-validation on the 400 training videos.
           8. Train the final form of every condition using the complete training set.
           9. Evaluate each final condition once on the 100 held-out videos.
           10. Save predictions first, then calculate all tables, figures, and comparisons from those predictions.

# 6. Model Implementation Plan

             Classical models: A--C

             The four classical model files reuse the same feature-building pipeline:

             - A supplies TF--IDF only;
             - B adds the three linguistic features;
             - C adds the four engagement and format features.

             The model-specific search spaces are:

             - Logistic Regression: `C = 0.1, 1, 10`;
             - Ridge Classifier: àlpha = 0.1, 1, 10`;
             - Complement Naive Bayes: àlpha = 0.1, 1, 10`;
             - Decision Tree: maximum depth `3, 5, 7`and minimum leaf size `2, 5, 10`.

              Frozen MiniLM: D

              `frozen_minilm.py`will:

              - encode the title/transcript text with àll-MiniLM-L6-v2`;
              - keep the encoder frozen;
              - produce one 384-dimensional embedding per video;
              - combine it with the seven linguistic and metadata features;
              - classify the combined features using Logistic Regression.

               Fine-tuned BERT: E

               `finetuned_bert.py`will:

               - tokenize title and transcript as a pair;
               - use `bert-base-uncased`with a maximum of 256 WordPiece tokens;
               - fine-tune all BERT parameters;
               - combine the 768-dimensional pooled text representation with seven scaled non-text features;
               - apply dropout and a four-class output layer;
               - train with class-weighted cross-entropy and AdamW;
               - use internal early stopping without accessing the held-out test set.

               The fixed initial settings are learning rate `2e-5`, batch size 8, dropout 0.1, maximum five epochs, patience 2, weight decay 0.01, warm-up 10%, gradient clipping 1.0, and seed 42.

# 7. Evaluation Rules

                - The 100-video held-out set is never used for feature fitting, model selection, early stopping, or debugging.
                - Configurations A--D use nested stratified cross-validation with five outer folds and three inner folds.
                - Configuration E uses the same five outer folds and a 10% early-stopping subset from each outer-training fold.
                - Quadratic weighted Cohen's kappa is the primary metric.
                - Accuracy, weighted F1, mean absolute error, per-class metrics, and confusion matrices are also reported.
                - Most-frequent and stratified-random predictions are included as baselines.
                - Held-out conditions are compared with 10,000 paired, label-stratified bootstrap resamples.
                - The five correlated outer-fold scores are not treated as independent observations in ordinary paired t-tests.

# 8. Principles

    ## Prevent leakage

    The label, claim counts, test labels, and statistics fitted on non-training rows cannot enter model training.

    # Keep comparisons identical

    All conditions use the same saved split, folds, identifiers, metrics, and output format.

    #Keep code simple

    Each file has one clear responsibility. New files are added only when an existing file would otherwise mix unrelated responsibilities.

    #Preserve source data

    Contributor transcripts and fact-checking records are never overwritten. Processed data and results are generated separately.

    #Use configuration as the source of truth

    Experiment settings belong in `configs/`, not in multiple scripts.

    #Make results traceable

    Every reported value must be reproducible from saved predictions, settings, and the dataset version.

    #Protect privacy

    Creator-identifying information and raw media are not placed in the public repository.

    #Do not invent results

    The code and thesis will contain numerical findings only after the actual experiments are completed.

# 9. Implementation Order

    Phase 1: Repository and data

                           - create the agreed folders and root files;
                           - settle the transcript and fact-checking filename format;
                           - implement merging, validation, and label auditing;
                           - create and save the fixed train/test split.

    Phase 2: Features

                            - implement common text preparation and TF--IDF;
                            - implement linguistic features;
                            - implement engagement transformations and scaling;
                            - implement MiniLM encoding and BERT tokenization.

    Phase 3: Classical models

                             - implement the four classical model files;
                             - connect them to feature configurations A, B, and C;
                             - run tests and nested cross-validation.

    Phase 4: Transformer models

        - implement frozen MiniLM with Logistic Regression;
                              - implement the metadata-aware fine-tuned BERT model;
                              - test dimensions, freezing, training, and prediction alignment.

    Phase 5: Final evaluation

                               - train the final fourteen conditions;
                               - evaluate the held-out set once;
                               - generate metrics, bootstrap comparisons, tables, and figures;
                               - verify that every thesis result can be traced to saved output.
