# SPDX-License-Identifier: MIT
"""Unit tests for telemetry redaction and Zero-PII compliance."""
import os
import pytest
from mental_models_mcp.telemetry import (
    DISALLOWED_PII_KEYS,
    SECRET_KEYS,
    _telemetry_disabled,
    scrub_props,
    track_tool_call,
)


def test_pii_keys_are_stripped():
    raw_props = {
        "tool_name": "route_mental_model",
        "problem": "Sensitive confidential architecture detail",
        "query": "DROP TABLE users",
        "user_input": "Secret strategy plan",
        "prompt": "Explain this private codebase",
        "model_id": "inversion",
        "status": "success",
    }
    cleaned = scrub_props(raw_props)

    assert "model_id" in cleaned
    assert "status" in cleaned
    assert "tool_name" in cleaned

    # All PII keys must be completely removed
    for pii_key in DISALLOWED_PII_KEYS:
        assert pii_key not in cleaned


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
    assert len(cleaned["note"]) == 200
    assert cleaned["short"] == "hello"


def test_opt_out_environment_variables(monkeypatch):
    for var in ("DO_NOT_TRACK", "MCP_TELEMETRY_OPT_OUT", "DISABLE_TELEMETRY", "NO_TELEMETRY"):
        monkeypatch.setenv(var, "1")
        assert _telemetry_disabled() is True
        monkeypatch.delenv(var, raising=False)
