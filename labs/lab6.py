# Using MCPs (Model Context Protocols)
# Streamable HTTP Clients

from strands import Agent, tool
from strands.models.ollama import OllamaModel

# New Imports
# from strands.tools.mcp import MCPClient
# from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client


# Ollama
ollama_model = OllamaModel(
  model_id="gpt-oss:20b",
  host="http://localhost:11434"

)

# Pre-req, run the following to start the streamable Http server, in a different terminal:
# python mcp-streamable-http/python-example/server/weather.py
streamable_http_mcp_client = MCPClient(
    lambda: streamablehttp_client(
        url="http://localhost:8123/mcp"
    ))

# Create an agent with MCP tools
with streamable_http_mcp_client:
    # Get the tools from the MCP server
    tools = streamable_http_mcp_client.list_tools_sync()

    # Create an agent with these tools
    agent = Agent(
        system_prompt="You are weather expert, provide weather details by using the available tools",
        model=ollama_model, 
        tools=tools
        )
    agent("What is weather in New York?")