# TypeScript Development Script (`typescript_dev.sh`)

A comprehensive development script for TypeScript-based VSCode extension development.

## Purpose

This script automates the TypeScript development workflow by:
1. Cleaning previous builds
2. Managing dependencies
3. Running linting checks
4. Compiling TypeScript
5. Running tests and generating coverage reports
6. Building the extension

## Usage

```bash
./scripts/typescript_dev.sh
```

## Requirements

- Node.js and npm (script verifies these)
- VSCode extension development environment
- TypeScript development tools

## Process

1. Verifies required tools (node, npm)
2. Cleans previous builds and artifacts
3. Manages package dependencies:
   - Checks package-lock.json sync
   - Runs npm install or npm ci as needed
4. Runs ESLint checks
5. Compiles TypeScript
6. Executes tests
7. Generates coverage reports
8. Builds the extension package

## Error Handling

- Script exits on any error (`set -e`)
- Verifies required tools before starting
- Provides colored output for different states
- Shows clear error messages

## Output

- Uses color-coded messages for different steps
- Shows test coverage summary
- Indicates success/failure of each step
- Displays final coverage report location

## Notes

- Automatically detects and handles package-lock.json sync state
- Provides comprehensive test coverage information
- Uses color-coded output for better visibility
- Maintains clean build state by removing previous artifacts 