# SPDX-License-Identifier: MIT
"""End-to-end integration tests over stdio transport."""
import json
import os
import sys
import pytest
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


@pytest.mark.asyncio
async def test_stdio_server_e2e():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-m", "mental_models_mcp"],
        env={**os.environ, "DO_NOT_TRACK": "1"},
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            init_res = await session.initialize()
            assert init_res.server_info.name == "mental-models-mcp"

            # 1. List tools
            tools_result = await session.list_tools()
            tool_names = {t.name for t in tools_result.tools}
            expected_tools = {
                "route_mental_model",
                "get_mental_model",
                "list_mental_models",
                "skills_list",
                "skill_read",
                "check_for_updates",
            }
            assert expected_tools.issubset(tool_names)

            # 2. Call route_mental_model (trivial)
            triv_res = await session.call_tool("route_mental_model", arguments={"problem": "fix typo"})
            assert not triv_res.is_error
            triv_data = json.loads(triv_res.content[0].text)
            assert triv_data["status"] == "NONE"

            # 3. Call route_mental_model (matched)
            match_res = await session.call_tool(
                "route_mental_model",
                arguments={"problem": "How do we invert this database rollout to avoid disaster and catastrophe?", "domain": "software"},
            )
            assert not match_res.is_error
            match_data = json.loads(match_res.content[0].text)
            assert match_data["status"] == "MATCHED"
            assert match_data["primary_model"] == "inversion"

            # 4. Call get_mental_model
            model_res = await session.call_tool(
                "get_mental_model",
                arguments={"model_id": "inversion", "mode": "checklist"},
            )
            assert not model_res.is_error
            playbook_text = model_res.content[0].text
            assert "Inversion" in playbook_text
            assert "When NOT to Use" in playbook_text

            # 5. Call list_mental_models
            list_res = await session.call_tool(
                "list_mental_models",
                arguments={"category": "systems_thinking"},
            )
            assert not list_res.is_error
            list_data = json.loads(list_res.content[0].text)
            assert list_data["count"] == 5

            # 6. Call skills_list
            skills_res = await session.call_tool("skills_list", arguments={})
            assert not skills_res.is_error
            skills_data = json.loads(skills_res.content[0].text)
            assert "setup" in skills_data["skills"]
            assert "mental-models-coach" in skills_data["skills"]

            # 7. Call skill_read (flat setup and agentskills.io package)
            skill_read_res = await session.call_tool("skill_read", arguments={"name": "setup"})
            assert not skill_read_res.is_error
            assert "Setting Up Mental Models MCP Server" in skill_read_res.content[0].text

            coach_read_res = await session.call_tool("skill_read", arguments={"name": "mental-models-coach"})
            assert not coach_read_res.is_error
            assert "mental-models-coach" in coach_read_res.content[0].text
            assert "agentskills.io" in coach_read_res.content[0].text

            tax_read_res = await session.call_tool("skill_read", arguments={"name": "taxonomy"})
            assert not tax_read_res.is_error
            assert "122 Models Across 8 Disciplines" in tax_read_res.content[0].text

            # 8. Call check_for_updates
            up_res = await session.call_tool("check_for_updates", arguments={})
            assert not up_res.is_error
            up_data = json.loads(up_res.content[0].text)
            assert up_data["server"] == "mental-models-mcp"
