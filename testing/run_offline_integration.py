"""Exercise all conditions and complete reporting with small local test encoders.

Run explicitly: python -m testing.run_offline_integration
Requires the full project dependencies. Uses the real source CSVs and classical
grids, but small randomly initialized transformer fixtures and fewer report
resamples. Outputs are test evidence in a separate temporary project, never
research results. No source data or active project configuration is changed.
"""

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import torch
from transformers import BertConfig, BertModel, BertTokenizerFast
from sentence_transformers import SentenceTransformer, models
import yaml


def main():
    torch.set_num_threads(1)
    torch.manual_seed(42)
    source = Path(__file__).resolve().parents[1]
    root = Path(tempfile.mkdtemp(prefix="raime_offline_integration_", dir=source.parent)) / "project"
    shutil.copytree(source, root, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "results"))
    fixtures = root / "test_encoders"
    fixtures.mkdir()
    vocab = fixtures / "vocab.txt"
    vocab.write_text("[PAD]\n[UNK]\n[CLS]\n[SEP]\n[MASK]\nadhd\nhealth\npeople\nmay\nprobably\nclearly\n")
    encoder_path = fixtures / "bert"
    tokenizer = BertTokenizerFast(vocab_file=str(vocab))
    tokenizer.save_pretrained(encoder_path)
    model = BertModel(BertConfig(vocab_size=11, hidden_size=12, num_hidden_layers=1, num_attention_heads=3, intermediate_size=24))
    model.save_pretrained(encoder_path)
    revision = hashlib.sha1((encoder_path / "model.safetensors").read_bytes()).hexdigest()
    sentence_path = fixtures / "sentence"
    SentenceTransformer(modules=[models.Transformer(str(encoder_path), max_seq_length=16), models.Pooling(12)], device="cpu").save(str(sentence_path))
    settings = yaml.safe_load((root / "configs/experiment_multiplatform.yaml").read_text())
    settings["minilm"].update(model_name=str(sentence_path), revision=revision, expected_embedding_dimension=12, expected_max_sequence_length=16)
    settings["evaluation"]["bootstrap_resamples"] = 40
    settings["reporting"]["association_bootstrap_resamples"] = 40
    (root / "configs/offline_test.yaml").write_text(yaml.safe_dump(settings, sort_keys=False))
    bert = yaml.safe_load((root / "configs/bert.yaml").read_text())
    bert.update(model_name=str(encoder_path), revision=revision, expected_hidden_size=12, max_length=16, max_epochs=2)
    (root / "configs/offline_bert.yaml").write_text(yaml.safe_dump(bert, sort_keys=False))
    environment = dict(os.environ, OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", TOKENIZERS_PARALLELISM="false", HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1")
    print(f"ISOLATED TEST PROJECT: {root}", flush=True)
    common = ["--config", "configs/offline_test.yaml", "--bert-config", "configs/offline_bert.yaml"]
    for module, arguments in (
        ("scripts.train_models", ["--model", "all", "--device", "cpu", *common]),
        ("scripts.generate_results", common),
        ("scripts.validate_study_outputs", common),
    ):
        log = root.parent / f"{module.rsplit('.', 1)[-1]}.log"
        with log.open("w") as output:
            completed = subprocess.run([sys.executable, "-m", module, *arguments], cwd=root, env=environment, stdout=output, stderr=subprocess.STDOUT)
        print(f"{module}: exit {completed.returncode}; log {log}", flush=True)
        if completed.returncode:
            print(log.read_text()[-10000:])
            raise SystemExit(completed.returncode)
    for relative in ("data/dataset.csv", "data/adhd_misinformation_tiktok.csv", "data/multiplatform/train_indices.csv", "data/multiplatform/test_indices.csv"):
        assert (source / relative).read_bytes() == (root / relative).read_bytes(), relative
    # Bypass file-checksum checks deliberately to exercise semantic validation.
    # The source artifact is restored byte-for-byte even if the check fails.
    script = r"""
from pathlib import Path
import pandas as pd
import yaml
from scripts.validate_study_outputs import verify_semantic_results
settings = yaml.safe_load(Path("configs/offline_test.yaml").read_text())
root = Path("results") / settings["reporting"]["default_run_name"]
path = root / "tables/rq1_class_distribution.csv"
original = path.read_bytes()
try:
    table = pd.read_csv(path)
    table.loc[0, "count"] += 1
    table.loc[1, "count"] -= 1
    table.to_csv(path, index=False)
    try:
        verify_semantic_results(root, settings, ())
    except ValueError as error:
        assert "recalculated evidence" in str(error), str(error)
        print("PASS: semantic validation rejected wrong class counts with an unchanged total.")
    else:
        raise AssertionError("Incorrect report values were accepted.")
finally:
    path.write_bytes(original)
"""
    checked = subprocess.run([sys.executable, "-c", script], cwd=root, env=environment, capture_output=True, text=True)
    print(checked.stdout, end="", flush=True)
    if checked.returncode:
        print(checked.stderr)
        raise SystemExit(checked.returncode)
    print("PASS: all 16 conditions, report generation, completion validation, source/split byte preservation, and semantic corruption rejection.", flush=True)


if __name__ == "__main__":
    main()
