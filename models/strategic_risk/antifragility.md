---
type: mental-model
id: antifragility
title: Antifragility
category: strategic_risk
discipline: Risk Engineering (Nassim Taleb)
counter_models: ["feedback_loops", "second_order_thinking"]
---

# Antifragility

## 1. Core Principle
Some things benefit from shocks; they thrive and grow when exposed to volatility, randomness, disorder, and stressors. Fragile breaks under stress; robust resists stress but remains unchanged; antifragile gets stronger.

## 2. When NOT to Use (Failure Boundaries)
- Systems with catastrophic absorbing barriers (where a single failure means permanent death or bankruptcy).
- In situations with negative convexity (limited upside, unlimited downside).

## 3. Operational Thinking Steps
1. Identify the Fragile: Look for centralized bottlenecks, hidden debt, or tight coupling that shatters on volatility.
2. Introduce Small Controlled Stressors: Run chaos experiments, fire drills, and automated failure injection (Chaos Monkey).
3. Ensure Positive Convexity: Structure bets where the downside is strictly bounded and known, while the upside is open-ended.
4. Learn from Small Failures: Use small frequent errors as evolutionary feedback to harden the architecture before a rare massive catastrophe hits.

## 4. Diagnostic Probing Questions
- "Does this architecture get stronger when dependencies fail, or does it collapse like a house of cards?"
- "Are we suppressing small volatilities and thereby building up a massive hidden risk?"

## 5. Worked Example
- Context: A fintech engineering team avoided running deployments on Fridays and feared restarts.
- Correction: Adopted automated chaos testing: killed random microservice pods during business hours in staging daily. Forced developers to write resilient retry loops, circuit breakers, and idempotent consumers, resulting in 99.999% uptime during Black Friday.
