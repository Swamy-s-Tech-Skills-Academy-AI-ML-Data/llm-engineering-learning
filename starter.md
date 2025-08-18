# Starter Guide: LLM Engineering Study Blueprint

Concise, actionable companion to the main `README`. Use this to spin up your personal learning workspace, pace the curriculum, and track progress with intent—not just consume videos.

---

## 🚀 Quick Start (Minimal)

1. Clone & create environment (after updating `environment.yml` if needed):

- `conda env create -f environment.yml`
- `conda activate llm-engineering`

2. Create baseline folders (only what you need now):

- `prompts/`, `notebooks/`, `rag/`, `eval/`, `agents/`, `scripts/`, `data/raw/`, `data/processed/`

3. Add a first notebook: `notebooks/00_diagnostics.ipynb` (token tests, API keys load, simple embedding call).
4. Start an experiment log: `eval/experiment_log.csv` (see Metrics section).
5. Commit early: small, frequent, tagged by week (`week01_prompt_basics`).

---

## 📅 12‑Week Baseline Plan (30 min / day)

| Week | Theme | Primary Outcomes | Anchor Artifact |
|------|-------|------------------|-----------------|
| 1 | Foundations & Environment | Reproducible env, API key management | Diagnostics notebook |
| 2 | Python & Data Handling | Clean data ingestion + utilities | `scripts/ingest.py` |
| 3 | LLM & Prompt Engineering | Prompt patterns + evaluation harness | Prompt variant matrix |
| 4 | Bots & Scraping | Basic scraper feeding LLM summarizer | News/website summarizer |
| 5 | Multi-Agent Intro | Simple multi-tool agent reasoning log | Agent loop prototype |
| 6 | Structured Outputs & Orchestration | Reliable JSON / tool calling | Function call schema set |
| 7 | Optimization & Performance | Latency + token cost reductions | Before/after metrics |
| 8 | Applied Mini Projects | One polished micro-app | Gradio or CLI app |
| 9 | Autonomous / Planning Agents | Planner vs reactive comparison | Planning eval notes |
| 10 | Deployment & Scaling | Local + lightweight cloud deploy | Deployment script |
| 11 | Capstone Build | Integrated RAG + tools + eval | Capstone repo folder |
| 12 | Review & Deep Dives | Retrospective + advanced experiments | Lessons learned doc |

Adapt pacing: (a) Double speed → collapse weeks 1–2, 5–6, 7–8, 9–10. (b) Half time → focus on Weeks 1–6 + Capstone sampling ideas from later weeks.

---

## 🧱 Suggested Working Structure

```text
notebooks/          # Explorations, each prefixed 00_, 01_, ...
prompts/            # Reusable prompt templates (+ metadata JSON)
rag/                # Index builders, retrievers, query pipelines
agents/             # Agent loops & tool registries
tools/              # Function/tool definitions (schema-first)
eval/               # Metrics, eval scripts, experiment_log.csv
data/raw/           # Unmodified source data (never commit secrets)
data/processed/     # Cleaned / chunked / vectorizable data
scripts/            # CLI utilities (ingest, batch_eval, cost_report)
docs/               # Decision logs, retrospectives, deep dives
```

Keep structure emergent: create folders only when you add first artifact.

---

## 🧪 Metrics & Experiment Log

Track minimal but useful fields (CSV or lightweight SQLite):

| Column | Description |
|--------|-------------|
| run_id | Short unique ID (date + counter) |
| task | High-level objective (e.g., qa_rag_baseline) |
| model | Provider + model name |
| prompt_hash | Stable hash of canonical prompt template |
| temperature | Generation setting |
| input_tokens / output_tokens | Usage for cost tracking |
| latency_ms | End-to-end measured latency |
| score_relevance | Manual or automated metric |
| score_factuality | Faithfulness / hallucination proxy |
| notes | Quick observation / anomaly |

Automate population for repeatability; never hand-edit historical rows.

---

## 🏗 Workflow Pattern (Daily 30 Minutes)

1. (5m) Review yesterday’s result + decide single micro‑goal.
2. (15–20m) Implement / refine (one change only: prompt tweak OR retriever variant—not both).
3. (3m) Run eval script; append row to log.
4. (2m) Capture decision or question in `docs/decisions.md`.
5. (Optional 5m) Stage next hypothesis.

Consistency > intensity.

---

## 🔑 Core Best Practices

| Area | Guideline |
|------|-----------|
| Prompts | Externalize templates + version in Git; keep variables explicit |
| Data | Preserve raw, transform forward only (no in‑place overwrites) |
| Eval | Always run baseline before claiming improvement |
| Tool Calling | Define JSON schema first; validate outputs defensively |
| Agents | Log reasoning / tool selection for post-mortem audits |
| Cost | Track cumulative token usage weekly; set soft budget ceiling |
| Reproducibility | Seed randomness (where supported) + pin critical deps |

---

## 📘 Topic Coverage Snapshot

* Foundations: env, APIs, Git hygiene
- Prompt engineering & structured output design
- Retrieval (chunking, embeddings, hybrid search, reranking)
- Agents & tool orchestration
- Evaluation (relevance, faithfulness, latency, cost)
- Optimization (caching, batching, model selection)
- Deployment & lightweight productization

---

## 🧪 Capstone Suggestions (Pick One)

| Idea | Core Components | Stretch Add-ons |
|------|-----------------|-----------------|
| Domain Q&A Assistant | RAG + prompt eval loop | Tool calling (search / calculator) |
| Multi-Source Summarizer | Scraper + batching + summarization | Timeline / topic clustering |
| Agentic Research Helper | Planner agent + retriever tools | Memory & critique loop |
| Structured Data Extractor | Prompted JSON + validation | Active learning correction pass |

---

## ✅ Personal Setup Checklist

- [ ] `environment.yml` resolved & environment activated
- [ ] API keys loaded via `.env` (never committed)
- [ ] `notebooks/00_diagnostics.ipynb` runs successfully
- [ ] `eval/experiment_log.csv` created
- [ ] First prompt template stored in `prompts/`
- [ ] Baseline run logged (token + latency metrics)

Revisit weekly; add/remove items as maturity grows.

---

## 🧭 Adapting for Different Goals

| Goal | Focus | Drop / Minimize |
|------|-------|-----------------|
| Rapid prototyping | Prompts, tool calling | Heavy evaluation, optimization early |
| Research depth | Retrieval variants, eval rigor | Deployment polish |
| Portfolio | 2 polished micro‑apps | Lower-value exploratory dead ends |
| Cost sensitivity | Model selection, caching | Large multi-model sweeps |

---

## 🔁 Retrospective Template (Weekly)

```text
Week: 03
Objective: Improve baseline retrieval relevance
What worked: Hybrid search + rerank improved relevance +12%
What didn’t: Over-aggressive chunk overlap increased cost
Change for next week: Introduce caching layer for embeddings
Risk / concern: Prompt drift; need hashing utility
```

Store retros in `docs/retros/` (one file per week) for longitudinal insight.

---

## 🏁 How to Use This Document

* Bootstrap: Follow Quick Start + Checklist.
- Guide pacing: Use Week plan table; adjust via Adaptation matrix.
- Improve deliberately: Log everything; compare against baselines.
- Reflect: Run weekly retrospective loop.

---

Evolve ruthlessly—delete stale experiments, promote reusable patterns, and keep learning velocity high.
