---
type: mental-model
id: via_negativa
title: Via Negativa (Improvement by Subtraction)
category: strategic_risk
discipline: Philosophy & Risk (Nassim Taleb)
counter_models: ["leverage_points", "first_principles"]
---

# Via Negativa (Improvement by Subtraction)

## 1. Core Principle
We know what is wrong with much more certainty than what is right. Systems are improved primarily by subtracting errors, removing unnecessary complexity, and eliminating failure paths, rather than by adding features or interventions.

## 2. When NOT to Use (Failure Boundaries)
- True 0-to-1 bootstrapping where no foundation exists yet.
- Necessary functional requirements that cannot be deleted.

## 3. Operational Thinking Steps
1. Identify Bloat: Look for unused dependencies, redundant microservices, dead config flags, and unnecessary meeting cadences.
2. Subtract Instead of Add: When a bug appears, ask: "What can we delete or simplify to make this bug structurally impossible?"
3. Measure by Deletion: Treat lines of code removed as higher value than lines of code added.

## 4. Diagnostic Probing Questions
- "What can we stop doing or delete today that will immediately make our system faster and safer?"
- "Are we patching a symptom by adding another layer of scaffolding, instead of deleting the broken layer underneath?"

## 5. Worked Example
- Context: A web application had complex caching layers, Redis clusters, and CDN purge webhooks to speed up a slow page load.
- Correction: Deleted the entire caching layer after optimizing the underlying SQL query and removing 14 unused third-party tracking scripts. Page load dropped from 3.2s to 180ms with 50% fewer infrastructure moving parts.
