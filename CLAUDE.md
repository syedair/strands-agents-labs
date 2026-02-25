# Strands Agents Labs

A hands-on lab collection for learning the [AWS Strands Agents framework](https://strandsagents.com/latest/).

## Project Setup

- **Language:** Python 3.13+
- **Package Manager:** [uv](https://docs.astral.sh/uv/)

Install dependencies:
```bash
uv sync
```

## Running Labs

All labs are run with `uv run`:
```bash
uv run labs/lab1.py   # Getting Started
uv run labs/lab2.py   # HTTP Tools
uv run labs/lab3.py   # Logging & Debugging
uv run labs/lab4a.py  # Custom Tools - Word Count
uv run labs/lab4b.py  # Custom Tools - RecipeBot
uv run labs/lab5.py   # MCP STDIO
uv run labs/lab6.py   # MCP Streamable HTTP
uv run labs/lab7.py   # Async Streaming with MCP
```

Labs 6 and 7 require the MCP server running first:
```bash
uv run mcp-streamable-http/python-example/server/weather.py
```

## Linting

```bash
ruff check labs/
```

## Dependencies

Key packages (see `pyproject.toml`):
- `strands-agents` — core agent framework
- `strands-agents-tools` — built-in tools (file_read, file_write, http_request, etc.)
- `fastapi` + `uvicorn` — HTTP server for MCP labs
- `ddgs` — DuckDuckGo search for lab4b

## Prerequisites

- [Ollama](https://ollama.ai/) running locally for model inference:
  ```bash
  ollama pull llama3.2:latest
  ollama serve
  ```
- Alternatively configure Amazon Bedrock, OpenAI, Anthropic, or LiteLLM as the model provider.
