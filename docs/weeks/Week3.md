# Week 3: LLM & Prompt Engineering - Chain-of-Thought Deep Dive

**Theme:** LLM & Prompt Engineering + Chain-of-Thought (CoT)  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Prompt patterns + evaluation harness + CoT mastery

---

## 🎯 Week 3 Learning Objectives

By the end of this week, you will:
- [ ] Understand prompt engineering fundamentals
- [ ] Master Chain-of-Thought (CoT) prompting
- [ ] Implement zero-shot and few-shot prompting
- [ ] Create prompt templates and patterns
- [ ] Build evaluation frameworks for prompts
- [ ] Apply CoT to complex reasoning tasks

---

## 📅 Day-by-Day Breakdown

### Day 1: Prompt Engineering Fundamentals (30 minutes)

**Learning Goal:** Understand what makes effective prompts

**Tasks (30 min):**

1. **Prompt Structure** (10 min)
   
   A good prompt has:
   - **Context**: Background information
   - **Task**: What you want done
   - **Examples**: Few-shot demonstrations (optional)
   - **Format**: Desired output structure
   
   ```python
   # Bad prompt
   prompt = "Summarize this text"
   
   # Good prompt
   prompt = """
   You are an expert technical writer. Your task is to create concise summaries.
   
   Task: Summarize the following text in 2-3 sentences, focusing on key points.
   
   Text: {text}
   
   Summary:
   """
   ```

2. **Zero-shot vs Few-shot** (10 min)
   
   **Zero-shot**: No examples provided
   ```python
   zero_shot = """
   Extract the main topic from this text:
   {text}
   """
   ```
   
   **Few-shot**: Examples provided
   ```python
   few_shot = """
   Extract the main topic from these examples:
   
   Example 1:
   Text: "Python is a programming language..."
   Topic: Programming Languages
   
   Example 2:
   Text: "Machine learning uses algorithms..."
   Topic: Machine Learning
   
   Now extract the topic from:
   Text: {text}
   Topic:
   """
   ```

3. **Create Prompt Template System** (10 min)
   
   Create `prompts/template_basic.py`:
   ```python
   from typing import Dict
   
   def format_prompt(template: str, **kwargs) -> str:
       """Format prompt template with variables"""
       return template.format(**kwargs)
   
   # Example template
   SUMMARY_TEMPLATE = """
   Role: {role}
   Task: {task}
   Input: {input_text}
   Output Format: {format}
   """
   
   # Usage
   prompt = format_prompt(
       SUMMARY_TEMPLATE,
       role="Expert summarizer",
       task="Summarize in 3 sentences",
       input_text="Long text here...",
       format="Bullet points"
   )
   ```

**Exercise:**
- [ ] Create 3 different prompts for the same task
- [ ] Compare zero-shot vs few-shot performance
- [ ] Build a prompt template library

**Resources:**
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- Ed Donner's Course: Prompt Engineering Basics

---

### Day 2: Chain-of-Thought (CoT) Introduction (30 minutes)

**Learning Goal:** Understand what Chain-of-Thought is and why it works

**Tasks (30 min):**

1. **What is Chain-of-Thought?** (10 min)
   
   **CoT** = Breaking down complex problems into intermediate reasoning steps
   
   Instead of:
   ```
   Question → Answer
   ```
   
   CoT does:
   ```
   Question → Step 1 → Step 2 → Step 3 → Answer
   ```

2. **Why CoT Works** (10 min)
   
   - LLMs are better at reasoning when they "think step by step"
   - Explicit reasoning reduces errors
   - Makes complex problems tractable
   - Improves accuracy on math, logic, multi-step tasks

3. **Simple CoT Example** (10 min)
   
   Create `prompts/cot_basic.py`:
   ```python
   # Without CoT
   simple_prompt = """
   What is 15 * 23?
   """
   
   # With CoT
   cot_prompt = """
   Solve this step by step:
   
   What is 15 * 23?
   
   Let me think step by step:
   1. First, I'll multiply 15 by 20: 15 * 20 = 300
   2. Then, I'll multiply 15 by 3: 15 * 3 = 45
   3. Finally, I'll add them: 300 + 45 = 345
   
   Answer: 345
   """
   ```

**Exercise:**
- [ ] Try a math problem without CoT
- [ ] Try the same problem with CoT
- [ ] Compare accuracy and reasoning quality

**Key Insight:** CoT makes the LLM's reasoning process explicit and verifiable.

---

### Day 3: Chain-of-Thought Deep Dive (30 minutes)

**Learning Goal:** Master CoT prompting techniques and variations

**Tasks (30 min):**

1. **CoT Prompting Patterns** (15 min)
   
   Create `prompts/cot_patterns.py`:
   
   **Pattern 1: Explicit Step-by-Step**
   ```python
   COT_EXPLICIT = """
   Solve this problem step by step. Show your reasoning.
   
   Problem: {problem}
   
   Step 1: [Your first step]
   Reasoning: [Why this step]
   
   Step 2: [Your second step]
   Reasoning: [Why this step]
   
   Step 3: [Final step]
   Reasoning: [Why this step]
   
   Final Answer: [Your answer]
   """
   ```
   
   **Pattern 2: Let's Think**
   ```python
   COT_LETS_THINK = """
   Let's think step by step to solve this:
   
   {problem}
   
   First, let's understand what we need to find...
   Then, we can...
   Finally, we conclude...
   
   Answer:
   """
   ```
   
   **Pattern 3: Structured CoT**
   ```python
   COT_STRUCTURED = """
   Analyze this problem:
   
   Problem: {problem}
   
   Given:
   - [List given information]
   
   Goal:
   - [What we need to find]
   
   Approach:
   1. [Step 1]
   2. [Step 2]
   3. [Step 3]
   
   Solution:
   [Work through the steps]
   
   Verification:
   [Check if answer makes sense]
   
   Answer:
   """
   ```

2. **Few-Shot CoT** (10 min)
   
   Provide examples of CoT reasoning:
   ```python
   FEW_SHOT_COT = """
   Here are examples of solving problems step by step:
   
   Example 1:
   Problem: If a store has 20 apples and sells 8, how many are left?
   Solution:
   Step 1: Start with 20 apples
   Step 2: Subtract 8 sold: 20 - 8 = 12
   Answer: 12 apples
   
   Example 2:
   Problem: A book costs $15. If you have $50, how much change?
   Solution:
   Step 1: You have $50
   Step 2: Book costs $15
   Step 3: Change = $50 - $15 = $35
   Answer: $35
   
   Now solve this problem step by step:
   Problem: {problem}
   Solution:
   """
   ```

3. **CoT for Different Tasks** (5 min)
   
   - **Math**: Show calculations
   - **Logic**: Show reasoning chain
   - **Analysis**: Show decomposition
   - **Planning**: Show steps

**Exercise:**
- [ ] Create CoT prompts for 3 different problem types
- [ ] Test few-shot CoT vs zero-shot CoT
- [ ] Compare accuracy with and without CoT

**Resources:**
- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903) (Wei et al., 2022)
- Ed Donner's Course: Advanced Prompting

---

### Day 4: Advanced CoT Patterns & Implementation (30 minutes)

**Learning Goal:** Implement CoT in real applications

**Tasks (30 min):**

1. **Auto-CoT (Automatic Chain-of-Thought)** (10 min)
   
   Let the model generate its own reasoning:
   ```python
   AUTO_COT_PROMPT = """
   Answer this question. Think through the problem step by step.
   
   Question: {question}
   
   Reasoning:
   [Model generates its own reasoning steps]
   
   Answer:
   """
   ```

2. **Self-Consistency CoT** (10 min)
   
   Run CoT multiple times, take majority vote:
   ```python
   def self_consistency_cot(question: str, num_runs: int = 5):
       """Run CoT multiple times, return most common answer"""
       answers = []
       for _ in range(num_runs):
           response = llm_call(COT_PROMPT.format(question=question))
           answer = extract_answer(response)
           answers.append(answer)
       
       # Return most common answer
       from collections import Counter
       return Counter(answers).most_common(1)[0][0]
   ```

3. **Tree-of-Thoughts (ToT)** (10 min)
   
   Explore multiple reasoning paths:
   ```python
   TOT_PROMPT = """
   Solve this problem by exploring multiple reasoning paths:
   
   Problem: {problem}
   
   Path 1:
   [First approach]
   
   Path 2:
   [Alternative approach]
   
   Path 3:
   [Another approach]
   
   Evaluate each path and choose the best solution.
   """
   ```

**Exercise:**
- [ ] Implement auto-CoT for a reasoning task
- [ ] Compare single CoT vs self-consistency CoT
- [ ] Create a CoT prompt template library

**Advanced Concept:** CoT can be combined with:
- Tool use (ReAct - Week 5)
- RAG (Week 7)
- Multi-agent systems (Week 9)

---

### Day 5: CoT Evaluation & Practice (30 minutes)

**Learning Goal:** Evaluate CoT effectiveness and build prompt library

**Tasks (30 min):**

1. **Create CoT Evaluation Framework** (15 min)
   
   Create `eval/cot_evaluator.py`:
   ```python
   def evaluate_cot(prompt_template: str, test_cases: list, 
                   with_cot: bool = True):
       """Evaluate CoT vs non-CoT on test cases"""
       results = []
       
       for case in test_cases:
           # Test with CoT
           if with_cot:
               prompt = prompt_template.format(problem=case['problem'])
           else:
               prompt = case['problem']  # Simple prompt
           
           response = llm_call(prompt)
           correct = check_answer(response, case['expected'])
           
           results.append({
               'problem': case['problem'],
               'correct': correct,
               'response': response
           })
       
       accuracy = sum(r['correct'] for r in results) / len(results)
       return accuracy, results
   ```

2. **Build Prompt Library** (10 min)
   
   Create `prompts/cot_library.json`:
   ```json
   {
     "patterns": {
       "explicit_steps": {
         "template": "...",
         "use_case": "Math problems",
         "accuracy_gain": "+15%"
       },
       "lets_think": {
         "template": "...",
         "use_case": "General reasoning",
         "accuracy_gain": "+10%"
       }
     }
   }
   ```

3. **Week 3 Reflection** (5 min)
   
   Document what you learned about CoT.

**Exercise:**
- [ ] Create 10 test cases for CoT evaluation
- [ ] Compare CoT vs non-CoT accuracy
- [ ] Document best practices in `docs/cot_guide.md`

**Deliverable:**
- [ ] CoT prompt library in `prompts/`
- [ ] Evaluation framework in `eval/`
- [ ] Test results and comparison

---

## 🧠 Deep Dive: Chain-of-Thought (CoT) - Complete Guide

### What is Chain-of-Thought?

**Chain-of-Thought (CoT)** is a prompting technique that encourages LLMs to solve problems by breaking them down into intermediate reasoning steps, rather than jumping directly to an answer.

### Why CoT Works

1. **Explicit Reasoning**: Makes the model's thought process visible
2. **Error Reduction**: Step-by-step reasoning catches mistakes
3. **Complex Problem Solving**: Breaks complex problems into manageable parts
4. **Better Accuracy**: Studies show 10-30% accuracy improvement on reasoning tasks

### CoT Prompting Patterns

#### Pattern 1: Explicit Step-by-Step
```
Problem: [Complex problem]

Step 1: [First action]
Step 2: [Second action]
Step 3: [Third action]
...
Final Answer: [Answer]
```

**Use when:** Solving multi-step problems, math, logic puzzles

#### Pattern 2: "Let's Think" Format
```
Let's think step by step:

[Problem]

First, we need to...
Then, we should...
Finally, we conclude...

Answer:
```

**Use when:** General reasoning, analysis, planning

#### Pattern 3: Structured Analysis
```
Problem: [Problem statement]

Given:
- [Known information 1]
- [Known information 2]

Goal:
- [What we need to find]

Approach:
1. [Method 1]
2. [Method 2]

Solution:
[Work through solution]

Answer:
```

**Use when:** Complex analysis, research problems

#### Pattern 4: Few-Shot CoT
```
Example 1:
Problem: [Problem 1]
Solution: [Step-by-step solution 1]
Answer: [Answer 1]

Example 2:
Problem: [Problem 2]
Solution: [Step-by-step solution 2]
Answer: [Answer 2]

Now solve:
Problem: [New problem]
Solution:
```

**Use when:** You want to teach the model a specific reasoning style

### CoT Variations

#### 1. Auto-CoT
Let the model generate its own reasoning without explicit instructions:
```python
prompt = "Solve this: {problem}. Think step by step."
```

#### 2. Self-Consistency CoT
Run CoT multiple times, take majority answer:
```python
# Run 5 times
answers = [cot_solve(problem) for _ in range(5)]
final_answer = most_common(answers)
```

#### 3. Tree-of-Thoughts (ToT)
Explore multiple reasoning paths:
```
Path 1: [Approach A]
Path 2: [Approach B]
Path 3: [Approach C]

Evaluate and choose best.
```

### When to Use CoT

✅ **Use CoT for:**
- Math problems
- Logic puzzles
- Multi-step reasoning
- Complex analysis
- Planning tasks
- Problem decomposition

❌ **Don't use CoT for:**
- Simple factual questions
- Single-step tasks
- When speed is critical
- When token cost matters most

### CoT Implementation Example

```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def solve_with_cot(problem: str) -> str:
    """Solve a problem using Chain-of-Thought"""
    
    cot_prompt = f"""
    Solve this problem step by step. Show your reasoning.
    
    Problem: {problem}
    
    Step 1: [Your first step]
    Reasoning: [Why this step is needed]
    
    Step 2: [Your second step]
    Reasoning: [Why this step is needed]
    
    Step 3: [Continue as needed]
    
    Final Answer: [Your answer]
    """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a logical problem solver."},
            {"role": "user", "content": cot_prompt}
        ],
        temperature=0.3  # Lower temperature for more consistent reasoning
    )
    
    return response.choices[0].message.content

# Example usage
problem = """
If a train travels 60 miles in 1 hour, and another train travels 
80 miles in 1.5 hours, which train is faster?
"""

solution = solve_with_cot(problem)
print(solution)
```

### CoT Best Practices

1. **Be Explicit**: Clearly ask for step-by-step reasoning
2. **Use Examples**: Few-shot CoT often works better
3. **Lower Temperature**: Use 0.3-0.5 for more consistent reasoning
4. **Verify Steps**: Check if intermediate steps make sense
5. **Iterate**: Refine CoT prompts based on results

### Measuring CoT Effectiveness

```python
def evaluate_cot_improvement(test_cases):
    """Compare CoT vs non-CoT accuracy"""
    
    # Without CoT
    simple_prompt = "{problem}\nAnswer:"
    simple_accuracy = test_prompt(simple_prompt, test_cases)
    
    # With CoT
    cot_prompt = "{problem}\n\nLet's think step by step:\n[reasoning]\n\nAnswer:"
    cot_accuracy = test_prompt(cot_prompt, test_cases)
    
    improvement = cot_accuracy - simple_accuracy
    print(f"CoT improves accuracy by {improvement:.1%}")
    
    return improvement
```

### Common CoT Mistakes

1. **Too Vague**: "Think about it" - be specific
2. **No Structure**: Unclear step format
3. **Wrong Temperature**: Too high = inconsistent reasoning
4. **No Examples**: Few-shot helps significantly
5. **Not Verifying**: Always check if reasoning makes sense

---

## 🎯 Week 3 Success Criteria

- ✅ Understand CoT fundamentals
- ✅ Can create effective CoT prompts
- ✅ Built CoT prompt library
- ✅ Evaluated CoT effectiveness
- ✅ Understand when to use CoT

---

## 📚 Additional Resources

- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903) - Original research
- [Prompt Engineering Guide - CoT](https://www.promptingguide.ai/techniques/cot)
- [Self-Consistency Paper](https://arxiv.org/abs/2203.11171)
- Ed Donner's Course: Advanced Prompting Techniques

---

## 🔄 Next Week Preview

**Week 4:** Bots & Scraping
- Web scraping basics
- Building bots that use LLMs
- News/website summarization
- Integrating CoT into real applications

---

**Remember:** CoT is powerful but not always needed. Use it when problems require multi-step reasoning!

