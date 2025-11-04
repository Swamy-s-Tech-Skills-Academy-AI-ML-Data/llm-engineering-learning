# Week 4: Bots & Scraping

**Theme:** Bots & Scraping  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Basic scraper feeding LLM summarizer  
**Platforms:** OpenAI + Azure OpenAI (Python) - Dual provider support from Week 1

---

## 🎯 Week 4 Learning Objectives

By the end of this week, you will:
- [ ] Understand web scraping basics
- [ ] Build a web scraper for text extraction
- [ ] Integrate scraping with LLM summarization
- [ ] Create a news/website summarizer bot
- [ ] Handle errors and edge cases in scraping
- [ ] Compare OpenAI vs Azure OpenAI for summarization tasks

---

## 📅 Day-by-Day Breakdown

### Day 1: Web Scraping Basics (30 minutes)

**Learning Goal:** Learn web scraping fundamentals

**Tasks (30 min):**

1. **Install Scraping Libraries** (5 min)
   ```bash
   pip install beautifulsoup4 requests lxml
   ```

2. **Basic Web Scraping** (15 min)
   
   Create `scripts/scraper_basic.py`:
   ```python
   import requests
   from bs4 import BeautifulSoup
   
   def scrape_url(url: str) -> str:
       """Scrape text content from a URL"""
       try:
           response = requests.get(url, timeout=10)
           response.raise_for_status()
           
           soup = BeautifulSoup(response.content, 'html.parser')
           
           # Remove script and style elements
           for script in soup(["script", "style"]):
               script.decompose()
           
           # Get text
           text = soup.get_text()
           
           # Clean up whitespace
           lines = (line.strip() for line in text.splitlines())
           chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
           text = ' '.join(chunk for chunk in chunks if chunk)
           
           return text
       except Exception as e:
           print(f"Error scraping {url}: {e}")
           return ""
   ```

3. **Test Scraping** (10 min)
   - Test on a simple website
   - Verify text extraction works

**Exercise:**
- [ ] Scrape 3 different websites
- [ ] Compare extracted text quality
- [ ] Handle errors gracefully

**Resources:**
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Ed Donner's Course: Web Scraping Basics

---

### Day 2: Advanced Scraping & Text Extraction (30 minutes)

**Learning Goal:** Improve text extraction quality

**Tasks (30 min):**

1. **Content-Specific Extraction** (15 min)
   ```python
   def extract_article_content(soup: BeautifulSoup) -> str:
       """Extract main article content"""
       # Try common article selectors
       selectors = [
           'article',
           '.article-content',
           '#article-body',
           'main',
           '.content'
       ]
       
       for selector in selectors:
           content = soup.select_one(selector)
           if content:
               return content.get_text()
       
       # Fallback to body
       return soup.body.get_text() if soup.body else ""
   ```

2. **Handle Different Content Types** (15 min)
   - Articles
   - Blog posts
   - News pages
   - Documentation

**Exercise:**
- [ ] Create content extractor for different site types
- [ ] Test on news sites, blogs, documentation

---

### Day 3: LLM Integration for Summarization (30 minutes)

**Learning Goal:** Combine scraping with LLM summarization

**Tasks (30 min):**

1. **Create Summarizer Bot** (20 min)
   
   Create `scripts/summarizer_bot.py`:
   ```python
   from scripts.scraper_basic import scrape_url
   from scripts.api_client import get_openai_client
   from scripts.chunking import chunk_by_tokens
   
   def summarize_url(url: str, max_length: int = 200) -> dict:
       """Scrape URL and summarize with LLM"""
       
       # Scrape content
       print(f"Scraping {url}...")
       content = scrape_url(url)
       
       if not content:
           return {"error": "Failed to scrape URL"}
       
       # Chunk if too long
       chunks = chunk_by_tokens(content, max_tokens=3000)
       
       # Summarize each chunk
       summaries = []
       client = get_openai_client()
       
       for i, chunk in enumerate(chunks):
           prompt = f"""
           Summarize the following content in {max_length} words or less:
           
           {chunk}
           
           Summary:
           """
           
           response = client.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[{"role": "user", "content": prompt}],
               max_tokens=300
           )
           
           summaries.append(response.choices[0].message.content)
       
       # Combine summaries
       final_summary = " ".join(summaries)
       
       return {
           "url": url,
           "original_length": len(content),
           "summary": final_summary,
           "summary_length": len(final_summary)
       }
   ```

2. **Test Summarizer** (10 min)
   - Test on different websites
   - Verify summaries are accurate

**Exercise:**
- [ ] Summarize 3 different articles
- [ ] Compare original vs summary length
- [ ] Evaluate summary quality

---

### Day 4: Building Complete Bot (30 minutes)

**Learning Goal:** Build a production-ready summarizer bot

**Tasks (30 min):**

1. **Add Error Handling** (10 min)
   - Network errors
   - Invalid URLs
   - Empty content
   - API failures

2. **Add Caching** (10 min)
   ```python
   import hashlib
   import json
   from pathlib import Path
   
   def get_cache_key(url: str) -> str:
       """Generate cache key from URL"""
       return hashlib.md5(url.encode()).hexdigest()
   
   def load_from_cache(url: str) -> dict:
       """Load summary from cache if exists"""
       cache_file = Path(f"cache/{get_cache_key(url)}.json")
       if cache_file.exists():
           return json.load(cache_file.open())
       return None
   
   def save_to_cache(url: str, summary: dict):
       """Save summary to cache"""
       Path("cache").mkdir(exist_ok=True)
       cache_file = Path(f"cache/{get_cache_key(url)}.json")
       cache_file.write_text(json.dumps(summary, indent=2))
   ```

3. **Create CLI Interface** (10 min)
   ```python
   import argparse
   
   def main():
       parser = argparse.ArgumentParser(description="URL Summarizer Bot")
       parser.add_argument("url", help="URL to summarize")
       parser.add_argument("--max-length", type=int, default=200)
       
       args = parser.parse_args()
       
       result = summarize_url(args.url, args.max_length)
       print(json.dumps(result, indent=2))
   
   if __name__ == "__main__":
       main()
   ```

**Exercise:**
- [ ] Complete bot with all features
- [ ] Test CLI interface
- [ ] Document usage

**Deliverable:** Working `scripts/summarizer_bot.py`

---

### Day 5: Review & Practice (30 minutes)

**Learning Goal:** Consolidate Week 4 learning

**Tasks (30 min):**

1. **Review Concepts** (10 min)
2. **Complete Exercises** (10 min)
3. **Week 4 Reflection** (10 min)

**Week 4 Deliverables:**
- [ ] `scripts/scraper_basic.py`
- [ ] `scripts/summarizer_bot.py`
- [ ] Tested on multiple websites
- [ ] Week 4 reflection

---

## 🔄 Next Week Preview

**Week 5:** Multi-Agent Intro + ReAct Deep Dive
- Introduction to agents
- ReAct (Reasoning + Acting) pattern
- Building agent loops
- Tool integration

