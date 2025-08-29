# Example Use-case for custom-tools
# Here we create a RecipeBot that recommends recipes and answers any cooking related questions.
# https://catalog.workshops.aws/strands-agents/en-US/01-fundamentals/11-quickstart
# https://static.us-east-1.prod.workshops.aws/public/765d51e8-8a6d-4ac6-a6e5-c2d4a79c74ac/static/images/interactive_recipe_agent.png

from strands import Agent, tool
from ddgs import DDGS
from ddgs.exceptions import RatelimitException
import logging
from strands.models.ollama import OllamaModel

# Configure logging
logging.getLogger("strands").setLevel(logging.INFO)

# Define a websearch tool
@tool
def websearch(keywords: str, region: str = "us-en", max_results: int | None = None) -> str:
    """Search the web to get updated information.
    Args:
        keywords (str): The search query keywords.
        region (str): The search region: wt-wt, us-en, uk-en, ru-ru, etc..
        max_results (int | None): The maximum number of results to return.
    Returns:
        List of dictionaries with search results.
    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except Exception as e:
        return f"Exception: {e}"


ollama_model = OllamaModel(
  model_id="gpt-oss:20b",
  host="http://localhost:11434"

)

# Create a recipe assistant agent
recipe_agent = Agent(
    model=ollama_model,
    system_prompt="""You are RecipeBot, a helpful cooking assistant.
    Help users find recipes based on ingredients and answer cooking questions.
    Use the websearch tool to find recipes when users mention ingredients or to look up cooking information.""",
    tools=[websearch], # Import the websearch tool we created above
)

response = recipe_agent("Suggest a recipe with chicken and broccoli.")

print(f"Metrics : {response.metrics}") # Optional, but recommended.