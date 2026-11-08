---
type: mental-model
id: first_principles
title: First Principles Reasoning
category: decision_analysis
discipline: Physics & Philosophy (Aristotle / Elon Musk)
counter_models: ["occam_razor", "inversion"]
---

# First Principles Reasoning

## 1. Core Principle
Boil things down to their most fundamental, irreducible truths (the physical laws or undeniable axioms) and reason upward from there, rather than reasoning by analogy or copying what others do.

## 2. When NOT to Use (Failure Boundaries)
- Routine operational tasks where standard conventions and patterns work well.
- When the cost of deriving from scratch far exceeds the marginal benefit over existing solutions.

## 3. Operational Thinking Steps
1. Identify Current Assumptions: Write down the conventional wisdom ("It costs $100k to build this", "We must use Kubernetes").
2. Deconstruct to Irreducible Truths: What are the fundamental physical or computational requirements? (e.g. CPU cycles, bytes transferred, network hops).
3. Reconstruct Upward: Design the minimal viable mechanism that satisfies the fundamental truths without inheriting industry bloat.

## 4. Diagnostic Probing Questions
- "Are we doing this because it is technically necessary, or because that's how everyone else does it?"
- "What are the raw materials and physics limits of this problem?"

## 5. Worked Example
- Context: Team claimed building an analytics pipeline required an expensive enterprise SaaS data warehouse ($4,000/mo) because "all modern stacks use it".
- Correction: Analyzed actual data velocity (50 events/sec = 4MB/hr). First principles showed a single SQLite database with litestream replication to S3 on a $10 VPS handled the load with sub-millisecond queries.
