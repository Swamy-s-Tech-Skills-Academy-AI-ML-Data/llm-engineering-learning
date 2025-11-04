# LLM Engineering Learning Repository Verification and Content Enhancement

## Context

You are working with **llm-engineering-learning**, a comprehensive learning repository for mastering LLM Engineering. The repository is designed to accompany **Ed Donner's "LLM Engineering: Master AI, Large Language Models & Agents"** Udemy course and provides:

- **20-Week Progressive Learning Path** (Foundations → Mastery)
- **5 Days × 30 Minutes per Week** structured learning
- **Deep Dives**: Chain-of-Thought (CoT), ReAct (Reasoning + Acting), and reasoning patterns
- **Practical Projects**: From simple scripts to production-ready applications

Target Folders for Verification:

- `docs/learning-plan.md` (Master document)
- `docs/weeks/` (Week1.md through Week20.md)
- `prompts/` (Prompt templates)
- `agents/` (Agent implementations)
- `tools/` (Tool definitions)
- `eval/` (Evaluation frameworks)
- `rag/` (RAG systems)
- `scripts/` (CLI utilities)
- `notebooks/` (Exploratory notebooks)
- `.github/` (Copilot instructions)

Primary Objective:
Perform a COMPREHENSIVE audit of the repository using LLM Engineering learning standards and quality criteria. Verify file contents, run structured checks, and produce actionable reports with suggestions and fixes.

---

## LLM Engineering Learning Verification Checks

### A. **File Content Inspection**

- Open and verify every file (no file skipped)
- Ensure markdown formatting compliance
- Check for completeness and consistency with learning objectives

### B. **Learning Path Alignment**

- Verify content aligns with correct Week (1-20)
- Validate prerequisites are appropriate and documented
- Check learning progression is logical and sequential (Week 1 → Week 20)
- Ensure cross-references between weeks are accurate
- Validate day-by-day structure (5 days × 30 minutes)
- Check alignment with Ed Donner's course content

### C. **Content Accuracy & Quality**

- Verify technical correctness and architectural soundness
- Ensure completeness for stated learning objectives
- Check alignment with architectural best practices and design patterns
- Validate examples are current, relevant, and runnable

### D. **LLM Engineering Learning Metadata Requirements**

Check for presence of:

- Week designation (Week 1-20)
- Day-by-day breakdown (Day 1-5)
- Prerequisites and dependencies (references to previous weeks)
- Learning Objectives (clear, measurable, specific)
- Core Topics (CoT, ReAct, RAG, Agents, etc.)
- Practical Projects and Exercises
- Deliverables per week
- Time Commitment (5 days × 30 minutes = 2.5 hours/week)
- Deep Dive sections (CoT in Week 3, ReAct in Week 5, Reasoning in Week 14)

### E. **Naming Convention Compliance**

- Use kebab-case for filenames
- Use consistent naming patterns within domain folders
- Verify folder structure follows repository standards
- Check zero-padded numeric prefixes (01_, 02_, not 00_)

### F. **Broken Links & References**

- Verify all internal cross-references work correctly
- Check README files and navigation structure
- Validate external resource links and references
- Ensure level/phase navigation links are accurate

### G. **Content Quality Standards**

- Spellcheck and grammar verification
- Character encoding validation (UTF-8 only)
- Markdown formatting compliance (markdownlint standards)
- Code example correctness and completeness
- Proper code fence language specification

### H. **Domain Organization**

- Verify proper placement in correct domain folder
- Check cross-domain references are accurate
- Validate level/phase organization is clear and discoverable
- Ensure no content duplication across domains

### I. **Repository Structure Clarity**

- Verify folder organization is intuitive
- Check navigability and discoverability
- Validate table of contents accuracy
- Ensure README files guide users through content

### J. **Content Currency & Relevance**

- Verify content reflects current technologies and practices
- Check for deprecated patterns or outdated information
- Validate relevance to stated learning objectives
- Assess alignment with industry trends in architecture

### K. **Practical Application**

- Verify examples are runnable and technically correct
- Check projects align with learning objectives
- Validate edge cases and error handling coverage
- Ensure code examples follow best practices for their language/framework

### L. **Educational Effectiveness**

- Assess clarity and readability for target audience
- Verify learning progression (simple → complex)
- Check engagement through practical relevance
- Validate use of multiple learning modalities (text, code, diagrams, examples)

### M. **Architecture Pattern Documentation**

- Verify pattern intent and participants are clearly explained
- Check when/when-not-to-use guidance is present
- Validate trade-offs are discussed
- Ensure implementation examples are provided in multiple languages where relevant

### N. **Diagram & Visual Quality**

- Verify ASCII diagrams are provided as fallback
- Check Mermaid diagrams are well-structured
- Validate visual clarity and accuracy
- Ensure diagrams support learning objectives

### O. **Cross-Week Integration**

- Check proper references between weeks
- Verify content connections across weeks (Week 3 CoT → Week 5 ReAct → Week 14 Reasoning)
- Validate integration between learning plan and weekly guides
- Ensure consistency in terminology (CoT, ReAct, tokens, context windows, etc.)
- Check that concepts build progressively

---

## LLM Engineering Learning Content Standards

### Learning Structure

- **20-Week Path**: Progressive from Week 1 (Foundations) to Week 20 (Mastery)
- **Weekly Structure**: 5 days × 30 minutes = 2.5 hours per week
- **Deep Dives**: Comprehensive coverage of CoT (Week 3), ReAct (Week 5), Reasoning Patterns (Week 14)
- **Progressive Complexity**: Content builds from basics (API calls) to advanced (multi-agent systems, production)

### Content Organization

- **By Week**: Content clearly indicates which week(s) it addresses (Week 1-20)
- **By Day**: Each week has 5 days with specific tasks
- **By Topic**: Organized by theme (Foundations, Prompt Engineering, Agents, RAG, etc.)
- **By Learning Modality**: Mix of conceptual explanation, code examples, exercises, and practical projects

### Quality Requirements

- **Accuracy**: Technically correct and architecturally sound
- **Completeness**: Addresses stated learning objectives fully
- **Clarity**: Clear explanations with practical examples and runnable code
- **Relevance**: Directly applicable to architecture practice and decision-making
- **Currency**: Reflects current technologies and best practices
- **Practicality**: Includes actionable guidance, patterns, and examples
- **Pedagogy**: Uses appropriate learning techniques for target audience

### File Standards

- **Naming**: kebab-case filenames, descriptive names indicating content focus
- **Structure**: Clear sections, logical flow, easy navigation
- **Metadata**: Learning level, prerequisites, objectives, topics, estimated time
- **References**: Cross-references to related content with working links
- **Examples**: Runnable code with multiple language implementations where relevant
- **Visuals**: ASCII diagrams and Mermaid diagrams where helpful
- **Length**: Focused, modular content (typically 100-300 lines for reference materials, scalable for complex topics)

---

## Output Requirements

### 1. SUMMARY (Top-level)

```json
{
  "repo_name": "llm-engineering-learning",
  "total_files_checked": 0,
  "total_issues_found": 0,
  "learning_plan_compliance_percentage": 0.0,
  "high_severity_count": 0,
  "medium_severity_count": 0,
  "low_severity_count": 0,
  "suggested_next_steps": ["step1", "step2", "step3"]
}
```

### 2. DETAILED_REPORT (array of file reports)

For each file:

```json
{
  "file_path": "string",
  "week_designation": "string (e.g., Week 3 - Chain-of-Thought Deep Dive)",
  "topic_category": "string (e.g., Prompt Engineering, Agents, RAG, Evaluation)",
  "checks_passed": ["list of check keys, e.g., A,B,C,F,G,I"],
  "learning_metadata_present": true/false,
  "content_quality_score": "0-100",
  "practical_application_score": "0-100",
  "issues": [
    {
      "id": "string (unique, e.g., AJ-001)",
      "severity": "high|medium|low",
      "line_start": 0,
      "line_end": 0,
      "description": "string",
      "suggested_fix": "string",
      "fix_type": "replace|delete|add|rename|format|link-fix|metadata-add",
      "llm_learning_violation_type": "string (e.g., missing-objectives, broken-link, outdated-pattern, missing-deep-dive)"
    }
  ],
  "overall_status": "learning_plan_compliant|needs_updates|remove",
  "quick_fix_patch": "string or null"
}
```

### 3. LEARNING_PATH_ANALYSIS

```json
{
  "week_coverage": { "Week1": 0, "Week2": 0, "..": 0, "Week20": 0 },
  "topic_distribution": { "Foundations": 0, "Prompt Engineering": 0, "Agents": 0, "RAG": 0, "Evaluation": 0, "Production": 0 },
  "deep_dive_coverage": { "CoT": false, "ReAct": false, "Reasoning Patterns": false },
  "progression_score": "0-100",
  "gap_analysis": ["identified learning gaps", "missing weekly guides", "incomplete deep dives"]
}
```

### 4. CONTENT_QUALITY_ANALYSIS

```json
{
  "technical_accuracy_score": "0-100",
  "clarity_and_readability_score": "0-100",
  "practical_application_score": "0-100",
  "learning_effectiveness_score": "0-100",
  "examples_quality_score": "0-100",
  "pattern_documentation_score": "0-100"
}
```

### 5. METADATA_COMPLIANCE_SUMMARY

```json
{
  "files_with_complete_metadata": 0,
  "files_missing_learning_objectives": 0,
  "files_missing_prerequisites": 0,
  "files_missing_core_topics": 0,
  "files_with_incorrect_naming": 0,
  "metadata_compliance_percentage": "0-100"
}
```

### 6. CROSS_REFERENCE_VALIDATION

```json
{
  "internal_links_valid": 0,
  "broken_internal_links": 0,
  "domain_cross_references": 0,
  "level_cross_references": 0,
  "phase_cross_references": 0,
  "external_link_validation": "needs_verification"
}
```

### 7. IMPROVEMENT_RECOMMENDATIONS

```json
{
  "structural_improvements": ["recommendation1"],
  "content_enhancements": ["recommendation2"],
  "metadata_additions": ["recommendation3"],
  "domain_reorganization": ["recommendation4"],
  "pattern_documentation": ["recommendation5"]
}
```

Formatting rules for output:

- Output only JSON (no prose outside JSON) so it can be parsed by automation.
- JSON must be UTF-8, compact but human-readable (use 2-space indentation).
- If you include patches, ensure diffs use unified diff format and are properly escaped inside JSON strings.

Strict privacy & reasoning constraint:

- Use ReAct-style internal reasoning and actions to determine findings BUT DO NOT OUTPUT ANY CHAIN-OF-THOUGHT, internal logs, or private reasoning. Only provide the JSON structured output described above.
- If you cannot confirm something (e.g., external API version), mark it "needs_verification" and state what command or URL the operator should run to confirm.

Deliverables:

- The complete JSON report as described above.
- For each suggested_fix that is small (<= 30 lines), include a quick_fix_patch.
- For larger fixes, include exact instructions and code snippets for maintainers to apply the change.
- A final top-level "suggested_next_steps" with three clear actions (e.g., run linter, open PR with patches, run link-checker CI).

Formatting rules for output:

- Output only JSON (no prose outside JSON) so it can be parsed by automation.
- JSON must be UTF-8, compact but human-readable (use 2-space indentation).
- If you include patches, ensure diffs use unified diff format and are properly escaped inside JSON strings.

Strict privacy & reasoning constraint:

- Use ReAct-style internal reasoning and actions to determine findings BUT DO NOT OUTPUT ANY CHAIN-OF-THOUGHT, internal logs, or private reasoning. Only provide the JSON structured output described above.
- If you cannot confirm something (e.g., external API version), mark it “needs_verification” and state what command or URL the operator should run to confirm.

Deliverables:

- The complete JSON report as described above.
- For each suggested_fix that is small (<= 30 lines), include a quick_fix_patch.
- For larger fixes, include exact instructions and code snippets for maintainers to apply the change.
- A final top-level "suggested_next_steps" with three clear actions (e.g., run linter, open PR with patches, run link-checker CI).

Behavioral expectations:

- **LLM Engineering Learning-First Approach**: Prioritize learning effectiveness and alignment with 20-week structure
- **Educational Quality Focus**: Flag content that doesn't meet LLM engineering standards
- **Learning Path Integrity**: Ensure content fits logically within weeks with proper prerequisites (Week N requires Week N-1)
- **Practical Relevance**: Verify content provides actionable LLM engineering guidance and hands-on exercises
- **Cross-Week Integration**: Validate proper connections between weeks (CoT Week 3 → ReAct Week 5 → Reasoning Week 14)
- **Metadata Compliance**: Prioritize missing learning objectives, deliverables, and day-by-day structure as high-severity
- **Progressive Complexity**: Ensure content properly builds from basics (API calls) to advanced (multi-agent systems)
- **Pattern Excellence**: Verify reasoning patterns (CoT, ReAct, ToT, etc.) include examples, use cases, and best practices
- **Code Quality**: Validate examples follow best practices, are runnable, and match copilot-instructions.md conventions
- **Deep Dive Completeness**: Ensure Week 3 (CoT), Week 5 (ReAct), and Week 14 (Reasoning) have comprehensive deep dives

---

## Formatting Rules

- Output as JSON (no prose outside JSON blocks)
- Use 2-space indentation for readability
- Escape patches in unified diff format
- UTF-8 encoding only
- Quote all JSON keys and string values

---

## Deliverables

1. Complete JSON report following ArchitectJourney output requirements
2. Compliance scoring and educational quality assessment
3. Learning path analysis and gap identification
4. Cross-reference validation results
5. Content quality analysis by domain and level
6. Three clear next steps to improve repository and learning effectiveness

---

## Start Now

Open every file in the repository tree, run ArchitectJourney-specific checks, and produce the structured JSON report following these requirements. Focus on learning effectiveness, content quality, architectural soundness, and alignment with the 9-level and 9-phase structure.
