---
type: mental-model
id: reversibility_two_way_doors
title: Decision Reversibility (Two-Way Doors)
category: decision_analysis
discipline: Decision Theory (Jeff Bezos)
counter_models: ["opportunity_cost", "lindy_effect"]
---

# Decision Reversibility (Two-Way Doors)

## 1. Core Principle
Decisions fall into two categories: Type 1 (one-way doors: irreversible, high blast radius; require deep deliberation) and Type 2 (two-way doors: easily reversible, low blast radius; require rapid execution). Treating Type 2 decisions with Type 1 caution kills organizational velocity.

## 2. When NOT to Use (Failure Boundaries)
- When a sequence of individually reversible choices creates an irreversible lock-in trap (compound irreversibility).
- When safety, legal, or security invariants are at risk.

## 3. Operational Thinking Steps
1. Assess Reversibility: If this decision turns out to be wrong, can we walk back through the door in less than 48 hours for negligible cost?
2. Assess Blast Radius: Does failure affect all users or an isolated sub-group?
3. Calibrate Process:
   - Type 2: Decide immediately with 70% information. Optimize for speed and feedback.
   - Type 1: Establish slow gates, red teams, and consensus before signing off.

## 4. Diagnostic Probing Questions
- "Is this truly a one-way door, or are we just afraid of looking foolish if we have to revert it?"
- "What is the cost of waiting one week for more data versus deciding now and reverting if wrong?"

## 5. Worked Example
- Context: Senior engineering spent 4 weeks debating whether a button should say 'Submit' or 'Continue'.
- Correction: Classified as a pure Type 2 decision. Implemented A/B test in 3 hours; real user data made the choice in 2 days.
