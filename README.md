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

## 📚 Primary Course Reference

Studying: "LLM Engineering: Master AI, Large Language Models & Agents" by Ed Donner on Udemy.
Course link: <https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/>

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

## 🛠 Recommended Local Setup (Placeholder)

Add once initial code lands—likely to include:

* Python 3.11+ (or split polyglot if Node components appear)
* Virtual environment instructions
* Requirements / lock files
* Optional GPU acceleration notes

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

## � Extended Learning Plan

For a detailed 12‑week study blueprint, daily workflow pattern, metrics schema, and capstone ideas see: [`docs/learning-plan.md`](docs/learning-plan.md)

## �🔐 Ethics & Safety Notes (Intent)

* Avoid storing or committing sensitive data
* Log only minimal necessary interaction metadata
* Track model + prompt versions for reproducibility

## 🤝 Contributions

Currently a personal learning space—external PRs likely paused until a baseline structure exists.

## 📝 License

See `LICENSE` for details.

---
If you're reading along: suggestions & refinement ideas welcome once core scaffolding ships.
