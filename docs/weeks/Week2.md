# Week 2: Python & Data Handling

**Theme:** Python & Data Handling  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Clean data ingestion + utilities (`scripts/ingest.py`)  
**Platforms:** OpenAI + Azure OpenAI (Python) - Dual provider support from Week 1

---

## 🎯 Week 2 Learning Objectives

By the end of this week, you will:
- [ ] Master Python data structures for LLM engineering
- [ ] Read and process different file formats (CSV, JSON, TXT)
- [ ] Clean and preprocess text data
- [ ] Chunk text for LLM processing
- [ ] Build robust data ingestion scripts
- [ ] Handle errors and edge cases in data processing
- [ ] Use both OpenAI and Azure OpenAI for data processing tasks

---

## 📅 Day-by-Day Breakdown

### Day 1: Python Fundamentals for LLM Engineering (30 minutes)

**Learning Goal:** Review and strengthen Python skills specific to LLM work

**Tasks (30 min):**

1. **Data Structures Review** (10 min)
   ```python
   # Lists - for batches, chunks
   texts = ["text1", "text2", "text3"]
   
   # Dictionaries - for API responses, configs
   config = {
       "model": "gpt-3.5-turbo",
       "temperature": 0.7,
       "max_tokens": 100
   }
   
   # List of dictionaries - for structured data
   messages = [
       {"role": "user", "content": "Hello"},
       {"role": "assistant", "content": "Hi there!"}
   ]
   ```

2. **JSON Handling** (10 min)
   
   Create `scripts/json_practice.py`:
   ```python
   import json
   
   # Read JSON
   with open('data/raw/sample.json', 'r') as f:
       data = json.load(f)
   
   # Write JSON
   output = {"result": "success", "tokens": 100}
   with open('data/processed/output.json', 'w') as f:
       json.dump(output, f, indent=2)
   
   # Parse JSON strings
   json_str = '{"key": "value"}'
   data = json.loads(json_str)
   ```

3. **File I/O Best Practices** (10 min)
   ```python
   # Reading text files
   with open('data/raw/text.txt', 'r', encoding='utf-8') as f:
       content = f.read()
   
   # Reading line by line (for large files)
   with open('data/raw/large.txt', 'r', encoding='utf-8') as f:
       for line in f:
           process_line(line)
   ```

**Exercise:**
- [ ] Create `scripts/data_utils.py` with helper functions
- [ ] Practice reading/writing JSON files
- [ ] Handle encoding errors (try different encodings)

**Resources:**
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- Ed Donner's Course: Data Handling Basics

---

### Day 2: CSV & Data Processing (30 minutes)

**Learning Goal:** Process CSV files and extract text for LLM processing

**Tasks (30 min):**

1. **CSV Reading** (15 min)
   
   Create `scripts/csv_processor.py`:
   ```python
   import csv
   from typing import List, Dict
   
   def read_csv(filepath: str) -> List[Dict]:
       """Read CSV file and return list of dictionaries"""
       data = []
       with open(filepath, 'r', encoding='utf-8') as f:
           reader = csv.DictReader(f)
           for row in reader:
               data.append(row)
       return data
   
   def extract_text_column(data: List[Dict], column: str) -> List[str]:
       """Extract specific column as list of strings"""
       return [row[column] for row in data if column in row]
   
   # Example usage
   if __name__ == "__main__":
       data = read_csv('data/raw/reviews.csv')
       texts = extract_text_column(data, 'review_text')
       print(f"Loaded {len(texts)} texts")
   ```

2. **Data Cleaning Basics** (15 min)
   ```python
   def clean_text(text: str) -> str:
       """Basic text cleaning"""
       # Remove extra whitespace
       text = ' '.join(text.split())
       # Remove special characters (optional)
       # text = re.sub(r'[^\w\s]', '', text)
       return text.strip()
   
   def remove_empty(data: List[str]) -> List[str]:
       """Remove empty strings"""
       return [item for item in data if item.strip()]
   ```

**Exercise:**
- [ ] Create a sample CSV file with text data
- [ ] Process it using your script
- [ ] Add error handling for missing files/columns

**Resources:**
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)

---

### Day 3: Text Chunking for LLMs (30 minutes)

**Learning Goal:** Split long texts into chunks that fit LLM context windows

**Tasks (30 min):**

1. **Simple Chunking** (10 min)
   ```python
   def chunk_by_sentences(text: str, chunk_size: int = 1000) -> List[str]:
       """Split text into chunks by sentences"""
       sentences = text.split('. ')
       chunks = []
       current_chunk = []
       current_size = 0
       
       for sentence in sentences:
           sentence_size = len(sentence)
           if current_size + sentence_size > chunk_size:
               chunks.append('. '.join(current_chunk) + '.')
               current_chunk = [sentence]
               current_size = sentence_size
           else:
               current_chunk.append(sentence)
               current_size += sentence_size
       
       if current_chunk:
           chunks.append('. '.join(current_chunk))
       return chunks
   ```

2. **Token-Aware Chunking** (15 min)
   
   Create `scripts/chunking.py`:
   ```python
   import tiktoken
   
   def chunk_by_tokens(text: str, max_tokens: int = 1000, 
                       model: str = "gpt-3.5-turbo") -> List[str]:
       """Split text into chunks with token limits"""
       encoding = tiktoken.encoding_for_model(model)
       tokens = encoding.encode(text)
       
       chunks = []
       for i in range(0, len(tokens), max_tokens):
           chunk_tokens = tokens[i:i + max_tokens]
           chunk_text = encoding.decode(chunk_tokens)
           chunks.append(chunk_text)
       
       return chunks
   ```

3. **Overlap Strategy** (5 min)
   ```python
   def chunk_with_overlap(text: str, chunk_size: int = 1000, 
                         overlap: int = 100) -> List[str]:
       """Chunk text with overlapping windows"""
       chunks = []
       start = 0
       
       while start < len(text):
           end = start + chunk_size
           chunk = text[start:end]
           chunks.append(chunk)
           start = end - overlap  # Overlap
       
       return chunks
   ```

**Exercise:**
- [ ] Test chunking on a long text file
- [ ] Verify chunks don't exceed token limits
- [ ] Compare chunk_by_sentences vs chunk_by_tokens

**Key Concept:** Chunking prevents context window overflow and improves retrieval.

---

### Day 4: Building Data Ingestion Script (30 minutes)

**Learning Goal:** Create a complete data ingestion pipeline

**Tasks (30 min):**

1. **Create Main Ingestion Script** (25 min)
   
   Create `scripts/ingest.py`:
   ```python
   import os
   import json
   import csv
   from pathlib import Path
   from typing import List, Dict
   from scripts.chunking import chunk_by_tokens
   from scripts.data_utils import clean_text
   
   def ingest_file(filepath: str, output_dir: str = "data/processed"):
       """Ingest a file and prepare it for LLM processing"""
       Path(output_dir).mkdir(parents=True, exist_ok=True)
       
       # Determine file type
       ext = Path(filepath).suffix.lower()
       
       if ext == '.json':
           with open(filepath, 'r', encoding='utf-8') as f:
               data = json.load(f)
           texts = extract_texts_from_json(data)
       elif ext == '.csv':
           texts = extract_texts_from_csv(filepath)
       elif ext == '.txt':
           with open(filepath, 'r', encoding='utf-8') as f:
               texts = [f.read()]
       else:
           raise ValueError(f"Unsupported file type: {ext}")
       
       # Clean and chunk
       cleaned = [clean_text(text) for text in texts]
       chunks = []
       for text in cleaned:
           chunks.extend(chunk_by_tokens(text, max_tokens=1000))
       
       # Save processed data
       output_file = Path(output_dir) / f"{Path(filepath).stem}_processed.json"
       with open(output_file, 'w') as f:
           json.dump({
               "source": filepath,
               "num_chunks": len(chunks),
               "chunks": chunks
           }, f, indent=2)
       
       print(f"✅ Processed {len(chunks)} chunks from {filepath}")
       return chunks
   
   def extract_texts_from_json(data):
       """Extract text fields from JSON"""
       # Handle different JSON structures
       if isinstance(data, list):
           return [item.get('text', str(item)) for item in data]
       elif isinstance(data, dict):
           return [data.get('text', str(data))]
       return []
   
   def extract_texts_from_csv(filepath: str, text_column: str = 'text'):
       """Extract text column from CSV"""
       import csv
       texts = []
       with open(filepath, 'r', encoding='utf-8') as f:
           reader = csv.DictReader(f)
           for row in reader:
               if text_column in row:
                   texts.append(row[text_column])
       return texts
   
   if __name__ == "__main__":
       # Example usage
       ingest_file("data/raw/sample.txt")
   ```

2. **Add Error Handling** (5 min)
   - File not found errors
   - Encoding errors
   - Invalid JSON/CSV errors

**Exercise:**
- [ ] Create sample data files (JSON, CSV, TXT)
- [ ] Run ingestion script on each
- [ ] Verify output files are created correctly
- [ ] Test error handling with invalid files

**Deliverable:** Working `scripts/ingest.py`

---

### Day 5: Review & Practice (30 minutes)

**Learning Goal:** Consolidate Week 2 learning

**Tasks (30 min):**

1. **Review Concepts** (10 min)
   - [ ] Can read/write JSON, CSV, TXT files
   - [ ] Understand text chunking strategies
   - [ ] Can build data processing pipelines

2. **Complete Exercises** (10 min)
   - Review all exercises from Days 1-4
   - Fix any errors

3. **Week 2 Reflection** (10 min)
   
   Create `docs/week02_reflection.md`:
   ```markdown
   # Week 2 Reflection
   
   ## What I Learned
   - 
   
   ## Challenges
   - 
   
   ## Key Takeaways
   - 
   ```

**Week 2 Deliverables:**
- [ ] `scripts/data_utils.py` with helper functions
- [ ] `scripts/csv_processor.py` working
- [ ] `scripts/chunking.py` with token-aware chunking
- [ ] `scripts/ingest.py` complete and tested
- [ ] Sample processed data in `data/processed/`

---

## 🧠 Deep Dive: Text Chunking Strategies

### Why Chunk?

1. **Context Window Limits**: LLMs have maximum token limits
2. **Better Retrieval**: Smaller chunks = more precise retrieval
3. **Cost Efficiency**: Process only relevant chunks
4. **Performance**: Smaller inputs = faster processing

### Chunking Strategies

**1. Fixed Size**
- Simple, fast
- May break sentences/words
- Good for: Uniform documents

**2. Sentence-Aware**
- Preserves sentence boundaries
- Better semantic coherence
- Good for: Natural language text

**3. Token-Aware**
- Respects model limits exactly
- Most accurate for LLMs
- Good for: Production systems

**4. Semantic Chunking** (Advanced - Week 7+)
- Groups by meaning
- Best quality but complex
- Good for: High-quality RAG

### Practice Exercise

Compare chunking methods:
```python
text = "Your long text here..."  # 5000 words

# Compare outputs
chunks_fixed = chunk_by_size(text, 1000)
chunks_sentence = chunk_by_sentences(text, 1000)
chunks_token = chunk_by_tokens(text, 1000)

print(f"Fixed: {len(chunks_fixed)} chunks")
print(f"Sentence: {len(chunks_sentence)} chunks")
print(f"Token: {len(chunks_token)} chunks")
```

---

## 🎯 Week 2 Success Criteria

- ✅ Can process different file formats
- ✅ Understand text chunking strategies
- ✅ Built working ingestion script
- ✅ Handles errors gracefully

---

## 🔄 Next Week Preview

**Week 3:** LLM & Prompt Engineering
- Prompt fundamentals
- Chain-of-Thought (CoT) deep dive
- Prompt patterns and templates
- Evaluation and A/B testing

