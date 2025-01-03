import os
from logger import logger

from config import LANGSMITH_API_KEY, OPENAI_API_KEY


class BaseTest():
    logger = logger.getChild("BaseTest")

    # Set Langsmith environment variables
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = f"XAI_Jeongguan - TestLLM"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = LANGSMITH_API_KEY  # Update to your API key

    # Set OpenAI environment variables
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    if not openai_api_key:
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
