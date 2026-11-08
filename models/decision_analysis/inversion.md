---
type: mental-model
id: inversion
title: Inversion
category: decision_analysis
discipline: Mathematics & Philosophy (Carl Jacobi / Charlie Munger)
counter_models: ["pre_mortem", "first_principles"]
---

# Inversion

## 1. Core Principle
"Invert, always invert." Many hard problems cannot be solved directly. Instead of asking how to achieve a desired outcome, systematically identify and eliminate all conditions that guarantee catastrophe.

## 2. When NOT to Use (Failure Boundaries)
- 0-to-1 exploratory ideation where creative optimism is required.
- Low-impact, easily reversible decisions (two-way doors).

## 3. Operational Thinking Steps
1. State the Desired Outcome: "We want a successful database migration with zero downtime."
2. Invert to Catastrophe: "How could we completely destroy data and guarantee 8 hours of downtime?"
3. Enumerate Disaster Vectors: Un-tested rollback scripts, concurrent schema locks, lack of point-in-time recovery, running scripts manually in prod.
4. Build Hard Constraints: Turn each disaster condition into a non-negotiable negative guardrail.

## 4. Diagnostic Probing Questions
- "If our goal was to guarantee this rollout fails silently, what would we do?"
- "What subtle assumptions are we treating as guaranteed facts?"

## 5. Worked Example
- Context: Planning an enterprise software migration. Instead of brainstorming ideal launch dates, the team inverted: "What guarantees a botched launch?" Answer: Migrating all users at once on a Friday evening with no rollback plan.
- Correction: Mandated canary deployments (1% -> 5% -> 25%), scheduled on Tuesday mornings with an automated rollback threshold if error rates exceeded 0.1%.
