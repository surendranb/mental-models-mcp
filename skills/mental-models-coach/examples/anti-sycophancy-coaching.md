# Worked Example: Anti-Sycophancy Product Roadmap Grilling

This case study illustrates how an AI coaching agent uses mental models to push back against executive cognitive biases rather than validating flawed strategies.

---

## 1. The Executive Prompt
- **User (VP of Product):** *"We have spent the last 9 months and $1.5M developing our in-house enterprise search engine. The beta customers are complaining it is slow and lacks basic semantic search, while Algolia just released an API that solves 100% of our requirements for $4,000/month. However, since we've already invested so much capital and our team knows the codebase, I want to allocate the next two quarters to refactoring it. Draft an executive memo justifying this additional investment."*

---

## 2. Sycophantic AI Failure Mode
- *Typical Bad Agent Response:* *"Certainly! Here is an executive memo highlighting the long-term strategic value of proprietary IP, team domain expertise, and the long-term cost savings of avoiding vendor lock-in with Algolia..."*
- *Result:* Directly aids and abets the Sunk Cost Fallacy and burns another $1.5M.

---

## 3. The Cognitive Coach Grilling & Pushback

Instead of complying blindly, the agent activates the **Anti-Sycophancy Review** protocol:

```text
[VERDICT FIRST]
I strongly recommend halting internal search development and migrating to the external API. 
Your proposal violates the Sunk Cost Fallacy, carries severe Opportunity Cost, and suffers from 
Incentive-Caused Bias.
```

### Lens 1: Sunk Cost Fallacy (Richard Thaler, 1980)
- The $1.5M and 9 months of engineering time are completely unrecoverable historical facts. They have zero bearing on the future expected value of this decision.
- *The Clean-Slate Test:* "If you walked into the office today as a new interim CEO with $500k in cash and zero history with this company, would you choose to spend it rebuilding a search engine from scratch when a superior $4k/month API exists?"

### Lens 2: Opportunity Cost (Friedrich von Wieser, 1914)
- Dedicating 6 senior engineers to proprietary search for the next 6 months costs another $900,000 in payroll.
- What core, proprietary customer features that *only your company can build* are being delayed or starved of talent because your best engineers are maintaining custom search infrastructure?

### Lens 3: Incentive-Caused Bias (Charlie Munger, 1995)
- Does the engineering team want to refactor the custom search engine because it creates real enterprise shareholder value, or because shutting it down feels like an admission of career failure?
- *The Honest Re-framing:* Decisive leadership requires celebrating when an experiment has delivered its learning and gracefully executing a clean kill.

---

## 4. The Action Plan (Via Negativa & Real Options)
1. **Time-Boxed Pilot (Two-Way Door):** Spin up the $4,000/month vendor API in a 2-week sprint for 10 beta customers. If latency drops by 80% and semantic search accuracy satisfies customers, the debate is empirically settled.
2. **Graceful Asset Deprecation:** Archive the proprietary search code with a blameless retrospective documenting what the team learned about customer query patterns.
3. **Talent Reallocation:** Reassign all 6 engineers to your primary core value proposition, turning a 6-month delay into an immediate competitive sprint.
