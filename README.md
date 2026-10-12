# MLOps course repository

Labs and homework for the MLOps course at AGH. Each folder is a standalone [uv](https://docs.astral.sh/uv/) project, so run every command from inside it, e.g. `cd lab01 && uv sync`.

| Folder | Topic |
|---|---|
| [lab01](lab01/) | Iris classifier served via a web API: uv, pre-commit, pytest, Docker Compose, SOPS-encrypted secrets |
| [lab01-homework](lab01-homework/) | Text classifier on Sentence Transformer embeddings, served via a web API in Docker |
| [lab02](lab02/) | PostgreSQL (psycopg) and DuckDB on the services-2024 dataset |

## Pre-commit

A single [.pre-commit-config.yaml](.pre-commit-config.yaml) in the repo root covers all labs: Ruff for every Python file, xenon for lab01, mypy for lab01-homework. Set it up once in the repo root with `uv tool install pre-commit && uvx pre-commit install`.

## Large files

Not versioned (see `.gitignore`):

- `lab02/data/*.csv`, download as described in [lab02/LAB_INSTRUCTION.md](lab02/LAB_INSTRUCTION.md)
- `lab01-homework/models/sentence_transformer.model/` (87 MB)

## Adding a lab

1. Put the lab materials in `labNN/` and the homework in `labNN-homework/`.
2. Inside the folder run `uv sync` if it has a `pyproject.toml`, otherwise `uv init`. Rename a provided `python-version.txt` to `.python-version` (uv reads only that name).
3. Add large data or model files to the root `.gitignore`, and lab-specific hooks to the root pre-commit config with a `files:` pattern for that folder.

Keep the repo root free of `pyproject.toml`, otherwise `uv init` in a new folder turns it into a workspace member.
