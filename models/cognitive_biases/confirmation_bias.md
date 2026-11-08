---
type: mental-model
id: confirmation_bias
title: Confirmation Bias
category: cognitive_biases
discipline: Cognitive Psychology
counter_models: ["inversion", "first_principles"]
---

# Confirmation Bias

## 1. Core Principle
The subconscious human tendency to search for, interpret, favor, and recall information that confirms preexisting beliefs or hypotheses, while aggressively discounting or ignoring disconfirming evidence.

## 2. When NOT to Use (Failure Boundaries)
- When executing well-established, mathematically verified standard operating procedures.

## 3. Operational Thinking Steps
1. Name the Hypothesis: Explicitly state the belief you are attached to ("Users are dropping off because the price is too high").
2. Hunt for Disconfirming Evidence: Search specifically for data that refutes your belief ("Where did users convert at an even higher price?").
3. Assign a Red Team: Designate someone whose explicit job is to argue the opposite case without social penalty.
4. Establish Pre-Commitment Gates: Define what metrics or observations will force you to admit your hypothesis was wrong *before* looking at the data.

## 4. Diagnostic Probing Questions
- "What evidence would convince us that our favorite hypothesis is completely false?"
- "Are we analyzing this data objectively, or are we shopping for charts to justify a decision we already made?"

## 5. Worked Example
- Context: Product team believed customers wanted a complex dashboard because 5 power users requested it in interviews. They ignored analytics showing 95% of active users never opened the analytics tab.
- Correction: Appointed a devil's advocate reviewer who pulled the hard database telemetry, stopping a $200k wasted engineering sprint and redirecting effort to mobile notifications.
