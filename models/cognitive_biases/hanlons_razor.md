---
type: mental-model
id: hanlons_razor
title: Hanlon's Razor
category: cognitive_biases
discipline: Philosophy & Human Relations
counter_models: ["incentive_caused_bias", "occam_razor"]
---

# Hanlon's Razor

## 1. Core Principle
"Never attribute to malice that which is adequately explained by stupidity, neglect, or misunderstanding." Assuming bad faith creates toxic paranoia, escalates minor conflicts, and blinds teams to systemic communication flaws.

## 2. When NOT to Use (Failure Boundaries)
- Adversarial cybersecurity, competitive espionage, or forensic fraud audits where active malicious intent is the explicit threat model.

## 3. Operational Thinking Steps
1. Pause Emotional Reaction: Resist assuming an API partner, coworker, or user intentionally harmed you.
2. Search for Benign Failures: Check for misconfigured webhooks, network timeouts, ambiguous documentation, or plain fatigue.
3. Fix the System: Address the missing guardrail or confusing interface rather than launching personal accusations.

## 4. Diagnostic Probing Questions
- "Could this disaster simply be the result of a tired engineer, ambiguous docs, or a broken script rather than a hostile conspiracy?"
- "What communication gap made this mistake easy to commit?"

## 5. Worked Example
- Context: Partner API suddenly stopped sending webhook events. Executive team assumed the partner was deliberately sabotaging the contract ahead of contract negotiations.
- Correction: Called their lead engineer: an automated SSL certificate rotation script had expired on their staging cluster. Fixed in 10 minutes; avoided a destructive legal dispute.
