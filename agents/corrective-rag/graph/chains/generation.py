from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from graph.llm import llm

prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()