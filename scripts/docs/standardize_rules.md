# Standardize Rules Script (`standardize_rules.py`)

A Python script for standardizing `.cursorrules` files across the project.

## Purpose

This script standardizes all `.cursorrules` files by:

1. Applying a consistent JSON structure
2. Adding required metadata
3. Preserving existing compatible data
4. Creating/updating README files

## Usage

```bash
./scripts/standardize_rules.py
```

## Requirements

- Python 3.6+
- Read/write access to the rules directory
- Valid `.cursorrules-template` file in the rules directory

## Process

1. Loads the template from `.cursorrules-template`
2. Iterates through all directories in the rules folder
3. For each directory:
   - Reads existing `.cursorrules` file if present
   - Creates new standardized version based on template
   - Preserves existing compatible data
   - Updates metadata (name, timestamp)
   - Creates/updates README.md if needed

## Template Structure

```json
{
  "version": "1.0.0",
  "name": "...",
  "description": "...",
  "author": {
    "name": "...",
    "github": "..."
  },
  "rules": {
    "language": "...",
    "framework": "...",
    "style": {
      "formatting": [],
      "conventions": []
    },
    "dependencies": [],
    "security": [],
    "performance": [],
    "testing": [],
    "documentation": []
  },
  "prompts": {
    "context": "",
    "instructions": [],
    "examples": []
  },
  "metadata": {
    "tags": [],
    "category": "",
    "lastUpdated": "...",
    "compatibility": {
      "cursorVersion": ">=0.1.0",
      "platform": ["darwin", "linux", "win32"]
    }
  }
}
```

## Error Handling

- Gracefully handles missing files
- Reports JSON parsing errors
- Skips problematic files without failing
- Provides clear error messages

## Notes

- Does not delete existing data
- Only updates files that can be parsed as JSON
- Creates basic README.md files if missing
- Maintains a consistent structure across all rules
