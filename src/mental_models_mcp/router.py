# SPDX-License-Identifier: MIT
"""Cognitive routing engine: matches problems to mental models or gates with NONE for trivial tasks."""
from __future__ import annotations
import re
from typing import Any, Dict, List, Set
from mental_models_mcp.catalog import load_index

TRIVIAL_PATTERNS = [
    r"\bfix\s+typo\b",
    r"\bsyntax\s+error\b",
    r"\blint\b",
    r"\bformat\s+code\b",
    r"\brename\s+variable\b",
    r"\bimport\s+module\b",
    r"\brun\s+tests?\b",
    r"\bhow\s+to\s+install\b",
    r"\bcss\s+color\b",
    r"\bindentation\b",
]

SATISFICING_THRESHOLD = 3.0

DOMAIN_KEYWORDS: Dict[str, Set[str]] = {
    "software": {"software", "code", "database", "api", "backend", "frontend", "server", "deploy", "repo", "service", "app", "dev", "bug", "refactor"},
    "architecture": {"architecture", "system", "systems", "infrastructure", "distributed", "scalability", "pipeline", "queue", "network", "microservices"},
    "business": {"business", "sales", "revenue", "customer", "market", "pricing", "growth", "client", "product", "hiring", "retention"},
    "personal": {"habit", "productivity", "career", "personal", "focus", "burnout", "learning", "time"},
}


def _simple_stem(word: str) -> str:
    w = word.lower()
    for sfx in ("ing", "tion", "sion", "ment", "ity", "ies", "es", "ed", "s"):
        if w.endswith(sfx) and len(w) > len(sfx) + 2:
            return w[:-len(sfx)]
    return w


def is_trivial_task(problem: str) -> bool:
    """Detects purely syntactic, superficial, or mechanical tasks that do not warrant cognitive modeling."""
    p = (problem or "").strip().lower()
    if not p:
        return True
    if len(p.split()) <= 3 and not any(k in p for k in ("why", "choose", "fail", "risk", "scale", "deadlock", "delay", "growth", "tradeoff", "invert")):
        return True
    for pat in TRIVIAL_PATTERNS:
        if re.search(pat, p):
            return True
    return False


def score_model(
    model: Dict[str, Any],
    problem_text: str,
    domain_filter: str = "",
    problem_type_filter: str = "",
) -> float:
    """Calculates heuristic alignment score between a problem and a mental model."""
    score = 0.0
    text_lower = problem_text.lower()
    words_in_text = set(re.findall(r"\b\w{3,}\b", text_lower))
    stems_in_text = {_simple_stem(w) for w in words_in_text}

    model_id = model.get("id", "").lower()
    model_title = model.get("title", "").lower()

    # 1. Direct model name / ID mention
    if model_id.replace("_", " ") in text_lower or model_title in text_lower:
        score += 3.5

    # Title stem matching
    title_stems = {_simple_stem(w) for w in re.findall(r"\b\w{3,}\b", model_title)}
    if title_stems.intersection(stems_in_text):
        score += 2.0

    # 2. Trigger matches (high value)
    triggers = [t.lower() for t in model.get("triggers", [])]
    for trig in triggers:
        if " " in trig or "-" in trig:
            clean_trig = trig.replace("-", " ")
            if trig in text_lower or clean_trig in text_lower:
                score += 3.0
        else:
            trig_stem = _simple_stem(trig)
            if trig in words_in_text or trig_stem in stems_in_text:
                score += 2.0

    # 3. Domain alignment
    model_domains = [d.lower() for d in model.get("domains", [])]
    if domain_filter:
        df = domain_filter.lower().strip()
        if df in model_domains:
            score += 1.5
    else:
        for md in model_domains:
            keywords = DOMAIN_KEYWORDS.get(md, {md})
            if keywords.intersection(words_in_text):
                score += 0.8
                break

    # 4. Problem type alignment
    model_pts = [pt.lower() for pt in model.get("problem_types", [])]
    if problem_type_filter:
        ptf = problem_type_filter.lower().strip()
        if ptf in model_pts:
            score += 1.5
    else:
        for pt in model_pts:
            pt_stem = _simple_stem(pt)
            if pt in words_in_text or pt_stem in stems_in_text:
                score += 0.8
                break

    # 5. Description word overlap
    desc_words = set(re.findall(r"\b\w{4,}\b", model.get("description", "").lower()))
    overlap_desc = desc_words.intersection(words_in_text)
    score += len(overlap_desc) * 0.4

    return score


def route_problem(
    problem: str,
    domain: str = "",
    problem_type: str = "",
) -> Dict[str, Any]:
    """Routes an ambiguous problem or architectural fork to the optimal mental model."""
    if is_trivial_task(problem):
        return {
            "status": "NONE",
            "message": "Routine or syntactic task detected. No mental model required; direct execution is optimal to avoid cognitive bloat.",
            "recommendations": [],
        }

    index = load_index()
    models = index.get("models", [])
    if not models:
        return {
            "status": "NONE",
            "message": "Catalog index is currently empty or unavailable.",
            "recommendations": [],
        }

    scored: List[tuple[float, Dict[str, Any]]] = []
    for m in models:
        s = score_model(m, problem, domain, problem_type)
        if s >= SATISFICING_THRESHOLD:
            scored.append((s, m))

    scored.sort(key=lambda x: x[0], reverse=True)

    if not scored:
        return {
            "status": "NONE",
            "message": f"No mental model exceeded the satisficing threshold ({SATISFICING_THRESHOLD}). The problem may be routine or domain-specific.",
            "recommendations": [],
        }

    top_matches = scored[:3]
    recommendations = []
    for rank, (score, m) in enumerate(top_matches, start=1):
        recommendations.append({
            "rank": rank,
            "model_id": m.get("id"),
            "title": m.get("title"),
            "category": m.get("category"),
            "discipline": m.get("discipline"),
            "match_score": round(score, 1),
            "description": m.get("description"),
            "instruction": f"Call get_mental_model(model_id='{m.get('id')}', mode='checklist') to operationalize.",
        })

    return {
        "status": "MATCHED",
        "primary_model": recommendations[0]["model_id"],
        "recommendations": recommendations,
    }
