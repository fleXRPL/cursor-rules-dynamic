# Package Extension Script (`package_extension.sh`)

A script for packaging the VSCode extension into a distributable VSIX file.

## Purpose

This script automates the process of creating a VSCode extension package by:
1. Setting up the necessary environment
2. Copying required files
3. Installing packaging tools
4. Creating the VSIX package
5. Cleaning up temporary files

## Usage

```bash
./scripts/package_extension.sh
```

## Requirements

- Node.js and npm
- VSCode extension development environment
- Internet connection (for installing vsce if needed)

## Process

1. Determines script and extension directories
2. Copies LICENSE file if not present
3. Installs `vsce` globally if not already installed
4. Cleans any existing VSIX packages
5. Creates new VSIX package
6. Verifies package creation
7. Cleans up temporary files

## Error Handling

- Script exits on any error (`set -e`)
- Verifies package creation success
- Provides colored output for success/failure states
- Cleans up temporary files even on failure

## Output

- Displays colored status messages
- Shows the created VSIX package details
- Indicates success or failure clearly

## Notes

- Automatically manages the LICENSE file
- Cleans up previous packages before creating new ones
- Uses color-coded output for better visibility 