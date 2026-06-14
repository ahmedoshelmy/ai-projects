from dotenv import load_dotenv, find_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama
import os

load_dotenv(find_dotenv())

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

# --- Config ---
LLM_MODEL = "devstral-small-2:24b-cloud"

# --- LLM (Ollama) ---
llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0,
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")}},
).bind_tools(tools)
