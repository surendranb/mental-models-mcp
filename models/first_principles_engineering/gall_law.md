---
type: mental-model
id: gall_law
title: Gall's Law
category: first_principles_engineering
discipline: Systems Engineering (John Gall)
counter_models: ["first_principles", "via_negativa"]
---

# Gall's Law

## 1. Core Principle
"A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system."

## 2. When NOT to Use (Failure Boundaries)
- Highly standardized, modular off-the-shelf assemblies where all components are pre-verified.

## 3. Operational Thinking Steps
1. Stop the Grand Rewrite: Reject all proposals to rebuild an entire production system from scratch in one big-bang release.
2. Find the Simplest Working Core: Strip the system down to the single most critical flow that works reliably.
3. Evolve Incrementally: Add capabilities, abstractions, and scale one step at a time, keeping the system continuously working in production at every iteration.

## 4. Diagnostic Probing Questions
- "Are we attempting to design a complex system from scratch instead of evolving it from a working core?"
- "What is the smallest version of this that can be running in production tomorrow?"

## 5. Worked Example
- Context: Company spent 2 years and $5M on a 'Second System' rewrite of their monolithic billing engine. It never reached feature parity, had hundreds of obscure edge-case bugs, and was ultimately scrapped.
- Correction: Team adopted Gall's Law: kept the working legacy core and carved out individual payment providers one service at a time (Strangler Fig pattern). Successfully migrated with zero downtime.
