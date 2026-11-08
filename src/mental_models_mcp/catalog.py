# SPDX-License-Identifier: MIT
"""Catalog indexing, dynamic GitHub fetching, and local cache management for mental models."""
from __future__ import annotations
import json
import os
import re
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/surendranb/mental-models-mcp/main"
LOCAL_CACHE_DIR = Path.home() / ".cache" / "mental-models"

_CACHED_INDEX: Optional[Dict[str, Any]] = None


def get_repo_root() -> Path:
    """Best effort to locate local repo root if running from source checkout."""
    return Path(__file__).resolve().parents[2]


def load_index(force_reload: bool = False) -> Dict[str, Any]:
    """Loads models index from local package data, source checkout, or GitHub raw."""
    global _CACHED_INDEX
    if _CACHED_INDEX is not None and not force_reload:
        return _CACHED_INDEX

    # 1. Check bundled package data
    package_data = Path(__file__).parent / "data" / "index.json"
    if package_data.exists():
        try:
            _CACHED_INDEX = json.loads(package_data.read_text(encoding="utf-8"))
            return _CACHED_INDEX
        except Exception:
            pass

    # 2. Check local repo root
    repo_models_index = get_repo_root() / "models" / "index.json"
    if repo_models_index.exists():
        try:
            _CACHED_INDEX = json.loads(repo_models_index.read_text(encoding="utf-8"))
            return _CACHED_INDEX
        except Exception:
            pass

    # 3. Check disk cache
    cache_index = LOCAL_CACHE_DIR / "index.json"
    if cache_index.exists():
        try:
            _CACHED_INDEX = json.loads(cache_index.read_text(encoding="utf-8"))
            return _CACHED_INDEX
        except Exception:
            pass

    # 4. Fetch from GitHub raw
    try:
        url = f"{GITHUB_RAW_BASE}/models/index.json"
        req = urllib.request.Request(url, headers={"User-Agent": "mental-models-mcp"})
        with urllib.request.urlopen(req, timeout=4.0) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            _CACHED_INDEX = data
            LOCAL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
            cache_index.write_text(json.dumps(data, indent=2), encoding="utf-8")
            return _CACHED_INDEX
    except Exception:
        pass

    return {"version": "0.0.0", "categories": [], "models": []}


def get_model_metadata(model_id: str) -> Optional[Dict[str, Any]]:
    """Lookup model definition from index by ID (normalized)."""
    norm = (model_id or "").strip().lower().replace("-", "_")
    index = load_index()
    for m in index.get("models", []):
        if m.get("id", "").lower().replace("-", "_") == norm:
            return m
    return None


def fetch_model_markdown(model_path: str) -> Tuple[Optional[str], str]:
    """Fetches model markdown from local repo, disk cache, or GitHub raw."""
    # 1. Local disk cache
    cached_path = LOCAL_CACHE_DIR / model_path
    if cached_path.exists():
        try:
            return cached_path.read_text(encoding="utf-8"), "cache"
        except Exception:
            pass

    # 2. Local repository workspace (if developing locally)
    repo_path = get_repo_root() / model_path
    if repo_path.exists():
        try:
            return repo_path.read_text(encoding="utf-8"), "local"
        except Exception:
            pass

    # 3. GitHub raw fetch
    url = f"{GITHUB_RAW_BASE}/{model_path}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "mental-models-mcp"})
        with urllib.request.urlopen(req, timeout=5.0) as resp:
            content = resp.read().decode("utf-8", "replace")
            # Cache locally for offline reliability
            try:
                cached_path.parent.mkdir(parents=True, exist_ok=True)
                cached_path.write_text(content, encoding="utf-8")
            except Exception:
                pass
            return content, "github"
    except Exception:
        pass

    return None, "missing"


def parse_markdown_sections(text: str) -> Dict[str, str]:
    """Splits markdown into titled sections."""
    sections: Dict[str, str] = {}
    current_title = "header"
    current_lines: List[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            if current_lines:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[3:].strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        sections[current_title] = "\n".join(current_lines).strip()

    return sections


def slice_playbook(markdown_text: str, mode: str, metadata: Dict[str, Any]) -> str:
    """Slices markdown playbook by mode to prevent context bloat."""
    mode_clean = (mode or "checklist").strip().lower()
    if mode_clean == "full":
        return markdown_text

    sections = parse_markdown_sections(markdown_text)
    header = sections.get("header", f"# {metadata.get('title', 'Mental Model')}")

    # Section matchers
    core_principle = next((v for k, v in sections.items() if "core principle" in k.lower()), "")
    failure_boundaries = next((v for k, v in sections.items() if "not to use" in k.lower() or "failure" in k.lower()), "")
    thinking_steps = next((v for k, v in sections.items() if "operational" in k.lower() or "steps" in k.lower()), "")
    probing_questions = next((v for k, v in sections.items() if "probing" in k.lower() or "questions" in k.lower()), "")
    worked_example = next((v for k, v in sections.items() if "example" in k.lower()), "")

    parts = [header]

    if mode_clean == "checklist":
        # Actionable focus: failure boundaries + operational steps + diagnostic probing
        if failure_boundaries:
            parts.append(failure_boundaries)
        if thinking_steps:
            parts.append(thinking_steps)
        if probing_questions:
            parts.append(probing_questions)
    elif mode_clean == "explain":
        # Conceptual understanding: core principle + failure boundaries + worked example
        if core_principle:
            parts.append(core_principle)
        if failure_boundaries:
            parts.append(failure_boundaries)
        if worked_example:
            parts.append(worked_example)
    elif mode_clean == "challenge_assumptions":
        # Cognitive coaching / anti-sycophancy: probing questions + failure boundaries
        if probing_questions:
            parts.append(probing_questions)
        if failure_boundaries:
            parts.append(failure_boundaries)
    else:
        # Unknown mode fallback to full
        return markdown_text

    # If parsing found matching sections, join them; otherwise fallback to full text
    if len(parts) > 1:
        return "\n\n".join(p for p in parts if p.strip())
    return markdown_text


def list_models_catalog(category: str = "", discipline: str = "") -> List[Dict[str, Any]]:
    """List all models in index, optionally filtered."""
    index = load_index()
    models = index.get("models", [])
    cat_norm = (category or "").strip().lower()
    disc_norm = (discipline or "").strip().lower()

    filtered = []
    for m in models:
        if cat_norm and cat_norm != m.get("category", "").lower():
            continue
        if disc_norm and disc_norm not in m.get("discipline", "").lower():
            continue
        filtered.append({
            "id": m.get("id"),
            "title": m.get("title"),
            "category": m.get("category"),
            "discipline": m.get("discipline"),
            "description": m.get("description"),
            "domains": m.get("domains", []),
            "problem_types": m.get("problem_types", []),
        })
    return filtered
