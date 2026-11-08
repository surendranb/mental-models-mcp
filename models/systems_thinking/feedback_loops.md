---
type: mental-model
id: feedback_loops
title: Feedback Loops
category: systems_thinking
discipline: Systems Science & Control Theory
counter_models: ["bottleneck_theory_of_constraints", "second_order_thinking"]
---

# Feedback Loops

## 1. Core Principle
In complex systems, outputs of a process are looped back as inputs, creating either self-reinforcing (amplifying/exponential) or balancing (stabilizing/homeostatic) dynamics. Delays in the feedback loop induce violent oscillations and overshoot.

## 2. When NOT to Use (Failure Boundaries)
- Linear, independent, single-transaction steps with zero memory or state.
- Short-lived scripts where downstream state is wiped on exit.
- Premature dynamic modeling for static configuration checks.

## 3. Operational Thinking Steps (Executable Actions)
1. Map the Loop: Identify if the cycle is Reinforcing (compounding gain or death spiral) or Balancing (seeking an equilibrium setpoint).
2. Quantify the Delay: Measure the time lag between action taken and system reaction. Long delays cause over-steering.
3. Identify Saturation Limits: No reinforcing loop grows forever; find the physical, financial, or architectural ceiling that turns it into a balancing loop.
4. Dampen Oscillations: Shorten feedback delays or introduce buffer dampening to prevent wild swings.

## 4. Diagnostic Probing Questions
- "Are we overreacting because the system hasn't registered our previous corrective action yet?"
- "What prevents this growth curve from hitting an abrupt structural wall?"
- "Is this metric stabilizing on its own, or are we artificially propping it up?"

## 5. Worked Example
- Context: A backend queue autoscaler scales up aggressively during latency spikes, but worker initialization takes 4 minutes. By the time 50 new pods boot, the traffic spike is over, leading to massive resource waste and rapid scaling collapse.
- Correction: Added hysteresis dampening, moving-average smoothing over 5 minutes, and a 10-minute cooldown period, eliminating oscillation and reducing cloud costs by 38%.
