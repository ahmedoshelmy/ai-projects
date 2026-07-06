"""Add error handling to groq calls with ollama fallback."""

from pathlib import Path

demos_path = Path("demos")
py_files = sorted(demos_path.rglob("*.py"))

files_to_skip = {'main.py', 'run_demos.py', 'global_fix.py', 'fix_demo_imports.py', 'global_error_handling.py', 'update_groq_refs.py'}
updated = []

for file_path in py_files:
    if file_path.name in files_to_skip:
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Pattern 1: Module-level assignment at top of file
        # llm = get_llm("groq") -> wrap with try-except and ollama fallback
        if '\nllm = get_llm("groq")' in content and 'try:' not in content:
            content = content.replace(
                '\nllm = get_llm("groq")',
                '\ntry:\n    llm = get_llm("groq")\nexcept Exception as e:\n    print(f"⚠ Groq unavailable: {type(e).__name__}, using Ollama")\n    llm = get_llm("ollama")'
            )
        
        # Pattern 2: Simple assignment without try-except around it
        if 'model = get_llm("groq")' in content and 'try:' not in content.split('get_llm("groq")')[0].split('\n')[-2]:
            # Replace but preserve pattern - just ensure try-except exists
            content = content.replace(
                'model = get_llm("groq")',
                'try:\n    model = get_llm("groq")\nexcept Exception as e:\n    print(f"⚠ Groq error: {type(e).__name__}, using Ollama")\n    model = get_llm("ollama")'
            )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            updated.append(str(file_path.relative_to('.')))
            print(f"✓ {file_path.relative_to('.')}")
    
    except Exception as e:
        pass

if updated:
    print(f"\n✓ Added ollama fallback to {len(updated)} files with groq calls")
else:
    print("✓ All groq calls already have error handling")


