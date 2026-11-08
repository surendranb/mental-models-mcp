---
description: Setup, client harness configuration, and quickstart guide for mental-models-mcp.
---

# Setting Up Mental Models MCP Server

A zero-configuration multi-disciplinary mental models, cognitive coaching, and dialectical reasoning engine for AI agents and humans.

Official Repository: [github.com/surendranb/mental-models-mcp](https://github.com/surendranb/mental-models-mcp)

---

## 1. Quickstart (Zero API Keys Required)

`mental-models-mcp` is completely self-contained:
- **Zero API keys, zero accounts, and zero cloud credentials required.**
- Operates locally via FastMCP stdio transport with on-demand dynamic playbook loading.
- Anonymous usage telemetry with automatic secret scrubbing and opt-out support.

---

## 2. Client Configuration

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

### Command Line / CLI Testing
```bash
uvx mental-models-mcp
```

---

## 3. Core Tools & Workflow

1. **`route_mental_model(problem, domain, problem_type)`**:
   Lightweight L0 index scoring candidate frameworks against your specific situation. Defaults to `NONE` on trivial or purely syntactic tasks to prevent unnecessary context consumption.
2. **`get_mental_model(model_id, mode)`**:
   Fetches the full operational playbook for a mental model with three execution modes:
   - `explain`: Core concept, historical origin, and real-world intuition.
   - `challenge_assumptions`: Dialectical anti-sycophancy sparring that aggressively stress-tests premises and uncovers confirmation bias.
   - `checklist`: Concrete step-by-step verification checklist and falsification criteria.
3. **`list_mental_models(category, discipline)`**:
   Categorical and topical exploration across the latticework.
4. **`skills_list()` / `skill_read(name="setup")`**:
   Load setup and diagnostic playbooks dynamically from GitHub.
5. **`check_for_updates()`**:
   PyPI version verification and automated upgrade hints.

---

## 4. Troubleshooting & Operational Guidance

- **Model Selection Ambiguity**: When unsure between two models, call `route_mental_model(problem=...)` to let the router suggest the highest-scoring framework or return complementary pairings.
- **Trivial Decisions**: If the router returns `NONE`, trust the verdict and proceed directly with implementation rather than forcing a complex mental framework.
- **Dynamic Skills & Offline Fallback**: Skills and model playbooks are fetched dynamically from GitHub with automatic disk caching in `~/.cache/mental-models/`. Once loaded, they remain fully accessible offline.
