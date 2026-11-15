"""GodVerse MCP server.

Exposes project metadata and safe, read-only information about the GodVerse
world-simulation project. This first version does not mutate a running world.
"""
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GodVerse", stateless_http=True, json_response=True)

PROJECT = {
    "name": "GodVerse",
    "repository": "https://github.com/noeljakisa2-ai/GodVerse",
    "description": "Browser-based 3D world and ecosystem simulation.",
    "current_scope": "World/landscape prototype and simulation controls.",
    "limitations": [
        "MCP currently exposes project information only.",
        "It is not connected to a live browser session or running simulation.",
        "It cannot yet create, edit, or control world entities."
    ],
}

@mcp.tool()
def godverse_status() -> dict:
    """Return the current integration status and known limitations of GodVerse."""
    return {
        "project": PROJECT["name"],
        "repository": PROJECT["repository"],
        "mcp_status": "online",
        "live_world_connection": False,
        "world_mutation_tools": False,
        "description": PROJECT["description"],
        "limitations": PROJECT["limitations"],
    }

@mcp.tool()
def godverse_project_info() -> dict:
    """Describe the GodVerse project and its current scope."""
    return PROJECT

@mcp.tool()
def godverse_capabilities() -> list:
    """List the tools currently exposed by the GodVerse MCP server."""
    return [
        {"tool": "godverse_status", "purpose": "Check MCP and live-world connection status"},
        {"tool": "godverse_project_info", "purpose": "Read GodVerse project metadata"},
        {"tool": "godverse_capabilities", "purpose": "List available MCP capabilities"},
    ]

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=int(os.getenv("PORT", "10000")))
