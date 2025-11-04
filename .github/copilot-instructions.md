# Copilot Project Instructions

Guidance for AI pair programming in this repository. These conventions help produce consistent, reproducible, and evaluation‑friendly outputs.

---

## 🎯 Project Focus

LLM engineering experimentation: prompt design, RAG, agents, tool/function calling, evaluation harnesses, lightweight deployment.

**Multi-Provider Support**: All implementations support both OpenAI and Azure OpenAI.

**Multi-Language Support**: Code examples provided in Python, Go, Node.js, Angular, React, Next.js, .NET Aspire, .NET Web API, and .NET Blazor where applicable.

**Learning Path**: This repository follows a structured 25-week learning plan. See `docs/learning-plan.md` for the master document and `docs/weeks/Week1.md` through `docs/weeks/Week25.md` for detailed weekly guides.

**Key Deep Dives**:
- **Week 3**: Chain-of-Thought (CoT) - Complete guide with patterns, examples, and best practices
- **Week 5**: ReAct (Reasoning + Acting) - Full implementation guide with tool integration
- **Week 14**: Reasoning Patterns Deep Dive - All patterns (CoT, ReAct, ToT, PoT, etc.)

---

## ✅ General Principles

- Favor small, composable modules over monolith scripts.
- Always separate concerns: data ingestion, retrieval logic, prompting, evaluation.
- Prefer explicit configuration (YAML / .env variables) over hidden constants.
- Make experiments reproducible (seed where supported, log model + prompt versions).
- Assume future evaluation; keep output structures stable.

---

## 🗂 Directory Expectations (Planned)

| Folder       | Purpose                                               |
| ------------ | ----------------------------------------------------- |
| `prompts/`   | Prompt templates + metadata (JSON/YAML)               |
| `rag/`       | Index builders, retrievers, query pipelines           |
| `agents/`    | Agent loops, reasoning traces, tool registries        |
| `tools/`     | Tool / function call schema definitions               |
| `eval/`      | Metrics calculators, experiment logs, harness scripts |
| `scripts/`   | CLI utilities (ingest, batch eval, cost reporting)    |
| `notebooks/` | Exploratory analysis & prototyping                    |
| `docs/`      | Decision logs, retrospectives, learning plan          |

If a folder is missing, create it with a minimal README or `.gitkeep` when first needed.

---

## 🧪 Experiment Logging Standard

When generating code that runs experiments, ensure it logs (CSV / JSONL acceptable):

```text
run_id, timestamp, task, model, prompt_hash, temperature, input_tokens, output_tokens, latency_ms, score_relevance, score_factuality, notes
```

- Provide a helper: `eval/log_utils.py` (create if missing) with `log_run(dict)`.
- Never silently swallow exceptions; log structured error rows.

---

## 🧱 Prompt Template Convention

Store prompt templates as plain `.txt` or `.jinja` in `prompts/` plus sidecar metadata: `name.prompt.txt` and `name.meta.json`:

```json
{
  "version": 1,
  "description": "Baseline QA context injection",
  "variables": ["question", "context"],
  "intended_model": "gpt-4o-mini",
  "notes": "Keep temperature <=0.2 for deterministic eval."
}
```

When requesting structured output, show an explicit JSON schema in the prompt and add validation code.

---

## 🔧 Tool / Function Calling

- Define each tool in `tools/` with: description, input schema (Pydantic or dataclass), handler function, safety notes.
- Include a `tools/registry.py` that exposes `get_tool_specs()` returning structured definitions (JSON-like) for the model.

---

## 🤖 Agents

- Keep first implementations simple (reactive loop) before adding planning.
- Always log: step number, thought (if model provided), selected tool, tool arguments, tool result, cumulative context size.
- Provide a cancellation condition (max steps, max tokens, explicit goal reached).

---

## 📦 Dependencies

**Python**: Prefer widely-used libs: `langchain`, `langchain-openai`, `langchain-azure-openai`, `chromadb`, `sentence-transformers`, `openai`, `anthropic`.

**Node.js**: `openai`, `@azure/openai`, `langchain`, `langchain-openai`.

**Go**: `github.com/sashabaranov/go-openai`, `github.com/azure/openai-assistant-go`.

**.NET**: `Azure.AI.OpenAI`, `OpenAI`, `LangChain.Net`.

**Frontend**: Framework-specific LLM libraries (React: `openai`, Angular: HTTP client, Next.js: API routes).

- Avoid adding a dependency if native stdlib or an existing installed lib suffices.
- Pin unusual or breakage-prone versions; otherwise allow minor updates.

---

## 🧹 Code Style

- Use type hints (PEP 484) for all new Python functions.
- Add a short doctring (one-line summary + param annotations if non-trivial).
- Keep functions < ~60 lines; refactor if growing.
- Return structured data (dict / dataclass) instead of raw tuples when multiple related fields.

---

## 🛡 Safety & Data Handling

- Never commit secrets; rely on `.env` + `python-dotenv`.
- For scraped content, sanitize before embedding (strip scripts, collapse whitespace).
- Redact potential PII fields in logs where feasible.

---

## 🧬 Evaluation Utilities

If creating evaluation code:

- Provide deterministic seed usage (`random`, `numpy`, framework-specific).
- Separate metric calculation from data loading.
- Include a CLI entry (e.g., `python -m eval.run --dataset qa_small.json --model openai:gpt-4o-mini`).

---

## 🧪 Testing Minimalism

- For utility modules, add a lightweight smoke test (even if not full pytest suite yet).
- When generating parsers / validators, include an inline `if __name__ == "__main__":` block that demo-runs with sample input.

---

## 🧾 Commit Message Pattern

Use conventional-ish style with context tag + concise action:

```text
rag: add hybrid retriever baseline
prompts: revise qa prompt for factuality emphasis
agents: log tool reasoning trace
```

Avoid generic messages like "update file".

---

## 🔄 Iteration Workflow (AI Assistance)

1. Propose minimal file additions/edits.
2. Generate code.
3. (If feasible) Provide usage snippet or smoke run.
4. Update docs if behavior or workflow changed.

---

## 🛠 Suggested Utility Stubs (May Create When Needed)

- `scripts/ingest.py` – ingest & chunk raw data (argparse interface)
- `rag/build_index.py` – build vector index from processed docs
- `eval/log_utils.py` – append or create experiment log
- `eval/metrics.py` – relevance & simple faithfulness placeholder
- `agents/simple_agent.py` – minimal reactive agent loop
- `tools/registry.py` – tool specification aggregator

---

## ❌ Anti-Patterns to Avoid

- Mixing prompt literals across multiple scripts without central template
- Hardcoding API keys
- Large multiline functions doing data load + retrieval + generation + formatting
- Silent `except Exception:` blocks
- Saving derived artifacts without metadata (model name, date, params)

---

## ✅ When Unsure

Prefer to ask (in comments / docs) or create a small, clearly named experimental script instead of over-engineering a general solution.

---

Happy building.
