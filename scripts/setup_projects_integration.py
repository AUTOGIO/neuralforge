#!/usr/bin/env python3
"""
Setup Projects Integration for NeuralForge
Integrates NeuralForge with the Obsidian Projects directory
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from integration.projects_integration import ProjectsIntegration

def main():
    """Main setup function"""
    print("🧠 NeuralForge Projects Integration Setup")
    print("=" * 50)
    
    # Get projects directory
    projects_root = input("Enter Projects directory path (or press Enter for default): ").strip()
    if not projects_root:
        projects_root = None  # Use default
    
    # Create integration
    integration = ProjectsIntegration(projects_root)
    
    # Run setup
    integration.run_integration_setup()
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Add environment variables to your shell profile")
    print("2. Test the launcher: ./launch_neuralforge.sh")
    print("3. Try the natural language interface")
    print("4. Explore the TUI interface")

if __name__ == "__main__":
    main()
