# This lab is to teach you about http_request tool

from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import file_read, file_write, http_request

# Configure the Ollama model
ollama_model = OllamaModel(
    model_id="gpt-oss:20b", # Make sure this is the model you downloaded from Ollama
    host="http://localhost:11434",
    params={
        "max_tokens": 2048,  # Adjust based on your model's capabilities
        "temperature": 0.7,  # Lower for more deterministic responses, higher for more creative
        "top_p": 0.9,        # Nucleus sampling parameter
        "stream": True,      # Enable streaming responses
    },
)


system_prompt = """
Weather Information
    - You can also make HTTP requests to the National Weather Service API.
    - Process and display weather forecast data for locations in the United States.
"""

# - When retrieving weather information, first get coordinates using https://api.weather.gov/points/{latitude},{longitude},  or
#         https://api.weather.gov/points/{zipcode}, then use the returned forecast URL. You can make additional http requests as well.

# Create the agent with tools
local_agent = Agent(
    system_prompt=system_prompt, # Define a system Prompt
    model=ollama_model,
    tools=[http_request],  # Add your custom tools here
)


local_agent("what is the weather in new york?")
