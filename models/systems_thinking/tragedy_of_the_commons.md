---
type: mental-model
id: tragedy_of_the_commons
title: Tragedy of the Commons
category: systems_thinking
discipline: Ecology & Political Economy (Garrett Hardin)
counter_models: ["incentive_caused_bias", "conways_law"]
---

# Tragedy of the Commons

## 1. Core Principle
When multiple independent actors share a finite, unmetered resource, each individual receives 100% of the benefit of consumption while sharing only a fraction of the cost of depletion. Without governance, mutual destruction of the resource is guaranteed.

## 2. When NOT to Use (Failure Boundaries)
- Non-rival, infinite resources (e.g. read-only static documentation, open-source code).
- Private resources with strict individual ownership and isolated cost attribution.

## 3. Operational Thinking Steps
1. Identify the Shared Asset: Shared database connections, unpartitioned message queues, shared rate limits, or organizational goodwill.
2. Unmask Asymmetric Incentives: Calculate individual payoff vs shared degradation.
3. Establish Boundaries: Transform the open commons into private allotments (quotas, client-specific rate limits, tenant pools).
4. Enforce Penalties: Implement circuit breakers and rate limit throttling on abusive actors to protect baseline service for all.

## 4. Diagnostic Probing Questions
- "Who pays the price when one tenant abuses this shared endpoint?"
- "Do individual users have any incentive to conserve this pool, or does being courteous make them a sucker?"

## 5. Worked Example
- Context: A shared Redis instance served both critical user session lookups and heavy analytics batch caching. An overnight analytics dump flooded Redis memory, evicting user session keys and logging out 15,000 active users.
- Correction: Segmented Redis into two isolated clusters with separate memory allocations and per-service client credential quotas.
