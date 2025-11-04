# LLM Engineering Learning Plan

**Complete guide for mastering LLM Engineering from basics to advanced**

This learning plan is designed to accompany **Ed Donner's "LLM Engineering: Master AI, Large Language Models & Agents"** Udemy course. Use this as your structured roadmap to build practical skills alongside the course content.

---

## 📋 Table of Contents

1. [Getting Started - Absolute Basics](#-getting-started---absolute-basics)
2. [Prerequisites & Fundamentals](#-prerequisites--fundamentals)
3. [Week-by-Week Detailed Breakdown](#-week-by-week-detailed-breakdown)
4. [Quick Start](#-quick-start-minimal)
5. [12-Week Learning Path](#-12week-learning-path-30-min--day)
6. [Daily Workflow](#-workflow-pattern-daily-30-minutes)
7. [Hands-On Exercises](#-hands-on-exercises)
8. [Resources & References](#-resources--references)
9. [Progress Tracking](#-progress-tracking)
10. [Troubleshooting Guide](#-troubleshooting-guide)
11. [Common Questions & Answers](#-common-questions--answers)

---

## 🌱 Getting Started - Absolute Basics

### Step 1: Understanding What You're Learning

**What is LLM Engineering?**
- LLM Engineering is the practical application of Large Language Models (like ChatGPT) to solve real-world problems
- It involves: writing prompts, connecting to APIs, building applications, and optimizing performance
- Think of it as software engineering + AI/ML concepts

**Why This Matters:**
- LLMs can understand and generate human-like text
- They can be "programmed" through prompts (no traditional coding needed for basic tasks)
- LLM Engineers build systems that use these models effectively

### Step 2: Your First 30 Minutes

**Goal:** Make your first API call to an LLM

**What You'll Do:**
1. Install Python (if not already installed)
2. Create a virtual environment
3. Install required packages
4. Make your first API call
5. See the LLM respond!

**Step-by-Step:**

```bash
# 1. Check if Python is installed
python --version  # Should show Python 3.8 or higher

# 2. Create a project folder
mkdir llm-learning
cd llm-learning

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 5. Install required packages
pip install openai python-dotenv requests

# 6. Create a .env file for your API key
# Get API key from: https://platform.openai.com/api-keys
# Create .env file with: OPENAI_API_KEY=your-key-here
```

**Your First Script (`hello_llm.py`):**

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make your first API call!
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Say hello and tell me what you can do!"}
    ]
)

print(response.choices[0].message.content)
```

**Run it:**
```bash
python hello_llm.py
```

**Congratulations!** You just made your first LLM call! 🎉

### Step 3: Understanding the Basics - Key Concepts

**1. What is a Prompt?**
- A prompt is the text you send to the LLM
- It's like giving instructions to a very smart assistant
- Example: "Write a short story about a robot learning to paint"

**2. What is an API?**
- API = Application Programming Interface
- It's how your code talks to the LLM service
- You send a request → LLM processes it → You get a response

**3. What is Tokenization?**
- LLMs don't understand words directly
- They convert text into "tokens" (pieces of text)
- Roughly: 1 token ≈ 3-4 characters or 0.75 words
- Example: "Hello world" = ~2 tokens

**4. What is Temperature?**
- Controls how "creative" or "random" the LLM is
- 0.0 = very focused, deterministic
- 1.0 = very creative, varied
- Default: 0.7 (balanced)

**5. What is Context Window?**
- The maximum amount of text the LLM can "remember" in one conversation
- Example: GPT-3.5-turbo has ~16,000 tokens context window
- If you exceed this, older parts get "forgotten"

### Step 4: Your Learning Path

**Week 0 (This Week):** Setup & Basics
- [ ] Complete Step 1-3 above
- [ ] Watch first 2-3 lessons from Ed Donner's course
- [ ] Make 5 different API calls with different prompts
- [ ] Understand what each parameter does (temperature, max_tokens, etc.)

**Next Steps:** Continue to Prerequisites section below, then follow the 12-week plan

---

## 🎯 Prerequisites & Fundamentals

Before diving into LLM Engineering, ensure you have these foundational skills:

### Essential Prerequisites

**Python Basics (Required)**
- [ ] Variables, data types (strings, lists, dictionaries)
- [ ] Functions and function arguments
- [ ] Working with JSON data
- [ ] File I/O (reading/writing files)
- [ ] Error handling (try/except)
- [ ] List comprehensions
- [ ] Working with libraries (import statements)

**Command Line (Required)**
- [ ] Basic navigation (`cd`, `ls`/`dir`, `pwd`)
- [ ] Running Python scripts
- [ ] Understanding file paths

**Git Basics (Recommended)**
- [ ] `git clone`, `git add`, `git commit`, `git push`
- [ ] Understanding `.gitignore`

**APIs & HTTP (Helpful)**
- [ ] What is an API?
- [ ] REST API concepts (GET, POST requests)
- [ ] API keys and authentication
- [ ] JSON response format

### Core Concepts to Understand First

**1. What are Large Language Models (LLMs)?**
- Transformers architecture (high-level understanding)
- Tokenization (text → tokens → embeddings)
- Context windows and limitations
- Prompt vs completion
- Temperature and sampling parameters

**2. API Basics**
- How to make API calls in Python (`requests` library)
- Authentication with API keys
- Handling API responses
- Error handling for API failures

**3. Data Formats**
- JSON structure and parsing
- CSV files for data/logging
- Text files for prompts and templates

**4. Environment Management**
- Virtual environments (why and how)
- Dependency management
- Environment variables (`.env` files)

### Learning Resources for Prerequisites

If you need to strengthen fundamentals:

- **Python**: [Python.org Tutorial](https://docs.python.org/3/tutorial/), [Real Python](https://realpython.com/)
- **APIs**: [HTTPie Guide](https://httpie.io/docs), [Postman Learning](https://learning.postman.com/)
- **Git**: [Git Handbook](https://guides.github.com/introduction/git-handbook/)

### Self-Assessment Quiz

Before moving forward, can you:
- [ ] Write a Python function that takes a list and returns only even numbers?
- [ ] Make an HTTP request using Python's `requests` library?
- [ ] Read a JSON file and extract specific values?
- [ ] Create and activate a Python virtual environment?
- [ ] Explain what an API key is and why it's important to keep it secret?

**If you answered "No" to 2+ questions:** Spend 2-3 days on Python basics first. Don't rush - strong fundamentals make everything easier!

---

## 📚 Week-by-Week Detailed Breakdown

### Week 1: Foundations & Environment (Days 1-7)

**Day 1-2: Setup**
- Complete the "Getting Started" section above
- Set up your development environment
- Create your first successful API call
- **Exercise:** Create `notebooks/00_diagnostics.ipynb` with:
  - API key loading test
  - Simple "hello world" LLM call
  - Token counting test
  - Error handling examples

**Day 3-4: Understanding API Calls**
- Learn different API providers (OpenAI, Anthropic, etc.)
- Understand request/response structure
- Practice with different models
- **Exercise:** Create a script that calls 3 different models and compares responses

**Day 5-6: Environment Management**
- Master virtual environments
- Learn `.env` file management
- Set up project structure
- **Exercise:** Create a proper project structure with folders

**Day 7: Review & Practice**
- Review Week 1 concepts
- Complete any unfinished exercises
- Watch corresponding course videos
- **Deliverable:** Working diagnostics notebook

### Week 2: Python & Data Handling (Days 8-14)

**Day 8-9: Python for LLM Engineering**
- Review Python basics (lists, dicts, functions)
- Working with JSON data
- File I/O operations
- **Exercise:** Create a script that reads a text file and sends it to an LLM for summarization

**Day 10-11: Data Processing**
- Loading different data formats (CSV, JSON, TXT)
- Data cleaning basics
- Chunking text for LLMs
- **Exercise:** Create `scripts/ingest.py` that processes a dataset

**Day 12-13: Error Handling**
- Try/except blocks
- API error handling
- Retry logic
- **Exercise:** Add robust error handling to your API calls

**Day 14: Review & Practice**
- Review Week 2 concepts
- Complete data processing script
- **Deliverable:** Working `scripts/ingest.py`

### Week 3: LLM & Prompt Engineering (Days 15-21)

**Day 15-16: Prompt Fundamentals**
- What makes a good prompt?
- Prompt structure (context, task, examples)
- Zero-shot vs few-shot prompting
- **Exercise:** Create 5 different prompts for the same task and compare results

**Day 17-18: Prompt Patterns**
- Chain-of-thought prompting
- Role-based prompting
- Template-based prompts
- **Exercise:** Create a prompt template system in `prompts/` folder

**Day 19-20: Prompt Evaluation**
- How to measure prompt quality?
- A/B testing prompts
- Creating evaluation metrics
- **Exercise:** Set up `eval/experiment_log.csv` and log your first experiments

**Day 21: Review & Practice**
- Review Week 3 concepts
- Create prompt library
- **Deliverable:** Prompt variant matrix with evaluation results

---

## 🚀 Quick Start (Minimal)

1. Clone & create environment:

 ```bash
 # Install uv if needed (see README for installation instructions)
 # Then:
 uv sync
 ```

1. Create baseline folders (only what you need now):

 `prompts/`, `notebooks/`, `rag/`, `eval/`, `agents/`, `scripts/`, `data/raw/`, `data/processed/`

1. Add a first notebook: `notebooks/00_diagnostics.ipynb` (token tests, API keys load, simple embedding call).

1. Start an experiment log: `eval/experiment_log.csv` (see Metrics section).

1. Commit early: small, frequent, tagged by week (`week01_prompt_basics`).

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

## 🧪 Hands-On Exercises

### Exercise 1: Your First LLM Application (Week 1)
**Goal:** Build a simple text summarizer

**Steps:**
1. Create a script that reads a long text file
2. Split it into chunks (if needed)
3. Send each chunk to LLM for summarization
4. Combine summaries
5. Save the result

**Success Criteria:**
- [ ] Script runs without errors
- [ ] Produces a summary shorter than original
- [ ] Handles errors gracefully

### Exercise 2: Prompt Engineering Practice (Week 3)
**Goal:** Optimize a prompt for a specific task

**Task:** Create a prompt that extracts key information from product reviews

**Steps:**
1. Write 3 different prompt versions
2. Test each on 10 sample reviews
3. Evaluate which works best
4. Document your findings

**Success Criteria:**
- [ ] At least 80% accuracy in extracting key info
- [ ] Documented comparison of all 3 prompts
- [ ] Best prompt saved in `prompts/` folder

### Exercise 3: Data Pipeline (Week 2)
**Goal:** Build a data processing pipeline

**Steps:**
1. Download or create a dataset (CSV or JSON)
2. Clean the data (remove nulls, format text)
3. Process it into chunks suitable for LLM
4. Save processed data

**Success Criteria:**
- [ ] Pipeline handles edge cases
- [ ] Code is well-commented
- [ ] Processed data is saved correctly

### Exercise 4: Evaluation System (Week 3)
**Goal:** Build a simple evaluation framework

**Steps:**
1. Create evaluation dataset (10-20 examples)
2. Write evaluation script that:
   - Runs prompts on dataset
   - Measures accuracy/relevance
   - Logs results to CSV
3. Compare different prompt versions

**Success Criteria:**
- [ ] Automated evaluation script works
- [ ] Results are logged properly
- [ ] Can compare different approaches

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

- Foundations: env, APIs, Git hygiene
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

- [ ] Virtual environment created and activated
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

- Bootstrap: Follow Quick Start + Checklist.
- Guide pacing: Use Week plan table; adjust via Adaptation matrix.
- Improve deliberately: Log everything; compare against baselines.
- Reflect: Run weekly retrospective loop.

---

## 🆘 Troubleshooting Guide

### Common Issues & Solutions

**Issue: "ModuleNotFoundError: No module named 'openai'"**
- **Solution:** Make sure you've activated your virtual environment and run `pip install openai`

**Issue: "API key not found"**
- **Solution:** 
  1. Check that `.env` file exists in project root
  2. Verify file contains `OPENAI_API_KEY=your-key-here` (no spaces around `=`)
  3. Make sure you're loading it with `load_dotenv()`

**Issue: "Rate limit exceeded"**
- **Solution:** 
  - You're making too many API calls too quickly
  - Add delays between calls: `time.sleep(1)`
  - Consider using a different tier or API provider

**Issue: "Context length exceeded"**
- **Solution:**
  - Your input is too long for the model's context window
  - Split your text into smaller chunks
  - Use a model with larger context window

**Issue: "Invalid API key"**
- **Solution:**
  - Check that your API key is correct
  - Make sure there are no extra spaces in `.env` file
  - Verify the key is active in your account

---

## ❓ Common Questions & Answers

### Q: Do I need to know deep learning to learn LLM Engineering?
**A:** No! LLM Engineering focuses on using existing models, not building them. Understanding how they work helps, but you don't need to train models.

### Q: How much Python do I need to know?
**A:** Basic to intermediate level is sufficient. You should be comfortable with:
- Variables, functions, loops
- Lists and dictionaries
- File operations
- Error handling

### Q: Which API provider should I use?
**A:** Start with OpenAI (most tutorials use it). Once comfortable, try:
- Anthropic (Claude) - great for long contexts
- Google (Gemini) - good free tier
- Open source models (Ollama) - free, local

### Q: How much will this cost?
**A:** 
- Learning: Free tier often sufficient (OpenAI gives $5 credit)
- Practice: $10-20/month for moderate usage
- Production: Varies widely, but optimization helps

### Q: How long until I'm "job-ready"?
**A:** 
- 3 months: Basic proficiency, can build simple apps
- 6 months: Intermediate level, portfolio projects
- 12+ months: Advanced, production-ready systems

**Focus on building projects, not just time!**

### Q: Should I focus on one model or try many?
**A:** Start with one (GPT-3.5-turbo or GPT-4), master it, then explore others. Understanding one deeply > knowing many superficially.

### Q: How do I track my progress?
**A:** 
- Use the experiment log (`eval/experiment_log.csv`)
- Weekly retrospectives (see template above)
- GitHub commits to track code progress
- Keep a learning journal

---

## 📊 Progress Tracking

### Weekly Progress Checklist

**Week 1 Checklist:**
- [ ] Environment set up and working
- [ ] Made first successful API call
- [ ] Created diagnostics notebook
- [ ] Understand basic API concepts
- [ ] Can explain what tokens are

**Week 2 Checklist:**
- [ ] Can process different data formats
- [ ] Created data ingestion script
- [ ] Understand error handling
- [ ] Can chunk text properly

**Week 3 Checklist:**
- [ ] Created prompt templates
- [ ] Understand prompt engineering basics
- [ ] Set up evaluation system
- [ ] Can compare different prompts

**Monthly Milestones:**
- [ ] **Month 1:** Can build basic LLM applications
- [ ] **Month 2:** Can build RAG systems
- [ ] **Month 3:** Can build multi-agent systems
- [ ] **Month 4+:** Can build production-ready applications

---

## 🎓 Learning Tips for Success

1. **Code Along:** Don't just watch the course - code along with it
2. **Build Projects:** Apply concepts immediately to real projects
3. **Experiment:** Try variations of what you learn
4. **Document:** Write down what you learn and why
5. **Join Community:** Engage with others learning (Discord, Reddit, etc.)
6. **Stay Curious:** LLM field moves fast - keep learning
7. **Practice Daily:** Even 30 minutes daily beats 5 hours once a week

---

## 🔄 Weekly Review Template

Use this template every Friday to review your week:

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

### Questions to Research
- 

### Time Spent
- Total: ___ hours
- Most productive session: ___ hours on [topic]
```

---

## 📚 Resources & References

### Essential Reading
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [LangChain Documentation](https://python.langchain.com/) - Useful library
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### Video Resources
- Ed Donner's Udemy Course (your primary resource)
- [Andrej Karpathy's LLM Course](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) - Deep dive
- [Fast.ai Practical Deep Learning](https://course.fast.ai/) - ML fundamentals

### Communities
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) - Reddit community
- [LangChain Discord](https://discord.gg/langchain) - Active community
- [Hugging Face Forums](https://discuss.huggingface.co/) - Model discussions

### Tools & Libraries
- **LangChain** - Framework for LLM applications
- **LlamaIndex** - RAG framework
- **Gradio** - Easy UI for demos
- **Streamlit** - Alternative UI framework

---

Evolve ruthlessly—delete stale experiments, promote reusable patterns, and keep learning velocity high.

**Remember:** Learning LLM Engineering is a journey. Start with basics, build consistently, and don't be afraid to experiment. Every expert was once a beginner!

---

<!-- END ORIGINAL CONTENT -->
