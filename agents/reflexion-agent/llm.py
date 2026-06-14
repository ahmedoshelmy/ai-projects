from langchain_ollama import ChatOllama
import os
# --- Config ---
LLM_MODEL = "minimax-m3:cloud"

# --- LLM (Ollama) ---
llm = ChatOllama(
    model=LLM_MODEL,
    temperature=0,
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")}},
)
