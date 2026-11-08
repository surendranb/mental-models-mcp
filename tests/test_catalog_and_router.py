# SPDX-License-Identifier: MIT
"""Unit tests for mental model catalog and cognitive router."""
import json
import pytest
from mental_models_mcp.catalog import (
    fetch_model_markdown,
    get_model_metadata,
    list_models_catalog,
    load_index,
    slice_playbook,
)
from mental_models_mcp.router import is_trivial_task, route_problem, score_model


def test_index_structure_and_count():
    index = load_index(force_reload=True)
    assert "categories" in index
    assert "models" in index
    assert len(index["categories"]) == 5
    assert len(index["models"]) == 25

    categories = set(index["categories"])
    for m in index["models"]:
        assert m["id"]
        assert m["title"]
        assert m["category"] in categories
        assert m["discipline"]
        assert isinstance(m["problem_types"], list)
        assert isinstance(m["domains"], list)
        assert isinstance(m["triggers"], list)
        assert m["description"]
        assert m["path"].endswith(".md")


def test_get_model_metadata():
    m = get_model_metadata("inversion")
    assert m is not None
    assert m["id"] == "inversion"
    assert m["category"] == "decision_analysis"

    # Case insensitivity and hyphen normalization
    m2 = get_model_metadata("FIRST-PRINCIPLES")
    assert m2 is not None
    assert m2["id"] == "first_principles"

    # Non-existent
    assert get_model_metadata("non_existent_model_xyz") is None


def test_fetch_and_slice_playbook():
    meta = get_model_metadata("inversion")
    content, source = fetch_model_markdown(meta["path"])
    assert content is not None
    assert len(content) > 200

    # Test modes
    full = slice_playbook(content, mode="full", metadata=meta)
    assert full == content

    checklist = slice_playbook(content, mode="checklist", metadata=meta)
    assert "Operational Thinking Steps" in checklist or "When NOT to Use" in checklist

    explain = slice_playbook(content, mode="explain", metadata=meta)
    assert "Core Principle" in explain or "Worked Example" in explain

    challenge = slice_playbook(content, mode="challenge_assumptions", metadata=meta)
    assert "Probing Questions" in challenge or "When NOT to Use" in challenge


def test_list_models_catalog_filters():
    all_models = list_models_catalog()
    assert len(all_models) == 25

    systems_models = list_models_catalog(category="systems_thinking")
    assert len(systems_models) == 5
    assert all(m["category"] == "systems_thinking" for m in systems_models)

    econ_models = list_models_catalog(discipline="Economics")
    assert len(econ_models) >= 1
    assert any("Economics" in m["discipline"] for m in econ_models)


def test_is_trivial_task():
    assert is_trivial_task("fix typo in readme") is True
    assert is_trivial_task("syntax error") is True
    assert is_trivial_task("format code") is True
    assert is_trivial_task("indentation") is True
    assert is_trivial_task("how to install") is True
    assert is_trivial_task("") is True

    # Substantive decisions should not be marked trivial
    assert is_trivial_task("Why is the pipeline queue delaying our rollout?") is False
    assert is_trivial_task("Should we choose Kafka or direct HTTP webhook?") is False


def test_router_trivial_gating():
    res = route_problem("fix typo in readme")
    assert res["status"] == "NONE"
    assert "Routine or syntactic task detected" in res["message"]
    assert res["recommendations"] == []


def test_router_high_signal_matching():
    # Inversion trigger
    res = route_problem("How do we invert this database rollout to avoid disaster and catastrophe?", domain="software")
    assert res["status"] == "MATCHED"
    assert res["primary_model"] == "inversion"
    assert len(res["recommendations"]) >= 1

    # Bottleneck trigger
    res_b = route_problem("Our async ingestion throughput is blocked by a queue bottleneck constraint", domain="software")
    assert res_b["status"] == "MATCHED"
    assert res_b["primary_model"] == "bottleneck_theory_of_constraints"
