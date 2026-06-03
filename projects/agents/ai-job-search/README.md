## Job Search Agent 

Use Case:

Search for job postings for a certain position 

First I ran uv init 

Then uv add langchain langchain-groq langchain-tavily tavily-python python-dotenv black isort 

Tavily is used here to connect our agent to the web 

To create agent we import the function create_agent from langchain 

An agent needs 2 things (llm + tools )

To create a tool we define it using @tool 

It's important to make a clear documentation for the comments 

