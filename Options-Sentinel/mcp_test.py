import subprocess
import os
import json
from dotenv import load_dotenv

load_dotenv()

# The Alpaca MCP server (v2) can be run via standard input/output.
# Note: The server you cloned is v2 (Python-based), not v1 (Node.js).
# We can invoke it using 'uvx' if 'uv' is installed, or by running the python module directly.

# Example of how you would configure an MCP client (like Claude Desktop or Cursor):
client_config = {
    "mcpServers": {
        "alpaca": {
            "command": "uvx",
            "args": ["alpaca-mcp-server"],
            "env": {
                "ALPACA_API_KEY": os.getenv("ALPACA_API_KEY", ""),
                "ALPACA_SECRET_KEY": os.getenv("ALPACA_SECRET_KEY", "")
            }
        }
    }
}

print("MCP Client Configuration needed:")
print(json.dumps(client_config, indent=2))
print("\nTo test, configure your MCP Client (e.g., Cursor, Claude Desktop) with the above settings.")
print("Then ask the AI: 'Show my Alpaca paper account balance.'")
