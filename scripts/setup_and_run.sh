#!/bin/bash

# Exit on error
set -e

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"
REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.txt"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🔧 Setting up environment for standardize_rules.py...${NC}"

# Create requirements.txt if it doesn't exist
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo -e "${YELLOW}📝 Creating requirements.txt...${NC}"
    cat > "$REQUIREMENTS_FILE" << EOF
pathlib
python-dateutil
EOF
fi

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}🌟 Creating virtual environment...${NC}"
    python3 -m venv "$VENV_DIR"
fi

# Activate virtual environment
echo -e "${YELLOW}🔌 Activating virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

# Install requirements
echo -e "${YELLOW}📦 Installing dependencies...${NC}"
pip install -r "$REQUIREMENTS_FILE"

# Run the Python script
echo -e "${GREEN}🚀 Running standardize_rules.py...${NC}"
python "$SCRIPT_DIR/standardize_rules.py"

# Cleanup and exit virtual environment
echo -e "${BLUE}🧹 Cleaning up environment...${NC}"
deactivate
echo -e "${BLUE}📤 Virtual environment deactivated${NC}"

echo -e "${GREEN}✅ Script execution completed!${NC}" 