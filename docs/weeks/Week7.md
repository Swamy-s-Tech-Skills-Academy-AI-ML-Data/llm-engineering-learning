# Week 7: Optimization & Performance

**Theme:** Optimization & Performance  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Latency + token cost reductions + Before/after metrics  
**Platforms:** OpenAI + Azure OpenAI (Python, Go, **Node.js intro**)

---

## 🎯 Week 7 Learning Objectives

By the end of this week, you will:
- [ ] Optimize API call latency
- [ ] Reduce token costs
- [ ] Implement caching strategies
- [ ] Select appropriate models
- [ ] Measure and track performance
- [ ] **Introduction to Node.js**: Implement optimization in Node.js

---

## 📅 Day-by-Day Breakdown

### Day 1: Latency Optimization (30 minutes)

**Learning Goal:** Reduce API response times

**Tasks (30 min):**

1. **Async API Calls** (15 min)
   ```python
   import asyncio
   from openai import AsyncOpenAI
   
   async def batch_calls(prompts: List[str]):
       """Make multiple API calls in parallel"""
       client = AsyncOpenAI()
       tasks = [
           client.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[{"role": "user", "content": prompt}]
           )
           for prompt in prompts
       ]
       return await asyncio.gather(*tasks)
   ```

2. **Streaming Responses** (15 min)
   ```python
   def stream_response(prompt: str):
       """Stream response for better perceived latency"""
       stream = client.chat.completions.create(
           model="gpt-3.5-turbo",
           messages=[{"role": "user", "content": prompt}],
           stream=True
       )
       
       for chunk in stream:
           if chunk.choices[0].delta.content:
               print(chunk.choices[0].delta.content, end="")
   ```

**Exercise:**
- [ ] Compare sync vs async performance
- [ ] Implement streaming
- [ ] Measure latency improvements

---

### Day 2: Token Cost Optimization (30 minutes)

**Learning Goal:** Reduce API costs

**Tasks (30 min):**

1. **Prompt Optimization** (15 min)
   - Remove unnecessary text
   - Use shorter prompts
   - Compress context

2. **Model Selection** (15 min)
   - GPT-3.5-turbo vs GPT-4
   - Cost comparison
   - When to use each

**Exercise:**
- [ ] Optimize 3 prompts
- [ ] Compare costs
- [ ] Document savings

---

### Day 3: Caching Strategies (30 minutes)

**Learning Goal:** Cache LLM responses

**Tasks (30 min):**

1. **Response Caching** (20 min)
   ```python
   import hashlib
   import json
   from functools import lru_cache
   
   cache = {}
   
   def cached_llm_call(prompt: str, model: str):
       """Cache LLM responses"""
       cache_key = hashlib.md5(f"{prompt}:{model}".encode()).hexdigest()
       
       if cache_key in cache:
           return cache[cache_key]
       
       response = client.chat.completions.create(...)
       cache[cache_key] = response.choices[0].message.content
       return cache[cache_key]
   ```

2. **Embedding Caching** (10 min)
   - Cache embeddings
   - Vector store caching

**Exercise:**
- [ ] Implement caching
- [ ] Measure cache hit rate
- [ ] Calculate cost savings

---

### Day 4: Performance Metrics (30 minutes)

**Learning Goal:** Track and measure performance

**Tasks (30 min):**

1. **Create Metrics System** (20 min)
   ```python
   class PerformanceTracker:
       def __init__(self):
           self.metrics = {
               "latency": [],
               "cost": [],
               "tokens": []
           }
       
       def track_call(self, latency: float, tokens: int, cost: float):
           self.metrics["latency"].append(latency)
           self.metrics["tokens"].append(tokens)
           self.metrics["cost"].append(cost)
       
       def get_stats(self):
           return {
               "avg_latency": sum(self.metrics["latency"]) / len(self.metrics["latency"]),
               "total_cost": sum(self.metrics["cost"]),
               "total_tokens": sum(self.metrics["tokens"])
           }
   ```

2. **Before/After Comparison** (10 min)
   - Measure baseline
   - Apply optimizations
   - Compare results

**Exercise:**
- [ ] Track metrics
- [ ] Compare before/after
- [ ] Document improvements

---

### Day 5: Node.js Introduction - Optimization (30 minutes)

**Learning Goal:** Implement optimization techniques in Node.js (optional, for multi-platform learning)

**Tasks (30 min):**

1. **Node.js Setup** (5 min)
   ```bash
   # Install Node.js if needed: https://nodejs.org/
   node --version  # Verify Node.js 18+
   
   # Create Node.js project
   mkdir llm-nodejs && cd llm-nodejs
   npm init -y
   npm install openai dotenv
   ```

2. **Node.js Implementation** (25 min)
   - Async/await patterns for latency optimization
   - Caching implementation
   - Performance tracking
   - Both OpenAI and Azure OpenAI support

**Exercise:**
- [ ] Set up Node.js environment
- [ ] Implement optimization in Node.js
- [ ] Test with both providers
- [ ] Compare Node.js vs Python implementations

**Note:** This is optional for Week 7. Focus on Python first, then try Node.js if time permits.

---

### Day 5 Alternative: Review & Practice (30 minutes)

**If focusing on Python only:**

**Tasks:**
- Review optimizations
- Complete exercises
- Week 7 reflection

**Deliverable:**
- [ ] Optimized system
- [ ] Performance metrics
- [ ] Before/after comparison
- [ ] (Optional) Node.js implementation

---

## 🔄 Next Week Preview

**Week 8:** Applied Mini Projects
- Build polished micro-applications
- Multi-language support (Python, Go, Node.js)
- Gradio or CLI interfaces

