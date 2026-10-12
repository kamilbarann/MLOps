# MLOps course repository

Labs and homework for the MLOps course at AGH. Each folder is a standalone [uv](https://docs.astral.sh/uv/) project, so run every command from inside it, e.g. `cd lab01 && uv sync`.

| Folder | Topic |
|---|---|
| [lab01](lab01/) | Iris classifier served via a web API: uv, pre-commit, pytest, Docker Compose, SOPS-encrypted secrets |
| [lab01-homework](lab01-homework/) | Text classifier on Sentence Transformer embeddings, served via a web API in Docker |
| [lab02](lab02/) | PostgreSQL (psycopg) and DuckDB on the services-2024 dataset |

Large files are not versioned. The lab02 dataset (`lab02/data/*.csv`) has to be downloaded as described in [lab02/LAB_INSTRUCTION.md](lab02/LAB_INSTRUCTION.md).
