from langchain.tools import tool
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field


class JobSearchInput(BaseModel):
    query: str = Field(description="Job title, skills, or keywords to search for")
    location: str = Field(default="", description="City or region to filter jobs by")


_tavily = TavilySearch(max_results=5)


@tool("search_jobs", args_schema=JobSearchInput)
def search_jobs(query: str, location: str = "") -> str:
    """Search for job postings on the web based on title, skills, and location."""
    search_query = f"{query} jobs {location}".strip()
    return _tavily.invoke(search_query)