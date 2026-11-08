---
type: mental-model
id: lindy_effect
title: The Lindy Effect
category: strategic_risk
discipline: Probability & Risk (Nassim Taleb)
counter_models: ["reversibility_two_way_doors", "gall_law"]
---

# The Lindy Effect

## 1. Core Principle
For non-perishable entities (technologies, ideas, books, software protocols), life expectancy is proportional to current age. A technology that has survived for 30 years (like C, SQL, or Unix) is expected to survive for another 30 years, whereas a framework released 6 months ago may disappear in 6 months.

## 2. When NOT to Use (Failure Boundaries)
- Rapidly evolving frontier domains where physical constraints force a generational shift (e.g. GPU architectures).
- Perishable goods or hardware subject to mechanical wear and tear.

## 3. Operational Thinking Steps
1. Identify Core Infrastructure: Distinguish foundational pillars from transient UI layers.
2. Check Survival Longevity: How long has this technology, format, or protocol existed in production?
3. Filter the Hype: Prefer boring, time-tested technologies (PostgreSQL, SQLite, stdlib) over bleeding-edge rewrites for mission-critical foundations.

## 4. Diagnostic Probing Questions
- "Will this new JavaScript framework still be maintained and documented in 5 years?"
- "Are we adopting this because it is proven, or because it is currently trending on social media?"

## 5. Worked Example
- Context: A startup debated building their core financial ledger on an unproven new NoSQL database versus PostgreSQL.
- Correction: Chose PostgreSQL (30+ years of battle-tested ACID transactions). When the startup scaled to millions in transactions, they had zero data corruption issues.
