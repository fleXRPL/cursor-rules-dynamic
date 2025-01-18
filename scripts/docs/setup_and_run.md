# Setup and Run Script Documentation

## Overview

The `setup_and_run.sh` script is a bash wrapper that manages the Python virtual environment and dependencies for the `standardize_rules.py` script. It ensures all necessary dependencies are installed and the script runs in an isolated environment.

## Features

- 🌟 Automatic virtual environment creation and management
- 📦 Dependency installation via requirements.txt
- 🔄 Environment cleanup after execution
- 🎨 Colorized output for better visibility

## Prerequisites

- Python 3.x installed
- Bash shell environment
- Write permissions in the script directory

## Usage

```bash
bash scripts/setup_and_run.sh
```

## Script Flow

1. **Environment Setup**
   - Creates a virtual environment in `.venv` if it doesn't exist
   - Creates `requirements.txt` if it doesn't exist with required packages:
     - pathlib
     - python-dateutil

2. **Dependency Management**
   - Activates the virtual environment
   - Installs all required packages from requirements.txt

3. **Script Execution**
   - Runs standardize_rules.py in the virtual environment
   - Handles any script output or errors

4. **Cleanup**
   - Deactivates the virtual environment
   - Provides execution status

## Output Colors

- 🟡 Yellow: Setup and processing steps
- 🟢 Green: Success messages and completion
- 🔵 Blue: Cleanup operations

## Directory Structure

```bash
scripts/
├── setup_and_run.sh
├── standardize_rules.py
├── requirements.txt
└── docs/
    └── setup_and_run.md
```

## Error Handling

- Exits on any error (set -e)
- Provides clear error messages
- Ensures virtual environment is properly deactivated

## Maintenance

The script is designed to be maintainable and extensible:

- Add new dependencies to `requirements.txt`
- Modify virtual environment location via `VENV_DIR`
- Customize output colors and messages

## Related Documentation

- [standardize_rules.md](standardize_rules.md) - Documentation for the main Python script
- [ci.md](ci.md) - Continuous Integration documentation
