# LLM Engineering Mastery Journey

Personal, hands-on exploration of modern Large Language Model (LLM) engineering, tooling, and real-world application patterns. This repo is a living notebook of experiments, mini-projects, and distilled learnings.

---

## 🎯 Objectives

* Build intuition around LLM architecture, capabilities, and limits
* Practice retrieval, fine‑tuning, function calling, and agent patterns
* Compare frameworks (LangChain, LlamaIndex, semantic kernels, etc.) pragmatically
* Establish reproducible, evaluable experiment workflows
* Develop small end‑to‑end AI features / micro‑apps

## 📦 Scope & Themes (Planned)

| Theme | Focus Areas | Sample Artifacts |
|-------|-------------|------------------|
| Foundations | Tokenization, prompting, context windows | Prompt variants, token cost notes |
| Retrieval Augmented Generation (RAG) | Chunking, embeddings, vector DBs, hybrid search | Evaluated retrievers, latency benchmarks |
| Evaluation | Hallucination detection, factual scoring, A/B harness | Eval scripts, metric dashboards |
| Tool & Function Calling | JSON mode, schema design, safety | Tool router prototypes |
| Agents | Planning vs reactive, memory stores | Simple multi-tool agent |
| Fine‑Tuning / Adapters | LoRA, prompt-tuning vs full FT tradeoffs | Cost comparison sheets |
| Optimization | Caching, batching, streaming, distillation | Throughput experiments |

> NOTE: Not all folders exist yet—will materialize as progress continues.

## 🧪 Current Status

Early setup & curriculum alignment phase. Experiment scaffolding and evaluation harness design in progress.

## References

> 1. <https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>

## ⚡ Quick Start (Local)

```powershell
# Clone (adjust URL if you forked)
git clone <YOUR_FORK_URL> llm-engineering-learning
cd llm-engineering-learning

pip install uv
uv self update

# Create environment via conda (preferred)
conda env create -f environment.yml
conda activate llm-engineering

# (Optional) Smoke test logging + metrics modules
python -m eval.log_utils
python -m eval.metrics
```

If conda is slow or fails, skip to the virtualenv option in Environment Setup below.

## 📚 Primary Course Reference

Studying: "LLM Engineering: Master AI, Large Language Models & Agents" by Ed Donner on Udemy.
Course link: <https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models>

Supplemented with official docs, open papers, and community benchmarks.

## 🗺 Roadmap (Incremental Milestones)

1. Environment & repo scaffolding (structure, dependency mgmt, basic eval harness)
2. Prompt engineering baseline & systematic variant logging
3. RAG baseline (single vector store) → hybrid search → reranking
4. Lightweight evaluation suite (faithfulness, answer relevance, latency)
5. Tool/function calling prototypes (deterministic schemas, error handling)
6. Simple agent w/ tool selection rationale logging
7. Cost & performance optimization (caching, batching, model selection matrix)
8. (Stretch) Fine‑tune / adapter experiment & comparison vs prompt engineering

## 🧱 Repository Structure (Planned Draft)

```text
├─ prompts/            # Prompt templates & variant experiments
├─ data/               # Sample corpora / synthetic sets (non-sensitive)
├─ rag/                # Retrieval prototypes (index builders, query flows)
├─ eval/               # Evaluation scripts & metric outputs
├─ agents/             # Agent & tool orchestration experiments
├─ tools/              # Custom tool / function call definitions
├─ notebooks/          # Exploratory Jupyter / analysis
├─ scripts/            # Utility CLIs (ingest, batch eval, etc.)
└─ docs/               # Deeper writeups & decision logs
```

## 🛠 Environment Setup (Choose One)

| Option | When to Prefer | Pros | Considerations |
|--------|----------------|------|----------------|
| Conda (Anaconda / Miniconda / Mamba) | Need compiled libs (PyTorch, CUDA later), reproducible YAML | Handles complex binaries | Slower solve (speed up with mamba) |
| Native virtualenv / venv | Simpler, fast creation, fewer moving parts | Lightweight & quick | Manual handling of some binary deps |

### Option A: Conda

1. **Install Anaconda / Miniconda** (Windows installer: <https://docs.anaconda.com/anaconda/install/windows/>)

 (Optional) After install, speed up solving:

 ```powershell
 conda install -n base -c conda-forge mamba
 ```

1. **Create Environment**

 ```powershell
 cd C:\Path\To\llm-engineering-learning
 conda env create -f environment.yml
 conda activate llm-engineering
 ```

 ArchiveError / long path issue? Enable long paths:
 <https://learn.microsoft.com/windows/win32/fileio/maximum-file-path-limitation>

1. **(Optional) Jupyter Smoke Test**

 ```powershell
 jupyter lab
 ```

 Close it after confirming it opens. Notebook: `notebooks/00_diagnostics.ipynb` will be added later.

Deactivate anytime with `conda deactivate`.

### Option B: Virtualenv / venv

PowerShell (Windows) shown; bash/zsh equivalents in comments.

```powershell
# 1. Verify tooling
python --version
pip --version

py -0p # To check installed Python versions (3.11+ required)

# 2. Create & activate virtual environment (force Python 3.12)
pip install virtualenv
py -3.12 -m venv .venv                  # Ensures the venv uses Python 3.12
. .venv/Scripts/Activate.ps1            # (bash/zsh: source .venv/bin/activate)

# 3. Upgrade pip
python -m pip install --upgrade pip

# 4. First install (Bootstrap alternative if no requirements.txt yet):
pip install openai tiktoken python-dotenv
pip freeze > requirements.txt

# 5. Install dependencies if requirements.txt exists
pip install -r requirements.txt         # If the file exists (preferred)

# 6. Provide your API key (either set env var or create .env)
setx OPENAI_API_KEY "sk-..."            # (bash/zsh: export OPENAI_API_KEY="sk-...")
# Then restart the shell so setx takes effect.
```

Optional version pinning: add a `.python-version` file at repo root (used by pyenv / some IDEs). Example:

```text
3.12
```

## 🔍 Evaluation Philosophy

* Prefer small, fast feedback loops
* Track: latency, token usage, factuality, relevance, refusal rate
* Store experiment metadata (prompt hash, model, temperature, dataset slice)
* Re-run baselines after significant changes

## ✅ Progress Log

| Date | Area | Activity | Notes |
|------|------|----------|-------|
| 2025-08-18 | Init | Enhanced README | Structured plan & roadmap |
| YYYY-MM-DD | RAG | Build first vector index |  |
| YYYY-MM-DD | Eval | Add basic factuality check |  |

## 📘 Key Resources (Growing List)

* OpenAI & Anthropic model docs
* LlamaIndex, LangChain, Semantic Kernel docs
* Papers: RAG triad (retrieval quality, generation control, evaluation), Toolformer, Self-Ask
* Evaluation frameworks: RAGAS, TruLens, LM Evaluation Harness

## 📎 Extended Learning Plan

For a detailed 12‑week study blueprint, daily workflow pattern, metrics schema, and capstone ideas see: [`docs/learning-plan.md`](docs/learning-plan.md)

## 🔐 Ethics & Safety Notes (Intent)

* Avoid storing or committing sensitive data
* Log only minimal necessary interaction metadata
* Track model + prompt versions for reproducibility

## 🤝 Contributions

Currently a personal learning space—external PRs likely paused until a baseline structure exists.

## 📝 License

See `LICENSE` for details.

---
If you're reading along: suggestions & refinement ideas welcome once core scaffolding ships.

## Development

### Docs quality checks (local)

Run Markdown lint against README and all docs before opening a PR:

```powershell
# From repo root
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"
```

This uses the repository's .markdownlint.json automatically.

### Link check (Lychee)

CI currently checks `README.md` and `docs/**/*.md`. To replicate locally (Docker image mirrors CI action):

```powershell
# List links only (no validation)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest \
 --config lychee.toml --no-progress --dump README.md docs/**/*.md .github/**/*.md

# Validate links (same as CI)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress README.md docs/**/*.md .github/**/*.md
```

If you add markdown elsewhere (e.g. prompt notes), update both:

* `.github/workflows/docs-quality.yml` (lychee args)
* `lychee.toml` (optional path excludes)

#### Excluded links

Certain domains (e.g. private course pages) can return steady 403s to unauthenticated bots. The Udemy course link in the Primary Course Reference section is intentionally excluded in `lychee.toml` via a regex literal to avoid noisy failures:

```toml
exclude = [
 # ...other patterns...
 'https?://www\.udemy\.com/course/llm-engineering-master-ai-and-large-language-models/?'
]
```

Remove that pattern if you want Lychee to re-validate it (may still 403). Keep exclusions minimal so real link rot is caught.

### Manual Docs Quality Workflow

CI runs automatically on PRs and pushes that modify documentation, but you can also trigger it manually:

1. Open GitHub → Actions → "Docs Quality" workflow
2. Click "Run workflow" (no inputs required)
3. View markdownlint + Lychee results; download the `lychee-report` artifact for details

Reason: Manual trigger accelerates iteration when adjusting large batches of links or performing structural renumbering.

### Local Experiment Logging Smoke Test

```powershell
python -m eval.log_utils
python -m eval.metrics
```

Expected: `eval/experiment_log.csv` created and a sample metrics dict printed.

### Consistency Checklist

| Item | Expectation |
|------|-------------|
| Prompts | Stored under `prompts/` with metadata sidecars |
| Experiments | Each new run logged via `log_utils.log_run` |
| Links | New external links validated or excluded intentionally |
| Structure | New folders documented in Repository Structure section |
| Reproducibility | No secrets committed; env handling via `.env` |
