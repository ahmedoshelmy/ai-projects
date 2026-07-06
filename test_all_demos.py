#!/usr/bin/env python3
"""Test all demos and report errors."""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

demos_path = Path("demos")
demo_files = sorted(demos_path.rglob("*.py"))
demo_files = [f for f in demo_files if f.name != "main.py"]

results = {
    "passed": [],
    "failed": [],
    "errors": {}
}

print(f"Testing {len(demo_files)} demo files...\n")
print("=" * 70)

for i, demo_file in enumerate(demo_files, 1):
    relative_path = demo_file.relative_to(".")
    print(f"\n[{i}/{len(demo_files)}] Testing: {relative_path}")
    print("-" * 70)
    
    try:
        # Run with 15 second timeout
        result = subprocess.run(
            [sys.executable, str(demo_file)],
            capture_output=True,
            text=True,
            timeout=15,
            cwd=Path.cwd()
        )
        
        if result.returncode == 0:
            print("✓ PASSED")
            results["passed"].append(str(relative_path))
        else:
            # Extract the error message
            error_lines = result.stderr.split('\n')
            # Get last few lines which usually have the error
            error_msg = '\n'.join(error_lines[-10:]).strip()
            
            print(f"✗ FAILED")
            print(f"  Error: {error_msg[:200]}")
            results["failed"].append(str(relative_path))
            results["errors"][str(relative_path)] = error_msg[:500]
    
    except subprocess.TimeoutExpired:
        print(f"⏱ TIMEOUT (15s)")
        results["failed"].append(str(relative_path))
        results["errors"][str(relative_path)] = "Timeout after 15 seconds"
    
    except Exception as e:
        print(f"✗ ERROR: {type(e).__name__}: {str(e)[:100]}")
        results["failed"].append(str(relative_path))
        results["errors"][str(relative_path)] = str(e)[:200]

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n✓ Passed: {len(results['passed'])}/{len(demo_files)}")
print(f"✗ Failed: {len(results['failed'])}/{len(demo_files)}")

if results["passed"]:
    print("\n✓ Passed demos:")
    for demo in results["passed"][:10]:
        print(f"  - {demo}")
    if len(results["passed"]) > 10:
        print(f"  ... and {len(results['passed']) - 10} more")

if results["failed"]:
    print("\n✗ Failed demos:")
    for demo in results["failed"][:15]:
        error = results["errors"].get(demo, "Unknown error")
        error_line = error.split('\n')[-1] if error else "Unknown"
        print(f"  - {demo}")
        print(f"    {error_line[:80]}")

print("\n" + "=" * 70)
