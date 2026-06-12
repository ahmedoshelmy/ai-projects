from agent import agent
from langchain_core.messages import HumanMessage


def main():
    query = "Find me some software engineering jobs in San Francisco."
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    response = result["structured_response"]
    print(f"Found {response.total_found} job(s):\n")
    for job in response.jobs:
        print(f"  {job.title} @ {job.company} — {job.location}")
        if job.url:
            print(f"  URL: {job.url}")
        print(f"  {job.summary}\n")


if __name__ == "__main__":
    main()
