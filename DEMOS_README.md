# Running Demos with Shared Virtual Environment

## Setup

The project uses a shared virtual environment (`.venv/`) in the project root.

### Install/Update Dependencies

```bash
# Using uv (faster)
uv pip install -e .

# Or using pip
.venv/Scripts/pip install -e .
```

### Configure Environment Variables

All keys are loaded from `.env` file in the project root. Make sure you have:
- `GROQ_API_KEY` - for Groq LLM
- `OLLAMA_API_KEY` - for Ollama LLM (if using)
- `HUGGING_FACE_API_KEY` - for HuggingFace embeddings

## Running Demos

### Run All Demos

```bash
# Activate venv first (Windows)
.venv\Scripts\activate

# Then run all demos
python run_demos.py
```

### Run Specific Demo

```bash
python demos/01_langchain/01_langchain_core_concepts.py
```

## Using Shared Utilities in Your Demos

In your demo files, you can use the shared utilities:

```python
from shared_utils import load_env_from_project, get_llm, get_embeddings

# Load environment variables
load_env_from_project()

# Get LLM (default: Groq)
llm = get_llm("groq")  # or "ollama"

# Get embeddings (HuggingFace API)
embeddings = get_embeddings()
```

## API Providers

### LLM Options
- **Groq** (default): Fast inference with various models (mixtral-8x7b-32768, etc.)
- **Ollama Cloud**: Cloud-hosted models (gpt-oss:120b-cloud, etc.) - requires OLLAMA_API_KEY

### Embeddings
- **HuggingFace**: Uses API key for inference, not local (BAAI/bge-small-en-v1.5)

## Project Structure

```
.
├── .venv/              # Shared virtual environment
├── .env                # Environment variables
├── shared_utils.py     # Shared utilities (LLM, embeddings, env loading)
├── run_demos.py        # Script to run all demos
├── demos/              # Demo files
│   ├── 01_langchain/
│   ├── 02_ingestion/
│   ├── 03_rag/
│   ├── 04_langgraph/
│   └── 05_multiagents/
└── ...
```
