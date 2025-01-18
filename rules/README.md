# Cursor Rules Directory

This directory contains `.cursorrules` files that define development guidelines and best practices for various technology stacks and frameworks.

## Directory Structure

```bash
rules/
├── backend
│   ├── deno
│   ├── elixir
│   ├── go
│   ├── java
│   ├── ml
│   ├── nodejs
│   ├── php
│   └── python
├── best-practices
├── database
│   ├── graphql
│   ├── nosql
│   └── sql
├── devops
│   ├── docker
│   ├── github
│   └── kubernetes
├── frontend
│   ├── angular
│   ├── astro
│   ├── javascript
│   ├── nextjs
│   ├── qwik
│   ├── react
│   ├── solid
│   ├── svelte
│   ├── typescript
│   └── vue
├── mobile
│   ├── android
│   ├── flutter
│   ├── ios
│   └── react-native
├── specialized
├── testing
│   ├── cypress
│   └── jest
├── tools
│   ├── cursor
│   ├── desktop
│   ├── electron
│   ├── extensions
│   ├── gui
│   ├── unity
│   └── vscode
└── web
    ├── html
    ├── htmx
    └── tailwind

59 directories
```   

## File Structure

Each `.cursorrules` file follows this standardized format:

```
// Title and Author
// Author: {{AUTHOR_NAME}} ({{GITHUB_USERNAME}})

// What you can build with this ruleset:
[List of features and capabilities]

// Project Structure
[Detailed directory structure with comments]

// Development Guidelines
[Numbered sections of specific guidelines]

// Dependencies
Core:
[List of required dependencies with versions]

Optional:
[List of optional dependencies with versions]

// Code Examples:
[Numbered examples with practical implementations]

// Best Practices:
[Numbered list of best practices]

// Security Considerations:
[Numbered list of security requirements]
```

## Usage

1. Each `.cursorrules` file serves as a comprehensive guide for developing applications with specific technology stacks.

2. The files contain:
   - Project structure recommendations
   - Development guidelines
   - Required dependencies
   - Code examples
   - Best practices
   - Security considerations

3. When starting a new project:
   - Reference the appropriate `.cursorrules` file
   - Follow the project structure
   - Implement the recommended patterns
   - Adhere to the security guidelines

4. For maintenance:
   - Keep dependencies updated to specified versions
   - Follow the documented best practices
   - Implement all security considerations
   - Use the code examples as reference patterns

## Contributing

When adding new rulesets:

1. Create a new directory following the naming pattern:
   `{technology}-{specific-focus}-cursorrules-prompt-file/`

2. Include a `.cursorrules` file following the standardized format

3. Ensure all sections are complete:
   - Project structure
   - Development guidelines
   - Dependencies
   - Code examples
   - Best practices
   - Security considerations

4. Update this README.md with the new ruleset information

## Maintenance

- Review and update dependency versions quarterly
- Validate code examples against latest framework versions
- Update security considerations based on new best practices
- Add new patterns and examples as technologies evolve 