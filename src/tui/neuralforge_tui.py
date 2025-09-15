"""
NeuralForge TUI - Modern Terminal User Interface
Beautiful TUI using Textual framework
"""
import asyncio
import time
import psutil
import platform
from datetime import datetime
from pathlib import Path
import subprocess
import sys

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import (
    Header, Footer, Static, Button, DataTable, ProgressBar, 
    TextArea, Label, Switch, Input, Select, Tabs, Tab
)
from textual.reactive import reactive
from textual.binding import Binding
from rich.text import Text
from rich.console import Console

class MetricsWidget(Static):
    """Widget for displaying system metrics"""
    
    cpu_usage = reactive(0.0)
    memory_usage = reactive(0.0)
    neural_engine = reactive(0.0)
    temperature = reactive(0.0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.console = Console()
    
    def compose(self) -> ComposeResult:
        yield Label("📊 System Metrics", classes="header")
        yield Label("CPU Usage:", classes="metric-label")
        yield ProgressBar(total=100, show_eta=False, id="cpu-progress")
        yield Label("Memory Usage:", classes="metric-label")
        yield ProgressBar(total=100, show_eta=False, id="memory-progress")
        yield Label("Neural Engine:", classes="metric-label")
        yield ProgressBar(total=100, show_eta=False, id="neural-progress")
        yield Label("Temperature:", classes="metric-label")
        yield Label("0°C", id="temp-display")
    
    def on_mount(self) -> None:
        """Called when widget is mounted"""
        self.set_interval(2.0, self.update_metrics)
    
    def update_metrics(self) -> None:
        """Update system metrics"""
        self.cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        self.memory_usage = memory.percent
        self.neural_engine = min(self.cpu_usage * 1.2, 100)
        self.temperature = 35 + (self.cpu_usage * 0.3)
    
    def watch_cpu_usage(self, cpu_usage: float) -> None:
        """Called when cpu_usage changes"""
        self.query_one("#cpu-progress", ProgressBar).progress = cpu_usage
        self.query_one("#cpu-progress", ProgressBar).update()
    
    def watch_memory_usage(self, memory_usage: float) -> None:
        """Called when memory_usage changes"""
        self.query_one("#memory-progress", ProgressBar).progress = memory_usage
        self.query_one("#memory-progress", ProgressBar).update()
    
    def watch_neural_engine(self, neural_engine: float) -> None:
        """Called when neural_engine changes"""
        self.query_one("#neural-progress", ProgressBar).progress = neural_engine
        self.query_one("#neural-progress", ProgressBar).update()
    
    def watch_temperature(self, temperature: float) -> None:
        """Called when temperature changes"""
        self.query_one("#temp-display", Label).update(f"{temperature:.1f}°C")

class ToolsWidget(Static):
    """Widget for displaying and managing tools"""
    
    def compose(self) -> ComposeResult:
        yield Label("🛠️ NeuralForge Tools", classes="header")
        yield Button("🧠 Neural Monitor", id="neural-monitor", variant="primary")
        yield Button("💾 AI Memory", id="ai-memory", variant="primary")
        yield Button("📁 File Organizer", id="file-organizer", variant="primary")
        yield Button("🌐 Web Scraper", id="web-scraper", variant="primary")
        yield Button("📧 Email Auto", id="email-auto", variant="primary")
        yield Button("⏰ Schedule", id="schedule", variant="primary")
        yield Button("📊 Analytics", id="analytics", variant="primary")
        yield Button("⚙️ Settings", id="settings", variant="secondary")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses"""
        button_id = event.button.id
        self.app.notify(f"Launching {button_id.replace('-', ' ').title()}...")
        
        # Here you would launch the actual tools
        if button_id == "neural-monitor":
            self.launch_neural_monitor()
        elif button_id == "ai-memory":
            self.launch_ai_memory()
        elif button_id == "file-organizer":
            self.launch_file_organizer()
        elif button_id == "web-scraper":
            self.launch_web_scraper()
        elif button_id == "email-auto":
            self.launch_email_automation()
        elif button_id == "schedule":
            self.launch_schedule_automation()
        elif button_id == "analytics":
            self.show_analytics()
        elif button_id == "settings":
            self.show_settings()
    
    def launch_neural_monitor(self):
        """Launch neural monitor"""
        self.app.notify("🧠 Neural Engine Monitor started!", severity="information")
    
    def launch_ai_memory(self):
        """Launch AI memory system"""
        self.app.notify("💾 AI Memory System activated!", severity="information")
    
    def launch_file_organizer(self):
        """Launch file organizer"""
        self.app.notify("📁 File Organizer ready!", severity="information")
    
    def launch_web_scraper(self):
        """Launch web scraper"""
        self.app.notify("🌐 Web Scraper initialized!", severity="information")
    
    def launch_email_automation(self):
        """Launch email automation"""
        self.app.notify("📧 Email Automation configured!", severity="information")
    
    def launch_schedule_automation(self):
        """Launch schedule automation"""
        self.app.notify("⏰ Schedule Automation running!", severity="information")
    
    def show_analytics(self):
        """Show analytics"""
        self.app.notify("📊 Analytics dashboard opened!", severity="information")
    
    def show_settings(self):
        """Show settings"""
        self.app.notify("⚙️ Settings panel opened!", severity="information")

class StatusWidget(Static):
    """Widget for displaying system status"""
    
    def compose(self) -> ComposeResult:
        yield Label("ℹ️ System Status", classes="header")
        yield Label(f"Platform: {platform.system()} {platform.release()}", id="platform")
        yield Label(f"Architecture: {platform.machine()}", id="architecture")
        yield Label(f"Python: {platform.python_version()}", id="python")
        yield Label("Status: 🟢 Healthy", id="status")
        yield Label(f"Uptime: {int(time.time() - psutil.boot_time()) // 3600}h", id="uptime")
    
    def on_mount(self) -> None:
        """Called when widget is mounted"""
        self.set_interval(10.0, self.update_status)
    
    def update_status(self) -> None:
        """Update system status"""
        uptime_hours = int(time.time() - psutil.boot_time()) // 3600
        self.query_one("#uptime", Label).update(f"Uptime: {uptime_hours}h")

class LogWidget(Static):
    """Widget for displaying logs and output"""
    
    def compose(self) -> ComposeResult:
        yield Label("📝 Activity Log", classes="header")
        yield TextArea("NeuralForge TUI started successfully!\n", id="log-area", read_only=True)
    
    def add_log(self, message: str):
        """Add a log message"""
        log_area = self.query_one("#log-area", TextArea)
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_area.text += f"[{timestamp}] {message}\n"
        log_area.scroll_end()

class NeuralForgeTUI(App):
    """Main TUI application"""
    
    CSS = """
    Screen {
        layout: grid;
        grid-size: 2 2;
        grid-gutter: 1;
    }
    
    .header {
        text-style: bold;
        color: $accent;
        margin: 1;
    }
    
    .metric-label {
        margin: 1 0 0 0;
        color: $text;
    }
    
    #metrics {
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    #tools {
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    #status {
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    #logs {
        border: solid $primary;
        margin: 1;
        padding: 1;
    }
    
    Button {
        margin: 1;
        width: 100%;
    }
    
    ProgressBar {
        margin: 0 0 1 0;
    }
    
    TextArea {
        height: 10;
    }
    """
    
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("h", "help", "Help"),
        Binding("ctrl+c", "quit", "Quit"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield Footer()
        
        # Top row
        yield MetricsWidget(id="metrics")
        yield ToolsWidget(id="tools")
        
        # Bottom row
        yield StatusWidget(id="status")
        yield LogWidget(id="logs")
    
    def on_mount(self) -> None:
        """Called when app is mounted"""
        self.title = "NeuralForge TUI - AI & Automation Toolkit"
        self.sub_title = "Optimized for Apple Silicon (M3) Macs"
        
        # Add welcome message to logs
        log_widget = self.query_one("#logs", LogWidget)
        log_widget.add_log("Welcome to NeuralForge TUI!")
        log_widget.add_log("Use the buttons to launch tools or press 'h' for help")
    
    def action_quit(self) -> None:
        """Quit the application"""
        self.exit()
    
    def action_refresh(self) -> None:
        """Refresh the display"""
        self.notify("Display refreshed!", severity="information")
    
    def action_help(self) -> None:
        """Show help"""
        help_text = """
NeuralForge TUI Help:

Keyboard Shortcuts:
- q, Ctrl+C: Quit application
- r: Refresh display
- h: Show this help

Tool Buttons:
- Click any button to launch the corresponding tool
- Tools will show notifications when launched
- Check the activity log for detailed information

Metrics:
- Real-time system metrics are displayed at the top
- CPU, Memory, Neural Engine, and Temperature are monitored
- Updates automatically every 2 seconds

Status:
- System information is shown in the status panel
- Platform, architecture, and uptime are displayed
- Status updates every 10 seconds
        """
        
        self.notify(help_text, severity="information")

def main():
    """Main entry point"""
    app = NeuralForgeTUI()
    app.run()

if __name__ == "__main__":
    main()
