# S.M.A.R.T. Prompt Framework for GitHub Copilot Coding Agents

**ArchitectJourney Edition** - Framework for creating high-quality coding agent instructions aligned with architectural excellence standards and progressive learning levels.

---

## 🎯 **The S.M.A.R.T. Framework**

Use this framework to create highly effective coding agent instructions:

```text
S - Specific Role Definition (Senior .NET Developer, DevOps Engineer, AI Architect, etc.)
M - Mission-Critical Requirements (What must be accomplished with measurable outcomes)
A - Audience-Aware Communication (Team expertise level, architectural maturity, domain context)
R - Response Format Control (Code structure, architecture patterns, documentation style)
T - Task-Oriented Constraints (Technology stack, architectural patterns, forbidden actions)
```

---

## 🏛️ **ArchitectJourney Alignment**

When creating prompts, consider:

- **Learning Level Context**: Is this for Level 1-3 (foundational), Level 4-6 (enterprise), or Level 7-9 (strategic)?
- **Domain Integration**: How does this task span across 13 reference domains?
- **Architectural Patterns**: Which design/architecture patterns should be applied?
- **Progressive Complexity**: Is the implementation scoped appropriately for the team's level?

## 🏗️ **Advanced Problem Statement Template**

Use this enhanced template for coding agent tasks:

```markdown
## ROLE DEFINITION

You are a [Specific Role] specializing in [Technology Stack] with expertise in [Domain Areas]

## MISSION

[Clear, specific objective with measurable outcomes]

## CONTEXT

[Brief overview of current situation and progress made]

## CURRENT STATUS

- **Progress Made**: [Specific achievements and metrics]
- **Main Issue**: [Root cause analysis]
- **Files Affected**: [List specific files]

## REMAINING WORK

### 1. [Priority Task Name] (Priority N)

- **Problem**: [Specific technical issue]
- **Current Error**: [Exact error messages]
- **Solution Approach**: [Concrete implementation steps]
- **Files to Modify**: [Specific file paths]

## TECHNICAL CONSTRAINTS

- **🚨 CRITICAL**: [Non-negotiable requirements]
- **Framework**: [Technology stack requirements]
- **Dependencies**: [Package/version constraints]

## RESPONSE FORMAT REQUIREMENTS

- [Specific code structure expectations]
- [Documentation requirements]
- [Testing requirements]
- [Build/deployment considerations]

## WHAT NOT TO DO

- ❌ [Explicit forbidden actions with reasoning]

## WHAT TO DO

- ✅ [Explicit required actions with priority]

## SUCCESS CRITERIA

[Measurable outcomes with acceptance criteria]

## QUALITY STANDARDS

- [Code quality requirements]
- [Performance expectations]
- [Security considerations]
- [Maintainability standards]
```

## 🎭 **Role-Based Specialization Examples**

### **For .NET/Azure Development:**

```markdown
ROLE: You are a Senior .NET Developer specializing in Azure Functions isolated worker model, Entity Framework Core, and microservices architecture

EXPERTISE FOCUS: Extension method limitations, Moq framework patterns, .NET 9 compatibility, Azure service integration

OUTPUT REQUIREMENTS: Production-ready C# code with comprehensive error handling, unit tests with proper mocking patterns, and enterprise-grade documentation

MANDATORY VALIDATION:
- ✅ dotnet build --configuration Release (0 errors required)
- ✅ dotnet test --configuration Release (0 failures required)
```

### **For DevOps/Infrastructure:**

```markdown
ROLE: You are a DevOps Engineer specializing in .NET application deployment, CI/CD pipelines, and Azure infrastructure

EXPERTISE FOCUS: Build automation, package management, framework migrations, container orchestration

OUTPUT REQUIREMENTS: Build scripts, deployment configurations, infrastructure as code, and monitoring setup

MANDATORY VALIDATION:
- ✅ All build scripts execute successfully
- ✅ Infrastructure templates validate without errors
- ✅ Deployment processes complete end-to-end
```

### **For AI Agent & Intelligent Systems Development:**

```markdown
ROLE: You are a Senior AI Architect specializing in LLM-powered agent development, AI/ML system design, and intelligent workflow orchestration

EXPERTISE FOCUS: 
- Prompt engineering and agent reasoning frameworks
- LLM integration patterns and RAG (Retrieval-Augmented Generation)
- Agent evaluation metrics and observability
- Responsible AI and guardrails implementation

OUTPUT REQUIREMENTS:
- Production-ready agent code with comprehensive error handling
- Evaluation frameworks with clear success metrics
- Tracing and observability for agent decisions
- Security guardrails and input validation
- Documentation with agent behavior specifications and limitations

ARCHITECTURAL PATTERNS:
- ReAct (Reasoning + Acting) for complex problem-solving
- Chain-of-Thought for transparent agent reasoning
- Tool integration with proper error handling
- State management for multi-turn conversations

MANDATORY VALIDATION:
- ✅ Agent evaluation tests pass with defined metrics
- ✅ Tracing logs captured for all critical decisions
- ✅ No security vulnerabilities in prompt injection or model manipulation
- ✅ Response quality meets baseline metrics across test dataset
```

### **For Enterprise Architecture & System Design:**

```markdown
ROLE: You are a Lead Enterprise Architect specializing in scalable microservices architecture, distributed systems design, and organizational technology strategy

EXPERTISE FOCUS:
- SOLID principles and architectural patterns (layered, hexagonal, event-driven)
- Microservices decomposition and domain-driven design
- Cloud-native architecture and infrastructure as code
- System resilience, scalability, and observability
- Cross-cutting concerns: security, compliance, monitoring

OUTPUT REQUIREMENTS:
- Architecture Decision Records (ADRs) documenting trade-offs
- System design diagrams with components and integration points
- Reference implementations in multiple languages
- Migration strategies and cost optimization recommendations
- Security, compliance, and operational considerations

SUCCESS CRITERIA:
- ✅ Architecture aligns with organizational constraints
- ✅ Trade-offs clearly documented with reasoning
- ✅ Scalability and resilience characteristics defined
- ✅ Implementation examples demonstrate pattern application
```

## 🚨 **Critical Constraint Guidelines**

### **Framework/Package Versions:**

```markdown
- 🚨 CRITICAL: Use .NET 9 ONLY - DO NOT downgrade to .NET 8
- ❌ DO NOT modify Directory.Packages.props
- ❌ DO NOT downgrade package versions
```

### **File Modification Boundaries:**

```markdown
- ❌ DO NOT modify [specific files]
- ✅ ONLY modify [allowed areas]
```

### **Build Requirements:**

```markdown
When building, use: cd /path/to/project && dotnet build
Ensure all projects target net9.0 framework
```

## ✅ **Effective Instruction Patterns**

### **DO - Be Specific and Explicit:**

- ✅ "Create IHttpRequestWrapper interface to avoid GetValues() extension method"
- ✅ "Update tests to mock wrapper instead of HttpHeaders extension methods"
- ✅ "Fix test data generation in TestDataBuilder.cs - check ZIP file structure"

### **DON'T - Be Vague:**

- ❌ "Fix the tests"
- ❌ "Make it work"
- ❌ "Update the code"

## 📝 **Constraint Language Examples**

### **Strong Constraint Language That Works:**

```markdown
🚨 ABSOLUTELY DO NOT modify Directory.Packages.props or downgrade any packages.

The following packages MUST remain at their current .NET 9 versions:
- Npgsql.EntityFrameworkCore.PostgreSQL: Version="9.0.3"
- Microsoft.EntityFrameworkCore: Version="9.0.9"

CRITICAL: Any attempt to change these versions will require task restart.
```

### **Weak Language That Doesn't Work:**

```markdown
Please try to maintain .NET 9 compatibility
Prefer keeping current package versions
```

## 🎯 **Advanced Prompt Design Patterns**

### **Multi-Layered Prompt Architecture:**

```markdown
SYSTEM LAYER:
You are a [Specialist Role] with expertise in [Technology Stack] and [Domain Expertise].

CONTEXT LAYER:  
[Project context, current situation, business requirements]

TASK LAYER:
[Specific implementation task with clear deliverables]

SPECIFICATION LAYER:
[Detailed technical requirements, constraints, and acceptance criteria]
```

### **Conditional Logic for Complex Scenarios:**

```markdown
LOGIC FRAMEWORK:
IF issue_type == "extension_method_mocking":
THEN approach: Create wrapper interfaces to avoid Moq limitations
AND include: Dependency injection setup and test updates

ELIF issue_type == "package_compatibility":  
THEN approach: Update implementation patterns, NOT package versions
AND include: Code refactoring to maintain .NET 9 compatibility

ELIF issue_type == "build_failures":
THEN approach: Install missing SDKs or fix code issues
AND include: Detailed error analysis and resolution steps
```

### **Progressive Refinement Pattern:**

```markdown
BASE PROMPT: [Core role and task definition]

REFINEMENT 1: Add specific technical constraints
REFINEMENT 2: Define output format requirements  
REFINEMENT 3: Include quality standards and acceptance criteria
REFINEMENT 4: Add monitoring and validation requirements

FINAL VALIDATION: Ensure all constraints are explicitly stated
```

## 📊 **Output Format Control**

### **For Code Generation Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- Production-ready code with comprehensive error handling
- Unit tests with proper mocking patterns (avoiding extension methods)
- XML documentation for public APIs
- Consistent code style following project conventions
- No explanatory comments in code - let the code be self-documenting
- Include integration points and dependency injection setup
```

### **For Infrastructure Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- Valid configuration files (JSON/YAML/XML as specified)
- Infrastructure as Code with proper variable definitions
- Deployment scripts with error handling and rollback procedures
- Monitoring and alerting configurations
- Documentation with setup and troubleshooting guides
```

### **For Debugging Tasks:**

```markdown
OUTPUT REQUIREMENTS:
- Root cause analysis with supporting evidence
- Step-by-step resolution procedures
- Test cases to validate the fix
- Prevention strategies for similar issues
- Performance impact assessment
```

## 🤖 **AI Agent Evaluation & Observability Framework**

When designing AI agent tasks, include evaluation and observability requirements:

### **AI Agent Evaluation Template:**

```markdown
## EVALUATION FRAMEWORK

### Evaluation Metrics
- **Accuracy**: Correctness of agent responses against ground truth (target: >95%)
- **Latency**: Response time within acceptable bounds (target: <2000ms)
- **Safety**: Adherence to guardrails and security constraints (target: 100%)
- **Coherence**: Response clarity and logical flow (1-5 scale)

### Test Dataset
- **Size**: Minimum 50 diverse test cases covering edge cases
- **Coverage**: Include normal operation, error conditions, and boundary scenarios
- **Distribution**: Representative of production usage patterns

### Success Criteria
- Baseline accuracy exceeds target threshold
- No security or safety violations across test dataset
- Latency remains within acceptable range
- Response quality consistent across diverse inputs

### Evaluation Execution
- Run evaluations against complete test dataset
- Capture detailed metrics and failure analysis
- Document performance improvements and regressions
- Validate changes don't degrade existing functionality
```

### **AI Agent Tracing & Observability Template:**

```markdown
## TRACING & OBSERVABILITY REQUIREMENTS

### Trace Coverage
- Agent decision points and reasoning steps
- Tool invocations and results
- Error handling and recovery attempts
- Performance metrics (latency, token usage)

### Tracing Implementation
- Structured logging with correlation IDs
- OpenTelemetry instrumentation for observability
- Trace storage and analysis tools
- Real-time monitoring dashboards

### Observable Signals
- Agent state transitions and context changes
- Token usage and cost tracking
- Error rates and failure patterns
- User satisfaction and feedback signals

### Analysis & Improvement
- Identify bottlenecks and failure modes
- Detect drift in agent behavior
- Measure business impact of improvements
- Plan optimizations based on observed patterns
```

## 🎯 **Success Indicators**

### **Agent is working correctly when:**

- ✅ It acknowledges constraints explicitly
- ✅ It asks clarifying questions about boundaries
- ✅ It installs missing SDKs instead of downgrading
- ✅ It focuses on code changes, not configuration changes
- ✅ It provides detailed progress updates

### **Agent needs restart when:**

- ❌ It immediately modifies forbidden files
- ❌ It changes package versions without asking
- ❌ It ignores explicit constraints
- ❌ It takes overly broad approach to simple problems

## 🔄 **Agent Restart Protocol**

### **When to restart the coding agent:**

- Agent modifies forbidden files (like Directory.Packages.props)
- Agent downgrades package versions
- Agent changes target framework
- Agent takes wrong architectural approach

### **How to restart:**

1. Close current pull request
2. Create new pull request with more explicit constraints
3. Include specific examples of what went wrong
4. Add stronger constraint language

## 🏗️ **Cross-Domain Architecture Patterns**

When tasks span multiple architectural domains, apply these patterns:

### **Pattern: Domain-Driven Design Integration**

```markdown
ARCHITECTURAL PATTERN: Domain-Driven Design (DDD) with Ubiquitous Language

DOMAINS INVOLVED:
- Core Domain: [Main business capability]
- Supporting Domain: [Shared services]
- Generic Domain: [Infrastructure/libraries]

IMPLEMENTATION REQUIREMENTS:
- Clear bounded contexts with explicit boundaries
- Shared kernel defined and documented
- Anticorruption layers for external integrations
- Value objects and aggregates properly designed
- Repository pattern for data access
- Domain events for cross-boundary communication

QUALITY GATES:
✅ Bounded contexts have clear interfaces
✅ Ubiquitous language used consistently across code and docs
✅ No circular dependencies between contexts
✅ Integration tests validate context boundaries
```

### **Pattern: Microservices Architecture**

```markdown
ARCHITECTURAL PATTERN: Event-Driven Microservices

CHARACTERISTICS:
- Independent deployment and scaling
- Asynchronous communication via events
- Database per service (no shared databases)
- API gateway for client communication
- Service mesh for inter-service concerns

IMPLEMENTATION REQUIREMENTS:
- Event schema definition and versioning
- Saga pattern for distributed transactions
- Circuit breaker for failure handling
- Service discovery and load balancing
- Distributed tracing across services
- Monitoring and alerting per service

QUALITY GATES:
✅ Services can be deployed independently
✅ Event contracts validated before deployment
✅ Failure scenarios handled gracefully
✅ End-to-end tracing captures cross-service flows
✅ No database coupling between services
```

### **Pattern: Hexagonal Architecture (Ports & Adapters)**

```markdown
ARCHITECTURAL PATTERN: Hexagonal (Ports & Adapters) - Isolate Business Logic

STRUCTURE:
- Core: Pure business logic (domain models, use cases)
- Ports: Interfaces defining system boundaries
- Adapters: Implementations of ports (frameworks, databases, APIs)

IMPLEMENTATION REQUIREMENTS:
- Business logic has zero framework dependencies
- Ports define contracts clearly
- Multiple adapter implementations possible
- Testing possible without external dependencies
- Clear separation of concerns

QUALITY GATES:
✅ Core domain testable in isolation
✅ Framework changes don't affect business logic
✅ Adapter implementations are interchangeable
✅ No circular dependencies
```

## 📋 **Universal PR Success Template**

Include this template in EVERY coding agent PR for consistent validation:

```markdown
## 🎯 MANDATORY SUCCESS CRITERIA (NON-NEGOTIABLE)

### Build Requirements
```powershell
# MUST PASS: Full solution build with zero errors
dotnet build --configuration Release --verbosity normal
# Expected Result: "Build succeeded. 0 Error(s)"
```

### Test Requirements

```powershell
# MUST PASS: All existing unit tests
dotnet test --configuration Release --logger "console;verbosity=normal"
# Expected Result: "Test Run Successful. Total tests: X, Passed: X, Failed: 0, Skipped: 0"
```

## 📋 FINAL CHECKLIST

Before marking this PR ready for review:

- [ ] ✅ `dotnet build` succeeds with 0 errors across entire solution
- [ ] ✅ `dotnet test` passes with 0 failures across all test projects
- [ ] ✅ All original issues resolved completely
- [ ] ✅ No package downgrades or framework changes
- [ ] ✅ All existing functionality preserved
- [ ] ✅ Production-ready error handling implemented

**CRITICAL**: Do not mark this PR as ready for review until ALL build and test validations pass successfully.

```

## 🚀 **TraceMind-Specific S.M.A.R.T. Example**

```markdown
ROLE: You are a Senior Enterprise Architect specializing in AI-powered root cause analysis systems, Azure cloud architecture, and .NET Aspire microservices orchestration

MISSION: Complete the TraceMind RCA Portal - an enterprise-grade, event-driven AI-powered RCA copilot for incident analysis using .NET 9, Blazor Web App, Azure Functions, PostgreSQL with pgvector, and Azure OpenAI GPT-5-chat

AUDIENCE: Development team with expertise in:
- .NET 9, Blazor Web App (Server + WASM modes), and Azure Functions
- Event-driven architecture with Azure Service Bus
- Azure cloud services (OpenAI GPT-5-chat, Blob Storage, Service Bus, AI Search)
- PostgreSQL with pgvector extensions and YARP API Gateway

RESPONSE FORMAT:
- Production-ready code with comprehensive error handling
- Azure Bicep infrastructure templates for automated deployment
- .NET Aspire AppHost orchestration for local development
- Enterprise-grade documentation with architecture diagrams

TASK CONSTRAINTS:
- 🚨 CRITICAL: Use .NET 9 ONLY - DO NOT downgrade to .NET 8
- Architecture: TraceMind.AppHost, TraceMind.ApiGateway, TraceMind.BlazorApp, etc.
- Quality Standards: Zero build warnings, 100% test pass rate
- Technology Stack: .NET 9 Aspire with microservices orchestration
```

## 📚 **Best Practices Summary**

1. **Be Specific**: Define exact roles, technologies, and constraints
2. **Set Clear Boundaries**: Use strong constraint language
3. **Define Success**: Include measurable outcomes and validation steps
4. **Control Output**: Specify exactly what format and quality you expect
5. **Plan for Failure**: Include restart protocols and troubleshooting
6. **Validate Everything**: Always include build and test requirements
7. **Document Thoroughly**: Ensure all decisions and constraints are recorded
8. **Align with Architecture**: Reference learning levels and architectural patterns
9. **Enable Observability**: Include tracing and evaluation requirements
10. **Progressive Complexity**: Scale scope to team's architectural maturity level

---

## ⚡ **Quick Reference Checklist**

Use this checklist before submitting any coding agent task:

### **Role Definition**

- [ ] Specific role/expertise clearly stated
- [ ] Technology stack and frameworks identified
- [ ] Expected audience knowledge level documented
- [ ] Domain context provided

### **Task Clarity**

- [ ] Mission and objectives clearly defined
- [ ] Success criteria are measurable
- [ ] Scope is appropriately sized
- [ ] Priority and sequencing defined

### **Technical Requirements**

- [ ] Framework and version constraints specified
- [ ] Architectural patterns identified
- [ ] Dependencies listed explicitly
- [ ] Integration points documented

### **Constraints & Boundaries**

- [ ] Forbidden actions explicitly listed (❌)
- [ ] Required actions explicitly listed (✅)
- [ ] File modification boundaries defined
- [ ] Architectural decision constraints included

### **Quality & Validation**

- [ ] Code quality standards specified
- [ ] Build/test requirements included
- [ ] Performance expectations defined
- [ ] Security considerations addressed

### **AI Agent Specifics** (if applicable)

- [ ] Evaluation metrics defined
- [ ] Test dataset requirements specified
- [ ] Tracing requirements included
- [ ] Safety guardrails documented

### **Output Expectations**

- [ ] Code format and style specified
- [ ] Documentation requirements defined
- [ ] Testing approach specified
- [ ] Deployment considerations included

---

## 📋 **FINAL VALIDATION CHECKLIST**

Before submitting ANY coding agent PR or task completion:

- [ ] ✅ All technical constraints acknowledged
- [ ] ✅ Success criteria clearly measurable
- [ ] ✅ Build passes without errors/warnings
- [ ] ✅ Tests pass with 0 failures
- [ ] ✅ No forbidden files modified
- [ ] ✅ Architectural patterns applied correctly
- [ ] ✅ Documentation is complete and accurate
- [ ] ✅ Evaluation metrics captured (for AI agents)
- [ ] ✅ Tracing configured (for AI agents)
- [ ] ✅ Code review readiness criteria met

---

## 🎓 **ArchitectJourney Learning Integration**

Align your coding agent tasks with the learning progression:

### **For Levels 1-3 (Foundation & Patterns):**

- Focus on design pattern application
- SOLID principles demonstration
- Clean code and testing practices
- Language-specific idioms and best practices

### **For Levels 4-6 (Enterprise & Cloud):**

- Microservices architecture implementation
- Cloud platform integration (Azure, AWS, GCP)
- DevOps and CI/CD pipeline design
- System scalability and resilience patterns

### **For Levels 7-9 (Strategy & AI/ML):**

- AI/ML system architecture
- Enterprise security and governance
- Strategic technology decisions
- Leadership and organizational transformation

This framework ensures consistent, high-quality results from GitHub Copilot coding agents while preventing common issues and maintaining enterprise-grade architectural standards aligned with ArchitectJourney learning levels.
