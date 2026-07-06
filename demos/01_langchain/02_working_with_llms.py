"""
Working with LLMs in LangChain V.1
Multiple providers, configuration, streaming, and cost optimization
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
import os
from shared_utils import load_env_from_project, get_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage

load_env_from_project()


def demo_groq_llm():
    """Demo using Groq LLM"""
    try:
        model = get_llm("groq")
        response = model.invoke("What is the capital of France? Answer in one word.")
        print(f"Response from Groq: {response.content}")
    except Exception as e:
        print(f"⚠ Groq demo skipped: {type(e).__name__}")
        print(f"  Note: Check available models at https://console.groq.com/docs/models")


def demo_ollama_llm():
    """Demo using Ollama cloud LLM"""
    try:
        model = get_llm("ollama")
        response = model.invoke("What is the capital of France? Answer in one word.")
        print(f"Response from Ollama Cloud: {response.content}")
    except Exception as e:
        print(f"⚠ Ollama demo skipped: {type(e).__name__}")


def demo_model_comparison():
    """Compare Groq and Ollama models"""
    prompt = "Explain recursion in one sentence."
    
    models = {
        "groq": ("Groq", get_llm("groq")),
        "ollama": ("Ollama", get_llm("ollama")),
    }

    print(f"Prompt: {prompt}\n")
    for model_key, (model_name, model) in models.items():
        try:
            response = model.invoke(prompt)
            print(f"Response from {model_name}: {response.content}\n")
        except Exception as e:
            print(f"⚠ {model_name} skipped: {type(e).__name__}\n")


def demo_message():
    """Demo using message objects"""
    try:
        model = get_llm("groq")
        
        # using message objects (more control over roles)
        messages = [
            SystemMessage(content="You are a pirate. Always answer like a pirate."),
            HumanMessage(content="What's the weather like today?"),
        ]

        response = model.invoke(messages)
        print(f"Response from the Pirate: {response.content}")

        # Multi-turn conversation using message objects
        messages.append(response)  # add model's response to the conversation
        messages.append(HumanMessage(content="What about tomorrow?"))

        print("\nMulti-turn conversation:")
        response = model.invoke(messages)
        print(f"Follow-up response from the Pirate: {response.content}")
    except Exception as e:
        print(f"⚠ Message demo skipped: {type(e).__name__}")


if __name__ == "__main__":
    print("=== Groq LLM Demo ===")
    demo_groq_llm()
    print("\n=== Model Comparison ===")
    demo_model_comparison()
    print("\n=== Message Objects Demo ===")
    demo_message()
