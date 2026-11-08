---
type: mental-model
id: bottleneck_theory_of_constraints
title: Theory of Constraints (Bottlenecks)
category: systems_thinking
discipline: Operations Research (Eliyahu Goldratt)
counter_models: ["pareto_principle", "leverage_points"]
---

# Theory of Constraints (Bottlenecks)

## 1. Core Principle
Any manageable system is limited in achieving more of its goals by a very small number of constraints (typically exactly one binding bottleneck at any given moment). Optimizing any part of the system other than the bottleneck is an expensive illusion.

## 2. When NOT to Use (Failure Boundaries)
- Early-stage ideation where throughput is unmeasured and direction matters more than velocity.
- Systems with unconstrained excess capacity where latency is negligible.

## 3. Operational Thinking Steps (Goldratt's 5 Focusing Steps)
1. Identify the Constraint: Find the single step with the largest queue or highest utilization (>95%).
2. Exploit the Constraint: Ensure the bottleneck is never idle, never works on low-priority items, and never handles defective inputs.
3. Subordinate Everything Else: Slow down upstream producers so they do not overwhelm the bottleneck with buffer bloat.
4. Elevate the Constraint: Invest resources, parallelism, or compute specifically into the bottleneck to break it.
5. Prevent Inertia: Once broken, immediately find the new bottleneck. Do not let old habits govern the new constraint.

## 4. Diagnostic Probing Questions
- "Where is work piling up right now?"
- "If we double the speed of this step, does total end-to-end throughput increase by even 1%?"
- "Are we optimizing a step purely because it is easy to measure rather than because it binds the system?"

## 5. Worked Example
- Context: Team spent 3 sprints optimizing SQL queries in an indexing service (improving query time from 40ms to 10ms), while the real bottleneck was single-threaded PDF OCR extraction taking 8.5 seconds per document.
- Correction: Reallocated effort to parallelize OCR workers across Celery tasks, increasing pipeline throughput from 12 docs/min to 180 docs/min.
