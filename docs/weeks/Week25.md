# Week 25: Agentic Frameworks Mastery

**Theme:** Agentic Frameworks (LangChain, LangGraph, SDKs)  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Mastery of all major agentic frameworks with OpenAI and Azure OpenAI

---

## 🎯 Week 25 Learning Objectives

By the end of this week, you will:
- [ ] Master LangChain for agent development
- [ ] Build workflows with LangGraph
- [ ] Use OpenAI Agent SDK effectively
- [ ] Implement Azure Agent SDK
- [ ] Compare frameworks and choose appropriately
- [ ] Build production-ready agentic applications

---

## 📅 Day-by-Day Breakdown

### Day 1: LangChain Deep Dive (30 minutes)

**Learning Goal:** Master LangChain with OpenAI and Azure OpenAI

**Tasks (30 min):**

1. **LangChain Setup** (5 min)
   ```bash
   pip install langchain langchain-openai langchain-azure-openai
   ```

2. **LangChain with OpenAI** (12 min)
   ```python
   # LangChain with OpenAI
   from langchain_openai import ChatOpenAI
   from langchain.prompts import ChatPromptTemplate
   from langchain.chains import LLMChain
   
   # Initialize OpenAI LLM
   llm_openai = ChatOpenAI(
       model="gpt-4",
       temperature=0.7,
       openai_api_key=os.getenv("OPENAI_API_KEY")
   )
   
   # Create prompt template
   prompt = ChatPromptTemplate.from_template(
       "You are a helpful assistant. Answer: {question}"
   )
   
   # Create chain
   chain = prompt | llm_openai
   
   # Run chain
   response = chain.invoke({"question": "What is LLM Engineering?"})
   print(response.content)
   ```

3. **LangChain with Azure OpenAI** (13 min)
   ```python
   # LangChain with Azure OpenAI
   from langchain_azure_openai import AzureChatOpenAI
   
   # Initialize Azure OpenAI LLM
   llm_azure = AzureChatOpenAI(
       azure_deployment="gpt-4",
       azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
       api_key=os.getenv("AZURE_OPENAI_API_KEY"),
       api_version="2024-02-15-preview",
       temperature=0.7
   )
   
   # Use same chain pattern
   chain_azure = prompt | llm_azure
   response = chain_azure.invoke({"question": "What is LLM Engineering?"})
   print(response.content)
   ```

**Exercise:**
- [ ] Set up LangChain
- [ ] Implement with both providers
- [ ] Build simple chain

---

### Day 2: LangGraph Workflows (30 minutes)

**Learning Goal:** Build complex agent workflows with LangGraph

**Tasks (30 min):**

1. **LangGraph Setup** (5 min)
   ```bash
   pip install langgraph
   ```

2. **Build Agent Workflow** (25 min)
   ```python
   # LangGraph workflow
   from langgraph.graph import StateGraph, END
   from langchain_openai import ChatOpenAI
   from typing import TypedDict, Annotated
   import operator
   
   # Define state
   class AgentState(TypedDict):
       messages: Annotated[list, operator.add]
       question: str
       answer: str
   
   # Initialize LLM (works with both OpenAI and Azure OpenAI)
   llm = ChatOpenAI(model="gpt-4", temperature=0.7)
   
   # Define nodes
   def research_node(state: AgentState):
       """Research step"""
       question = state["question"]
       # Research logic here
       research_result = "Research findings..."
       return {"messages": [{"role": "assistant", "content": research_result}]}
   
   def answer_node(state: AgentState):
       """Answer generation step"""
       messages = state["messages"]
       response = llm.invoke(messages)
       return {
           "answer": response.content,
           "messages": [{"role": "assistant", "content": response.content}]
       }
   
   # Build graph
   workflow = StateGraph(AgentState)
   workflow.add_node("research", research_node)
   workflow.add_node("answer", answer_node)
   
   # Define edges
   workflow.set_entry_point("research")
   workflow.add_edge("research", "answer")
   workflow.add_edge("answer", END)
   
   # Compile and run
   app = workflow.compile()
   
   result = app.invoke({
       "question": "What is ReAct?",
       "messages": [],
       "answer": ""
   })
   
   print(result["answer"])
   ```

**Exercise:**
- [ ] Set up LangGraph
- [ ] Build workflow
- [ ] Test with both providers

---

### Day 3: OpenAI Agent SDK (30 minutes)

**Learning Goal:** Use OpenAI's native Agent SDK

**Tasks (30 min):**

1. **OpenAI Agent SDK Setup** (5 min)
   ```bash
   pip install openai[agents]
   ```

2. **Build Agent with SDK** (25 min)
   ```python
   # OpenAI Agent SDK
   from openai import OpenAI
   from openai.agents import Agent, AgentExecutor
   
   # Initialize client
   client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
   
   # Define tools
   def calculator(expression: str) -> str:
       """Calculate mathematical expressions"""
       try:
           result = eval(expression)
           return str(result)
       except:
           return "Error: Invalid expression"
   
   # Create agent
   agent = Agent(
       name="math_assistant",
       instructions="You are a helpful math assistant.",
       model="gpt-4",
       tools=[calculator],
       client=client
   )
   
   # Execute agent
   executor = AgentExecutor(agent)
   result = executor.run("What is 15 * 23?")
   print(result)
   ```

**Exercise:**
- [ ] Set up OpenAI Agent SDK
- [ ] Create agent with tools
- [ ] Test agent execution

---

### Day 4: Azure Agent SDK (30 minutes)

**Learning Goal:** Use Azure's Agent SDK

**Tasks (30 min):**

1. **Azure Agent SDK Setup** (5 min)
   ```bash
   pip install azure-ai-agents
   ```

2. **Build Agent with Azure SDK** (25 min)
   ```python
   # Azure Agent SDK
   from azure.ai.agents import Agent, AgentExecutor
   from azure.ai.agents.models import AzureOpenAIConnection
   
   # Create Azure OpenAI connection
   connection = AzureOpenAIConnection(
       endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
       api_key=os.getenv("AZURE_OPENAI_API_KEY"),
       api_version="2024-02-15-preview"
   )
   
   # Define tools (same as OpenAI)
   def calculator(expression: str) -> str:
       """Calculate mathematical expressions"""
       try:
           result = eval(expression)
           return str(result)
       except:
           return "Error: Invalid expression"
   
   # Create agent with Azure
   agent = Agent(
       name="azure_math_assistant",
       instructions="You are a helpful math assistant using Azure OpenAI.",
       model="gpt-4",  # Deployment name
       tools=[calculator],
       connection=connection
   )
   
   # Execute agent
   executor = AgentExecutor(agent)
   result = executor.run("What is 15 * 23?")
   print(result)
   ```

**Exercise:**
- [ ] Set up Azure Agent SDK
- [ ] Create agent
- [ ] Compare with OpenAI SDK

---

### Day 5: Framework Comparison & Selection Guide (30 minutes)

**Learning Goal:** Understand when to use each framework

**Tasks (30 min):**

1. **Framework Comparison** (20 min)
   
   **LangChain:**
   - ✅ Best for: Complex chains, RAG, multi-step workflows
   - ✅ Strengths: Extensive tooling, community, integrations
   - ❌ Weaknesses: Can be verbose, learning curve
   - 🎯 Use when: Building RAG systems, complex pipelines
   
   **LangGraph:**
   - ✅ Best for: Stateful workflows, complex agent logic
   - ✅ Strengths: Visual workflows, state management
   - ❌ Weaknesses: Newer, less documentation
   - 🎯 Use when: Complex multi-step agents, stateful processes
   
   **OpenAI Agent SDK:**
   - ✅ Best for: Simple agents, OpenAI-only projects
   - ✅ Strengths: Native, simple, well-supported
   - ❌ Weaknesses: OpenAI-specific, less flexible
   - 🎯 Use when: Quick prototypes, OpenAI-focused apps
   
   **Azure Agent SDK:**
   - ✅ Best for: Azure ecosystem, enterprise deployments
   - ✅ Strengths: Azure integration, enterprise features
   - ❌ Weaknesses: Azure-specific, newer
   - 🎯 Use when: Azure deployments, enterprise needs

2. **Selection Guide** (10 min)
   ```python
   # Framework selection helper
   def choose_framework(requirements):
       if requirements["provider"] == "openai_only":
           return "OpenAI Agent SDK"
       elif requirements["provider"] == "azure":
           return "Azure Agent SDK"
       elif requirements["complexity"] == "high":
           return "LangGraph"
       elif requirements["rag"] == True:
           return "LangChain"
       else:
           return "LangChain"  # Default
   ```

**Exercise:**
- [ ] Complete comparison matrix
- [ ] Create selection guide
- [ ] Week 25 reflection

**Deliverable:**
- [ ] Working implementations in all frameworks
- [ ] Comparison documentation
- [ ] Selection guide
- [ ] Framework mastery achieved!

---

## 🎓 Congratulations on Completing 25 Weeks!

You've achieved comprehensive mastery in LLM Engineering across:
- ✅ **25 Weeks** of progressive learning
- ✅ **OpenAI & Azure OpenAI** expertise
- ✅ **Multi-Language** proficiency (Python, Go, Node.js, Angular, React, Next.js, .NET)
- ✅ **Agentic Frameworks** mastery (LangChain, LangGraph, SDKs)
- ✅ **Production-Ready** skills

**You Are Now:**
- An LLM Engineering expert across multiple platforms
- Capable of building production systems in any language
- Equipped with framework selection knowledge
- Ready for advanced work and leadership

---

## 🔄 Mastery Achieved!

**Complete Learning Path:**
- Weeks 1-5: Foundations (CoT, ReAct)
- Weeks 6-10: Intermediate (Structured outputs, Optimization)
- Weeks 11-15: Advanced (RAG, Multi-agent, Reasoning)
- Weeks 16-20: Production (Deployment, Evaluation, Specialization)
- Weeks 21-25: Multi-Platform Mastery (Azure, Multi-language, Frameworks)

**Keep learning, building, and sharing! 🚀**

