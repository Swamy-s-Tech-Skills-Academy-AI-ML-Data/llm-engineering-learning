# Week 8: Applied Mini Projects

**Theme:** Applied Mini Projects  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** One polished micro-app (Gradio or CLI app)  
**Platforms:** OpenAI + Azure OpenAI (Python, Go, Node.js)

---

## 🎯 Week 8 Learning Objectives

By the end of this week, you will:
- [ ] Build a complete LLM application
- [ ] Create user interfaces (Gradio/CLI)
- [ ] Integrate all learned concepts
- [ ] Deploy a working application
- [ ] Polish and document your project
- [ ] Choose implementation language (Python, Go, or Node.js)
- [ ] Support both OpenAI and Azure OpenAI

---

## 📅 Day-by-Day Breakdown

### Day 1: Project Planning (30 minutes)

**Learning Goal:** Plan your mini project

**Tasks (30 min):**

1. **Choose Project** (10 min)
   - Text summarizer
   - Q&A bot
   - Content generator
   - Data extractor

2. **Define Requirements** (10 min)
   - Features
   - User interface
   - Technical stack

3. **Create Project Structure** (10 min)
   - Set up folders
   - Create initial files

**Exercise:**
- [ ] Document project plan
- [ ] List features
- [ ] Set up structure

---

### Day 2: Core Implementation (30 minutes)

**Learning Goal:** Build core functionality

**Tasks (30 min):**

1. **Implement Core Logic** (20 min)
   - LLM integration
   - Data processing
   - Business logic

2. **Add Error Handling** (10 min)
   - Input validation
   - API error handling
   - User-friendly messages

**Exercise:**
- [ ] Core features working
- [ ] Error handling complete
- [ ] Test core functionality

---

### Day 3: User Interface (30 minutes)

**Learning Goal:** Build user interface

**Tasks (30 min):**

1. **Choose Interface** (5 min)
   - Gradio (web UI)
   - CLI (command line)
   - Both

2. **Implement Interface** (25 min)
   
   **Gradio Example:**
   ```python
   import gradio as gr
   
   def summarize(text):
       # Your summarization logic
       return summary
   
   interface = gr.Interface(
       fn=summarize,
       inputs="textbox",
       outputs="textbox",
       title="Text Summarizer"
   )
   interface.launch()
   ```

**Exercise:**
- [ ] Interface working
- [ ] User-friendly
- [ ] Tested

---

### Day 4: Polish & Integration (30 minutes)

**Learning Goal:** Polish the application

**Tasks (30 min):**

1. **Add Features** (15 min)
   - Input validation
   - Progress indicators
   - Help text

2. **Documentation** (15 min)
   - README
   - Usage examples
   - Installation guide

**Exercise:**
- [ ] Polish complete
- [ ] Documentation written
- [ ] Ready for deployment

---

### Day 5: Deployment & Review (30 minutes)

**Learning Goal:** Deploy and review

**Tasks (30 min):**

1. **Deploy** (15 min)
   - Local testing
   - Share with others
   - Get feedback

2. **Week 8 Reflection** (15 min)
   - What worked
   - What to improve
   - Lessons learned

**Deliverable:**
- [ ] Working application
- [ ] User interface
- [ ] Documentation
- [ ] Deployed project

---

## 🔄 Next Week Preview

**Week 9:** Autonomous / Planning Agents
- Planning agents vs reactive
- Advanced reasoning patterns
- Multi-step planning

