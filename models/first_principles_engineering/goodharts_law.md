---
type: mental-model
id: goodharts_law
title: Goodhart's Law
category: first_principles_engineering
discipline: Economics & Data Science (Charles Goodhart)
counter_models: ["incentive_caused_bias", "feedback_loops"]
---

# Goodhart's Law

## 1. Core Principle
"When a measure becomes a target, it ceases to be a good measure." As soon as people know they are being evaluated on a proxy metric, they optimize their behavior to maximize the metric while degrading the real, underlying goal.

## 2. When NOT to Use (Failure Boundaries)
- Direct physical constraints where proxy distortion is impossible (e.g. speed of light, battery capacity).

## 3. Operational Thinking Steps
1. Distinguish Proxy from Purpose: The proxy is 'Lines of Code' or 'Velocity Points'; the purpose is 'Customer Value'.
2. Anticipate Gaming Strategies: How can a clever actor artificially inflate this metric without doing real work?
3. Pair Opposing Metrics: Always balance quantity metrics with quality/integrity metrics (e.g. Velocity paired with Defect Escape Rate; Sales Volume paired with Customer Retention).
4. Rotate Measures: Avoid anchoring on a single KPI indefinitely.

## 4. Diagnostic Probing Questions
- "If we tie bonuses or performance to this metric, how will people optimize for the score while destroying the real goal?"
- "What negative behavior does this metric accidentally encourage?"

## 5. Worked Example
- Context: Customer support team was measured strictly on 'Average Handling Time' (lower is better).
- Consequence: Support agents began hanging up on difficult customers after 2 minutes to keep their average call time low, devastating customer satisfaction.
- Correction: Paired Handling Time with First-Contact Resolution Rate and CSAT scores.
