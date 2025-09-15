#!/usr/bin/env python3
"""
NeuralForge CLI - Command Line Interface
Natural language command processor
"""
import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from nlp.natural_language_interface import NaturalLanguageInterface

def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="NeuralForge CLI - Natural Language Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  neuralforge "organize my files"
  neuralforge "monitor my system"
  neuralforge "scrape website https://example.com"
  neuralforge "send email to user@example.com"
  neuralforge "schedule task for tomorrow"
  neuralforge "show analytics"
  neuralforge --interactive
        """
    )
    
    parser.add_argument(
        "command",
        nargs="?",
        help="Natural language command to execute"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Start interactive mode"
    )
    
    parser.add_argument(
        "--help-commands",
        action="store_true",
        help="Show available commands"
    )
    
    args = parser.parse_args()
    
    # Initialize interface
    interface = NaturalLanguageInterface()
    
    # Show help commands
    if args.help_commands:
        print(interface.processor._get_help_message())
        return
    
    # Interactive mode
    if args.interactive or not args.command:
        print("🧠 NeuralForge CLI - Interactive Mode")
        print("=" * 40)
        print("Type your commands in natural language!")
        print("Examples:")
        print("• 'Organize my files'")
        print("• 'Monitor my system'")
        print("• 'Help' for available commands")
        print("• 'quit' to exit")
        print()
        
        while True:
            try:
                user_input = input("NeuralForge> ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                response = interface.chat(user_input)
                print(f"Response: {response}")
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
    
    # Single command mode
    else:
        response = interface.chat(args.command)
        print(response)

if __name__ == "__main__":
    main()
