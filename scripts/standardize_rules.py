#!/usr/bin/env python3

import os
import json
import datetime
from pathlib import Path

def load_template():
    """Load the .cursorrules template file."""
    template_path = Path("rules/.cursorrules-template")
    with open(template_path) as f:
        return json.load(f)

def process_directory(dir_path, template):
    """Process a single directory containing .cursorrules file."""
    cursorrules_path = dir_path / ".cursorrules"
    readme_path = dir_path / "README.md"
    
    # Skip if no .cursorrules file exists
    if not cursorrules_path.exists():
        print(f"No .cursorrules file found in {dir_path}")
        return
    
    try:
        # Load existing .cursorrules file
        with open(cursorrules_path) as f:
            existing_rules = json.load(f)
    except json.JSONDecodeError:
        print(f"Invalid JSON in {cursorrules_path}")
        return
    except Exception as e:
        print(f"Error processing {cursorrules_path}: {e}")
        return
    
    # Create new standardized rules
    new_rules = template.copy()
    new_rules["name"] = dir_path.name
    new_rules["metadata"]["lastUpdated"] = datetime.datetime.now().isoformat()
    
    # Transfer existing data if it matches our schema
    for key in existing_rules:
        if key in new_rules:
            new_rules[key] = existing_rules[key]
    
    # Save the standardized rules
    with open(cursorrules_path, 'w') as f:
        json.dump(new_rules, f, indent=2)
    
    # Create README.md if it doesn't exist
    if not readme_path.exists():
        with open(readme_path, 'w') as f:
            f.write(f"# {new_rules['name']}\n\n")
            if "description" in new_rules:
                f.write(f"{new_rules['description']}\n\n")
            f.write("## Usage\n\n")
            f.write("Copy the `.cursorrules` file to your project's root directory.\n")

def main():
    """Main function to process all rule directories."""
    rules_dir = Path("rules")
    template = load_template()
    
    # Process each directory in rules/
    for dir_path in rules_dir.iterdir():
        if dir_path.is_dir() and not dir_path.name.startswith('.'):
            print(f"Processing {dir_path}...")
            process_directory(dir_path, template)

if __name__ == "__main__":
    main() 