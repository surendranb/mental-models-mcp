# mental-models-mcp

> Multi-disciplinary mental models, cognitive orientation coaching, and dialectical reasoning engine for AI agents and humans. Zero API keys.

`mental-models-mcp` transforms AI assistants into high-leverage thinking partners. Instead of agreeable sycophancy or generic advice, it equips models with a structured latticework of mental models across systems thinking, decision analysis, strategic risk, cognitive biases, and first-principles engineering.

---

## Quickstart

### Claude Desktop (`claude_desktop_config.json`)

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

### Cursor (`.cursor/mcp.json`)

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

### CLI / Test Execution

```bash
uvx mental-models-mcp
```

---

## Core Capabilities

1. **`route_mental_model(problem, domain, problem_type)`**:
   Lightweight L0 index (~200 tokens) scoring candidate frameworks against your specific situation. Defaults to `NONE` on trivial or purely syntactic tasks to prevent unnecessary context consumption.
2. **`get_mental_model(model_id, mode)`**:
   Fetches the full operational playbook for a mental model with three execution modes:
   - `explain`: Core concept, historical origin, and real-world intuition.
   - `challenge_assumptions`: Dialectical anti-sycophancy sparring that aggressively stress-tests premises and uncovers confirmation bias.
   - `checklist`: Concrete step-by-step verification checklist and falsification criteria.
3. **`list_mental_models(category, discipline)`**:
   Categorical and topical exploration across the latticework.
4. **`skills_list()` / `skill_read(name)`**:
   Dynamic runtime onboarding and setup guidance fetched live from GitHub with local disk cache fallback.
5. **`check_for_updates()`**:
   PyPI version verification and automated upgrade hints.

---

## Privacy & Zero-PII Guarantee

When used for personal dilemmas or high-stakes corporate decisions ("Should I fire employee X?", "Should we acquire company Y?"), **user prompt and problem text is never transmitted or logged**. Telemetry captures strictly operational metadata (`model_id`, execution duration, status code, client harness type, and a salted one-way session hash).

---

## License

MIT © [Surendran B](https://github.com/surendranb)
