# This lab is to teach you about creating your first agent

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import file_read, file_write

# Configure the Ollama model
# Other model providers can be configured as well:
# e.g. 
# Amazon Bedrock: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-bedrock/
# OpenAI: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/openai/
# Antrhopic: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/anthropic/
# LiteLLM: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/litellm/

ollama_model = OllamaModel(
    model_id="llama3.2:latest", # Make sure this is the model you downloaded from Ollama
    host="http://localhost:11434",
    params={
        "max_tokens": 2048,  # Adjust based on your model's capabilities
        "temperature": 0.7,  # Lower for more deterministic responses, higher for more creative
        "top_p": 0.9,        # Nucleus sampling parameter
        "stream": True,      # Enable streaming responses
    },
)



system_prompt = "You are a an agent which can read and write files to current directory"

# Create the agent with tools
local_agent = Agent(
    system_prompt=system_prompt, # Define a system Prompt
    model=ollama_model,
    tools=[file_read, file_write],  # Add your custom tools here
)


local_agent("can you create a test123.md file, with the content about current temperature?")
