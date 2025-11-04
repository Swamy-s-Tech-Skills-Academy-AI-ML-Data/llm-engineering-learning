# Week 6: Structured Outputs & Orchestration

**Theme:** Structured Outputs & Orchestration  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Reliable JSON / tool calling + Function call schema set

---

## 🎯 Week 6 Learning Objectives

By the end of this week, you will:
- [ ] Generate structured JSON outputs from LLMs
- [ ] Use function calling APIs
- [ ] Define tool schemas
- [ ] Build reliable structured output systems
- [ ] Handle validation and errors

---

## 📅 Day-by-Day Breakdown

### Day 1: JSON Schema & Structured Outputs (30 minutes)

**Learning Goal:** Generate reliable JSON from LLMs

**Tasks (30 min):**

1. **JSON Schema Definition** (10 min)
   ```python
   schema = {
       "type": "object",
       "properties": {
           "summary": {"type": "string"},
           "key_points": {
               "type": "array",
               "items": {"type": "string"}
           },
           "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]}
       },
       "required": ["summary", "key_points"]
   }
   ```

2. **Structured Output Generation** (20 min)
   ```python
   def get_structured_output(text: str, schema: dict) -> dict:
       """Get structured output from LLM"""
       prompt = f"""
       Analyze this text and return JSON matching this schema:
       {json.dumps(schema, indent=2)}
       
       Text: {text}
       
       Return only valid JSON:
       """
       
       response = client.chat.completions.create(
           model="gpt-4",
           messages=[{"role": "user", "content": prompt}],
           response_format={"type": "json_object"}  # GPT-4 feature
       )
       
       return json.loads(response.choices[0].message.content)
   ```

**Exercise:**
- [ ] Create JSON schema for a task
- [ ] Generate structured outputs
- [ ] Validate JSON structure

---

### Day 2: Function Calling API (30 minutes)

**Learning Goal:** Use OpenAI function calling

**Tasks (30 min):**

1. **Define Functions** (15 min)
   ```python
   functions = [
       {
           "name": "get_weather",
           "description": "Get current weather",
           "parameters": {
               "type": "object",
               "properties": {
                   "location": {"type": "string"},
                   "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
               },
               "required": ["location"]
           }
       }
   ]
   ```

2. **Function Calling** (15 min)
   ```python
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": "What's the weather in Paris?"}],
       functions=functions,
       function_call="auto"
   )
   
   # Check if function call requested
   message = response.choices[0].message
   if message.function_call:
       function_name = message.function_call.name
       arguments = json.loads(message.function_call.arguments)
       # Execute function
   ```

**Exercise:**
- [ ] Create function definitions
- [ ] Test function calling
- [ ] Handle function execution

---

### Day 3: Tool Schema Design (30 minutes)

**Learning Goal:** Design robust tool schemas

**Tasks (30 min):**

1. **Schema Best Practices** (15 min)
   - Clear descriptions
   - Required vs optional
   - Type validation
   - Enum values

2. **Schema Registry** (15 min)
   ```python
   class ToolRegistry:
       def __init__(self):
           self.tools = {}
       
       def register(self, name: str, schema: dict, handler: callable):
           self.tools[name] = {
               "schema": schema,
               "handler": handler
           }
       
       def get_function_definitions(self):
           """Convert to OpenAI function format"""
           return [
               {
                   "name": name,
                   "description": tool["schema"].get("description", ""),
                   "parameters": tool["schema"]
               }
               for name, tool in self.tools.items()
           ]
   ```

**Exercise:**
- [ ] Create tool registry
- [ ] Register 3+ tools
- [ ] Test schema conversion

---

### Day 4: Validation & Error Handling (30 minutes)

**Learning Goal:** Ensure reliable structured outputs

**Tasks (30 min):**

1. **JSON Validation** (15 min)
   ```python
   import jsonschema
   
   def validate_output(data: dict, schema: dict) -> tuple[bool, str]:
       """Validate JSON against schema"""
       try:
           jsonschema.validate(data, schema)
           return True, "Valid"
       except jsonschema.ValidationError as e:
           return False, str(e)
   ```

2. **Error Recovery** (15 min)
   - Retry on invalid JSON
   - Fix common errors
   - Fallback strategies

**Exercise:**
- [ ] Implement validation
- [ ] Add error recovery
- [ ] Test with invalid inputs

---

### Day 5: Review & Practice (30 minutes)

**Tasks:**
- Review concepts
- Complete exercises
- Week 6 reflection

**Deliverable:**
- [ ] Tool registry with schemas
- [ ] Function calling working
- [ ] Validation system

---

## 🔄 Next Week Preview

**Week 7:** Optimization & Performance
- Latency optimization
- Token cost reduction
- Caching strategies
- Model selection

