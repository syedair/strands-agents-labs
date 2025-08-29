# Strands Agents Labs

A comprehensive collection of hands-on labs for learning AWS Strands Agents framework. This repository contains practical examples demonstrating agent creation, tool integration, and advanced features like Model Context Protocol (MCP) implementations.

For understand more, please refer to [Strands Agents SDK](https://strandsagents.com/latest/)

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.ai/) installed and running
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Installation

1. Clone this repository:
```bash
git clone https://github.com/syedair/strands-agents-labs.git
cd strands-agents-labs
```

2. Install dependencies:
```bash
uv sync
```

3. If you would like to run model locally, ensure Ollama is running with required models:
```bash
ollama pull llama3.2:latest
ollama pull gpt-oss:20b
```

Note:
For other model providers, you can find information here:
[Amazon Bedrock](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-bedrock/)
[OpenAI](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/openai/)
[Anthropic](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/anthropic/)



## 📚 Lab Overview

### Lab 1: Getting Started
**File:** `labs/lab1.py`

Learn the fundamentals of creating your first Strands agent with basic file operations.

**Features:**
- Agent initialization with Ollama model
- File read/write tools integration
- Basic system prompt configuration

**Run:**
```bash
uv run labs/lab1.py
```

### Lab 2: HTTP Tools Integration
**File:** `labs/lab2.py`

Explore HTTP request capabilities for external API integration.

**Features:**
- National Weather Service API integration
- HTTP request tool usage
- Weather data processing

**Run:**
```bash
uv run labs/lab2.py
```

### Lab 3: Logging and Debugging
**File:** `labs/lab3.py`

Master logging configuration for better debugging and monitoring.

**Features:**
- Strands logger configuration
- Debug output formatting
- Error tracking and analysis

**Run:**
```bash
uv run labs/lab3.py
```

### Lab 4: Custom Tools Development
**Files:** `labs/lab4a.py`, `labs/lab4b.py`

Create custom tools and build specialized agents.

**Lab 4a - Basic Custom Tool:**
- Simple word count tool creation
- Tool decorator usage
- Function-to-tool conversion

**Lab 4b - RecipeBot Agent:**
- Web search integration with DuckDuckGo
- Recipe recommendation system
- Advanced tool composition

**Run:**
```bash
uv run labs/lab4a.py
uv run labs/lab4b.py
```

### Lab 5: Model Context Protocol (MCP) - STDIO
**File:** `labs/lab5.py`

Integrate MCP servers using STDIO transport for enhanced capabilities.

**Features:**
- AWS Documentation MCP server integration
- STDIO client configuration
- Cross-platform compatibility

**Run:**
```bash
uv run labs/lab5.py
```

### Lab 6: MCP Streamable HTTP
**File:** `labs/lab6.py`

Implement MCP using HTTP streamable transport for better performance.

**Features:**
- HTTP-based MCP communication
- Weather service integration
- Streamable transport protocol

**Prerequisites:**
Start the MCP server in a separate terminal:
```bash
python mcp-streamable-http/python-example/server/weather.py
```

**Run:**
```bash
uv run labs/lab6.py
```

### Lab 7: Async Streaming with MCP
**File:** `labs/lab7.py`

Advanced asynchronous processing with streaming responses.

**Features:**
- Asynchronous iterators
- Real-time streaming responses
- Event loop lifecycle management
- Advanced error handling

**Prerequisites:**
Ensure the MCP server is running:
```bash
uv run mcp-streamable-http/python-example/server/weather.py
```

**Run:**
```bash
uv run labs/lab7.py
```

## 🛡️ Security Considerations

This repository has been reviewed for security vulnerabilities:

- ✅ No hardcoded API keys or secrets
- ✅ Environment variables used for sensitive data
- ✅ Proper error handling for external APIs
- ✅ Input validation where applicable
- ⚠️ Development-focused (localhost URLs used)

## 📖 Resources

- [AWS Strands Agents Workshop](https://catalog.workshops.aws/strands-agents/en-US)
- [Strands Agents Documentation](https://strandsagents.com/latest/)
- [Sample Implementations](https://github.com/strands-agents/samples/tree/main/02-samples/05-personal-assistant)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**Ollama Connection Errors:**
- Ensure Ollama is running: `ollama serve`
- Check model availability: `ollama list`
- Verify model names match those in the lab files

**MCP Server Connection Issues:**
- Confirm server is running on correct port
- Check firewall settings for localhost connections
- Verify uvx installation for MCP servers

**Import Errors:**
- Ensure all dependencies are installed: `uv sync`
- Check Python version compatibility (3.13+)
- Verify virtual environment activation

### Getting Help

If you encounter issues:
1. Check the troubleshooting section above
2. Review the official documentation links
3. Open an issue in this repository with detailed error information
