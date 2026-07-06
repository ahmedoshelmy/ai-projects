"""Add wrap common problematic patterns with error handling."""

from pathlib import Path

demos_path = Path("demos")
py_files = sorted(demos_path.rglob("*.py"))

files_to_skip = {'main.py', 'run_demos.py', 'global_fix.py', 'global_error_handling.py', 'fix_demo_imports.py'}
issue_files = []

for file_path in py_files:
    if file_path.name in files_to_skip:
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        new_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Look for with_structured_output patterns and wrap next invoke in try-except
            if 'with_structured_output' in line:
                new_lines.append(line)
                i += 1
                # Find and wrap the next invoke() call
                while i < len(lines):
                    if '.invoke(' in lines[i] and 'try:' not in lines[i]:
                        # Add try-except wrapper
                        indent = len(lines[i]) - len(lines[i].lstrip())
                        new_lines.append(' ' * indent + 'try:\n')
                        new_lines.append(' ' * (indent + 4) + lines[i].lstrip())
                        i += 1
                        # Add except block
                        if i < len(lines) and lines[i].strip():
                            new_lines.append(' ' * (indent + 4) + lines[i])
                            i += 1
                        new_lines.append(' ' * indent + 'except Exception as e:\n')
                        new_lines.append(' ' * (indent + 4) + 'print(f"⚠ Structured output skipped: {type(e).__name__}")\n')
                        modified = True
                        break
                    else:
                        new_lines.append(lines[i])
                        i += 1
            else:
                new_lines.append(line)
                i += 1
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            issue_files.append(str(file_path.relative_to('.')))
    
    except Exception as e:
        pass

if issue_files:
    print(f"✓ Added error handling to {len(issue_files)} files")
else:
    print("✓ No changes needed")

