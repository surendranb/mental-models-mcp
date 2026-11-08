---
type: mental-model
id: pareto_principle
title: The Pareto Principle (80/20 Rule)
category: first_principles_engineering
discipline: Mathematics & Economics (Vilfredo Pareto)
counter_models: ["bottleneck_theory_of_constraints", "leverage_points"]
---

# The Pareto Principle (80/20 Rule)

## 1. Core Principle
For many outcomes, roughly 80% of consequences come from 20% of causes. In software, 80% of crashes originate from 20% of bugs; 80% of revenue comes from 20% of clients. Radical focus on the vital few beats spreading effort across the trivial many.

## 2. When NOT to Use (Failure Boundaries)
- Uniform distribution environments where risk is evenly spread.
- Zero-tolerance safety-critical systems (e.g. aerospace flight controls) where the remaining 20% can be fatal.

## 3. Operational Thinking Steps
1. Plot the Distribution: Gather raw data and rank items by impact.
2. Isolate the Vital 20%: Identify the small cluster producing the vast majority of output, latency, or failures.
3. Ruthlessly Prune the Trivial 80%: Stop polishing low-impact edge cases until the high-impact core is optimized.

## 4. Diagnostic Probing Questions
- "Which 20% of our codebase or features causes 80% of our customer complaints?"
- "Are we wasting 80% of our time on minor details that yield only 20% of customer value?"

## 5. Worked Example
- Context: Mobile app development team had a backlog of 150 reported bugs.
- Correction: Analyzed crash logs: discovered 3 bugs accounted for 84% of total app crashes. Fixed those 3 bugs in 2 days; crash rate dropped from 4.8% to 0.4%.
