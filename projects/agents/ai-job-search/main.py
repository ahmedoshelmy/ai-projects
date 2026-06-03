from agent import agent
from langchain_core.messages import HumanMessage


def main():
    query = "Find me some software engineering jobs in San Francisco."
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    print(result)
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
