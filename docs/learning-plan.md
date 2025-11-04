# LLM Engineering Learning Plan

**Complete 25-week guide for mastering LLM Engineering from basics to multi-platform mastery**

This learning plan is designed to accompany **Ed Donner's "LLM Engineering: Master AI, Large Language Models & Agents"** Udemy course. Use this as your structured roadmap to build practical skills alongside the course content.

---

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [Prerequisites](#-prerequisites)
3. [25-Week Learning Path](#-25-week-learning-path)
4. [Learning Structure](#-learning-structure)
5. [Workflow & Best Practices](#-workflow--best-practices)
6. [Progress Tracking](#-progress-tracking)
7. [Troubleshooting](#-troubleshooting)
8. [Resources](#-resources)

---

## 🚀 Quick Start

### Your First 5 Minutes

1. **Set up environment:**
   ```bash
   python --version  # Verify Python 3.8+
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install openai python-dotenv
   ```

2. **Get API keys:**
   - OpenAI: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Azure OpenAI: [portal.azure.com](https://portal.azure.com) → Create Azure OpenAI resource

3. **Create `.env` file:**
   ```env
   OPENAI_API_KEY=sk-your-key-here
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
   AZURE_OPENAI_API_KEY=your-azure-key-here
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   ```

4. **Start Week 1:** Open [`docs/weeks/Week1.md`](weeks/Week1.md) and follow day-by-day

---

## 🎯 Prerequisites

### Essential Skills

**Python Basics** (Required for Weeks 1-21)
- Variables, data types, functions
- Working with JSON, file I/O
- Error handling (try/except)
- List comprehensions

**Other Languages** (Weeks 22-24)
- **Go**: Basic syntax, interfaces, error handling
- **Node.js**: JavaScript/TypeScript, async/await
- **Frontend**: React, Angular, or Next.js basics
- **.NET**: C# basics, ASP.NET Core

**API Concepts** (Helpful)
- REST API basics
- API keys and authentication
- JSON response format

### Self-Assessment

Before starting, can you:
- [ ] Write a Python function that processes a list?
- [ ] Make an HTTP request and parse JSON response?
- [ ] Create and activate a virtual environment?
- [ ] Explain what an API key is?

**If "No" to 2+ questions:** Spend 2-3 days on Python basics first.

---

## 📅 25-Week Learning Path

**Structure:** 5 days × 30 minutes = 2.5 hours per week  
**Total Time:** ~62.5 hours  
**Multi-Platform from Week 1:** OpenAI + Azure OpenAI + Python + Go + Node.js + Frontend + .NET  
**Progressive Language Introduction:** Python (Weeks 1-5) → Add Go/Node.js (Weeks 6-10) → Add Frontend (Weeks 11-15) → Add .NET (Weeks 16-20) → Master All (Weeks 21-25)

| Week | Theme | Primary Outcomes | Deep Dives | Guide |
|------|-------|------------------|------------|-------|
| **Foundation Phase** |
| 1 | Foundations & Environment | Reproducible env, API key management | OpenAI + Azure OpenAI setup | [`Week1.md`](weeks/Week1.md) |
| 2 | Python & Data Handling | Clean data ingestion + utilities | Text chunking strategies | [`Week2.md`](weeks/Week2.md) |
| 3 | LLM & Prompt Engineering | Prompt patterns + evaluation | **Chain-of-Thought (CoT)** | [`Week3.md`](weeks/Week3.md) |
| 4 | Bots & Scraping | Basic scraper + LLM summarizer | Web scraping + integration | [`Week4.md`](weeks/Week4.md) |
| 5 | Multi-Agent Intro + ReAct | Agent reasoning log | **ReAct (Reasoning + Acting)** | [`Week5.md`](weeks/Week5.md) |
| **Intermediate Phase** |
| 6 | Structured Outputs & Orchestration | Reliable JSON / tool calling | Function calling APIs | [`Week6.md`](weeks/Week6.md) |
| 7 | Optimization & Performance | Latency + cost reductions | Caching, batching, model selection | [`Week7.md`](weeks/Week7.md) |
| 8 | Applied Mini Projects | Polished micro-app | Gradio or CLI app | [`Week8.md`](weeks/Week8.md) |
| 9 | Autonomous / Planning Agents | Planner vs reactive comparison | Planning algorithms | [`Week9.md`](weeks/Week9.md) |
| 10 | Deployment & Scaling | Local + cloud deployment | Scaling strategies | [`Week10.md`](weeks/Week10.md) |
| **Advanced Phase** |
| 11 | Capstone Build | Integrated RAG + tools + eval | Full-stack application | [`Week11.md`](weeks/Week11.md) |
| 12 | Review & Deep Dives | Retrospective + experiments | Lessons learned | [`Week12.md`](weeks/Week12.md) |
| 13 | Advanced RAG | Hybrid search + reranking | Semantic chunking | [`Week13.md`](weeks/Week13.md) |
| 14 | Reasoning Patterns Deep Dive | Pattern mastery | **All patterns (CoT, ReAct, ToT, PoT)** | [`Week14.md`](weeks/Week14.md) |
| 15 | Multi-Agent Systems | Agent coordination + communication | Multi-agent architectures | [`Week15.md`](weeks/Week15.md) |
| **Production Phase** |
| 16 | Production Optimization | Cost + performance optimization | Production best practices | [`Week16.md`](weeks/Week16.md) |
| 17 | Advanced Evaluation | Comprehensive evaluation framework | Custom metrics | [`Week17.md`](weeks/Week17.md) |
| 18 | Specialized Applications | Domain-specific applications | Industry use cases | [`Week18.md`](weeks/Week18.md) |
| 19 | Research & Experimentation | Research framework | Experimental design | [`Week19.md`](weeks/Week19.md) |
| 20 | Mastery & Beyond | Complete mastery + portfolio | Advanced portfolio | [`Week20.md`](weeks/Week20.md) |
| **Multi-Platform Mastery Phase** |
| 21 | Azure OpenAI Deep Dive | Multi-provider patterns | **Azure OpenAI + abstraction** | [`Week21.md`](weeks/Week21.md) |
| 22 | Multi-Language Implementation | Python, Go, Node.js apps | **Cross-language patterns** | [`Week22.md`](weeks/Week22.md) |
| 23 | Frontend Integration | React, Angular, Next.js apps | **Frontend LLM integration** | [`Week23.md`](weeks/Week23.md) |
| 24 | .NET Ecosystem | Aspire, Web API, Blazor apps | **Full-stack .NET** | [`Week24.md`](weeks/Week24.md) |
| 25 | Agentic Frameworks | LangChain, LangGraph, SDKs | **Framework mastery** | [`Week25.md`](weeks/Week25.md) |

---

## 📚 Learning Structure

### Weekly Structure

Each week follows this pattern:
- **5 days** × **30 minutes** = **2.5 hours total**
- **Day-by-day breakdown** with specific tasks
- **Exercises** with success criteria
- **Deliverables** to track progress
- **Deep dives** for key concepts (Weeks 3, 5, 14, 21-25)

### Key Deep Dives

- **Week 3**: Chain-of-Thought (CoT) - Complete patterns, examples, best practices
- **Week 5**: ReAct (Reasoning + Acting) - Full implementation guide
- **Week 14**: Reasoning Patterns - All patterns (CoT, ReAct, ToT, PoT, etc.)
- **Week 21**: Azure OpenAI - Setup, deployment, multi-provider patterns
- **Week 22**: Multi-Language - Python, Go, Node.js comparison
- **Week 23**: Frontend - React, Angular, Next.js integration
- **Week 24**: .NET - Full-stack .NET applications
- **Week 25**: Frameworks - LangChain, LangGraph, OpenAI/Azure SDKs

### Multi-Provider & Multi-Language Support

- **All weeks**: OpenAI + Azure OpenAI implementations
- **Weeks 22-24**: Multiple languages (Python, Go, Node.js, Angular, React, Next.js, .NET)
- **Week 25**: Agentic frameworks (LangChain, LangGraph, SDKs)

---

## 🏗 Workflow & Best Practices

### Daily Workflow (30 Minutes)

1. **(5m)** Review yesterday's result + decide single micro-goal
2. **(15-20m)** Implement / refine (one change only)
3. **(3m)** Run eval script; append to log
4. **(2m)** Capture decision in `docs/decisions.md`
5. **(Optional 5m)** Stage next hypothesis

**Consistency > intensity.**

### Project Structure

```
notebooks/          # Explorations (00_, 01_, ...)
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

### Core Best Practices

| Area | Guideline |
|------|-----------|
| Prompts | Externalize templates + version in Git; keep variables explicit |
| Data | Preserve raw, transform forward only (no in-place overwrites) |
| Eval | Always run baseline before claiming improvement |
| Tool Calling | Define JSON schema first; validate outputs defensively |
| Agents | Log reasoning / tool selection for post-mortem audits |
| Cost | Track cumulative token usage weekly; set soft budget ceiling |
| Reproducibility | Seed randomness (where supported) + pin critical deps |

### Experiment Logging

Track minimal but useful fields (CSV):

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

---

## 📊 Progress Tracking

### Weekly Checklist Template

Use this for each week:
- [ ] Week objectives completed
- [ ] All exercises finished
- [ ] Deliverables created
- [ ] Reflection documented
- [ ] Ready for next week

### Monthly Milestones

- [ ] **Month 1:** Can build basic LLM applications (Python, OpenAI + Azure OpenAI)
- [ ] **Month 2:** Can build RAG systems (Advanced patterns)
- [ ] **Month 3:** Can build multi-agent systems (ReAct, planning)
- [ ] **Month 4:** Can build production-ready applications (Deployment, optimization)
- [ ] **Month 5:** Can build full-stack LLM applications (Multi-language, frameworks)
- **Month 6+:** Complete mastery across all platforms

### Weekly Reflection Template

```markdown
## Week [X] Review - [Date]

### What I Learned
- 

### What I Built
- 

### Challenges Faced
- 

### Solutions Found
- 

### Next Week Goals
- 

### Time Spent
- Total: ___ hours
```

---

## 🆘 Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'openai'"**
- Solution: Activate virtual environment and run `pip install openai`

**"API key not found"**
- Solution: Check `.env` file exists, contains `OPENAI_API_KEY=...` (no spaces), and use `load_dotenv()`

**"Rate limit exceeded"**
- Solution: Add delays between calls: `time.sleep(1)`, or use different tier

**"Context length exceeded"**
- Solution: Split text into smaller chunks, or use model with larger context window

**"Invalid API key"**
- Solution: Verify key is correct, no extra spaces in `.env`, key is active

---

## 📚 Resources

### Essential Reading
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [LangChain Documentation](https://python.langchain.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Video Resources
- **Ed Donner's Udemy Course** (your primary resource)
- [Andrej Karpathy's LLM Course](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) - Deep dive

### Communities
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) - Reddit community
- [LangChain Discord](https://discord.gg/langchain) - Active community
- [Hugging Face Forums](https://discuss.huggingface.co/) - Model discussions

### Tools & Libraries
- **LangChain** - Framework for LLM applications
- **LangGraph** - Stateful agent workflows
- **LlamaIndex** - RAG framework
- **Gradio** - Easy UI for demos
- **Streamlit** - Alternative UI framework

---

## 🎓 Learning Tips

1. **Code Along:** Don't just watch - code along with the course
2. **Build Projects:** Apply concepts immediately to real projects
3. **Experiment:** Try variations of what you learn
4. **Document:** Write down what you learn and why
5. **Practice Daily:** Even 30 minutes daily beats 5 hours once a week
6. **Use Both Providers:** Practice with OpenAI and Azure OpenAI
7. **Explore Languages:** Try implementations in different languages (Weeks 22-24)

---

## 🏁 How to Use This Plan

1. **Start:** Read this document, then open [`Week1.md`](weeks/Week1.md)
2. **Progress:** Follow weekly guides day-by-day (5 days × 30 minutes)
3. **Track:** Use weekly checklists and reflection templates
4. **Adapt:** Adjust pacing based on your schedule (see adaptation notes in weekly guides)
5. **Reflect:** Complete weekly retrospectives to consolidate learning

---

## 📖 Detailed Weekly Guides

All 25 weeks have comprehensive day-by-day guides with:
- Learning objectives
- Daily task breakdowns
- Practical exercises
- Code examples (Python, Go, Node.js, Angular, React, Next.js, .NET)
- Deep dive sections for key concepts
- Deliverables and success criteria

**Start with:** [`docs/weeks/Week1.md`](weeks/Week1.md)

---

**Remember:** Learning LLM Engineering is a journey. Start with basics, build consistently, and don't be afraid to experiment. Every expert was once a beginner!

Evolve ruthlessly—delete stale experiments, promote reusable patterns, and keep learning velocity high.
