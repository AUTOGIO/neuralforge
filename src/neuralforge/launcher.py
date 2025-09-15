#!/usr/bin/env python3
"""
NEURAL_CORE_VAULT Launch Script
Quick launcher for all your AI tools and monitoring systems
"""
import os
import sys
import subprocess
from pathlib import Path
import argparse

class NeuralVaultLauncher:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.core_dir = self.project_root / "core"
        self.ai_dir = self.project_root / "ai"
        self.web_dir = self.project_root / "web"
        self.automation_dir = self.project_root / "automation"
        
    def show_banner(self):
        """Display the project banner"""
        print("🧠" + "="*60 + "🧠")
        print("🚀 NEURAL_CORE_VAULT - AI & Automation Toolkit")
        print("🧠" + "="*60 + "🧠")
        print("🎯 Optimized for Apple Silicon (M3) Macs")
        print("🔧 PostgreSQL 17 + Neural Engine + Core ML")
        print("🧠" + "="*60 + "🧠")
        
    def show_menu(self):
        """Display the main menu"""
        print("\n🛠️  Available Tools:")
        print("1. 🧠 Neural Engine Monitor")
        print("2. 📁 File Organizer")
        print("3. 🔧 Core ML Integration")
        print("4. 💾 AI Memory System")
        print("5. 🌐 Web Scraper")
        print("6. 📧 Email Automation")
        print("7. ⏰ Schedule Automation")
        print("8. 🧪 Run All Tests")
        print("9. 📊 Project Status")
        print("0. 🚪 Exit")
        
    def launch_neural_monitor(self):
        """Launch the Neural Engine monitoring tool"""
        print("\n🧠 Launching Neural Engine Monitor...")
        script_path = self.core_dir / "neural_check.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Neural monitor failed to start")
        else:
            print("❌ Neural monitor script not found")
            
    def launch_file_organizer(self):
        """Launch the file organization tool"""
        print("\n📁 Launching File Organizer...")
        script_path = self.core_dir / "folder_organizer.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ File organizer failed to start")
        else:
            print("❌ File organizer script not found")
            
    def launch_coreml_tool(self):
        """Launch the Core ML integration tool"""
        print("\n🔧 Launching Core ML Integration...")
        script_path = self.core_dir / "coreml.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Core ML tool failed to start")
        else:
            print("❌ Core ML script not found")
            
    def launch_memory_system(self):
        """Launch the AI memory system"""
        print("\n💾 Launching AI Memory System...")
        script_path = self.ai_dir / "memory_buffer.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Memory system failed to start")
        else:
            print("❌ Memory system script not found")
            
    def launch_web_scraper(self):
        """Launch the web scraping tool"""
        print("\n🌐 Launching Web Scraper...")
        script_path = self.web_dir / "gui_scraper.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Web scraper failed to start")
        else:
            print("❌ Web scraper script not found")
            
    def launch_email_automation(self):
        """Launch the email automation tool"""
        print("\n📧 Launching Email Automation...")
        script_path = self.automation_dir / "email_automation.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Email automation failed to start")
        else:
            print("❌ Email automation script not found")
            
    def launch_schedule_automation(self):
        """Launch the schedule automation tool"""
        print("\n⏰ Launching Schedule Automation...")
        script_path = self.automation_dir / "schedule_automation.py"
        if script_path.exists():
            try:
                subprocess.run([sys.executable, str(script_path)], check=True)
            except subprocess.CalledProcessError:
                print("❌ Schedule automation failed to start")
        else:
            print("❌ Schedule automation script not found")
            
    def run_tests(self):
        """Run the test suite"""
        print("\n🧪 Running Test Suite...")
        try:
            subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], check=True)
        except subprocess.CalledProcessError:
            print("❌ Tests failed to run")
        except FileNotFoundError:
            print("❌ pytest not installed. Install with: pip install pytest")
            
    def show_project_status(self):
        """Show the current project status"""
        print("\n📊 NEURAL_CORE_VAULT Project Status:")
        print("="*50)
        
        # Check core tools
        print("🔧 Core Tools:")
        for tool in ["neural_check.py", "folder_organizer.py", "coreml.py"]:
            path = self.core_dir / tool
            status = "✅" if path.exists() else "❌"
            print(f"   {status} {tool}")
            
        # Check AI tools
        print("\n🧠 AI Tools:")
        for tool in ["memory_buffer.py", "document_tagger.py"]:
            path = self.ai_dir / tool
            status = "✅" if path.exists() else "❌"
            print(f"   {status} {tool}")
            
        # Check web tools
        print("\n🌐 Web Tools:")
        for tool in ["gui_scraper.py"]:
            path = self.web_dir / tool
            status = "✅" if path.exists() else "❌"
            print(f"   {status} {tool}")
            
        # Check automation tools
        print("\n🤖 Automation Tools:")
        for tool in ["email_automation.py", "schedule_automation.py"]:
            path = self.automation_dir / tool
            status = "✅" if path.exists() else "❌"
            print(f"   {status} {tool}")
            
        # Check configuration
        print("\n⚙️  Configuration:")
        config_path = self.project_root / "config" / "memory_config.json"
        status = "✅" if config_path.exists() else "❌"
        print(f"   {status} PostgreSQL Configuration")
        
        # Check dependencies
        print("\n📦 Dependencies:")
        req_path = self.project_root / "requirements.txt"
        status = "✅" if req_path.exists() else "❌"
        print(f"   {status} Requirements File")
        
        print("\n🎯 Project is ready for AI development!")
        
    def main_loop(self):
        """Main application loop"""
        while True:
            self.show_menu()
            try:
                choice = input("\n🎯 Select an option (0-9): ").strip()
                
                if choice == "1":
                    self.launch_neural_monitor()
                elif choice == "2":
                    self.launch_file_organizer()
                elif choice == "3":
                    self.launch_coreml_tool()
                elif choice == "4":
                    self.launch_memory_system()
                elif choice == "5":
                    self.launch_web_scraper()
                elif choice == "6":
                    self.launch_email_automation()
                elif choice == "7":
                    self.launch_schedule_automation()
                elif choice == "8":
                    self.run_tests()
                elif choice == "9":
                    self.show_project_status()
                elif choice == "0":
                    print("\n👋 Thanks for using NEURAL_CORE_VAULT!")
                    print("🚀 Keep building amazing AI systems!")
                    break
                else:
                    print("❌ Invalid option. Please select 0-9.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Launch interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                
            input("\n⏸️  Press Enter to continue...")
            os.system('clear' if os.name == 'posix' else 'cls')

def main():
    """Main entry point"""
    launcher = NeuralVaultLauncher()
    launcher.show_banner()
    launcher.main_loop()

if __name__ == "__main__":
    main()
