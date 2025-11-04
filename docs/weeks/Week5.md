# Week 5: Multi-Agent Intro + ReAct Deep Dive

**Theme:** Multi-Agent Intro + ReAct (Reasoning + Acting)  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Simple multi-tool agent reasoning log + ReAct mastery

---

## 🎯 Week 5 Learning Objectives

By the end of this week, you will:
- [ ] Understand what agents are and how they work
- [ ] Master ReAct (Reasoning + Acting) pattern
- [ ] Build agent loops with tool integration
- [ ] Implement reasoning traces
- [ ] Create multi-tool agents
- [ ] Understand when to use ReAct vs other patterns

---

## 📅 Day-by-Day Breakdown

### Day 1: Introduction to Agents (30 minutes)

**Learning Goal:** Understand what agents are and basic concepts

**Tasks (30 min):**

1. **What are Agents?** (10 min)
   
   **Agents** = LLM-powered systems that can:
   - Make decisions
   - Use tools (search, calculator, APIs)
   - Take actions
   - Learn from feedback
   
   **Key Components:**
   - LLM (brain/reasoning)
   - Tools (actions it can take)
   - Memory (conversation history)
   - Loop (observation → thought → action → repeat)

2. **Simple Agent Example** (10 min)
   
   Create `agents/simple_agent.py`:
   ```python
   from scripts.api_client import get_openai_client
   
   class SimpleAgent:
       def __init__(self):
           self.client = get_openai_client()
           self.memory = []
       
       def think(self, user_input: str) -> str:
           """Agent thinks about what to do"""
           prompt = f"""
           You are a helpful assistant. The user said: {user_input}
           
           What should you do? Respond with your action.
           """
           
           response = self.client.chat.completions.create(
               model="gpt-3.5-turbo",
               messages=[{"role": "user", "content": prompt}]
           )
           
           return response.choices[0].message.content
       
       def run(self, user_input: str):
           """Run the agent"""
           thought = self.think(user_input)
           self.memory.append({"input": user_input, "thought": thought})
           return thought
   ```

3. **Agent vs Simple LLM** (10 min)
   
   **Simple LLM:**
   - One-shot: Question → Answer
   - No tools
   - No memory
   
   **Agent:**
   - Loop: Observe → Think → Act → Observe...
   - Has tools
   - Has memory
   - Can make decisions

**Exercise:**
- [ ] Create a simple agent
- [ ] Compare agent response vs simple LLM call
- [ ] Understand the difference

**Resources:**
- Ed Donner's Course: Introduction to Agents

---

### Day 2: ReAct Pattern Introduction (30 minutes)

**Learning Goal:** Understand ReAct (Reasoning + Acting) pattern

**Tasks (30 min):**

1. **What is ReAct?** (15 min)
   
   **ReAct** = **Reasoning** + **Acting**
   
   - **Reasoning**: LLM thinks about what to do
   - **Acting**: LLM uses tools to take actions
   - **Observation**: See results of actions
   - **Repeat**: Continue until goal achieved
   
   **ReAct Loop:**
   ```
   Thought: [What should I do?]
   Action: [Use tool X]
   Observation: [Result from tool]
   Thought: [What next?]
   Action: [Use tool Y]
   Observation: [Result]
   ...
   Final Answer: [Conclusion]
   ```

2. **Why ReAct?** (10 min)
   
   - **Better Reasoning**: Explicit thought process
   - **Tool Integration**: Can use external tools
   - **Transparency**: See agent's reasoning
   - **Error Recovery**: Can fix mistakes
   - **Complex Tasks**: Solves multi-step problems

3. **Simple ReAct Example** (5 min)
   ```python
   # ReAct prompt structure
   REACT_PROMPT = """
   Question: {question}
   
   Thought: I need to {reasoning}
   Action: {tool_name}
   Action Input: {tool_input}
   
   Observation: {tool_result}
   
   Thought: {next_reasoning}
   Action: {next_tool}
   ...
   
   Final Answer: {answer}
   """
   ```

**Exercise:**
- [ ] Understand ReAct flow
- [ ] Identify reasoning vs acting steps
- [ ] Think of 3 use cases for ReAct

**Key Insight:** ReAct combines CoT (Chain-of-Thought) with tool use.

---

### Day 3: ReAct Deep Dive - Implementation (30 minutes)

**Learning Goal:** Implement ReAct pattern from scratch

**Tasks (30 min):**

1. **Build ReAct Agent Core** (20 min)
   
   Create `agents/react_agent.py`:
   ```python
   from typing import List, Dict, Callable
   from scripts.api_client import get_openai_client
   
   class ReActAgent:
       def __init__(self, tools: Dict[str, Callable]):
           self.client = get_openai_client()
           self.tools = tools
           self.history = []
       
       def format_tools_description(self) -> str:
           """Format tool descriptions for prompt"""
           descriptions = []
           for name, func in self.tools.items():
               doc = func.__doc__ or "No description"
               descriptions.append(f"- {name}: {doc}")
           return "\n".join(descriptions)
       
       def parse_response(self, response: str) -> Dict:
           """Parse ReAct response into thought/action/observation"""
           # Simple parsing - can be improved
           lines = response.split("\n")
           result = {"thought": "", "action": "", "action_input": "", "observation": ""}
           
           for line in lines:
               if line.startswith("Thought:"):
                   result["thought"] = line.replace("Thought:", "").strip()
               elif line.startswith("Action:"):
                   result["action"] = line.replace("Action:", "").strip()
               elif line.startswith("Action Input:"):
                   result["action_input"] = line.replace("Action Input:", "").strip()
           
           return result
       
       def step(self, question: str, max_steps: int = 5) -> str:
           """Execute one ReAct step"""
           
           # Build prompt with tools
           tools_desc = self.format_tools_description()
           history_str = "\n".join([str(h) for h in self.history[-3:]])
           
           prompt = f"""
           You are a ReAct agent. Use the following tools to answer questions.
           
           Available Tools:
           {tools_desc}
           
           Previous Steps:
           {history_str}
           
           Question: {question}
           
           Use this format:
           Thought: [Your reasoning about what to do]
           Action: [Tool name]
           Action Input: [Input for tool]
           
           Then I will provide the Observation, and you continue.
           """
           
           response = self.client.chat.completions.create(
               model="gpt-4",  # GPT-4 works better for ReAct
               messages=[{"role": "user", "content": prompt}],
               temperature=0.3
           )
           
           parsed = self.parse_response(response.choices[0].message.content)
           
           # Execute action if tool specified
           if parsed["action"] and parsed["action"] in self.tools:
               tool = self.tools[parsed["action"]]
               observation = tool(parsed["action_input"])
               parsed["observation"] = observation
           
           self.history.append(parsed)
           return parsed
       
       def run(self, question: str, max_steps: int = 5) -> str:
           """Run ReAct loop until answer found"""
           for step_num in range(max_steps):
               result = self.step(question)
               
               # Check if we have final answer
               if "Final Answer:" in str(result):
                   return result
               
               # Prevent infinite loops
               if step_num >= max_steps - 1:
                   return "Max steps reached"
           
           return "No answer found"
   ```

2. **Define Tools** (10 min)
   ```python
   # Example tools
   def calculator(expression: str) -> str:
       """Evaluate mathematical expressions"""
       try:
           result = eval(expression)
           return str(result)
       except:
           return "Error: Invalid expression"
   
   def search_knowledge(query: str) -> str:
       """Search knowledge base"""
       # Simplified - replace with actual search
       return f"Information about {query}"
   
   # Initialize agent with tools
   tools = {
       "calculator": calculator,
       "search": search_knowledge
   }
   agent = ReActAgent(tools)
   ```

**Exercise:**
- [ ] Implement ReAct agent
- [ ] Create 2-3 simple tools
- [ ] Test agent with a question requiring tools

---

### Day 4: Advanced ReAct Patterns (30 minutes)

**Learning Goal:** Master advanced ReAct techniques

**Tasks (30 min):**

1. **Self-Consistency ReAct** (10 min)
   ```python
   def self_consistency_react(question: str, num_runs: int = 3):
       """Run ReAct multiple times, take consensus"""
       answers = []
       for _ in range(num_runs):
           agent = ReActAgent(tools)
           answer = agent.run(question)
           answers.append(answer)
       
       # Return most common answer
       from collections import Counter
       return Counter(answers).most_common(1)[0][0]
   ```

2. **ReAct with Memory** (10 min)
   ```python
   class ReActAgentWithMemory(ReActAgent):
       def __init__(self, tools, memory_size=10):
           super().__init__(tools)
           self.memory_size = memory_size
       
       def add_to_memory(self, item):
           """Add item to memory, maintain size"""
           self.history.append(item)
           if len(self.history) > self.memory_size:
               self.history.pop(0)
   ```

3. **ReAct with Error Recovery** (10 min)
   ```python
   def step_with_recovery(self, question: str):
       """ReAct step with error recovery"""
       try:
           result = self.step(question)
           
           # If error, try to recover
           if "error" in result.get("observation", "").lower():
               # Agent can think about error and retry
               recovery = self.step(f"Previous action failed. {question}")
               return recovery
           
           return result
       except Exception as e:
           # Log error and continue
           return {"error": str(e), "thought": "Need to try different approach"}
   ```

**Exercise:**
- [ ] Implement error recovery
- [ ] Add memory to agent
- [ ] Test on complex multi-step problems

---

### Day 5: ReAct Evaluation & Practice (30 minutes)

**Learning Goal:** Evaluate ReAct and build complete system

**Tasks (30 min):**

1. **Create ReAct Evaluation Framework** (15 min)
   
   Create `eval/react_evaluator.py`:
   ```python
   def evaluate_react_agent(agent, test_cases: List[Dict]):
       """Evaluate ReAct agent on test cases"""
       results = []
       
       for case in test_cases:
           question = case["question"]
           expected = case["expected"]
           
           answer = agent.run(question)
           correct = check_answer(answer, expected)
           
           results.append({
               "question": question,
               "answer": answer,
               "expected": expected,
               "correct": correct,
               "steps": len(agent.history)
           })
       
       accuracy = sum(r["correct"] for r in results) / len(results)
       avg_steps = sum(r["steps"] for r in results) / len(results)
       
       return {
           "accuracy": accuracy,
           "avg_steps": avg_steps,
           "results": results
       }
   ```

2. **Build Complete System** (10 min)
   - Agent with multiple tools
   - Error handling
   - Logging
   - Evaluation

3. **Week 5 Reflection** (5 min)

**Exercise:**
- [ ] Create 5 test cases for ReAct agent
- [ ] Evaluate agent performance
- [ ] Document best practices

**Deliverable:**
- [ ] Working ReAct agent
- [ ] Tool registry
- [ ] Evaluation framework
- [ ] Week 5 reflection

---

## 🧠 Deep Dive: ReAct (Reasoning + Acting) - Complete Guide

### What is ReAct?

**ReAct** is a framework that combines **Reasoning** (Chain-of-Thought) with **Acting** (tool use) to solve complex problems that require both thinking and actions.

### ReAct Architecture

```
┌─────────────────────────────────────┐
│         User Question                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Thought: [What should I do?]       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Action: [Use tool X]               │
│   Action Input: [Parameters]         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Observation: [Tool result]         │
└──────────────┬──────────────────────┘
               │
               ▼
         [Repeat until done]
               │
               ▼
┌─────────────────────────────────────┐
│   Final Answer: [Solution]           │
└─────────────────────────────────────┘
```

### ReAct vs Other Patterns

| Pattern | Reasoning | Tool Use | When to Use |
|---------|-----------|----------|-------------|
| **Simple LLM** | Implicit | No | Simple Q&A |
| **Chain-of-Thought** | Explicit | No | Complex reasoning, no tools needed |
| **ReAct** | Explicit | Yes | Complex problems requiring tools |
| **Planning Agents** | Explicit | Yes | Multi-step planning |

### ReAct Prompt Template

```python
REACT_TEMPLATE = """
You are a ReAct agent. Use tools to answer questions.

Available Tools:
{tools_description}

Previous Steps:
{history}

Question: {question}

Format your response as:
Thought: [Your reasoning]
Action: [Tool name]
Action Input: [Tool parameters]

After I provide the Observation, continue with:
Thought: [Next reasoning]
Action: [Next tool]
...

When you have the answer:
Final Answer: [Your answer]
"""
```

### Implementing ReAct Agent

#### Step 1: Define Tools

```python
def calculator(expression: str) -> str:
    """Evaluate mathematical expressions. Input: expression string"""
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error: Invalid expression"

def web_search(query: str) -> str:
    """Search the web for information. Input: search query"""
    # Implement web search
    return f"Search results for: {query}"

def get_weather(city: str) -> str:
    """Get current weather. Input: city name"""
    # Implement weather API
    return f"Weather in {city}: Sunny, 72°F"

tools = {
    "calculator": calculator,
    "web_search": web_search,
    "get_weather": get_weather
}
```

#### Step 2: Create ReAct Loop

```python
class ReActAgent:
    def __init__(self, tools):
        self.tools = tools
        self.history = []
        self.client = get_openai_client()
    
    def run(self, question: str, max_steps: int = 10):
        """Run ReAct loop"""
        for step in range(max_steps):
            # Get reasoning and action from LLM
            response = self.get_react_response(question)
            parsed = self.parse_react(response)
            
            # Execute action
            if parsed["action"] in self.tools:
                tool_result = self.tools[parsed["action"]](parsed["action_input"])
                parsed["observation"] = tool_result
                self.history.append(parsed)
                
                # Check if done
                if "Final Answer" in response:
                    return self.extract_final_answer(response)
            else:
                parsed["observation"] = f"Unknown tool: {parsed['action']}"
                self.history.append(parsed)
        
        return "Max steps reached"
    
    def get_react_response(self, question: str) -> str:
        """Get ReAct response from LLM"""
        tools_desc = self.format_tools()
        history = self.format_history()
        
        prompt = REACT_TEMPLATE.format(
            tools_description=tools_desc,
            history=history,
            question=question
        )
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        return response.choices[0].message.content
```

### ReAct Best Practices

1. **Clear Tool Descriptions**
   - Describe what each tool does
   - Specify input format
   - Give examples

2. **Manage History**
   - Keep last 3-5 steps in context
   - Don't exceed context window
   - Focus on relevant history

3. **Error Handling**
   - Catch tool errors
   - Let agent recover
   - Provide helpful error messages

4. **Temperature Settings**
   - Use 0.3-0.5 for consistent reasoning
   - Higher temperature = more creative but less reliable

5. **Step Limits**
   - Set max_steps to prevent infinite loops
   - Monitor for stuck agents

### ReAct Use Cases

✅ **Good for ReAct:**
- Multi-step problem solving
- Tasks requiring external data
- Complex reasoning + tool use
- Research tasks
- Planning and execution

❌ **Not ideal for ReAct:**
- Simple one-step questions
- Tasks without tool needs
- When speed is critical
- When cost must be minimal

### ReAct Example: Research Agent

```python
# Question: "What's the weather in Paris and convert 25°C to Fahrenheit?"

# Step 1:
# Thought: I need weather in Paris
# Action: get_weather
# Action Input: Paris
# Observation: Weather in Paris: 25°C, Cloudy

# Step 2:
# Thought: Now I need to convert 25°C to Fahrenheit using formula: F = (C * 9/5) + 32
# Action: calculator
# Action Input: (25 * 9/5) + 32
# Observation: 77.0

# Step 3:
# Thought: I have all the information
# Final Answer: Weather in Paris is 25°C (77°F), Cloudy
```

### ReAct vs Chain-of-Thought

**Chain-of-Thought (CoT):**
- Reasoning only
- No external tools
- Good for: Math, logic, analysis

**ReAct:**
- Reasoning + Actions
- Uses external tools
- Good for: Complex tasks requiring both

**Combined:** ReAct uses CoT for reasoning steps!

### Advanced ReAct Patterns

#### 1. ReAct with Memory
```python
class ReActAgentWithMemory(ReActAgent):
    def __init__(self, tools, memory_size=10):
        super().__init__(tools)
        self.long_term_memory = []
        self.memory_size = memory_size
    
    def remember(self, key: str, value: str):
        """Store in long-term memory"""
        self.long_term_memory.append({"key": key, "value": value})
        if len(self.long_term_memory) > self.memory_size:
            self.long_term_memory.pop(0)
    
    def recall(self, key: str) -> str:
        """Retrieve from memory"""
        for item in self.long_term_memory:
            if item["key"] == key:
                return item["value"]
        return None
```

#### 2. ReAct with Planning
```python
def react_with_planning(question: str):
    """ReAct with initial planning phase"""
    # Phase 1: Plan
    plan = create_plan(question)
    
    # Phase 2: Execute with ReAct
    agent = ReActAgent(tools)
    result = agent.execute_plan(plan)
    
    return result
```

#### 3. Multi-Agent ReAct
```python
class MultiAgentReAct:
    def __init__(self, agents: List[ReActAgent]):
        self.agents = agents
    
    def coordinate(self, question: str):
        """Coordinate multiple agents"""
        # Distribute tasks
        # Agents work in parallel
        # Combine results
        pass
```

### Measuring ReAct Performance

```python
def evaluate_react(agent, test_cases):
    metrics = {
        "accuracy": 0,
        "avg_steps": 0,
        "tool_usage": {},
        "error_rate": 0
    }
    
    for case in test_cases:
        result = agent.run(case["question"])
        
        # Check accuracy
        if check_answer(result, case["expected"]):
            metrics["accuracy"] += 1
        
        # Count steps
        metrics["avg_steps"] += len(agent.history)
        
        # Track tool usage
        for step in agent.history:
            tool = step.get("action", "")
            metrics["tool_usage"][tool] = metrics["tool_usage"].get(tool, 0) + 1
    
    metrics["accuracy"] /= len(test_cases)
    metrics["avg_steps"] /= len(test_cases)
    
    return metrics
```

### Common ReAct Mistakes

1. **Unclear Tool Descriptions**
   - Agent doesn't know when to use tools
   - Solution: Detailed, example-rich descriptions

2. **No Step Limits**
   - Infinite loops
   - Solution: Set max_steps, monitor

3. **Poor Error Handling**
   - Crashes on tool errors
   - Solution: Catch errors, let agent recover

4. **Context Window Overflow**
   - Too much history
   - Solution: Limit history, summarize old steps

5. **Wrong Temperature**
   - Too high = inconsistent
   - Solution: Use 0.3-0.5

---

## 🎯 Week 5 Success Criteria

- ✅ Understand ReAct pattern
- ✅ Built working ReAct agent
- ✅ Integrated tools
- ✅ Evaluated agent performance
- ✅ Understand when to use ReAct

---

## 📚 Additional Resources

- [ReAct Paper](https://arxiv.org/abs/2210.03629) - Original research
- [LangChain ReAct](https://python.langchain.com/docs/modules/agents/agent_types/react)
- Ed Donner's Course: Agents & ReAct

---

## 🔄 Next Week Preview

**Week 6:** Structured Outputs & Orchestration
- JSON schema generation
- Function calling
- Tool calling APIs
- Reliable structured outputs

---

**Remember:** ReAct combines the best of CoT (reasoning) with tool use (acting). It's powerful for complex multi-step problems!

