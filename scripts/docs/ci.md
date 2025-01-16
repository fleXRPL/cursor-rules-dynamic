# CI Script (`ci.sh`)

A continuous integration script that runs essential checks and tests for the VSCode extension.

## Purpose

This script automates the continuous integration process by:

1. Installing dependencies
2. Compiling TypeScript code
3. Running ESLint checks
4. Executing tests (with xvfb support in CI environments)
5. Building the extension package

## Usage

```bash
./scripts/ci.sh
```

## Requirements

- Node.js and npm
- In CI environments: `xvfb` for headless testing
- VSCode extension development dependencies

## Process

1. Changes to the `vscode-extension` directory
2. Runs `npm ci` to install dependencies
3. Compiles TypeScript using `npm run compile`
4. Runs ESLint checks using `npm run lint`
5. Executes tests (with xvfb-run in CI environments)
6. Builds the extension package using `npm run vscode:prepublish`

## Error Handling

- Script exits on any error (`set -e`)
- Provides clear console output for each step
- Automatically detects CI environment and adjusts test execution accordingly

## Notes

- Uses `xvfb-run` only in CI environments for headless testing
- Ensures clean dependency installation with `npm ci`
