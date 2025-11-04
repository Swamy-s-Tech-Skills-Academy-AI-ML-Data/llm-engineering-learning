# Week 9: Autonomous / Planning Agents

**Theme:** Autonomous / Planning Agents  
**Time Commitment:** 5 days × 30 minutes = 2.5 hours  
**Primary Outcome:** Planner vs reactive comparison + Planning eval notes

---

## 🎯 Week 9 Learning Objectives

By the end of this week, you will:
- [ ] Understand planning agents
- [ ] Compare planning vs reactive approaches
- [ ] Build planning agents
- [ ] Implement advanced reasoning
- [ ] Evaluate planning effectiveness

---

## 📅 Day-by-Day Breakdown

### Day 1: Planning Agents Introduction (30 minutes)

**Learning Goal:** Understand planning agents

**Tasks (30 min):**

1. **Planning vs Reactive** (15 min)
   - **Reactive**: Respond to current state
   - **Planning**: Create plan first, then execute

2. **Planning Agent Structure** (15 min)
   ```python
   class PlanningAgent:
       def plan(self, goal: str) -> List[str]:
           """Create plan to achieve goal"""
           pass
       
       def execute(self, plan: List[str]):
           """Execute plan steps"""
           pass
   ```

**Exercise:**
- [ ] Understand planning concepts
- [ ] Compare approaches
- [ ] Design planning agent

---

### Day 2: Building Planning Agents (30 minutes)

**Learning Goal:** Build a planning agent

**Tasks (30 min):**

1. **Plan Generation** (15 min)
   ```python
   def generate_plan(goal: str) -> List[str]:
       """Generate plan using LLM"""
       prompt = f"""
       Create a step-by-step plan to achieve this goal:
       Goal: {goal}
       
       Plan:
       1. [Step 1]
       2. [Step 2]
       3. [Step 3]
       """
       # Use LLM to generate plan
   ```

2. **Plan Execution** (15 min)
   - Execute steps sequentially
   - Handle failures
   - Update plan if needed

**Exercise:**
- [ ] Implement planning agent
- [ ] Test plan generation
- [ ] Test execution

---

### Day 3: Advanced Planning (30 minutes)

**Learning Goal:** Advanced planning techniques

**Tasks (30 min):**

1. **Hierarchical Planning** (15 min)
   - Break plans into sub-plans
   - Multi-level planning

2. **Dynamic Planning** (15 min)
   - Adapt plans based on results
   - Re-plan when needed

**Exercise:**
- [ ] Implement hierarchical planning
- [ ] Add dynamic replanning
- [ ] Test on complex goals

---

### Day 4: Planning Evaluation (30 minutes)

**Learning Goal:** Evaluate planning agents

**Tasks (30 min):**

1. **Create Evaluation Framework** (20 min)
   - Compare planning vs reactive
   - Measure success rates
   - Track planning quality

2. **Run Comparisons** (10 min)
   - Test both approaches
   - Document results

**Exercise:**
- [ ] Evaluate agents
- [ ] Compare results
- [ ] Document findings

---

### Day 5: Review & Practice (30 minutes)

**Tasks:**
- Review planning concepts
- Complete exercises
- Week 9 reflection

**Deliverable:**
- [ ] Planning agent
- [ ] Evaluation results
- [ ] Comparison notes

---

## 🔄 Next Week Preview

**Week 10:** Deployment & Scaling
- Local deployment
- Cloud deployment
- Scaling strategies
- Production considerations

