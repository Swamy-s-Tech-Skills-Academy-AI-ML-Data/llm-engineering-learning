# Week 1: Foundations & Environment Setup

**Theme:** Foundations & Environment  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Reproducible environment, API key management, working diagnostics notebook

---

## 🎯 Week 1 Learning Objectives

By the end of this week, you will:
- [ ] Set up a complete development environment for LLM Engineering
- [ ] Successfully make API calls to LLM providers (OpenAI, Anthropic, etc.)
- [ ] Understand API authentication and key management
- [ ] Create a diagnostics notebook to test your setup
- [ ] Understand tokens, context windows, and basic API parameters
- [ ] Handle errors and edge cases in API calls

---

## 📅 Day-by-Day Breakdown

### Day 1: Environment Setup (30 minutes)

**Learning Goal:** Set up Python environment and understand project structure

**Tasks (30 min):**
1. **Install Python** (5 min)
   - Verify Python 3.8+ is installed: `python --version`
   - If needed, install from [python.org](https://www.python.org/downloads/)

2. **Create Project Structure** (10 min)
   ```bash
   # Create project directory
   mkdir llm-engineering-learning
   cd llm-engineering-learning
   
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   
   # Create folder structure
   mkdir notebooks prompts rag eval agents tools scripts data docs
   mkdir data/raw data/processed
   ```

3. **Install Core Dependencies** (10 min)
   ```bash
   pip install openai anthropic python-dotenv requests jupyter
   pip freeze > requirements.txt
   ```

4. **Create .gitignore** (5 min)
   ```bash
   # Create .gitignore file
   echo "venv/
   .env
   __pycache__/
   *.pyc
   .ipynb_checkpoints/
   data/raw/*
   !data/raw/.gitkeep" > .gitignore
   ```

**Exercise:**
- [ ] Verify virtual environment is activated (you should see `(venv)` in terminal)
- [ ] Verify all packages installed: `pip list`
- [ ] Create a `README.md` with project description

**Resources:**
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- Ed Donner's Course: Lesson 1-2 (Setup & Environment)

---

### Day 2: API Keys & Authentication (30 minutes)

**Learning Goal:** Understand API key management and security best practices

**Tasks (30 min):**

1. **Get API Keys** (10 min)
   - OpenAI: Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy the key (you won't see it again!)

2. **Set Up Environment Variables** (10 min)
   ```bash
   # Create .env file in project root
   # NEVER commit this file!
   ```
   
   Create `.env` file:
   ```env
   # OpenAI
   OPENAI_API_KEY=sk-your-key-here
   
   # Azure OpenAI
   AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
   AZURE_OPENAI_API_KEY=your-azure-key-here
   AZURE_OPENAI_API_VERSION=2024-02-15-preview
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
   
   # Other providers (optional)
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```

3. **Create API Client Helper** (10 min)
   
   Create `scripts/api_client.py`:
   ```python
   import os
   from dotenv import load_dotenv
   from openai import OpenAI
   from openai import AzureOpenAI
   
   # Load environment variables
   load_dotenv()
   
   def get_openai_client():
       """Initialize and return OpenAI client"""
       api_key = os.getenv("OPENAI_API_KEY")
       if not api_key:
           raise ValueError("OPENAI_API_KEY not found in .env file")
       return OpenAI(api_key=api_key)
   
   def get_azure_openai_client():
       """Initialize and return Azure OpenAI client"""
       endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
       api_key = os.getenv("AZURE_OPENAI_API_KEY")
       api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
       
       if not endpoint or not api_key:
           raise ValueError("Azure OpenAI credentials not found in .env file")
       
       return AzureOpenAI(
           api_key=api_key,
           azure_endpoint=endpoint,
           api_version=api_version
       )
   
   def test_api_connection(provider="openai"):
       """Test if API connection works"""
       try:
           if provider == "openai":
               client = get_openai_client()
               response = client.chat.completions.create(
                   model="gpt-3.5-turbo",
                   messages=[{"role": "user", "content": "Say hello!"}],
                   max_tokens=10
               )
           elif provider == "azure_openai":
               client = get_azure_openai_client()
               deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo")
               response = client.chat.completions.create(
                   model=deployment,  # Azure uses deployment name
                   messages=[{"role": "user", "content": "Say hello!"}],
                   max_tokens=10
               )
           else:
               raise ValueError(f"Unknown provider: {provider}")
           
           print(f"✅ {provider.upper()} API connection successful!")
           print(f"Response: {response.choices[0].message.content}")
           return True
       except Exception as e:
           print(f"❌ {provider.upper()} API connection failed: {e}")
           return False
   
   if __name__ == "__main__":
       # Test both providers
       print("Testing OpenAI...")
       test_api_connection("openai")
       
       print("\nTesting Azure OpenAI...")
       test_api_connection("azure_openai")
   ```

**Exercise:**
- [ ] Run `python scripts/api_client.py` - should see success messages for both providers
- [ ] Verify `.env` is in `.gitignore`
- [ ] Test that you get an error if you remove the API keys
- [ ] Compare OpenAI vs Azure OpenAI response formats

**Security Checklist:**
- [ ] `.env` file is NOT committed to git
- [ ] `.env` is in `.gitignore`
- [ ] API keys are never hardcoded in scripts
- [ ] You understand the cost implications of API usage

**Resources:**
- Ed Donner's Course: Lesson 3 (API Authentication)
- [OpenAI API Key Best Practices](https://platform.openai.com/docs/guides/production-best-practices)

---

### Day 3: Your First LLM Call (30 minutes)

**Learning Goal:** Make your first successful API call and understand the response structure

**Tasks (30 min):**

1. **Create Hello World Script** (15 min)
   
   Create `notebooks/01_hello_llm.py`:
   ```python
   import sys
   sys.path.append('..')
   from scripts.api_client import get_openai_client
   
   def main():
       client = get_openai_client()
       
       # Your first LLM call!
       response = client.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": "What is LLM Engineering in one sentence?"}
           ],
           temperature=0.7,
           max_tokens=100
       )
       
       # Print the response
       print("Question: What is LLM Engineering?")
       print(f"Answer: {response.choices[0].message.content}")
       print(f"\nToken Usage:")
       print(f"  Input tokens: {response.usage.prompt_tokens}")
       print(f"  Output tokens: {response.usage.completion_tokens}")
       print(f"  Total tokens: {response.usage.total_tokens}")
   
   if __name__ == "__main__":
       main()
   ```

2. **Understand Response Structure** (10 min)
   - Study the response object
   - Understand `choices`, `usage`, `model` fields
   - Learn about `role` and `content` in messages

3. **Experiment with Parameters** (5 min)
   - Try different `temperature` values (0.0, 0.7, 1.0)
   - Try different `max_tokens` values
   - Observe how outputs change

**Exercise:**
- [ ] Run the script successfully
- [ ] Modify the prompt and see how response changes
- [ ] Try different models: `gpt-4`, `gpt-3.5-turbo`
- [ ] Document what you learned about parameters

**Key Concepts Learned:**
- Message roles: `system`, `user`, `assistant`
- Temperature: Controls randomness (0.0 = deterministic, 1.0 = creative)
- Max tokens: Limits response length
- Token usage: Track your API costs

**Resources:**
- Ed Donner's Course: Lesson 4 (Making Your First Call)
- [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat)

---

### Day 4: Diagnostics Notebook (30 minutes)

**Learning Goal:** Create a comprehensive diagnostics notebook to test your entire setup

**Tasks (30 min):**

1. **Create Jupyter Notebook** (25 min)
   
   Create `notebooks/00_diagnostics.ipynb` with these cells:

   **Cell 1: Import and Setup**
   ```python
   import sys
   sys.path.append('..')
   import os
   from dotenv import load_dotenv
   from openai import OpenAI
   from scripts.api_client import get_openai_client
   
   load_dotenv()
   print("✅ Environment loaded")
   ```

   **Cell 2: API Key Check**
   ```python
   api_key = os.getenv("OPENAI_API_KEY")
   if api_key:
       print(f"✅ API Key found: {api_key[:10]}...")
   else:
       print("❌ API Key not found!")
   ```

   **Cell 3: Token Counting Test**
   ```python
   from tiktoken import get_encoding
   
   encoding = get_encoding("cl100k_base")  # GPT-3.5/GPT-4 encoding
   
   test_text = "Hello, this is a test of token counting!"
   tokens = encoding.encode(test_text)
   
   print(f"Text: {test_text}")
   print(f"Tokens: {len(tokens)}")
   print(f"Token IDs: {tokens[:5]}...")  # Show first 5
   ```

   **Cell 4: Simple API Call**
   ```python
   client = get_openai_client()
   
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": "Count to 5"}],
       max_tokens=20
   )
   
   print("Response:", response.choices[0].message.content)
   print("Usage:", response.usage.total_tokens, "tokens")
   ```

   **Cell 5: Error Handling Test**
   ```python
   # Test error handling
   try:
       client = get_openai_client()
       response = client.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[{"role": "user", "content": "Test"}],
           max_tokens=10
       )
       print("✅ API call successful")
   except Exception as e:
       print(f"❌ Error: {type(e).__name__}: {e}")
   ```

2. **Run All Cells** (5 min)
   - Execute each cell
   - Verify all checks pass
   - Fix any errors

**Exercise:**
- [ ] All cells execute successfully
- [ ] Add a cell that tests Anthropic API (if you have key)
- [ ] Add a cell that calculates estimated cost for a sample call
- [ ] Save the notebook

**Deliverable:**
- Working `notebooks/00_diagnostics.ipynb` with all tests passing

**Resources:**
- [Jupyter Notebook Tutorial](https://jupyter-notebook.readthedocs.io/)
- [tiktoken Library](https://github.com/openai/tiktoken) - Token counting

---

### Day 5: Review & Practice (30 minutes)

**Learning Goal:** Consolidate Week 1 learning and prepare for Week 2

**Tasks (30 min):**

1. **Review Week 1 Concepts** (10 min)
   - [ ] Environment setup complete
   - [ ] API keys secured
   - [ ] First API call successful
   - [ ] Diagnostics notebook working
   - [ ] Understand tokens and context windows

2. **Complete Any Missing Exercises** (10 min)
   - Review all exercises from Days 1-4
   - Complete any you skipped
   - Fix any errors

3. **Reflection & Documentation** (10 min)
   
   Create `docs/week01_reflection.md`:
   ```markdown
   # Week 1 Reflection
   
   ## What I Learned
   - 
   
   ## What Was Challenging
   - 
   
   ## Key Takeaways
   - 
   
   ## Questions for Next Week
   - 
   ```

4. **Prepare for Week 2** (5 min)
   - Review Week 2 preview in learning-plan.md
   - Ensure all Week 1 deliverables are complete

**Week 1 Deliverables Checklist:**
- [ ] Virtual environment created and activated
- [ ] `.env` file with API keys (not committed)
- [ ] `scripts/api_client.py` working
- [ ] `notebooks/00_diagnostics.ipynb` complete and passing
- [ ] `notebooks/01_hello_llm.py` working
- [ ] `requirements.txt` created
- [ ] `.gitignore` configured
- [ ] Week 1 reflection completed

**Self-Assessment:**
- [ ] Can I explain what tokens are?
- [ ] Can I make an API call without looking at documentation?
- [ ] Do I understand why `.env` files shouldn't be committed?
- [ ] Can I read and understand API response structure?

---

## 🧠 Deep Dive: Understanding Tokens & Context Windows

### What Are Tokens?

**Tokens** are the units LLMs process. They're not exactly words:
- 1 token ≈ 0.75 words (English)
- 1 token ≈ 3-4 characters
- Common words = 1 token
- Rare/complex words = multiple tokens

**Example:**
```
"Hello world" = 2 tokens
"LLM Engineering" = 3 tokens (LLM + Engineering = 3)
"ChatGPT" = 1 token
```

### Why Tokens Matter

1. **Cost**: You pay per token (input + output)
   - GPT-3.5-turbo: ~$0.0015 per 1K input tokens, $0.002 per 1K output tokens
   - Example: 1000 input + 500 output = ~$0.0025

2. **Context Window**: Maximum tokens in a conversation
   - GPT-3.5-turbo: 16,385 tokens
   - GPT-4: 8,192 tokens (some variants have 32,768)
   - Exceeding = error or truncation

3. **Speed**: More tokens = slower responses

### Practice Exercise

Create a token counting utility:

```python
import tiktoken

def count_tokens(text, model="gpt-3.5-turbo"):
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Test
text = "This is a sample text for token counting."
print(f"Text: {text}")
print(f"Tokens: {count_tokens(text)}")
print(f"Estimated cost (GPT-3.5): ${count_tokens(text) * 0.0015 / 1000:.6f}")
```

---

## 🎯 Week 1 Success Criteria

You've successfully completed Week 1 if:
- ✅ You can make API calls without errors
- ✅ Your diagnostics notebook runs end-to-end
- ✅ You understand token counting basics
- ✅ Your API keys are secure (not committed)
- ✅ You can explain what happens in an API call

---

## 📚 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- Ed Donner's Course: Weeks 1-2 (Setup & Basics)

---

## 🔄 Next Week Preview

**Week 2:** Python & Data Handling
- Working with different data formats (CSV, JSON, TXT)
- Data cleaning and preprocessing
- Chunking text for LLMs
- Building data ingestion scripts

---

**Remember:** Take your time, experiment, and don't rush. Understanding the fundamentals deeply will make everything easier later!

