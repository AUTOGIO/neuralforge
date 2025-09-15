"""
Projects Directory Integration for NeuralForge
Integrates with the Obsidian Projects directory structure
"""
import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess
import sys

class ProjectsIntegration:
    """Integrates NeuralForge with the Projects directory structure"""
    
    def __init__(self, projects_root: str = None):
        if projects_root:
            self.projects_root = Path(projects_root)
        else:
            # Default to Obsidian Projects directory
            self.projects_root = Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / "Obsidian" / "Projects"
        
        self.neuralforge_root = Path(__file__).parent.parent.parent
        self.setup_directories()
    
    def setup_directories(self):
        """Setup the Projects directory structure"""
        # Create main directories
        directories = [
            "System_Setup",
            "GIOVANNINI_VAULT", 
            "NeuralForge",
            "NeuralForge/Logs",
            "NeuralForge/Config",
            "NeuralForge/Data",
            "NeuralForge/Reports"
        ]
        
        for directory in directories:
            dir_path = self.projects_root / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created directory: {dir_path}")
    
    def create_project_readme(self):
        """Create a comprehensive README for the Projects directory"""
        readme_content = f"""# 🧠 NeuralForge Projects Directory

## Overview
This directory contains all NeuralForge-related projects and data, organized for easy access and management.

## Directory Structure

```
Projects/
├── System_Setup/              # System profiling and setup tools
│   ├── export_setup_to_obsidian.py
│   └── Logs/                  # System profiling logs
├── GIOVANNINI_VAULT/          # Main AI vault and tools
│   ├── PYTHON_EXTRA/          # Python tools and scripts
│   └── NEURAL_CORE_VAULT/     # Core AI functionality
├── NeuralForge/               # NeuralForge toolkit
│   ├── Logs/                  # Application logs
│   ├── Config/                # Configuration files
│   ├── Data/                  # Data storage
│   └── Reports/               # Generated reports
└── README.md                  # This file
```

## Quick Start

### 1. System Profiling
```bash
cd System_Setup
python3 export_setup_to_obsidian.py
```

### 2. NeuralForge TUI
```bash
cd NeuralForge
python3 src/tui/neuralforge_tui.py
```

### 3. Natural Language Interface
```bash
cd NeuralForge
python3 src/nlp/natural_language_interface.py
```

### 4. Visual Interfaces
```bash
cd NeuralForge
python3 scripts/launch_visual.py
```

## Available Commands

### Natural Language Commands
- "Organize my files" - Clean up and organize files
- "Monitor my system" - Check system performance
- "Show AI memory" - View conversation history
- "Scrape website" - Extract data from websites
- "Send email" - Automate email sending
- "Schedule task" - Set up automated tasks
- "Show analytics" - View usage statistics

### Direct Tool Access
- File Organizer: `python3 src/core/folder_organizer.py`
- Neural Monitor: `python3 src/core/neural_check.py`
- AI Memory: `python3 src/ai/memory_buffer.py`
- Web Scraper: `python3 src/web/gui_scraper.py`

## Configuration

### Environment Variables
```bash
export NEURALFORGE_PROJECTS_ROOT="{self.projects_root}"
export NEURALFORGE_CONFIG="{self.projects_root}/NeuralForge/Config"
export NEURALFORGE_LOGS="{self.projects_root}/NeuralForge/Logs"
```

### Configuration Files
- `NeuralForge/Config/memory_config.json` - AI memory settings
- `NeuralForge/Config/system_config.json` - System settings
- `NeuralForge/Config/automation_config.json` - Automation settings

## Integration Points

### 1. System_Setup Integration
- Automatically profiles system on startup
- Stores logs in `System_Setup/Logs/`
- Integrates with NeuralForge monitoring

### 2. GIOVANNINI_VAULT Integration
- Shares AI memory system
- Integrates with vault tools
- Cross-project data sharing

### 3. Obsidian Integration
- Markdown reports in `NeuralForge/Reports/`
- Automatic note generation
- Knowledge graph integration

## Usage Examples

### Daily Workflow
1. **Morning**: Check system status with "Monitor my system"
2. **Work**: Use "Organize my files" to clean up downloads
3. **Research**: Use "Scrape website" to gather data
4. **Communication**: Use "Send email" for automated messages
5. **Evening**: Use "Show analytics" to review daily activity

### Project Management
1. **Setup**: Run system profiling to understand environment
2. **Development**: Use TUI for real-time monitoring
3. **Automation**: Set up scheduled tasks
4. **Analysis**: Generate reports and analytics

## Troubleshooting

### Common Issues
- **Permission errors**: Check file permissions in Projects directory
- **Missing dependencies**: Run `pip install -r requirements.txt`
- **Configuration errors**: Check config files in `NeuralForge/Config/`

### Getting Help
- Use "help" command in natural language interface
- Check logs in `NeuralForge/Logs/`
- Review configuration in `NeuralForge/Config/`

## Last Updated
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---
*Generated by NeuralForge Projects Integration*
"""
        
        readme_path = self.projects_root / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"✅ Created README: {readme_path}")
    
    def create_launcher_script(self):
        """Create a launcher script for the Projects directory"""
        launcher_content = f"""#!/bin/bash
# NeuralForge Projects Launcher
# Quick access to all NeuralForge tools

PROJECTS_ROOT="{self.projects_root}"
NEURALFORGE_ROOT="$PROJECTS_ROOT/NeuralForge"

echo "🧠 NeuralForge Projects Launcher"
echo "================================="
echo ""

# Check if NeuralForge exists
if [ ! -d "$NEURALFORGE_ROOT" ]; then
    echo "❌ NeuralForge not found at $NEURALFORGE_ROOT"
    echo "Please run the integration setup first."
    exit 1
fi

cd "$NEURALFORGE_ROOT"

echo "Available options:"
echo "1. 🖥️  TUI Interface"
echo "2. 💬 Natural Language Interface"
echo "3. 🎨 Visual Interfaces"
echo "4. 📊 System Profiling"
echo "5. 🛠️  All Tools"
echo "0. 🚪 Exit"
echo ""

read -p "Select an option (0-5): " choice

case $choice in
    1)
        echo "🖥️  Launching TUI Interface..."
        python3 src/tui/neuralforge_tui.py
        ;;
    2)
        echo "💬 Launching Natural Language Interface..."
        python3 src/nlp/natural_language_interface.py
        ;;
    3)
        echo "🎨 Launching Visual Interfaces..."
        python3 scripts/launch_visual.py
        ;;
    4)
        echo "📊 Running System Profiling..."
        cd ../System_Setup
        python3 export_setup_to_obsidian.py
        ;;
    5)
        echo "🛠️  Launching All Tools..."
        python3 scripts/launch_visual.py --interface all
        ;;
    0)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid option"
        exit 1
        ;;
esac
"""
        
        launcher_path = self.projects_root / "launch_neuralforge.sh"
        with open(launcher_path, 'w', encoding='utf-8') as f:
            f.write(launcher_content)
        
        # Make executable
        os.chmod(launcher_path, 0o755)
        print(f"✅ Created launcher script: {launcher_path}")
    
    def create_desktop_shortcut(self):
        """Create desktop shortcut for easy access"""
        shortcut_content = f"""#!/bin/bash
# NeuralForge Desktop Shortcut
cd "{self.projects_root}"
./launch_neuralforge.sh
"""
        
        desktop_path = Path.home() / "Desktop" / "NeuralForge.command"
        with open(desktop_path, 'w', encoding='utf-8') as f:
            f.write(shortcut_content)
        
        # Make executable
        os.chmod(desktop_path, 0o755)
        print(f"✅ Created desktop shortcut: {desktop_path}")
    
    def setup_environment(self):
        """Setup environment variables and configuration"""
        env_content = f"""# NeuralForge Environment Configuration
export NEURALFORGE_PROJECTS_ROOT="{self.projects_root}"
export NEURALFORGE_CONFIG="{self.projects_root}/NeuralForge/Config"
export NEURALFORGE_LOGS="{self.projects_root}/NeuralForge/Logs"
export NEURALFORGE_DATA="{self.projects_root}/NeuralForge/Data"

# Add NeuralForge to PATH
export PATH="$PATH:{self.neuralforge_root}/scripts"

# Aliases for quick access
alias neuralforge="cd {self.projects_root} && ./launch_neuralforge.sh"
alias neural-tui="cd {self.neuralforge_root} && python3 src/tui/neuralforge_tui.py"
alias neural-chat="cd {self.neuralforge_root} && python3 src/nlp/natural_language_interface.py"
alias neural-visual="cd {self.neuralforge_root} && python3 scripts/launch_visual.py"
"""
        
        env_path = self.projects_root / "neuralforge.env"
        with open(env_path, 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        print(f"✅ Created environment file: {env_path}")
        print("💡 Add 'source {}/neuralforge.env' to your ~/.zshrc or ~/.bashrc".format(env_path))
    
    def create_config_files(self):
        """Create default configuration files"""
        config_dir = self.projects_root / "NeuralForge" / "Config"
        config_dir.mkdir(parents=True, exist_ok=True)
        
        # System configuration
        system_config = {
            "monitoring": {
                "enabled": True,
                "interval": 2,
                "alerts": True
            },
            "file_organization": {
                "auto_organize": False,
                "target_directories": ["~/Downloads", "~/Desktop"],
                "categories": ["images", "videos", "documents", "archives", "data", "others"]
            },
            "ai_memory": {
                "provider": "postgresql",
                "auto_save": True,
                "retention_days": 30
            }
        }
        
        with open(config_dir / "system_config.json", 'w') as f:
            json.dump(system_config, f, indent=2)
        
        # Automation configuration
        automation_config = {
            "email": {
                "enabled": False,
                "smtp_server": "smtp.gmail.com",
                "smtp_port": 587
            },
            "scheduling": {
                "enabled": True,
                "default_timezone": "UTC"
            },
            "web_scraping": {
                "enabled": True,
                "default_timeout": 30,
                "respect_robots_txt": True
            }
        }
        
        with open(config_dir / "automation_config.json", 'w') as f:
            json.dump(automation_config, f, indent=2)
        
        print(f"✅ Created configuration files in {config_dir}")
    
    def run_integration_setup(self):
        """Run the complete integration setup"""
        print("🚀 Setting up NeuralForge Projects Integration...")
        print("=" * 50)
        
        # Setup directories
        self.setup_directories()
        
        # Create README
        self.create_project_readme()
        
        # Create launcher script
        self.create_launcher_script()
        
        # Create desktop shortcut
        self.create_desktop_shortcut()
        
        # Setup environment
        self.setup_environment()
        
        # Create config files
        self.create_config_files()
        
        print("\n✅ Integration setup complete!")
        print(f"📁 Projects directory: {self.projects_root}")
        print(f"🚀 Launcher script: {self.projects_root}/launch_neuralforge.sh")
        print(f"🖥️  Desktop shortcut: ~/Desktop/NeuralForge.command")
        print("\n💡 Usage:")
        print("• Double-click 'NeuralForge.command' on Desktop")
        print("• Or run: cd {} && ./launch_neuralforge.sh".format(self.projects_root))
        print("• Or use natural language: 'neuralforge' command")

def main():
    """Main entry point"""
    integration = ProjectsIntegration()
    integration.run_integration_setup()

if __name__ == "__main__":
    main()
