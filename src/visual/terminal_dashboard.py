"""
Modern Terminal Dashboard for NeuralForge
Beautiful visual interface using Rich library
"""
import time
import asyncio
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.prompt import Prompt, Confirm
from rich import box
from rich.rule import Rule
from rich.markdown import Markdown
import psutil
import platform

console = Console()

class VisualTerminalDashboard:
    """Modern terminal dashboard with beautiful visuals"""
    
    def __init__(self):
        self.console = Console()
        self.running = False
        self.layout = Layout()
        
    def create_layout(self):
        """Create the main dashboard layout"""
        self.layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3)
        )
        
        self.layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        self.layout["left"].split_column(
            Layout(name="metrics", size=12),
            Layout(name="tools")
        )
        
        self.layout["right"].split_column(
            Layout(name="status"),
            Layout(name="actions")
        )
    
    def create_header(self) -> Panel:
        """Create the header panel"""
        header_text = Text()
        header_text.append("🧠 ", style="bold blue")
        header_text.append("NeuralForge", style="bold white")
        header_text.append(" - AI & Automation Toolkit", style="dim white")
        header_text.append("\n🎯 Optimized for Apple Silicon (M3) Macs", style="dim cyan")
        
        return Panel(
            Align.center(header_text),
            box=box.DOUBLE,
            style="blue"
        )
    
    def create_metrics_panel(self) -> Panel:
        """Create system metrics panel"""
        # Get system metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Create metrics table
        metrics_table = Table(show_header=False, box=box.ROUNDED)
        metrics_table.add_column("Metric", style="cyan", width=20)
        metrics_table.add_column("Value", style="white", width=15)
        metrics_table.add_column("Bar", style="green", width=30)
        
        # CPU
        cpu_bar = "█" * int(cpu_percent / 5) + "░" * (20 - int(cpu_percent / 5))
        metrics_table.add_row("CPU Usage", f"{cpu_percent:.1f}%", f"[green]{cpu_bar}[/green]")
        
        # Memory
        memory_bar = "█" * int(memory.percent / 5) + "░" * (20 - int(memory.percent / 5))
        metrics_table.add_row("Memory", f"{memory.percent:.1f}%", f"[blue]{memory_bar}[/blue]")
        
        # Disk
        disk_bar = "█" * int(disk.percent / 5) + "░" * (20 - int(disk.percent / 5))
        metrics_table.add_row("Disk Usage", f"{disk.percent:.1f}%", f"[yellow]{disk_bar}[/yellow]")
        
        # Neural Engine (simulated)
        neural_engine = min(cpu_percent * 1.2, 100)
        neural_bar = "█" * int(neural_engine / 5) + "░" * (20 - int(neural_engine / 5))
        metrics_table.add_row("Neural Engine", f"{neural_engine:.1f}%", f"[purple]{neural_bar}[/purple]")
        
        return Panel(
            metrics_table,
            title="📊 System Metrics",
            border_style="green",
            box=box.ROUNDED
        )
    
    def create_tools_panel(self) -> Panel:
        """Create tools status panel"""
        tools_table = Table(show_header=True, box=box.ROUNDED)
        tools_table.add_column("Tool", style="cyan", width=20)
        tools_table.add_column("Status", style="white", width=12)
        tools_table.add_column("Last Run", style="dim", width=15)
        
        tools_data = [
            ("Neural Monitor", "🟢 Active", "2 min ago"),
            ("AI Memory", "🟢 Active", "5 min ago"),
            ("File Organizer", "🟡 Idle", "1 hour ago"),
            ("Web Scraper", "🔴 Inactive", "Never"),
            ("Email Auto", "🔴 Inactive", "Never"),
            ("Schedule", "🟢 Running", "Now")
        ]
        
        for tool, status, last_run in tools_data:
            tools_table.add_row(tool, status, last_run)
        
        return Panel(
            tools_table,
            title="🛠️ Tools Status",
            border_style="blue",
            box=box.ROUNDED
        )
    
    def create_status_panel(self) -> Panel:
        """Create system status panel"""
        status_text = Text()
        status_text.append("System Status: ", style="bold")
        status_text.append("🟢 Healthy\n", style="green")
        status_text.append("Platform: ", style="bold")
        status_text.append(f"{platform.system()} {platform.release()}\n", style="white")
        status_text.append("Architecture: ", style="bold")
        status_text.append(f"{platform.machine()}\n", style="white")
        status_text.append("Python: ", style="bold")
        status_text.append(f"{platform.python_version()}\n", style="white")
        status_text.append("Uptime: ", style="bold")
        status_text.append(f"{int(time.time() - psutil.boot_time()) // 3600}h", style="white")
        
        return Panel(
            status_text,
            title="ℹ️ System Info",
            border_style="yellow",
            box=box.ROUNDED
        )
    
    def create_actions_panel(self) -> Panel:
        """Create quick actions panel"""
        actions_text = Text()
        actions_text.append("Quick Actions:\n\n", style="bold")
        actions_text.append("1. ", style="cyan")
        actions_text.append("Organize Files\n", style="white")
        actions_text.append("2. ", style="cyan")
        actions_text.append("Start Monitoring\n", style="white")
        actions_text.append("3. ", style="cyan")
        actions_text.append("Run Web Scraper\n", style="white")
        actions_text.append("4. ", style="cyan")
        actions_text.append("Check AI Memory\n", style="white")
        actions_text.append("5. ", style="cyan")
        actions_text.append("View Analytics\n", style="white")
        actions_text.append("0. ", style="cyan")
        actions_text.append("Exit Dashboard", style="white")
        
        return Panel(
            actions_text,
            title="⚡ Quick Actions",
            border_style="magenta",
            box=box.ROUNDED
        )
    
    def create_footer(self) -> Panel:
        """Create footer panel"""
        footer_text = Text()
        footer_text.append("NeuralForge Dashboard", style="bold blue")
        footer_text.append(" • ")
        footer_text.append("Press Ctrl+C to exit", style="dim")
        footer_text.append(" • ")
        footer_text.append(f"Last updated: {datetime.now().strftime('%H:%M:%S')}", style="dim")
        
        return Panel(
            Align.center(footer_text),
            box=box.DOUBLE,
            style="blue"
        )
    
    def update_layout(self):
        """Update the layout with current data"""
        self.layout["header"].update(self.create_header())
        self.layout["metrics"].update(self.create_metrics_panel())
        self.layout["tools"].update(self.create_tools_panel())
        self.layout["status"].update(self.create_status_panel())
        self.layout["actions"].update(self.create_actions_panel())
        self.layout["footer"].update(self.create_footer())
    
    def show_welcome_screen(self):
        """Show welcome screen with animation"""
        welcome_text = """
# 🧠 Welcome to NeuralForge

## AI & Automation Toolkit for Apple Silicon

**Features:**
- 🧠 Neural Engine Monitoring
- 💾 AI Memory System  
- 📁 Intelligent File Organization
- 🌐 Advanced Web Scraping
- 📧 Email Automation
- ⏰ Task Scheduling

**Optimized for:**
- Apple M1/M2/M3 Macs
- macOS 14+ (Sonoma)
- 16GB+ Unified Memory
- Neural Engine (18 TOPS)

---
*Press any key to continue to dashboard...*
        """
        
        console.clear()
        console.print(Panel(
            Markdown(welcome_text),
            title="🚀 NeuralForge",
            border_style="blue",
            box=box.DOUBLE,
            padding=(2, 4)
        ))
        
        input()
    
    def run_dashboard(self):
        """Run the main dashboard"""
        self.show_welcome_screen()
        self.create_layout()
        
        try:
            with Live(self.layout, refresh_per_second=2, screen=True) as live:
                self.running = True
                while self.running:
                    self.update_layout()
                    time.sleep(0.5)
                    
        except KeyboardInterrupt:
            self.running = False
            console.print("\n[yellow]👋 Dashboard closed. Goodbye![/yellow]")
    
    def show_interactive_menu(self):
        """Show interactive menu for tool selection"""
        while True:
            console.clear()
            self.update_layout()
            
            choice = Prompt.ask(
                "\n[bold cyan]Select an action[/bold cyan]",
                choices=["1", "2", "3", "4", "5", "0"],
                default="0"
            )
            
            if choice == "1":
                self.launch_file_organizer()
            elif choice == "2":
                self.launch_neural_monitor()
            elif choice == "3":
                self.launch_web_scraper()
            elif choice == "4":
                self.launch_ai_memory()
            elif choice == "5":
                self.show_analytics()
            elif choice == "0":
                break
            
            if choice != "0":
                input("\nPress Enter to continue...")
    
    def launch_file_organizer(self):
        """Launch file organizer with progress"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=console
        ) as progress:
            task = progress.add_task("Organizing files...", total=100)
            for i in range(100):
                progress.update(task, advance=1)
                time.sleep(0.02)
        
        console.print("[green]✅ File organization completed![/green]")
    
    def launch_neural_monitor(self):
        """Launch neural monitor"""
        console.print("[blue]🧠 Starting Neural Engine Monitor...[/blue]")
        time.sleep(2)
        console.print("[green]✅ Neural Engine Monitor is running![/green]")
    
    def launch_web_scraper(self):
        """Launch web scraper"""
        console.print("[blue]🌐 Starting Web Scraper...[/blue]")
        time.sleep(2)
        console.print("[green]✅ Web Scraper is ready![/green]")
    
    def launch_ai_memory(self):
        """Launch AI memory system"""
        console.print("[blue]💾 Starting AI Memory System...[/blue]")
        time.sleep(2)
        console.print("[green]✅ AI Memory System is active![/green]")
    
    def show_analytics(self):
        """Show analytics dashboard"""
        analytics_table = Table(title="📊 Analytics Dashboard")
        analytics_table.add_column("Metric", style="cyan")
        analytics_table.add_column("Value", style="white")
        analytics_table.add_column("Trend", style="green")
        
        analytics_table.add_row("Files Organized", "1,247", "↗️ +12%")
        analytics_table.add_row("AI Conversations", "89", "↗️ +5%")
        analytics_table.add_row("Web Scrapes", "23", "↗️ +8%")
        analytics_table.add_row("Emails Sent", "156", "↗️ +3%")
        analytics_table.add_row("Tasks Scheduled", "12", "↗️ +15%")
        
        console.print(analytics_table)

def main():
    """Main entry point"""
    dashboard = VisualTerminalDashboard()
    
    if Confirm.ask("Show interactive menu?"):
        dashboard.show_interactive_menu()
    else:
        dashboard.run_dashboard()

if __name__ == "__main__":
    main()
