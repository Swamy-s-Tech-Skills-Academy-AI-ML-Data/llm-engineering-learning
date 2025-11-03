# Diagnostics Script - Setup and Testing

This directory contains diagnostic tools to verify your LLM Engineering Learning environment setup.

## Quick Start - Running Diagnostics

### Using run_diagnostics.py (Recommended)

Execute the notebook code path programmatically:

**From project root (recommended):**
```powershell
uv run python notebooks\01-setup\run_diagnostics.py
```

**Or from the 01-setup directory:**
```powershell
cd notebooks\01-setup
python run_diagnostics.py
```

This script uses the same path resolution logic as the notebook and is useful for automated execution.

---

## Files

- **`01_diagnostics.py`** - Main diagnostics script that checks system configuration, dependencies, network connectivity, and environment setup
- **`run_diagnostics.py`** - Python script that executes the notebook code path (recommended for programmatic execution)
- **`02_diagnostics.ipynb`** - Jupyter notebook interface for running diagnostics
- **`03_troubleshooting.ipynb`** - Comprehensive troubleshooting guide for Windows 11 + Python 3.12 setup

## Running the Diagnostics

This project uses **uv** for package management. All dependencies are defined in `pyproject.toml` at the project root.

### Method 1: Using uv (Recommended)

From the project root directory:

```powershell
# Ensure all dependencies are installed
uv sync

# Run the diagnostics script
uv run python notebooks\01-setup\01_diagnostics.py
```

### Method 2: With Activated Environment

If you're already in an activated environment:

```powershell
cd notebooks\01-setup
python 01_diagnostics.py
```

### Method 3: Using run_diagnostics.py (Notebook Code Path)

Execute the notebook's code path programmatically. This is the recommended method for programmatic execution.

**From project root (recommended):**
```powershell
uv run python notebooks\01-setup\run_diagnostics.py
```

**Or from the 01-setup directory:**
```powershell
cd notebooks\01-setup
python run_diagnostics.py
```

This script uses the same path resolution logic as the notebook and is useful for automated execution or CI/CD pipelines.

### Method 4: Via Jupyter Notebook

1. Open `02_diagnostics.ipynb` in your Jupyter environment
2. Run the cells to execute the diagnostics
3. The script will automatically find `01_diagnostics.py` and run all checks

**Note:** Make sure you've run `uv sync` from the project root before running the notebook to ensure all dependencies are installed.

## What the Diagnostics Check

The diagnostics script performs comprehensive checks including:

1. **System Information** - OS, RAM, disk space, processor
2. **File System** - Permissions, directory structure
3. **Git Repository** - Repository status, remote configuration
4. **Environment File** - `.env` file existence and API key configuration
5. **Python Environment** - Virtual environment, conda, Python version
6. **Dependencies** - Required packages (openai, python-dotenv, requests, etc.)
7. **Network Connectivity** - Internet connection, response times, bandwidth (optional)
8. **Environment Variables** - Python paths, API keys
9. **Additional Diagnostics** - Potential import conflicts, temp directory access

## Output

The script generates a detailed report saved to:
```
docs/reports/diagnostics-report-YYYYMMDD_HHMMSS.txt
```

This report contains all diagnostic information and can be shared for troubleshooting support.

## Troubleshooting

If you encounter issues:

1. **Missing Dependencies**: Run `uv sync` from the project root
2. **Import Errors**: Ensure you're using the correct Python environment
3. **Path Errors**: Make sure you're running from the project root directory
4. **Network Issues**: Check firewall/VPN settings if connectivity tests fail

For detailed troubleshooting guidance, see `03_troubleshooting.ipynb`.

