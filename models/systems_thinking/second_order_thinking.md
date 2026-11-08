---
type: mental-model
id: second_order_thinking
title: Second-Order Thinking
category: systems_thinking
discipline: Philosophy & Decision Science (Howard Marks)
counter_models: ["first_principles", "opportunity_cost"]
---

# Second-Order Thinking

## 1. Core Principle
First-order thinking asks: "What is the immediate, obvious result of this action?" Second-order thinking asks: "And then what?" It evaluates the reactions of people, competitors, systems, and downstream ripple effects over time.

## 2. When NOT to Use (Failure Boundaries)
- Immediate tactical triage during an active outage where stopping the bleeding is paramount.
- Low-stakes, highly reversible decisions.

## 3. Operational Thinking Steps
1. Define the First-Order Payoff: What good thing happens immediately?
2. Ask "And Then What?": Trace the downstream consequences over 3 intervals: 1 month, 6 months, 2 years.
3. Model Human/System Adaptation: How will competitors, users, or other services change their behavior once this rule is active?
4. Evaluate Net Long-Term Value: Does the delayed downside outweigh the initial benefit?

## 4. Diagnostic Probing Questions
- "What happens after this works exactly as planned?"
- "How will people game, exploit, or adapt to this new policy once it is standard?"

## 5. Worked Example
- Context: A company offered cash bonuses to developers for every bug fixed. First-order result: bug fix count skyrocketed. Second-order result: developers wrote sloppy, fragile code to artificially inflate future bug counts.
- Correction: Replaced per-bug bounties with zero-incident production reliability SLA bonuses tied to team sprint velocity and test coverage.
