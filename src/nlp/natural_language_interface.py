"""
Natural Language Interface for NeuralForge
Process natural language commands and execute actions
"""
import re
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import subprocess
import sys

@dataclass
class Command:
    """Represents a parsed command"""
    action: str
    target: str
    parameters: Dict[str, str]
    confidence: float

class NaturalLanguageProcessor:
    """Processes natural language commands for NeuralForge"""
    
    def __init__(self):
        self.command_patterns = self._load_command_patterns()
        self.tool_mappings = self._load_tool_mappings()
        self.context = {}
    
    def _load_command_patterns(self) -> Dict[str, List[str]]:
        """Load command patterns for different actions"""
        return {
            "organize_files": [
                r"organize\s+(?:my\s+)?(?:files|downloads|desktop|documents)",
                r"clean\s+up\s+(?:my\s+)?(?:files|downloads|desktop|documents)",
                r"sort\s+(?:my\s+)?(?:files|downloads|desktop|documents)",
                r"arrange\s+(?:my\s+)?(?:files|downloads|desktop|documents)",
                r"organize\s+(?:the\s+)?(?:files\s+in\s+)?(.+)",
                r"clean\s+up\s+(?:the\s+)?(?:files\s+in\s+)?(.+)",
            ],
            "monitor_system": [
                r"monitor\s+(?:my\s+)?(?:system|computer|mac)",
                r"check\s+(?:my\s+)?(?:system|computer|mac)\s+(?:status|health)",
                r"show\s+(?:my\s+)?(?:system|computer|mac)\s+(?:status|metrics)",
                r"how\s+is\s+(?:my\s+)?(?:system|computer|mac)\s+(?:doing|performing)",
                r"neural\s+engine\s+(?:status|monitor)",
            ],
            "ai_memory": [
                r"show\s+(?:my\s+)?(?:ai\s+)?(?:memory|conversations)",
                r"check\s+(?:my\s+)?(?:ai\s+)?(?:memory|conversations)",
                r"ai\s+memory\s+(?:status|info)",
                r"conversation\s+(?:history|log)",
            ],
            "web_scraping": [
                r"scrape\s+(?:the\s+)?(?:website|site|page)\s+(.+)",
                r"extract\s+(?:data\s+from\s+)?(?:the\s+)?(?:website|site|page)\s+(.+)",
                r"get\s+(?:data\s+from\s+)?(?:the\s+)?(?:website|site|page)\s+(.+)",
                r"web\s+scrape\s+(.+)",
            ],
            "email_automation": [
                r"send\s+(?:an\s+)?(?:email|message)\s+(?:to\s+)?(.+)",
                r"email\s+(.+)",
                r"automate\s+(?:my\s+)?(?:emails|email\s+sending)",
                r"setup\s+(?:email\s+)?(?:automation|workflow)",
            ],
            "schedule_task": [
                r"schedule\s+(?:a\s+)?(?:task|job)\s+(?:for\s+)?(.+)",
                r"set\s+(?:up\s+)?(?:a\s+)?(?:reminder|task)\s+(?:for\s+)?(.+)",
                r"remind\s+(?:me\s+)?(?:to\s+)?(.+)",
                r"automate\s+(?:this\s+)?(?:task|process)",
            ],
            "analytics": [
                r"show\s+(?:me\s+)?(?:analytics|stats|statistics)",
                r"how\s+(?:many|much)\s+(?:files|emails|tasks)\s+(?:have\s+)?(?:i\s+)?(?:organized|sent|completed)",
                r"performance\s+(?:report|stats)",
                r"usage\s+(?:statistics|stats)",
            ],
            "help": [
                r"help",
                r"what\s+(?:can\s+)?(?:you\s+)?(?:do|help\s+with)",
                r"how\s+(?:do\s+)?(?:i\s+)?(?:use|work\s+with)\s+(?:this|neuralforge)",
                r"commands?",
                r"options?",
            ]
        }
    
    def _load_tool_mappings(self) -> Dict[str, str]:
        """Load mappings from actions to tool scripts"""
        return {
            "organize_files": "src/core/folder_organizer.py",
            "monitor_system": "src/core/neural_check.py",
            "ai_memory": "src/ai/memory_buffer.py",
            "web_scraping": "src/web/gui_scraper.py",
            "email_automation": "src/automation/email_automation.py",
            "schedule_task": "src/automation/schedule_automation.py",
            "analytics": "src/visual/terminal_dashboard.py",
            "help": "help"
        }
    
    def parse_command(self, user_input: str) -> Optional[Command]:
        """Parse natural language input into a command"""
        user_input = user_input.lower().strip()
        
        best_match = None
        best_confidence = 0.0
        
        for action, patterns in self.command_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, user_input, re.IGNORECASE)
                if match:
                    confidence = self._calculate_confidence(user_input, pattern, match)
                    if confidence > best_confidence:
                        best_match = {
                            'action': action,
                            'target': match.group(1) if match.groups() else "",
                            'parameters': self._extract_parameters(user_input, action),
                            'confidence': confidence
                        }
                        best_confidence = confidence
        
        if best_match and best_confidence > 0.3:  # Minimum confidence threshold
            return Command(**best_match)
        
        return None
    
    def _calculate_confidence(self, user_input: str, pattern: str, match) -> float:
        """Calculate confidence score for a match"""
        # Base confidence from regex match
        base_confidence = 0.7
        
        # Boost confidence for exact keyword matches
        keywords = ['organize', 'monitor', 'scrape', 'email', 'schedule', 'analytics']
        keyword_boost = sum(0.1 for keyword in keywords if keyword in user_input)
        
        # Boost confidence for complete sentences
        sentence_boost = 0.1 if len(user_input.split()) > 3 else 0
        
        return min(base_confidence + keyword_boost + sentence_boost, 1.0)
    
    def _extract_parameters(self, user_input: str, action: str) -> Dict[str, str]:
        """Extract parameters from user input"""
        parameters = {}
        
        # Extract target directory for file operations
        if action == "organize_files":
            if "downloads" in user_input:
                parameters["target"] = "~/Downloads"
            elif "desktop" in user_input:
                parameters["target"] = "~/Desktop"
            elif "documents" in user_input:
                parameters["target"] = "~/Documents"
            else:
                parameters["target"] = "~/Downloads"  # Default
        
        # Extract URL for web scraping
        elif action == "web_scraping":
            url_match = re.search(r'https?://[^\s]+', user_input)
            if url_match:
                parameters["url"] = url_match.group(0)
            else:
                parameters["url"] = "https://example.com"  # Default
        
        # Extract email recipient
        elif action == "email_automation":
            email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', user_input)
            if email_match:
                parameters["recipient"] = email_match.group(0)
            else:
                parameters["recipient"] = "user@example.com"  # Default
        
        # Extract task description for scheduling
        elif action == "schedule_task":
            # Extract time references
            time_match = re.search(r'(?:at|in|for)\s+(\d+)\s*(?:am|pm|hours?|minutes?|days?)', user_input)
            if time_match:
                parameters["time"] = time_match.group(1)
            
            # Extract task description
            task_match = re.search(r'(?:to|for)\s+(.+)', user_input)
            if task_match:
                parameters["task"] = task_match.group(1)
        
        return parameters
    
    def execute_command(self, command: Command) -> Tuple[bool, str]:
        """Execute a parsed command"""
        try:
            if command.action == "help":
                return True, self._get_help_message()
            
            tool_script = self.tool_mappings.get(command.action)
            if not tool_script:
                return False, f"Unknown action: {command.action}"
            
            # Build command arguments
            args = [sys.executable, tool_script]
            
            # Add parameters
            for key, value in command.parameters.items():
                args.extend([f"--{key}", value])
            
            # Execute the tool
            result = subprocess.run(args, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                return True, f"✅ {command.action.replace('_', ' ').title()} completed successfully!\n{result.stdout}"
            else:
                return False, f"❌ {command.action.replace('_', ' ').title()} failed:\n{result.stderr}"
                
        except subprocess.TimeoutExpired:
            return False, f"❌ {command.action.replace('_', ' ').title()} timed out"
        except Exception as e:
            return False, f"❌ Error executing {command.action}: {str(e)}"
    
    def _get_help_message(self) -> str:
        """Get help message with available commands"""
        return """
🧠 NeuralForge Natural Language Interface

Available Commands:

📁 File Management:
• "Organize my files" or "Clean up my downloads"
• "Sort my desktop" or "Arrange my documents"

🧠 System Monitoring:
• "Monitor my system" or "Check my computer status"
• "Show neural engine status" or "How is my Mac doing?"

💾 AI Memory:
• "Show my AI memory" or "Check my conversations"
• "AI memory status" or "Conversation history"

🌐 Web Scraping:
• "Scrape the website https://example.com"
• "Extract data from the page" or "Web scrape example.com"

📧 Email Automation:
• "Send an email to user@example.com"
• "Setup email automation" or "Automate my emails"

⏰ Task Scheduling:
• "Schedule a task for tomorrow" or "Remind me to check files"
• "Set up a reminder for 3pm" or "Automate this process"

📊 Analytics:
• "Show me analytics" or "Performance report"
• "How many files have I organized?" or "Usage statistics"

❓ Help:
• "Help" or "What can you do?" or "Commands"

Examples:
• "Organize my downloads folder"
• "Monitor my system performance"
• "Scrape data from https://news.com"
• "Send an email to john@company.com"
• "Schedule a backup task for tonight"
• "Show me my usage analytics"
        """
    
    def process_input(self, user_input: str) -> str:
        """Process user input and return response"""
        command = self.parse_command(user_input)
        
        if not command:
            return "❌ I didn't understand that command. Try 'help' to see available commands."
        
        if command.confidence < 0.5:
            return f"🤔 I think you want to {command.action.replace('_', ' ')}, but I'm not sure. Could you be more specific?"
        
        success, message = self.execute_command(command)
        return message

class NaturalLanguageInterface:
    """Main interface for natural language processing"""
    
    def __init__(self):
        self.processor = NaturalLanguageProcessor()
        self.conversation_history = []
    
    def chat(self, user_input: str) -> str:
        """Process a chat message"""
        # Add to conversation history
        self.conversation_history.append({
            "user": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Process the input
        response = self.processor.process_input(user_input)
        
        # Add response to history
        self.conversation_history.append({
            "assistant": response,
            "timestamp": datetime.now().isoformat()
        })
        
        return response
    
    def get_conversation_history(self) -> List[Dict]:
        """Get conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

def main():
    """Main entry point for testing"""
    interface = NaturalLanguageInterface()
    
    print("🧠 NeuralForge Natural Language Interface")
    print("=" * 50)
    print("Type your commands in natural language!")
    print("Examples:")
    print("• 'Organize my downloads'")
    print("• 'Monitor my system'")
    print("• 'Help'")
    print("• 'quit' to exit")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = interface.chat(user_input)
            print(f"NeuralForge: {response}")
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
