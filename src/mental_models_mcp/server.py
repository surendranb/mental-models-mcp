# SPDX-License-Identifier: MIT
"""Mental Models MCP Server: Multi-disciplinary mental models and cognitive orientation engine."""
from __future__ import annotations
import functools
import json
import os
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from mcp.server.mcpserver import MCPServer
from mental_models_mcp.catalog import (
    fetch_model_markdown,
    get_model_metadata,
    list_models_catalog,
    slice_playbook,
)
from mental_models_mcp.router import route_problem
from mental_models_mcp.telemetry import (
    MCP_SERVER_VERSION,
    SERVER_NAME,
    announce_and_fire_boot_events,
    track_event,
    track_tool_call,
)
from mental_models_mcp.updates import append_upgrade_nudge, check_server_update

INSTRUCTIONS = """
Mental Models MCP provides multi-disciplinary mental models, cognitive orientation coaching,
and dialectical reasoning frameworks for complex engineering and decision-making problems.
Invoke 'route_mental_model' to discover relevant models for ambiguous or architectural problems,
and 'get_mental_model' to obtain structured operational checklists and probing questions.
Do NOT invoke for routine syntax errors, package installations, or trivial code formatting.
""".strip()

mcp = MCPServer(
    SERVER_NAME,
    title="Mental Models MCP Server",
    description="Multi-disciplinary mental models, cognitive orientation coaching, and dialectical reasoning engine.",
    instructions=INSTRUCTIONS,
    version=MCP_SERVER_VERSION,
    website_url="https://mental-models.builditwithai.xyz",
)


def _wrap_tool(orig_tool: Callable[..., Any]) -> Callable[..., Any]:
    def tool_decorator(*args: Any, **kwargs: Any) -> Any:
        if len(args) == 1 and callable(args[0]) and not kwargs:
            fn = args[0]
            @functools.wraps(fn)
            def wrapper(*f_args: Any, **f_kwargs: Any) -> Any:
                res = fn(*f_args, **f_kwargs)
                if isinstance(res, str):
                    return append_upgrade_nudge(SERVER_NAME, MCP_SERVER_VERSION, res)
                return res
            return orig_tool()(wrapper)

        def dec(fn: Callable[..., Any]) -> Callable[..., Any]:
            @functools.wraps(fn)
            def wrapper(*f_args: Any, **f_kwargs: Any) -> Any:
                res = fn(*f_args, **f_kwargs)
                if isinstance(res, str):
                    return append_upgrade_nudge(SERVER_NAME, MCP_SERVER_VERSION, res)
                return res
            return orig_tool(*args, **kwargs)(wrapper)
        return dec
    return tool_decorator


tool = _wrap_tool(mcp.tool)

SKILLS_URL = "https://raw.githubusercontent.com/surendranb/mental-models-mcp/main/skills"


@tool()
def route_mental_model(problem: str, domain: str = "", problem_type: str = "") -> str:
    """Route an ambiguous challenge, architectural fork, or strategic situation to the optimal mental model.

    Args:
        problem: The situation, question, or fork to analyze (e.g. 'Choosing between async worker queue vs direct HTTP').
        domain: Optional domain filter ('software', 'business', 'architecture', 'personal').
        problem_type: Optional problem type ('diagnose', 'decide', 'optimize', 'strategy', 'risk', 'understand').
    """
    t0 = time.perf_counter()
    try:
        res = route_problem(problem, domain=domain, problem_type=problem_type)
        duration_ms = (time.perf_counter() - t0) * 1000
        out = json.dumps(res, indent=2)

        # Zero-PII telemetry: problem text is stripped, only metadata logged
        top_model = res.get("primary_model") if res.get("status") == "MATCHED" else None
        track_tool_call(
            tool_name="route_mental_model",
            duration_ms=duration_ms,
            status="success",
            rows_returned=len(res.get("recommendations", [])),
            result_chars=len(out),
            model_id=top_model,
        )
        return out
    except Exception as e:
        duration_ms = (time.perf_counter() - t0) * 1000
        err_msg = f"[ERROR] Failed to route mental model: {type(e).__name__}: {e}"
        track_tool_call(
            tool_name="route_mental_model",
            duration_ms=duration_ms,
            status="error",
            error_category=type(e).__name__,
            error_message=str(e),
        )
        return err_msg


@tool()
def get_mental_model(model_id: str, mode: str = "checklist") -> str:
    """Fetch the operational playbook for a specific mental model.

    Args:
        model_id: Model identifier (e.g. 'inversion', 'feedback_loops', 'first_principles', 'chestertons_fence').
        mode: Playbook view mode:
              - 'checklist' (default): Operational thinking steps + failure boundaries + diagnostic probing questions.
              - 'explain': Core principle + origin + failure boundaries + worked example.
              - 'challenge_assumptions': Diagnostic probing questions + failure boundaries (ideal for anti-sycophancy coaching).
              - 'full': Complete unabridged markdown playbook.
    """
    t0 = time.perf_counter()
    raw_id = (model_id or "").strip().lower().replace("-", "_")
    meta = get_model_metadata(raw_id)
    if not meta:
        duration_ms = (time.perf_counter() - t0) * 1000
        out = f"[INPUT_FIXABLE] Unknown mental model '{model_id}'. Call list_mental_models to see available models."
        track_tool_call(
            tool_name="get_mental_model",
            duration_ms=duration_ms,
            status="error",
            model_id=raw_id,
            error_category="ModelNotFound",
            error_message=f"Unknown model {model_id}",
        )
        return out

    content, source = fetch_model_markdown(meta.get("path", ""))
    duration_ms = (time.perf_counter() - t0) * 1000

    if not content:
        out = (
            f"[ENVIRONMENT_FIXABLE: STOP & ASK HUMAN] Playbook for '{model_id}' could not be fetched from GitHub "
            f"or local cache. Ensure network access to github.com is available."
        )
        track_tool_call(
            tool_name="get_mental_model",
            duration_ms=duration_ms,
            status="error",
            model_id=raw_id,
            category=meta.get("category"),
            error_category="FetchError",
            error_message="Model playbook content unavailable",
        )
        return out

    sliced = slice_playbook(content, mode=mode, metadata=meta)
    track_tool_call(
        tool_name="get_mental_model",
        duration_ms=duration_ms,
        status="success",
        rows_returned=1,
        result_chars=len(sliced),
        model_id=raw_id,
        category=meta.get("category"),
    )
    return sliced


@tool()
def list_mental_models(category: str = "", discipline: str = "") -> str:
    """List available mental models in the catalog, optionally filtered.

    Args:
        category: Optional category ('systems_thinking', 'decision_analysis', 'strategic_risk', 'cognitive_biases', 'first_principles_engineering').
        discipline: Optional discipline substring (e.g. 'Physics', 'Economics', 'Philosophy', 'Engineering').
    """
    t0 = time.perf_counter()
    models = list_models_catalog(category=category, discipline=discipline)
    duration_ms = (time.perf_counter() - t0) * 1000
    res = {
        "count": len(models),
        "category_filter": category or "all",
        "discipline_filter": discipline or "all",
        "models": models,
    }
    out = json.dumps(res, indent=2)
    track_tool_call(
        tool_name="list_mental_models",
        duration_ms=duration_ms,
        status="success",
        rows_returned=len(models),
        result_chars=len(out),
        category=category,
    )
    return out


@tool()
def skills_list() -> str:
    """List starter skills (dynamic, GitHub-first)."""
    try:
        local_skills_dir = Path(__file__).resolve().parents[2] / "skills"
        local = sorted(p.stem for p in local_skills_dir.glob("*.md")) if local_skills_dir.exists() else []
    except Exception:
        local = []
    names = set(local or [])
    names.add("setup")
    names.add("mental_models_setup")
    names_sorted = sorted(names)
    track_event("skill_read", {"action": "skills_list", "count": len(names_sorted)})
    return json.dumps({"skills": names_sorted, "source": "github+local"}, indent=2)


@tool()
def skill_read(name: str) -> str:
    """Fetch SKILL.md by name from GitHub, fallback to local file."""
    t0 = time.perf_counter()
    raw = (name or "").strip().lower()
    if raw.endswith(".md"):
        raw = raw[:-3]
    if raw in ("setup", "mental-models-setup", "mental_models_setup", "mental-setup", "mental_setup"):
        safe = "setup"
    else:
        safe = "".join(c for c in raw if c.isalnum() or c in ("_", "-"))

    if not safe:
        duration_ms = (time.perf_counter() - t0) * 1000
        out = "[INPUT_FIXABLE] Empty skill name. Call skills_list first."
        track_tool_call(
            tool_name="skill_read",
            duration_ms=duration_ms,
            status="error",
            error_category="ValidationError",
            error_message=out,
        )
        return out

    # 1. Fetch from GitHub raw
    try:
        url = f"{SKILLS_URL}/{safe}.md"
        req = urllib.request.Request(url, headers={"User-Agent": "mental-models-mcp"})
        with urllib.request.urlopen(req, timeout=5.0) as r:
            text = r.read().decode("utf-8", "replace")
        duration_ms = (time.perf_counter() - t0) * 1000
        track_tool_call(tool_name="skill_read", duration_ms=duration_ms, status="success", rows_returned=1, result_chars=len(text))
        return text
    except Exception:
        # 2. Local fallback
        local_path = Path(__file__).resolve().parents[2] / "skills" / f"{safe}.md"
        if local_path.exists():
            text = local_path.read_text(encoding="utf-8")
            duration_ms = (time.perf_counter() - t0) * 1000
            track_tool_call(tool_name="skill_read", duration_ms=duration_ms, status="success", rows_returned=1, result_chars=len(text))
            return text

        duration_ms = (time.perf_counter() - t0) * 1000
        out = (
            f"[INPUT_FIXABLE] Unknown skill '{name}'. Candidates: call skills_list. "
            f"If network is blocked: [TRANSIENT] retry, or [ENVIRONMENT_FIXABLE: STOP & ASK HUMAN] if GitHub is unreachable."
        )
        track_tool_call(
            tool_name="skill_read",
            duration_ms=duration_ms,
            status="error",
            error_category="NotFoundError",
            error_message=out,
        )
        return out


@tool()
def check_for_updates() -> str:
    """Check PyPI for newer versions of mental-models-mcp and get upgrade instructions."""
    res = check_server_update(SERVER_NAME, MCP_SERVER_VERSION, force_check=True)
    return json.dumps(res, indent=2)


def main() -> None:
    announce_and_fire_boot_events()
    track_event("mcp_started", {})
    mcp.run()


if __name__ == "__main__":
    main()
