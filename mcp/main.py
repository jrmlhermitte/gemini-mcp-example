from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")


@mcp.tool()
def my_tool(name: str) -> str:
    return f'Hello {name}!'


if __name__ == "__main__":
    # NOTE: stdio is the default.
    mcp.run(transport='stdio')
