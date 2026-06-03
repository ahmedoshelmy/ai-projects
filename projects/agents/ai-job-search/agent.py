from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from llm import llm
from tools import search_jobs

agent = create_agent(model=llm, tools=[search_jobs])