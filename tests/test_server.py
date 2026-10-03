"""End-to-end MCP check: launch the real server and call every tool."""

import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def test_stdio_server():
    async def check():
        parameters = StdioServerParameters(command=sys.executable, args=["-m", "mcp_tools_lab"])
        async with stdio_client(parameters) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                listed = await session.list_tools()
                examples = {
                    "analyze_text": {"text": "hello"},
                    "process_json": {"text": '{"hello": 1}'},
                    "inspect_csv": {"text": "name\nAda"},
                    "hash_text": {"text": "abc"},
                    "compare_text": {"before": "old", "after": "new"},
                    "convert_timestamp": {"value": "0"},
                    "inspect_url": {"url": "https://example.com"},
                }
                assert {tool.name for tool in listed.tools} == set(examples)
                for name, arguments in examples.items():
                    result = await session.call_tool(name, arguments)
                    assert not result.isError, (name, result)
                    assert result.content
                invalid = await session.call_tool("convert_timestamp", {"value": "not-a-number"})
                assert invalid.isError
                assert not (await session.call_tool("hash_text", {"text": "still alive"})).isError
    asyncio.run(asyncio.wait_for(check(), timeout=45))
