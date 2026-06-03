from langchain_tavily import TavilySearch

search_jobs = TavilySearch(
    max_results=5,
    name="search_jobs",
    description="Search for job postings on the web. Use this to find job listings based on title, location, or company.",
)