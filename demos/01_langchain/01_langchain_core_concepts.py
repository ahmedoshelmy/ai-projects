"""
LangChain Core Concepts - LCEL and Runnables
Uses Groq (cloud) or Ollama (local) instead of OpenAI/Anthropic
"""

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# Initialize LLM - use Ollama if available, else Groq
def get_llm(use_ollama=False):
    """Get LLM instance. Set use_ollama=True to use local Ollama."""
    if use_ollama:
        return ChatOllama(model="mistral", temperature=0.7)
    else:
        # Groq - requires GROQ_API_KEY in .env
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            print("⚠️  GROQ_API_KEY not found in .env")
            print("   Either:")
            print("   1. Add GROQ_API_KEY=your_key to .env (get free key at https://console.groq.com)")
            print("   2. Use get_llm(use_ollama=True) if Ollama is running")
            raise ValueError("GROQ_API_KEY not configured")
        # Use latest Groq model - update this if specific models are deprecated
        return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)


def demo_basic_chain():
    """Demonstrates a basic chain using LCEL and Runnables."""

    # Component 1: Define the prompt template using LCEL
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Answer in one sentence: {question}"
    )
    model = get_llm()
    parser = StrOutputParser()

    # Compose with pipe operator
    chain = prompt | model | parser

    # Execute the chain with an input
    result = chain.invoke({"question": "What is LangChain?"})
    print(f"Response: {result}")

    return chain


def demo_batch_exectution():
    """Demonstrate batch execution for multiple inputs."""
    prompt = ChatPromptTemplate.from_template("Translate to French: {text}")
    model = get_llm()
    parser = StrOutputParser()

    chain = prompt | model | parser

    # Batch - run with multiple inputs
    inputs = [
        {"text": "Hello, how are you?"},
        {"text": "What is your name?"},
        {"text": "Where is the nearest restaurant?"},
    ]
    results = chain.batch(inputs)

    for text in zip(inputs, results):
        print(f"Input: {text[0]['text']} => Output: {text[1]}")


def demo_streaming():
    """Demonstrate streaming for real-time output."""
    prompt = ChatPromptTemplate.from_template("Write a haiku about: {topic}")
    model = get_llm()
    parser = StrOutputParser()

    chain = prompt | model | parser

    # Streaming - run with streaming enabled
    print("Streaming output: ")
    for chunk in chain.stream({"topic": "nature"}):
        print(chunk, end="", flush=True)
    print()  # for newline after streaming


def demo_schema_inspection():
    """Demonstrate input/output schema inspection."""
    prompt = ChatPromptTemplate.from_template("Summarize the following text: {text}")
    model = get_llm()
    parser = StrOutputParser()

    chain = prompt | model | parser

    # Inspect input and output schemas
    input_schema = chain.input_schema.model_json_schema()
    output_schema = chain.output_schema.model_json_schema()

    print(f"Input Schema: {input_schema}")
    print(f"Output Schema: {output_schema}")


# ------- Exercise the demos -------#
# Exercise: Build your first chain
def exercise_first_chain():
    """
    EXERCISE: Create a chain that:
    1. Takes a product name and target audience
    2. Generates a marketing tagline
    3. Returns just the tagline as a string

    Test with: product="AI Course", audience="developers"
    """

    # YOUR CODE HERE
    prompt = ChatPromptTemplate.from_template(
        "Create a marketing tagline for a product named '{product}' targeting '{audience}'."
    )
    model = get_llm()
    parser = StrOutputParser()

    chain = prompt | model | parser

    # Test the chain
    result = chain.invoke({"product": "AI Course", "audience": "developers"})
    print(f"Marketing Tagline: {result}")


def new_way():
    # Using the helper
    model = get_llm()

    # Or use provider-specific directly

    from langchain_groq import ChatGroq
    from langchain_ollama import ChatOllama

    groq_model = ChatGroq(model="llama-3.3-70b-versatile",
                          temperature=0.7,
                          max_tokens=1500,
                          timeout=30,
                          max_retries=3)
    
    ollama_model = ChatOllama(model="mistral", temperature=0.7)


if __name__ == "__main__":
    demo_basic_chain()
    demo_batch_exectution()
    demo_streaming()
    demo_schema_inspection()
    exercise_first_chain()
