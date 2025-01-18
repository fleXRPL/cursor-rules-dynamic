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

def convert_text_to_rules(text_content, dir_name):
    """Convert text content to standardized rules format."""
    try:
        # First try to parse as JSON in case it is valid JSON
        return json.loads(text_content)
    except json.JSONDecodeError:
        # If not valid JSON, create a new structure with the text as content
        return {
            "name": dir_name,
            "description": "Cursor.sh AI rules for development",
            "version": "1.0.0",
            "content": text_content.strip(),
            "metadata": {
                "lastUpdated": datetime.datetime.now().isoformat(),
                "format": "text",
                "originalFileName": ".cursorrules"
            }
        }

def process_directory(dir_path, template):
    """Process a single directory containing .cursorrules file."""
    cursorrules_path = dir_path / ".cursorrules"
    readme_path = dir_path / "README.md"
    
    # Skip if no .cursorrules file exists
    if not cursorrules_path.exists():
        print(f"No .cursorrules file found in {dir_path}")
        return
    
    try:
        # Load existing .cursorrules file as text
        with open(cursorrules_path) as f:
            existing_content = f.read()
        
        # Convert the content to rules format
        existing_rules = convert_text_to_rules(existing_content, dir_path.name)
        
        # Create new standardized rules
        new_rules = template.copy()
        new_rules["name"] = dir_path.name
        new_rules["metadata"]["lastUpdated"] = datetime.datetime.now().isoformat()
        
        # Transfer existing data if it matches our schema
        for key in existing_rules:
            if key in new_rules:
                new_rules[key] = existing_rules[key]
            elif key == "content":
                # Store the original text content in a specific field
                new_rules["prompt"] = existing_rules["content"]
        
        # Save the standardized rules
        with open(cursorrules_path, 'w') as f:
            json.dump(new_rules, f, indent=2)
        
        print(f"✅ Successfully processed {dir_path}")
        
        # Create README.md if it doesn't exist
        if not readme_path.exists():
            with open(readme_path, 'w') as f:
                f.write(f"# {new_rules['name']}\n\n")
                if "description" in new_rules:
                    f.write(f"{new_rules['description']}\n\n")
                f.write("## Usage\n\n")
                f.write("Copy the `.cursorrules` file to your project's root directory.\n")
    
    except Exception as e:
        print(f"⚠️  Error processing {dir_path}: {e}")
        return

def main():
    """Main function to process all rule directories."""
    rules_dir = Path("rules")
    template = load_template()
    
    # Process each directory in rules/
    for dir_path in rules_dir.iterdir():
        if dir_path.is_dir() and not dir_path.name.startswith('.'):
            print(f"🔄 Processing {dir_path}...")
            process_directory(dir_path, template)

if __name__ == "__main__":
    main() 