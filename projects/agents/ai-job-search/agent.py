from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent 
from llm import llm
from tools import search_jobs
from langchain_core.messages import HumanMessage, SystemMessage


agent = create_agent(model=llm, tools=[search_jobs], verbose=True)

result = agent.invoke({"messages": HumanMessage(content="Find me some software engineering jobs in San Francisco.")})
print(result)