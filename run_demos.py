"""Runner script to execute all demo files with shared environment setup."""

import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Add shared utils to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load environment variables
if (PROJECT_ROOT / ".env").exists():
    load_dotenv(PROJECT_ROOT / ".env")
    print(f"Loaded environment from {PROJECT_ROOT / '.env'}\n")

DEMOS_PATH = PROJECT_ROOT / "demos"


def get_demo_files():
    """Get all Python files from demos folder recursively."""
    py_files = sorted(DEMOS_PATH.rglob("*.py"))
    # Exclude main.py and any other utility files
    return [f for f in py_files if f.name != "main.py"]


def run_demo(file_path: Path, index: int, total: int):
    """Run a single demo file."""
    relative_path = file_path.relative_to(DEMOS_PATH)
    print(f"\n{'='*80}")
    print(f"[{index}/{total}] Running: {relative_path}")
    print(f"{'='*80}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(file_path)],
            capture_output=False,
            text=True,
            timeout=300  # 5 minute timeout per demo
        )
        
        if result.returncode == 0:
            print(f"✓ Completed: {relative_path}")
        else:
            print(f"✗ Failed with return code {result.returncode}: {relative_path}")
        
        return result.returncode == 0
    
    except subprocess.TimeoutExpired:
        print(f"✗ Timeout (5min exceeded): {relative_path}")
        return False
    except Exception as e:
        print(f"✗ Error running {relative_path}: {e}")
        return False


def main():
    """Run all demo files."""
    demo_files = get_demo_files()
    
    if not demo_files:
        print("No Python files found in demos folder!")
        return
    
    print(f"Found {len(demo_files)} demo files to run\n")
    
    results = {
        "passed": [],
        "failed": []
    }
    
    for idx, file_path in enumerate(demo_files, 1):
        success = run_demo(file_path, idx, len(demo_files))
        
        relative_path = file_path.relative_to(DEMOS_PATH)
        if success:
            results["passed"].append(str(relative_path))
        else:
            results["failed"].append(str(relative_path))
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Total: {len(demo_files)}")
    print(f"Passed: {len(results['passed'])}")
    print(f"Failed: {len(results['failed'])}")
    
    if results["failed"]:
        print(f"\nFailed demos:")
        for f in results["failed"]:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
