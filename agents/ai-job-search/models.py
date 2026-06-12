from pydantic import BaseModel, Field, model_validator


class JobPosting(BaseModel):
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    location: str = Field(description="Job location")
    url: str = Field(default="", description="Link to the job posting")
    summary: str = Field(description="Brief summary of the role and requirements")
    source_urls: list[str] = Field(default_factory=list, description="Source URLs where this job posting was found")


class JobSearchResponse(BaseModel):
    jobs: list[JobPosting] = Field(description="List of relevant job postings found")
    total_found: int = Field(default=0, description="Total number of job postings returned")

    @model_validator(mode="after")
    def set_total_found(self) -> "JobSearchResponse":
        self.total_found = len(self.jobs)
        return self
