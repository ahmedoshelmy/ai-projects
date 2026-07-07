from dotenv import load_dotenv
from importlib.metadata import version
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

load_dotenv()

core_version = version("langchain-core")
lg_version = version("langgraph")
from shared_utils import load_env_from_project, get_llm

load_env_from_project()

print(f"langchain-core version: {core_version}")
print(f"langgraph version: {lg_version}")


def main():

    # Test Groq
    llm = get_llm("groq")
    response = llm.invoke("Say 'setup complete!' in one word")
    print(f"Response from Groq: {response}")

    # Test Ollama cloud
    llm_ollama = get_llm("ollama")
    response_ollama = llm_ollama.invoke("Say 'setup complete!' in one word")
    print(f"Response from Ollama: {response_ollama}")

    print("Setup complete!")


if __name__ == "__main__":
    main()
