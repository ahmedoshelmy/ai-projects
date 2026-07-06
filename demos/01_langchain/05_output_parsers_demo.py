import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from shared_utils import load_env_from_project, get_llm
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_env_from_project()

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_template("wire a short poem about {topic}")

llm = get_llm("ollama")

chain = prompt | llm | parser

response = chain.invoke({"topic": "nature"})

print(type(response))


# JsonOutputParser example
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template(
    "Return a JSON object with 'name' and 'age' for: {description}"
)

chain = prompt | llm | parser

result = chain.invoke({"description": "A 25-year-old developer named Alex"})
print(result)  # {'name': 'Alex', 'age': 25}

# PydanticOutputParser example
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    occupation: str = Field(description="The person's occupation")


parser = PydanticOutputParser(pydantic_object=Person)

prompt = ChatPromptTemplate.from_template(
    "Return a JSON object with 'name', 'age', and 'occupation' for: {description}"
).partial(format_instructions=parser.get_format_instructions())
chain = prompt | llm | parser
result = chain.invoke({"description": "A 30-year-old artist named Maria"})
print(result)  # Person(name='Maria', age=30, occupation='artist')


# Structured Output
class MovieReview(BaseModel):
    title: str = Field(description="The title of the movie")
    review: str = Field(description="A brief review of the movie")
    rating: int = Field(description="The rating of the movie out of 10")


# Bind the schema to the model
structured_model = llm.with_structured_output(MovieReview)

try:
    result = structured_model.invoke("Review: Inception is a mind-bending thriller. 9/10")
    print(result)  # MovieReview(title='Inception', review='A mind-bending thriller.', rating=9)
except Exception as e:
    print(f"⚠ Structured output demo skipped: {type(e).__name__}")
    print(f"  Note: Some models don't support structured output constraints")