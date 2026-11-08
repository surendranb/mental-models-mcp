# Failure Boundaries & Anti-Patterns in Mental Model Application

A mental model applied outside its valid operating envelope ceases to be an analytical tool and becomes a cognitive hazard.

Every practitioner and AI agent must run this **Failure Boundary Checklist** before delivering advice based on a mental model.

---

## 1. When Foundational Models Fail

### Inversion
- **Valid Boundary:** High-consequence decisions with fatal absorbing barriers (data loss, bankruptcy, security breaches, server outages).
- **Failure Boundary:** 0-to-1 creative ideation or early-stage exploratory brainstorming. Inverting on a nascent product idea generates crippling pessimism and kills fragile innovative ideas before they take root.
- **Remedy:** Switch to **Antifragile Probing** (cheap, safe-to-fail experiments).

### First Principles Thinking
- **Valid Boundary:** When industry convention has ossified around outdated physical/economic realities (e.g. battery pack costs, custom hardware, space exploration).
- **Failure Boundary:** Battle-tested security primitives, cryptographic protocols, or heavily debugged POSIX systems. "Reinventing from first principles" in cryptography or distributed consensus invariably produces rookie vulnerabilities that took the industry 30 years to solve.
- **Remedy:** Switch to **Chesterton's Fence** and **Lindy Effect**.

### Gall's Law
- **Valid Boundary:** Software architectures, organizational structures, product platforms.
- **Failure Boundary:** Tightly integrated physical engineering or regulatory hardware where retrospective incremental evolution is physically impossible (e.g., launching an interplanetary space probe or laying a subsea fiber-optic cable).
- **Remedy:** Switch to **Pre-Mortem** and rigorous formal verification.

### Occam's Razor
- **Valid Boundary:** Diagnostic troubleshooting when multiple explanations fit the data equally well.
- **Failure Boundary:** Complex adaptive systems exhibiting multi-causality. Selecting the "simplest single cause" for a market crash or distributed outage ignores **Lollapalooza effects** where 5 distinct small anomalies combined to trigger the failure.
- **Remedy:** Switch to **Systems Thinking (Interactive Complexity)** and **Swiss Cheese Model**.

### Theory of Constraints
- **Valid Boundary:** Linear processing pipelines, manufacturing plants, serial data processing.
- **Failure Boundary:** Shifting, dynamic networks where the bottleneck rapidly migrates based on unpredictable traffic patterns (e.g., an ad-hoc graph database query). Pouring fixed capital into a transient bottleneck is wasteful.
- **Remedy:** Switch to **Dynamic Load Shedding** and **Loose Coupling**.

### Sunk Cost Fallacy (Over-Correction)
- **Valid Boundary:** Cutting losses on a doomed technical or business direction that has no future expected value.
- **Failure Boundary:** Premature abandonment of difficult projects experiencing normal developmental friction. Calling every plateau a "sunk cost" leads to an organization that never finishes anything hard.
- **Remedy:** Evaluate strictly via **Opportunity Cost** and **Expected Value of Completion**.

---

## 2. Meta-Biases in AI Agents Applying Mental Models

### The "Aphorism As Answer" Anti-Pattern
- **Symptom:** The agent simply quotes Charlie Munger or quoting "Conway's Law" without doing the operational work of mapping the model to specific code lines, architectural modules, or database tables.
- **Rule:** A mental model is only valid if it produces a concrete, falsifiable recommendation or non-negotiable negative constraint.

### Sycophantic Validation
- **Symptom:** The user presents a deeply flawed idea (e.g., "Let's rewrite our entire database in Redis"), and the agent selectively finds a mental model (like "First Principles") to validate the user's bias.
- **Rule:** The agent must proactively invoke counter-models (e.g. *Chesterton's Fence*, *Gall's Law*, *Sunk Cost Fallacy*) to pressure-test the user's proposal.

### Context Bloat
- **Symptom:** Dumping a 10-page treatise on the history of thermodynamics when the user asked a focused question about cache invalidation.
- **Rule:** Use progressive disclosure. Provide the bottom-line verdict and the diagnostic steps first; link to deep references only for background.
