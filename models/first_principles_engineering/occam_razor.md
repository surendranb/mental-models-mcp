---
type: mental-model
id: occam_razor
title: Occam's Razor
category: first_principles_engineering
discipline: Philosophy & Logic (William of Ockham)
counter_models: ["first_principles", "chestertons_fence"]
---

# Occam's Razor

## 1. Core Principle
"Entities should not be multiplied beyond necessity." When presented with competing hypotheses that explain the observed data equally well, choose the one with the fewest assumptions. Simplicity is an indicator of truth.

## 2. When NOT to Use (Failure Boundaries)
- Oversimplifying inherently complex, non-linear adaptive systems.
- When the simpler explanation ignores verified, inconvenient edge-case data.

## 3. Operational Thinking Steps
1. Enumerate Hypotheses: List all explanations for the observed bug, anomaly, or behavior.
2. Count Unverified Assumptions: For each hypothesis, count how many unproven assumptions must hold true for it to be correct.
3. Test the Simplest First: Start investigation with the hypothesis requiring the least extraordinary leaps of logic.

## 4. Diagnostic Probing Questions
- "Are we inventing an elaborate conspiracy or exotic kernel bug when a simple typo or expired token explains the behavior?"
- "What is the simplest hypothesis that explains all observed facts?"

## 5. Worked Example
- Context: A microservice failed to connect to a database after a deployment. The team spent 3 hours investigating VPC peering, DNS routing, and firewall rules.
- Correction: Applied Occam's Razor: checked the environment variables. The new deployment had an extra space in the `DB_PASSWORD` string.
