---
type: mental-model
id: pre_mortem
title: Pre-Mortem Analysis
category: decision_analysis
discipline: Cognitive Psychology (Gary Klein)
counter_models: ["inversion", "second_order_thinking"]
---

# Pre-Mortem Analysis

## 1. Core Principle
Unlike a post-mortem that analyzes a disaster after it happens, a pre-mortem operates before launch: Assume the project has completely failed 12 months in the future. Write the comprehensive post-mortem today to break team optimism bias and uncover hidden vulnerabilities.

## 2. When NOT to Use (Failure Boundaries)
- Low-stakes, daily operational code changes.
- Situations where paralysis by analysis stalls immediate prototyping.

## 3. Operational Thinking Steps
1. Set the Stage: Gather the core team and state: "It is one year from now. The project was an unmitigated disaster. What happened?"
2. Silent Brainstorming: Every participant independently writes down every reason for the failure without fear of social penalty.
3. Consolidate & Rank: Categorize failure vectors by probability and catastrophic impact.
4. Re-engineer the Roadmap: Convert top vulnerabilities into preventive action items on the immediate sprint plan.

## 4. Diagnostic Probing Questions
- "If this project fails 6 months from now, what was the elephant in the room that everyone saw but nobody named?"
- "Where is our single point of failure that we are hoping will magically hold up?"

## 5. Worked Example
- Context: A startup planned a massive multi-region cloud launch. Pre-mortem revealed that nobody on call had tested cross-region database replication failover during a network partition.
- Correction: Simulated a partition in staging; discovered failover locked the entire application pool. Fixed before production launch.
