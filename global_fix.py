"""Global fix script for all demo files."""

from pathlib import Path

demos_path = Path("demos")
py_files = sorted(demos_path.rglob("*.py"))

print(f"Found {len(py_files)} Python files in demos/\n")

files_to_skip = {'main.py', 'run_demos.py', 'global_fix.py', 'fix_demo_imports.py'}
fixed_files = []

for file_path in py_files:
    if file_path.name in files_to_skip:
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove unused imports
        content = content.replace('from langchain.chat_models import init_chat_model\n', '')
        content = content.replace('from langchain.chat_models import init_chat_model', '')
        
        # Replace init_chat_model calls
        # Pattern: init_chat_model(...) -> get_llm("ollama")
        import re
        content = re.sub(r'init_chat_model\s*\([^)]*\)', 'get_llm("ollama")', content)
        
        # Replace ChatOpenAI calls  
        # Pattern: ChatOpenAI(...) -> get_llm("ollama")
        content = re.sub(r'ChatOpenAI\s*\([^)]*\)', 'get_llm("ollama")', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed_files.append(str(file_path.relative_to('.')))
            print(f"✓ {file_path.relative_to('.')}")
    
    except Exception as e:
        print(f"✗ {file_path.relative_to('.')}: {e}")

print(f"\n✓ Fixed {len(fixed_files)} files")

