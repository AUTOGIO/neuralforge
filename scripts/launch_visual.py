#!/usr/bin/env python3
"""
Visual Interface Launcher for NeuralForge
Choose between different visual interfaces
"""
import sys
import subprocess
from pathlib import Path
import argparse

def show_menu():
    """Show visual interface menu"""
    print("🎨 NeuralForge Visual Interface Launcher")
    print("=" * 50)
    print("Choose your preferred interface:")
    print()
    print("1. 🖥️  Modern Terminal Dashboard (Rich)")
    print("2. 🖼️  GUI Dashboard (CustomTkinter)")
    print("3. 🌐 Web Dashboard (Next.js)")
    print("4. 📱 Mobile-Responsive Web")
    print("5. 🎯 All Interfaces (Demo Mode)")
    print("0. 🚪 Exit")
    print()

def launch_terminal_dashboard():
    """Launch terminal dashboard"""
    print("🖥️  Launching Modern Terminal Dashboard...")
    script_path = Path(__file__).parent.parent / "src" / "visual" / "terminal_dashboard.py"
    if script_path.exists():
        try:
            subprocess.run([sys.executable, str(script_path)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch terminal dashboard: {e}")
    else:
        print("❌ Terminal dashboard script not found")

def launch_gui_dashboard():
    """Launch GUI dashboard"""
    print("🖼️  Launching GUI Dashboard...")
    script_path = Path(__file__).parent.parent / "src" / "visual" / "gui_dashboard.py"
    if script_path.exists():
        try:
            subprocess.run([sys.executable, str(script_path)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch GUI dashboard: {e}")
    else:
        print("❌ GUI dashboard script not found")

def launch_web_dashboard():
    """Launch web dashboard"""
    print("🌐 Launching Web Dashboard...")
    web_dir = Path(__file__).parent.parent / "web-dashboard"
    if web_dir.exists():
        try:
            # Check if node_modules exists
            if not (web_dir / "node_modules").exists():
                print("📦 Installing dependencies...")
                subprocess.run(["npm", "install"], cwd=web_dir, check=True)
            
            print("🚀 Starting development server...")
            subprocess.run(["npm", "run", "dev"], cwd=web_dir, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to launch web dashboard: {e}")
        except FileNotFoundError:
            print("❌ Node.js not found. Please install Node.js to use the web dashboard.")
    else:
        print("❌ Web dashboard directory not found")

def launch_mobile_web():
    """Launch mobile-responsive web interface"""
    print("📱 Launching Mobile-Responsive Web Interface...")
    # This would launch a mobile-optimized version
    print("📱 Mobile interface coming soon!")
    print("💡 For now, use the web dashboard on your mobile device")

def launch_all_interfaces():
    """Launch all interfaces in demo mode"""
    print("🎯 Launching All Interfaces (Demo Mode)...")
    print("This will open all available interfaces for comparison.")
    print()
    
    # Launch terminal dashboard in background
    print("1. Starting Terminal Dashboard...")
    terminal_process = subprocess.Popen([
        sys.executable, 
        str(Path(__file__).parent.parent / "src" / "visual" / "terminal_dashboard.py")
    ])
    
    # Launch GUI dashboard
    print("2. Starting GUI Dashboard...")
    try:
        gui_process = subprocess.Popen([
            sys.executable, 
            str(Path(__file__).parent.parent / "src" / "visual" / "gui_dashboard.py")
        ])
    except Exception as e:
        print(f"❌ GUI Dashboard failed: {e}")
    
    # Launch web dashboard
    print("3. Starting Web Dashboard...")
    try:
        web_dir = Path(__file__).parent.parent / "web-dashboard"
        if web_dir.exists():
            web_process = subprocess.Popen([
                "npm", "run", "dev"
            ], cwd=web_dir)
        else:
            print("❌ Web dashboard not available")
    except Exception as e:
        print(f"❌ Web Dashboard failed: {e}")
    
    print("\n✅ All interfaces launched!")
    print("Press Ctrl+C to stop all interfaces...")
    
    try:
        # Wait for user to stop
        while True:
            pass
    except KeyboardInterrupt:
        print("\n🛑 Stopping all interfaces...")
        terminal_process.terminate()
        if 'gui_process' in locals():
            gui_process.terminate()
        if 'web_process' in locals():
            web_process.terminate()
        print("✅ All interfaces stopped.")

def main():
    """Main launcher function"""
    parser = argparse.ArgumentParser(description="NeuralForge Visual Interface Launcher")
    parser.add_argument("--interface", "-i", choices=["terminal", "gui", "web", "mobile", "all"], 
                       help="Launch specific interface directly")
    
    args = parser.parse_args()
    
    if args.interface:
        if args.interface == "terminal":
            launch_terminal_dashboard()
        elif args.interface == "gui":
            launch_gui_dashboard()
        elif args.interface == "web":
            launch_web_dashboard()
        elif args.interface == "mobile":
            launch_mobile_web()
        elif args.interface == "all":
            launch_all_interfaces()
        return
    
    # Interactive menu
    while True:
        show_menu()
        try:
            choice = input("🎯 Select an option (0-5): ").strip()
            
            if choice == "1":
                launch_terminal_dashboard()
            elif choice == "2":
                launch_gui_dashboard()
            elif choice == "3":
                launch_web_dashboard()
            elif choice == "4":
                launch_mobile_web()
            elif choice == "5":
                launch_all_interfaces()
            elif choice == "0":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid option. Please select 0-5.")
            
            if choice != "0":
                input("\n⏸️  Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Launcher interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
