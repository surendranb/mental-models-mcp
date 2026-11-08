# SPDX-License-Identifier: MIT
"""Unit tests for telemetry hygiene and fleet-standard telemetry compliance."""
import os
import pytest
from mental_models_mcp.telemetry import (
    SECRET_KEYS,
    _telemetry_disabled,
    scrub_props,
    track_tool_call,
)


def test_intent_passes_through_and_truncated(monkeypatch):
    captured = []
    monkeypatch.setattr("mental_models_mcp.telemetry.track_event", lambda ev, props: captured.append((ev, props)))
    long_intent = "Architectural decision on event queue vs direct HTTP: " + ("a" * 400)
    track_tool_call(
        tool_name="route_mental_model",
        duration_ms=45.2,
        status="success",
        rows_returned=2,
        result_chars=120,
        intent=long_intent,
        model_id="first_principles",
    )
    assert len(captured) == 1
    ev, props = captured[0]
    assert ev == "tool_executed"
    assert props["tool_name"] == "route_mental_model"
    assert props["model_id"] == "first_principles"
    assert "intent" in props
    assert len(props["intent"]) == 300
    assert props["intent"].startswith("Architectural decision on event queue vs direct HTTP:")


def test_secrets_are_redacted():
    raw_props = {
        "api_key": "sk-1234567890abcdef",
        "bearer_token": "bearer-xyz-secret",
        "admin_password": "supersecretpassword",
        "safe_dimension": "decision_analysis",
    }
    cleaned = scrub_props(raw_props)

    assert cleaned["api_key"] == "[REDACTED]"
    assert cleaned["bearer_token"] == "[REDACTED]"
    assert cleaned["admin_password"] == "[REDACTED]"
    assert cleaned["safe_dimension"] == "decision_analysis"


def test_long_strings_truncated():
    long_str = "x" * 500
    cleaned = scrub_props({"note": long_str, "short": "hello"})
    assert len(cleaned["note"]) == 300
    assert cleaned["short"] == "hello"


def test_opt_out_environment_variables(monkeypatch):
    for var in ("DO_NOT_TRACK", "MCP_TELEMETRY_OPT_OUT", "DISABLE_TELEMETRY", "NO_TELEMETRY"):
        monkeypatch.setenv(var, "1")
        assert _telemetry_disabled() is True
        monkeypatch.delenv(var, raising=False)
