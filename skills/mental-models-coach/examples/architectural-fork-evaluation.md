# Worked Example: Evaluating Monolith vs. Microservices

This case study demonstrates the multi-disciplinary latticework in action during a contentious architectural decision fork.

---

## 1. The Decision Context
- **Company:** B2B SaaS startup with 8 software engineers.
- **Problem Statement:** The lead engineer proposes breaking up their monolithic Rails/PostgreSQL backend into 12 distinct Go microservices, arguing that "microservices are the industry standard for scalability and modern teams."
- **Requested Decision:** Should leadership approve the 6-month microservice migration roadmap?

---

## 2. Multi-Model Evaluation

### Lens 1: Conway's Law (Melvin Conway, 1968)
- *Principle:* System architecture reflects the communication structure of the organization.
- *Diagnosis:* An 8-person engineering team sits together in one Slack channel and one daily standup. Decomposing the system into 12 independently deployable services creates an impedance mismatch: 8 people must now maintain 12 CI pipelines, 12 Dockerfiles, and cross-service RPC contracts.
- *Verdict:* The team's communication graph is a unified clique, not a partitioned graph. Conway's Law dictates that 12 microservices will create massive cross-service pull request bottlenecks.

### Lens 2: Gall's Law (John Gall, 1975)
- *Principle:* A complex system that works invariably evolved from a simple system that worked. A complex system designed from scratch never works.
- *Diagnosis:* Attempting to design 12 new service boundary interfaces upfront without deep transactional knowledge will result in the wrong boundaries (distributed monolith), where a single business change requires coordinated commits across 4 services.
- *Verdict:* You cannot design the correct microservice seams before the business domain model stabilizes.

### Lens 3: Second-Order Thinking (Garrett Hardin / Howard Marks)
- *First-Order Effect:* Engineers get to write clean, isolated Go code in fresh repositories.
- *Second-Order Effect:* Debugging a customer transaction now requires distributed tracing (Jaeger/OpenTelemetry), two-phase commits or saga patterns for database transactions, network retry idempotency, and handling partial network failures.
- *Third-Order Effect:* Developer velocity drops by 60% as engineers spend their time managing Kubernetes YAML and network retries rather than shipping customer features.

---

## 3. The Anti-Sycophancy Recommendation & Action Plan

Instead of validating the lead engineer's proposal or flatly rejecting it without nuance, the agent formulates a structured compromise using **Via Negativa** and **Modular Monolith**:

1. **Hard Negative Constraint:** Reject the distributed network split. Mandate zero network boundaries between business logic modules for the next 12 months.
2. **Subtractive Architecture (Modular Monolith):** Enforce strict domain module boundaries *inside* the existing monolith (e.g. using Packwerk or domain packages). Forbid direct cross-domain ActiveRecord table joins.
3. **Evolutionary Seam (Strangler Fig Pattern):** Only when an individual domain module proves to have wildly different scaling characteristics (e.g. an asynchronous PDF processing queue) is that single bounded context extracted into an external worker.
