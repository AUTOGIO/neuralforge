#!/bin/bash
# Setup Git Repository for NeuralForge
# This script initializes a Git repository and sets up the initial commit

set -e

echo "🚀 Setting up Git Repository for NeuralForge"
echo "============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    print_error "Please run this script from the NeuralForge root directory"
    exit 1
fi

# Initialize Git repository
print_status "Initializing Git repository..."
if [ ! -d ".git" ]; then
    git init
    print_success "Git repository initialized"
else
    print_warning "Git repository already exists"
fi

# Add all files
print_status "Adding files to Git..."
git add .

# Create initial commit
print_status "Creating initial commit..."
git commit -m "Initial commit: NeuralForge v1.0.0

🧠 NeuralForge - Professional AI & Automation Toolkit for Apple Silicon

Features:
- Neural Engine monitoring for Apple Silicon (M1/M2/M3)
- AI Memory System with PostgreSQL integration
- Core ML model conversion and optimization
- File organization and management tools
- Web scraping capabilities
- Document processing and tagging
- System integration and automation
- n8n and Node-RED workflow templates
- Raycast integration for macOS
- Comprehensive test suite
- CI/CD pipeline with GitHub Actions

Optimized for Apple Silicon with enterprise-grade features."

print_success "Initial commit created"

# Create main branch
print_status "Setting up main branch..."
git branch -M main

# Show repository status
print_status "Repository status:"
git status

print_success "Git repository setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Add the remote origin:"
echo "   git remote add origin https://github.com/yourusername/neuralforge.git"
echo "3. Push to GitHub:"
echo "   git push -u origin main"
echo ""
echo "🔗 GitHub repository setup:"
echo "1. Go to https://github.com/new"
echo "2. Repository name: neuralforge"
echo "3. Description: Professional AI & Automation Toolkit for Apple Silicon"
echo "4. Make it public or private"
echo "5. Don't initialize with README (we already have one)"
echo "6. Create repository"
echo ""
echo "⚙️ After creating the repository:"
echo "git remote add origin https://github.com/yourusername/neuralforge.git"
echo "git push -u origin main"
echo ""
print_success "NeuralForge is ready for GitHub! 🧠✨"
