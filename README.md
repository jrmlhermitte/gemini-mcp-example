## MCP Example

Quick repo to demonstrate MCP. Nothing more.

## Setup
Quick setup of a new project:

1. [Install
UV](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
(linux and mac)

2. Create a project and setup python env

```bash
mkdir my_project
cd my_project
uv init
uv add "mcp[cli]" httpx
source .venv/bin/activate
```

3. Write your file:
```py3
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
```

4. Run file
```
python main.py
```


5. Init communication

We're going to initialize the
[2024-11-05](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
protocol version.

Paste this exactly into your shell:

```json
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{"roots":{"listChanged":true},"tools":{"listChanged":true},"sampling":{},"elicitation":{}},"clientInfo":{"name":"ExampleClient","title":"ExampleClientDisplayName","version":"1.0.0"}}}
```

You should see:

```json
{"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2024-11-05","capabilities":{"experimental":{},"prompts":{"listChanged":false},"resources":{"subscribe":false,"listChanged":false},"tools":{"listChanged":false}},"serverInfo":{"name":"weather","version":"1.10.1"}}}
```

When you do, paste this to start the connection:
```json
{"jsonrpc":"2.0","method":"notifications/initialized"}
```

Now type this to list available tools:
```json
{"jsonrpc":"2.0","method":"tools/list","id":1}
```

you should see something like this (you may see additional logging):

```json
{"jsonrpc":"2.0","id":1,"result":{"tools":[{"name":"my_tool","description":"","inputSchema":{"properties":{"name":{"title":"Name","type":"string"}},"required":["name"],"title":"my_toolArguments","type":"object"},"outputSchema":{"properties":{"result":{"title":"Result","type":"string"}},"required":["result"],"title":"my_toolOutput","type":"object"}}]}}
```

Congratulations! You have successfully started a Stdio connection with an MCP
server! This is how you're going to setup an MCP server with Gemini.


## Gemini CLI
Integrating with Gemini CLI.

1. [install node](https://nodejs.org/en/download)
2. 
