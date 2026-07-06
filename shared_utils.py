"""Shared utilities for AI demos - LLM, embeddings, and environment configuration."""

import os
import sys
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


def safe_print(*args, **kwargs):
    """Print that safely handles Unicode encoding issues on Windows."""
    try:
        print(*args, **kwargs)
    except UnicodeEncodeError:
        # Encode with error handling for Windows terminal
        output = " ".join(str(arg) for arg in args)
        print(output.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


def load_env_from_project(project_root: Optional[Path] = None) -> None:
    """Load environment variables from .env file in project root or ai-projects root.
    
    Args:
        project_root: Path to project root. If None, searches for ai-projects root.
    """
    if project_root is None:
        # Search for ai-projects directory
        current = Path.cwd()
        while current != current.parent:
            if (current / ".env").exists() and (current / "pyproject.toml").exists():
                project_root = current
                break
            current = current.parent
        
        # Fallback to ai-projects if found
        if project_root is None:
            ai_projects = Path("c:/code/Personal/ai-projects")
            if ai_projects.exists():
                project_root = ai_projects
    
    if project_root and (project_root / ".env").exists():
        load_dotenv(project_root / ".env")


def get_groq_llm(model: str = "llama-3.3-70b-versatile"):
    """Get a Groq LLM instance with fallback to working models.
    
    Args:
        model: Model name (default: "llama-3.3-70b-versatile")
               Note: Groq frequently deprecates models. If a model fails, the calling code
               should catch the exception and use ollama as fallback.
    
    Returns:
        ChatGroq instance
        
    Raises:
        ValueError: If GROQ_API_KEY not in environment
        BadRequestError: If model is deprecated (fallback to ollama in calling code)
    """
    from langchain_groq import ChatGroq
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment")
    
    return ChatGroq(
        model=model,
        api_key=api_key,
        temperature=0.7
    )


def get_ollama_llm(model: str = "gpt-oss:120b-cloud"):
    """Get an Ollama cloud LLM instance.
    
    Args:
        model: Model name (default: gpt-oss:120b-cloud). Use cloud models (e.g., "gpt-oss:120b-cloud")
    
    Returns:
        ChatOllama instance
    """
    from langchain_ollama import ChatOllama
    
    api_key = os.getenv("OLLAMA_API_KEY")
    if not api_key:
        raise ValueError("OLLAMA_API_KEY not found in environment")
    
    return ChatOllama(
        model=model,
        base_url="https://ollama.com",
        client_kwargs={"headers": {"Authorization": f"Bearer {api_key}"}},
        temperature=0.7
    )


def get_llm(provider: str = "ollama", model: Optional[str] = None):
    """Get an LLM instance from Groq or Ollama cloud.
    
    Args:
        provider: "groq" or "ollama" (default: "ollama" - more reliable)
        model: Optional model name. Uses defaults if not specified.
               - Groq: "llama-3.3-70b-versatile" (check https://console.groq.com/docs/models for current)
               - Ollama: "gpt-oss:120b-cloud" (most reliable)
    
    Returns:
        LLM instance (ChatGroq or ChatOllama)
    """
    if provider.lower() == "groq":
        # Note: Groq deprecates models frequently. Check console.groq.com for current models
        return get_groq_llm(model or "llama-3.3-70b-versatile")
    elif provider.lower() == "ollama":
        return get_ollama_llm(model or "gpt-oss:120b-cloud")
    else:
        raise ValueError(f"Unknown LLM provider: {provider}")


def get_huggingface_embeddings(model: str = "BAAI/bge-small-en-v1.5"):
    """Get HuggingFace embeddings instance using API.
    
    Args:
        model: Model name from HuggingFace hub
    
    Returns:
        HuggingFaceInferenceAPIEmbeddings instance
    """
    from langchain_huggingface import HuggingFaceInferenceAPIEmbeddings
    
    api_key = os.getenv("HUGGING_FACE_API_KEY")
    if not api_key:
        raise ValueError("HUGGING_FACE_API_KEY not found in environment")
    
    return HuggingFaceInferenceAPIEmbeddings(
        api_key=api_key,
        model_name=model
    )


def get_embeddings(model: str = "BAAI/bge-small-en-v1.5"):
    """Get embeddings instance (using HuggingFace API).
    
    Args:
        model: Model name from HuggingFace hub
    
    Returns:
        HuggingFaceInferenceAPIEmbeddings instance
    """
    return get_huggingface_embeddings(model)


# Example usage patterns
if __name__ == "__main__":
    load_env_from_project()
    
    # Test Groq LLM
    print("Testing Groq LLM...")
    llm = get_llm("groq")
    print(f"LLM: {llm}")
    
    # Test embeddings
    print("\nTesting HuggingFace Embeddings...")
    embeddings = get_embeddings()
    print(f"Embeddings: {embeddings}")
