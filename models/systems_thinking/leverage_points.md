---
type: mental-model
id: leverage_points
title: Places to Intervene in a System
category: systems_thinking
discipline: Systems Dynamics (Donella Meadows)
counter_models: ["first_principles", "via_negativa"]
---

# Leverage Points (Donella Meadows)

## 1. Core Principle
Complex systems have varying leverage points where small interventions yield disproportionately large effects. Most interventions target low-leverage parameters (constants, buffer sizes), while true leverage lies in information flows, system rules, goals, and paradigms.

## 2. When NOT to Use (Failure Boundaries)
- Immediate life-threatening emergencies requiring immediate local band-aids.
- Purely deterministic, non-systemic calculations.

## 3. Operational Thinking Steps (From Low to High Leverage)
1. Parameters & Numbers (Lowest): Changing constants, timeouts, buffer sizes.
2. Buffers & Stocks: Adding queues or capacity headroom.
3. Feedback Delays: Accelerating reporting loops so signals arrive in real time.
4. Information Flows: Making previously hidden system states visible to decision-makers.
5. System Rules: Changing incentives, access controls, penalties, and interfaces.
6. System Goals & Paradigms (Highest): Redefining what success means for the entire system.

## 4. Diagnostic Probing Questions
- "Are we endlessly tweaking parameters while the system's underlying goal remains perverse?"
- "What vital feedback signal is currently hidden from the people making decisions?"

## 5. Worked Example
- Context: Customer support team had a 48-hour SLA backlog. Engineering kept adjusting timeout thresholds and adding database indexes (low leverage).
- Correction: Intervened at the information flow level: surfaced error logs directly inside the customer support dashboard with automated error categorization, allowing non-engineers to resolve 60% of tickets on first contact.
