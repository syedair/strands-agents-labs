# Using MCPs (Model Context Protocols)
# Streamable HTTP Clients
# With Asynchronous Iterators using stream_async

from strands import Agent, tool
from strands.models.ollama import OllamaModel

# New Imports
# from strands.tools.mcp import MCPClient
# from mcp import stdio_client, StdioServerParameters
from strands.tools.mcp.mcp_client import MCPClient
from mcp.client.streamable_http import streamablehttp_client

# New Imports
import asyncio


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




async def process_streaming_response():
    # Create an agent with MCP tools inside the context manager
    with streamable_http_mcp_client:
        # Get the tools from the MCP server
        tools = streamable_http_mcp_client.list_tools_sync()

        # Create an agent with these tools
        agent = Agent(
            system_prompt="You are weather expert, provide weather details by using the available tools",
            model=ollama_model, 
            tools=tools
        )
        
        agent_stream = agent.stream_async("What is the weather in New York?")
        async for event in agent_stream:
            # Track event loop lifecycle
            if event.get("init_event_loop", False):
                print("🔄 Event loop initialized")
            elif event.get("start_event_loop", False):
                print("▶️ Event loop cycle starting")
            elif event.get("start", False):
                print("📝 New cycle started")
            elif "message" in event:
                print(f"📬 New message created: {event['message']['role']}")
            elif event.get("complete", False):
                print("✅ Cycle completed")
            elif event.get("force_stop", False):
                print(
                    f"🛑 Event loop force-stopped: {event.get('force_stop_reason', 'unknown reason')}"
                )

asyncio.run(process_streaming_response())