"""
Section 1 Project: Smart Q&A Bot
A production-ready question-answering bot with structured output
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from langchain_core.prompts import ChatPromptTemplate
from shared_utils import load_env_from_project, get_llm, safe_print
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
from langsmith import traceable, Client
import os

load_env_from_project()

# -- LangSmith Configuration --
if os.getenv("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ.setdefault("LANGSMITH_PROJECT", "Smart Q&A Bot Project")
    safe_print(f"LangSmith is configured. - Project: {os.getenv('LANGSMITH_PROJECT')}")


# Schema Definition
class QAResponse(BaseModel):
    answer: str = Field(description="The answer to the user's question.")
    confidence: str = Field(description="Confidence level: high, medium, or low")
    reasoning: str = Field(description="The reasoning behind the answer provided.")
    follow_up_questions: List[str] = Field(
        description="A list of follow-up questions related to the topic.",
        default_factory=list,
    )
    sources_needed: bool = Field(
        description="Indicates whether sources are needed for the answer.",
        default=False,
    )

    # Bot implementation


class SmartQABot:
    def __init__(
        self,
        temperature: float = 0.3,
    ):
        self.model = get_llm("ollama").with_structured_output(QAResponse)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a knowledgeable Q&A assistant.

Your guidelines:
- Answer questions accurately and concisely
- Be honest about uncertainty - set confidence to 'low' if unsure
- Provide clear reasoning for your answers
- Suggest relevant follow-up questions
- Indicate if external sources would help

Always respond with accurate, helpful information.""",
                ),
                ("human", "{question}"),
            ]
        )
        self.chain = self.prompt | self.model

    @traceable(name="ask_question", run_type="chain")
    def ask(self, question: str) -> QAResponse:
        try:
            response = self.chain.invoke({"question": question})
            return response
        except Exception as e:
            # return a greaceful error response
            return QAResponse(
                answer="I'm sorry, I couldn't process your question at this time.",
                confidence="low",
                reasoning=str(e),
                follow_up_questions=["Could you please try again later?"],
                sources_needed=True,
            )

    @traceable(name="ask_batch", run_type="chain")
    def ask_batch(self, questions: List[str]) -> List[QAResponse]:
        """Ask multiple questions in parallel."""
        try:
            inputs = [{"question": q} for q in questions]
            return self.chain.batch(inputs)
        except Exception as e:
            print(f"⚠ Batch processing failed: {type(e).__name__}")
            return [
                QAResponse(
                    answer="Batch processing error",
                    confidence="low",
                    reasoning=str(e),
                    follow_up_questions=[],
                    sources_needed=True,
                ) for _ in questions
            ]


# Demo Usage
def demo_qa_bot():
    bot = SmartQABot()

    questions = [
        "What is the capital of France?",
        "Explain the theory of relativity.",
        "How does photosynthesis work?",
    ]

    safe_print("=" * 60)
    safe_print("SMART Q&A BOT DEMO")
    safe_print("=" * 60)

    for question in questions:

        safe_print(f"\n Question: {question}")
        safe_print("-" * 40)

        response = bot.ask(question)

        safe_print(f"Question: {question}")
        safe_print(f"Answer: {response.answer}")
        safe_print(f"Confidence: {response.confidence}")
        safe_print(f"Reasoning: {response.reasoning}")
        safe_print(f"Follow-up Questions: {response.follow_up_questions}")
        safe_print(f"Sources Needed: {response.sources_needed}")
        safe_print("-" * 60)


@traceable(name="error_handling_demo", run_type="chain")
def demo_error_handling():
    """Demonstrate error handling."""

    bot = SmartQABot()

    safe_print("\n" + "=" * 60)
    safe_print("ERROR HANDLING DEMO")
    safe_print("=" * 60)

    # Test with a very long question (edge case)
    long_question = "What is " + "very " * 100 + "important?"

    response = bot.ask(long_question)
    safe_print(f"Handled gracefully: {response.confidence}")


@traceable(name="batch_demo", run_type="chain")
def demo_batch_processing():
    """Demonstrate batch processing."""

    bot = SmartQABot()

    questions = [
        "What is Python?",
        "What is JavaScript?",
        "What is Rust?",
    ]

    safe_print("\n" + "=" * 60)
    safe_print("BATCH PROCESSING DEMO")
    safe_print("=" * 60)

    responses = bot.ask_batch(questions)

    for q, r in zip(questions, responses):
        print(f"\n{q}")
        print(f"  -> {r.answer[:100]}...")
        print(f"  Confidence: {r.confidence}")


if __name__ == "__main__":

    try:
        demo_qa_bot()
        demo_batch_processing()
        demo_error_handling()

        print("\n" + "=" * 60)
        print("Section 1 Complete!")
        print("=" * 60)
        print(
            """
What you learned:
- LangChain ecosystem overview
- Environment setup with uv
- Core concepts: Runnables, LCEL, pipe operator
- Working with multiple LLM providers
- Prompt templates and message types
- Output parsers and structured output
- Building a production Q&A bot
- LangSmith tracing with @traceable decorator

Next: Section 2 - Chains, RAG & Memory
        """
        )
    finally:
        pass
    # uncomment the line below to flush traces to LangSmith, but you'll alse see an error at the end of a run, which is not harmful at all, but annoying!
    # Client().flush()  # Ensure all traces are sent to LangSmith
