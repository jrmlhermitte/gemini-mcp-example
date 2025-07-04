from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("greeter")


@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}!"


if __name__ == "__main__":
    # NOTE: stdio is the default.
    mcp.run(transport="stdio")
