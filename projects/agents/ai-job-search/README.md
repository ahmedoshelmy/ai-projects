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

What Langchain does when u define a tool is that it defines a ToolMEssage and u can see when accessing the messages in the result 

Behind the scenes, langraph will be executing the agent 

Structured Output allows agents to return data in a specific, predictable format. 
It has 2 strategies 
1- Tool Strategy
2- Provider Strategy 

Langchain by default uses 2 

Most models have the option to define the output whether pydantic or typedict 

Tool calling we force the llm to always use the tool 
