import subprocess
import sys
from pathlib import Path

def run_all_scripts():
    # Get the directory of the main script
    main_dir = Path(__file__).parent
    
    # Find all .py files, excluding the main script itself
    scripts = sorted([
        f for f in main_dir.glob("*.py") 
        if f.name != "main.py"
    ])
    
    if not scripts:
        print("No Python files found.")
        return

    print(f"Found {len(scripts)} Python files to run.")
    
    for script in scripts:
        print(f"\nRunning: {script.name}")
        try:
            # Run the script using the current Python interpreter
            result = subprocess.run(
                [sys.executable, str(script)],
                capture_output=True,
                text=True,
                check=True  # Raise exception if return code is non-zero
            )
            print(f"Output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"Error running {script.name}: {e.stderr}")
            # Decide whether to stop on error or continue
            # break 

if __name__ == "__main__":
    run_all_scripts()   