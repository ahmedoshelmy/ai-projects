"""Script to fix all remaining demo files - multiagent and production_llms"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# List of all files to update
files_to_update = [
    "demos/05_multiagents/01_tool_calling_agent.py",
    "demos/05_multiagents/02_supervisor_agent.py",
    "demos/05_multiagents/agent_communication.py",
    "demos/05_multiagents/hierarchical_agents.py",
    "demos/05_multiagents/multi_agent_research_system.py",
    "demos/05_multiagents/parallel_agents.py",
    "demos/06_production_llms/testing_patterns.py",
    "demos/06_production_llms/security_patterns.py",
    "demos/06_production_llms/monitoring.py",
    "demos/06_production_llms/error_handling.py",
    "demos/06_production_llms/cost_optimization.py",
]

replacements = [
    (
        "from langchain_openai import ChatOpenAI",
        "import sys\nfrom pathlib import Path\nsys.path.insert(0, str(Path(__file__).parent.parent.parent))\n\nfrom shared_utils import load_env_from_project, get_llm",
    ),
    (
        "from langchain_openai import ChatOpenAI, OpenAIEmbeddings",
        "import sys\nfrom pathlib import Path\nsys.path.insert(0, str(Path(__file__).parent.parent.parent))\n\nfrom shared_utils import load_env_from_project, get_llm, get_embeddings",
    ),
    ("load_dotenv()", "load_env_from_project()"),
    ("ChatOpenAI(", "get_llm(\"groq\", "),
    (
        "OpenAIEmbeddings(",
        'get_embeddings(',
    ),
]

def process_file(file_path):
    """Process a single file"""
    full_path = Path(__file__).parent / file_path
    
    if not full_path.exists():
        print(f"⚠ File not found: {full_path}")
        return False
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
    
    if content != original_content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Updated: {file_path}")
        return True
    else:
        print(f"- No changes needed: {file_path}")
        return False

if __name__ == "__main__":
    print("Fixing demo file imports...\n")
    
    updated = 0
    for file in files_to_update:
        if process_file(file):
            updated += 1
    
    print(f"\n{updated}/{len(files_to_update)} files updated")
