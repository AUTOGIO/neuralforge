#!/bin/bash

# 🧠 NEURAL_CORE_VAULT GitHub Repository Setup Script
# This script helps initialize and push your project to GitHub

set -e  # Exit on any error

echo "🧠============================================================🧠"
echo "🚀 NEURAL_CORE_VAULT - GitHub Repository Setup"
echo "🧠============================================================🧠"
echo "📦 This script will help you set up your GitHub repository"
echo "🔧 Make sure you have GitHub CLI installed: brew install gh"
echo "🧠============================================================🧠"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if we're in the right directory
if [[ ! -f "launch_neural_vault.py" ]]; then
    print_error "Not in NEURAL_CORE_VAULT directory. Please run from project root."
    exit 1
fi

print_status "Found NEURAL_CORE_VAULT project"

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    print_error "GitHub CLI not found. Please install it:"
    echo "  brew install gh"
    echo "  Or visit: https://cli.github.com/"
    exit 1
fi

print_status "GitHub CLI found"

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    print_warning "Not authenticated with GitHub. Please login:"
    echo ""
    gh auth login
    echo ""
fi

print_status "GitHub authentication verified"

# Initialize git repository if not already done
if [[ ! -d ".git" ]]; then
    print_info "Initializing Git repository..."
    git init
    print_status "Git repository initialized"
else
    print_status "Git repository already initialized"
fi

# Create .gitignore if it doesn't exist
if [[ ! -f ".gitignore" ]]; then
    print_info "Creating .gitignore file..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
venv_new/
venv_dev/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# macOS
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

# Project specific
config/memory_config.json
*.log
*.sqlite
*.db
.env
.env.local
.env.production

# Test coverage
htmlcov/
.coverage
coverage.xml
*.cover
.pytest_cache/

# Documentation builds
docs/_build/
site/

# Jupyter
.ipynb_checkpoints

# Security
bandit-report.json
safety-report.json
EOF
    print_status ".gitignore created"
fi

# Get repository name from user
echo ""
print_info "Repository Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Default repository name
DEFAULT_REPO_NAME="neural-core-vault"
read -p "📝 Repository name (default: $DEFAULT_REPO_NAME): " REPO_NAME
REPO_NAME=${REPO_NAME:-$DEFAULT_REPO_NAME}

# Repository visibility
echo ""
echo "🔒 Repository Visibility:"
echo "1) Public (recommended for open source)"
echo "2) Private (for personal/commercial use)"
read -p "Choose (1-2, default: 1): " VISIBILITY_CHOICE
VISIBILITY_CHOICE=${VISIBILITY_CHOICE:-1}

if [[ $VISIBILITY_CHOICE == "2" ]]; then
    VISIBILITY="--private"
    print_info "Repository will be private"
else
    VISIBILITY="--public"
    print_info "Repository will be public"
fi

# Repository description
DEFAULT_DESCRIPTION="🧠 Professional AI & Automation Toolkit optimized for Apple Silicon (M3) Macs with PostgreSQL 17 integration"
read -p "📄 Description (default provided): " REPO_DESCRIPTION
REPO_DESCRIPTION=${REPO_DESCRIPTION:-$DEFAULT_DESCRIPTION}

echo ""
print_info "Creating GitHub repository..."
echo "  Name: $REPO_NAME"
echo "  Visibility: $(echo $VISIBILITY | sed 's/--//')"
echo "  Description: $REPO_DESCRIPTION"
echo ""

# Confirm before proceeding
read -p "🤔 Proceed with repository creation? (y/N): " CONFIRM
if [[ ! $CONFIRM =~ ^[Yy]$ ]]; then
    print_warning "Repository creation cancelled"
    exit 0
fi

# Add all files to git
print_info "Adding files to git..."
git add .

# Create initial commit
print_info "Creating initial commit..."
git commit -m "🎉 Initial commit: NEURAL_CORE_VAULT v1.0.0

🧠 Professional AI & Automation Toolkit for Apple Silicon

Features:
✅ Neural Engine monitoring with real-time performance tracking
✅ PostgreSQL 17 powered AI memory system
✅ Core ML integration and model conversion
✅ Smart file organization and web scraping tools
✅ Comprehensive testing framework and CI/CD

Ready for production use on macOS Apple Silicon (M1/M2/M3) systems."

# Create GitHub repository
print_info "Creating GitHub repository..."
gh repo create "$REPO_NAME" $VISIBILITY --description "$REPO_DESCRIPTION" --source=.

print_status "GitHub repository created successfully!"

# Push code to GitHub
print_info "Pushing code to GitHub..."
git branch -M main
git push -u origin main

print_status "Code pushed to GitHub!"

# Set up repository topics/tags
print_info "Adding repository topics..."
gh repo edit --add-topic "ai"
gh repo edit --add-topic "automation"
gh repo edit --add-topic "apple-silicon"
gh repo edit --add-topic "neural-engine"
gh repo edit --add-topic "core-ml"
gh repo edit --add-topic "postgresql"
gh repo edit --add-topic "python"
gh repo edit --add-topic "macos"
gh repo edit --add-topic "m1"
gh repo edit --add-topic "m2"
gh repo edit --add-topic "m3"

# Enable GitHub features
print_info "Configuring repository settings..."
gh repo edit --enable-issues
gh repo edit --enable-wiki
gh repo edit --enable-projects

# Create repository website URL
REPO_URL=$(gh repo view --json url --jq .url)

echo ""
echo "🎉============================================================🎉"
echo "🚀 NEURAL_CORE_VAULT GitHub Repository Ready!"
echo "🎉============================================================🎉"
echo ""
print_status "Repository URL: $REPO_URL"
print_status "Repository created and configured successfully!"
echo ""
echo "📋 Next Steps:"
echo "1. 🌟 Star your repository: gh repo view --web"
echo "2. 📝 Update repository description if needed"
echo "3. 🔧 Configure branch protection rules"
echo "4. 👥 Add collaborators if working in a team"
echo "5. 🚀 Set up GitHub Pages for documentation"
echo ""
echo "💡 Useful Commands:"
echo "• View repository: gh repo view --web"
echo "• Create issue: gh issue create"
echo "• Create PR: gh pr create"
echo "• View actions: gh workflow list"
echo ""
echo "🔧 CI/CD Pipeline:"
echo "Your GitHub Actions workflows are already configured!"
echo "They will run automatically on push and pull requests."
echo ""
echo "📚 Documentation:"
echo "• README.md - Main project documentation"
echo "• CONTRIBUTING.md - Contribution guidelines"
echo "• SECURITY.md - Security policies"
echo "• docs/api/ - API documentation"
echo ""
print_status "Setup complete! Your NEURAL_CORE_VAULT is now on GitHub! 🎉"

# Open repository in browser
read -p "🌐 Open repository in browser? (y/N): " OPEN_BROWSER
if [[ $OPEN_BROWSER =~ ^[Yy]$ ]]; then
    gh repo view --web
fi

echo ""
echo "🧠 Happy coding with NEURAL_CORE_VAULT! 🚀"
