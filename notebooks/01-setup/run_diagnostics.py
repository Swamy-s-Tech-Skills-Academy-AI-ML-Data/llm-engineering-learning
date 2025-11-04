"""
Run Diagnostics Script

This script executes the diagnostics notebook code programmatically.
It performs the same operations as the Jupyter notebook 02_diagnostics.ipynb.

Usage Examples:

    # From project root (recommended)
    uv run python notebooks\01-setup\run_diagnostics.py

    # Or from the 01-setup directory
    cd notebooks\01-setup
    python run_diagnostics.py

    # Or if environment is already activated
    cd notebooks\01-setup
    python run_diagnostics.py
"""

from __future__ import absolute_import
import sys
import os
from pathlib import Path

# Note: If using uv, ensure dependencies are installed via 'uv sync' from project root
# Required packages: requests, speedtest-cli, psutil, setuptools (all in pyproject.toml)
# If packages are missing, run from project root: uv sync

def find_diagnostics_script():
    """
    Find the 01_diagnostics.py file using multiple path resolution strategies.
    
    Returns:
        Path: Path to the directory containing 01_diagnostics.py
        
    Raises:
        FileNotFoundError: If 01_diagnostics.py cannot be found
    """
    current_dir = Path.cwd()
    
    # Try multiple approaches to find the correct path
    possible_paths = [
        current_dir / "notebooks" / "01-setup",  # If launched from project root
        current_dir,  # If launched from notebooks/01-setup directory
        Path(__file__).parent if '__file__' in globals() else None,  # Script's directory
    ]

    script_dir = None
    for path in possible_paths:
        if path and (path / "01_diagnostics.py").exists():
            script_dir = path
            break

    if script_dir is None:
        # Fallback: try to find the file by searching from current directory
        for root, dirs, files in os.walk(current_dir):
            if "01_diagnostics.py" in files:
                script_dir = Path(root)
                break

    if script_dir is None:
        raise FileNotFoundError(
            "Could not find 01_diagnostics.py. "
            "Please make sure you're running this script from the project directory."
        )
    
    return script_dir


def main():
    """Main execution function to run diagnostics."""
    print("=" * 60)
    print("Running Diagnostics via Notebook Code Path")
    print("=" * 60)
    print()
    
    # Find the diagnostics script
    try:
        script_dir = find_diagnostics_script()
        print(f"Found diagnostics script in: {script_dir}")
        print()
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Add the script directory to Python path to import the diagnostics module
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))

    # Import from the actual filename: 01_diagnostics.py
    try:
        import importlib.util
        diagnostics_file = script_dir / "01_diagnostics.py"
        spec = importlib.util.spec_from_file_location("diagnostics_module", str(diagnostics_file))
        diagnostics_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(diagnostics_module)
        
        # Run the diagnostics
        diagnostics_module.Diagnostics().run()
        
    except Exception as e:
        print(f"ERROR: Failed to run diagnostics: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

