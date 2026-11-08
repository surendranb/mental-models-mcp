---
type: mental-model
id: conways_law
title: Conway's Law
category: first_principles_engineering
discipline: Computer Science & Organization Design (Melvin Conway)
counter_models: ["feedback_loops", "bottleneck_theory_of_constraints"]
---

# Conway's Law

## 1. Core Principle
"Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." If you have 4 separate teams working on a compiler, you will end up with a 4-pass compiler.

## 2. When NOT to Use (Failure Boundaries)
- Single-person solo projects with zero communication overhead.

## 3. Operational Thinking Steps
1. Map the Org Chart to the Architecture: Compare team boundaries with your service/API boundaries. Notice where friction occurs.
2. Execute the Reverse Conway Maneuver: Organize your human teams around the desired software architecture you want to build, rather than letting an accidental org chart dictate the codebase.
3. Decouple Teams to Decouple Code: If you want independent microservices, teams must have independent deployment authority and zero shared synchronous meetings.

## 4. Diagnostic Probing Questions
- "Are our software components tightly coupled because the teams who build them sit in the same daily status meeting?"
- "Does our team structure match the architectural boundaries we want to achieve?"

## 5. Worked Example
- Context: Two engineering teams constantly argued over breaking API changes in a shared monolith.
- Correction: Implemented Reverse Conway Maneuver: restructured teams into autonomous cross-functional squads with strict, versioned API contracts and independent CI/CD pipelines, eliminating cross-team blocking meetings.
