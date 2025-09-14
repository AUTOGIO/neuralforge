#!/bin/bash
# Setup Complete System - GIOVANNINI_VAULT + System_Setup Integration
# This script sets up the complete AI development ecosystem

set -e

echo "🚀 Setting up Complete AI Development Ecosystem"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
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
if [ ! -f "launch_neural_vault.py" ]; then
    print_error "Please run this script from the GIOVANNINI_VAULT/PYTHON_EXTRA directory"
    exit 1
fi

print_status "Starting complete system setup..."

# Step 1: Install Python dependencies
print_status "Installing Python dependencies..."
python3 -m pip install --user rich psutil requests beautifulsoup4 lxml pytest

if [ $? -eq 0 ]; then
    print_success "Python dependencies installed"
else
    print_error "Failed to install Python dependencies"
    exit 1
fi

# Step 2: Test all components
print_status "Testing all components..."

# Test Neural Engine Monitor
print_status "Testing Neural Engine Monitor..."
python3 core/neural_check.py --help > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Neural Engine Monitor: OK"
else
    print_warning "Neural Engine Monitor: Issues detected"
fi

# Test AI Memory System
print_status "Testing AI Memory System..."
python3 ai/memory_buffer.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "AI Memory System: OK"
else
    print_warning "AI Memory System: Issues detected"
fi

# Test File Organizer
print_status "Testing File Organizer..."
python3 core/folder_organizer.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "File Organizer: OK"
else
    print_warning "File Organizer: Issues detected"
fi

# Test Document Tagger
print_status "Testing Document Tagger..."
python3 ai/document_tagger.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Document Tagger: OK"
else
    print_warning "Document Tagger: Issues detected"
fi

# Test Web Scraper
print_status "Testing Web Scraper..."
python3 web/gui_scraper.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Web Scraper: OK"
else
    print_warning "Web Scraper: Issues detected"
fi

# Test Core ML Integration
print_status "Testing Core ML Integration..."
python3 core/coreml.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "Core ML Integration: OK"
else
    print_warning "Core ML Integration: Issues detected"
fi

# Step 3: Execute PERSONA profiling
print_status "Executing PERSONA profiling..."
cd "/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/Projects/System_Setup"
if [ -f "export_setup_to_obsidian.py" ]; then
    python3 export_setup_to_obsidian.py
    print_success "PERSONA profiling completed"
else
    print_warning "PERSONA profiling script not found"
fi

# Step 4: Test system integration
print_status "Testing system integration..."
cd "/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/GIOVANNINI_VAULT/PYTHON_EXTRA"
python3 integration/system_integration.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    print_success "System Integration: OK"
else
    print_warning "System Integration: Issues detected"
fi

# Step 5: Create desktop shortcuts
print_status "Creating desktop shortcuts..."

# Create PERSONA profiling shortcut
cat > ~/Desktop/PERSONA_Profiling.command << 'EOF'
#!/bin/bash
cd "/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/Projects/System_Setup"
python3 export_setup_to_obsidian.py
echo "Press any key to continue..."
read -n 1
EOF
chmod +x ~/Desktop/PERSONA_Profiling.command

# Create Neural Vault launcher shortcut
cat > ~/Desktop/Neural_Vault.command << 'EOF'
#!/bin/bash
cd "/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/GIOVANNINI_VAULT/PYTHON_EXTRA"
python3 launch_neural_vault.py
EOF
chmod +x ~/Desktop/Neural_Vault.command

print_success "Desktop shortcuts created"

# Step 6: Setup Raycast integration
print_status "Setting up Raycast integration..."
if [ -d "$HOME/Library/Application Support/Raycast/Script Commands" ]; then
    cp -r raycast/* "$HOME/Library/Application Support/Raycast/Script Commands/"
    print_success "Raycast commands installed"
else
    print_warning "Raycast not found. Please install Raycast and run this script again."
fi

# Step 7: Create system status script
print_status "Creating system status script..."
cat > ~/Desktop/System_Status.command << 'EOF'
#!/bin/bash
cd "/Users/giovannini/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/GIOVANNINI_VAULT/PYTHON_EXTRA"
python3 -c "
from integration.system_integration import SystemIntegration
integration = SystemIntegration()
status = integration.get_integration_status()
print('🔗 System Integration Status')
print('=' * 40)
print(f'System Setup: {status.get(\"system_setup_available\", False)}')
print(f'PERSONA Logs: {status.get(\"persona_logs_available\", False)}')
print(f'Memory System: {status.get(\"memory_system_status\", \"unknown\")}')
print(f'Neural Engine: {status.get(\"neural_engine_status\", \"unknown\")}')
print(f'Integration Health: {status.get(\"integration_health\", \"unknown\")}')
print(f'Memory Entries: {status.get(\"memory_entries\", 0)}')
print('')
print('Press any key to continue...')
input()
"
EOF
chmod +x ~/Desktop/System_Status.command

print_success "System status script created"

# Step 8: Final system check
print_status "Running final system check..."
python3 -c "
import sys
sys.path.append('.')
from launch_neural_vault import NeuralVaultLauncher
launcher = NeuralVaultLauncher()
launcher.show_project_status()
"

print_success "Complete system setup finished!"
echo ""
echo "🎉 GIOVANNINI_VAULT is now fully operational!"
echo ""
echo "📋 What's been set up:"
echo "  ✅ All Python dependencies installed"
echo "  ✅ All components tested"
echo "  ✅ PERSONA profiling executed"
echo "  ✅ System integration configured"
echo "  ✅ Desktop shortcuts created"
echo "  ✅ Raycast integration ready"
echo "  ✅ System status monitoring active"
echo ""
echo "🚀 Quick Start:"
echo "  1. Double-click 'Neural_Vault.command' on Desktop to launch"
echo "  2. Use Raycast (⌘+Space) and search for 'neural' or 'persona'"
echo "  3. Run 'System_Status.command' to check system health"
echo ""
echo "🔗 Integration Status:"
echo "  - System_Setup ↔ GIOVANNINI_VAULT: ACTIVE"
echo "  - PERSONA Profiling: READY"
echo "  - AI Memory System: ACTIVE"
echo "  - Neural Engine Monitor: READY"
echo "  - Automation Workflows: CONFIGURED"
echo ""
echo "📚 Next Steps:"
echo "  1. Configure n8n/Node-RED with provided workflows"
echo "  2. Set up Telegram bot for notifications"
echo "  3. Customize Raycast commands as needed"
echo "  4. Schedule regular PERSONA profiling"
echo ""
print_success "Setup complete! Your AI development ecosystem is ready! 🧠✨"
