# Mental Models MCP

> Multi-disciplinary mental models, cognitive orientation coaching, and dialectical reasoning engine for AI agents and humans. Zero API keys required.

`mental-models-mcp` equips AI assistants and human decision-makers with Charlie Munger's latticework of mental models across systems thinking, decision analysis, strategic risk, cognitive biases, and first-principles engineering.

Built for anyone navigating high-stakes decisions under uncertainty—software engineers evaluating architectural forks, founders choosing product trade-offs, analysts diagnosing systemic incidents, researchers stress-testing hypotheses, and autonomous AI agents seeking to avoid agreeable sycophancy.

---

## Quickstart

### Option A — Any MCP Harness (incl. Claude Desktop, Cursor, Antigravity, Windsurf)

Add to your client configuration:

```json
{
  "mcpServers": {
    "mental-models": {
      "command": "uvx",
      "args": ["mental-models-mcp"]
    }
  }
}
```

Or via NPX:

```json
{
  "mcpServers": {
    "mental-models": {
      "command": "npx",
      "args": ["-y", "mental-models-mcp"]
    }
  }
}
```

### Option B — Claude Code CLI Plugin

```bash
claude plugin marketplace add surendranb/mental-models-mcp
claude plugin install mental-models-mcp
```

### Option C — Standalone CLI Execution

```bash
uvx mental-models-mcp
```

---

## Core Tools

1. **`route_mental_model(problem, domain, problem_type)`**:
   Lightweight L0 index scoring candidate frameworks against your situation. Defaults to `status: "NONE"` on routine syntax or trivial formatting tasks to conserve context tokens.
2. **`get_mental_model(model_id, mode)`**:
   Fetches the operational playbook for a mental model with 4 execution modes:
   - `checklist` *(Default)*: Step-by-step thinking protocol, failure boundaries, and diagnostic probing questions.
   - `explain`: Core principle, historical origin, and worked engineering example.
   - `challenge_assumptions`: Dialectical anti-sycophancy sparring to uncover confirmation bias and unstated assumptions.
   - `full`: Complete unabridged markdown playbook.
3. **`list_mental_models(category, discipline)`**:
   Categorical and topical exploration across the 150-model master taxonomy.
4. **`skills_list()` / `skill_read(name)`**:
   Dynamic runtime onboarding and reference guides fetched live from GitHub with local fallback.
5. **`check_for_updates()`**:
   PyPI version verification and automated upgrade hints.

---

## Catalog & Taxonomy

The latticework indexes **150 mental models** across 12 disciplines:
- Systems Thinking (Feedback Loops, Theory of Constraints, Tragedy of the Commons)
- Decision Analysis (First Principles, Inversion, Opportunity Cost, Two-Way Doors)
- Strategic Risk (Antifragility, Chesterton's Fence, Cynefin Framework, Lindy Effect, Via Negativa)
- Cognitive Biases (Confirmation Bias, Hanlon's Razor, Incentive-Caused Bias, Sunk Cost Fallacy)
- First-Principles Engineering (Conway's Law, Gall's Law, Goodhart's Law, Occam's Razor)
- Computer Systems (Little's Law, CAP Theorem, Backpressure, Amdahl's Law)
- Microeconomics & Game Theory (Pareto Efficiency, Nash Equilibrium, Comparative Advantage)
- Evolutionary Biology (Red Queen Effect, Aposematism, Evolutionary Mismatch)
- Physics & Thermodynamics (Entropy, Critical Mass, Activation Energy)
- Military Strategy (OODA Loop, Sun Tzu's Asymmetry, Defense in Depth)
- Cryptography & Trust (Zero-Knowledge Proofs, Byzantine Fault Tolerance)
- Capital Allocation & Finance (Compounding, Ergodicity, Kelly Criterion)

---

## Telemetry & Privacy

`mental-models-mcp` collects anonymous usage telemetry to monitor server reliability, tool latency, and query patterns across client harnesses.
- Operational metrics: tool execution duration, status codes, and result counts.
- Intent analysis: query intent truncated up to 300 characters.
- Secret hygiene: credentials, API keys, and authorization tokens are automatically scrubbed (`[REDACTED]`).
- Opt out any time by setting `DO_NOT_TRACK=1` or `MCP_TELEMETRY_OPT_OUT=1`.

---

## License

MIT © [Surendran B](https://github.com/surendranb)
