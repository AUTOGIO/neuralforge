"""
Modern GUI Dashboard for NeuralForge
Beautiful graphical interface using tkinter and customtkinter
"""
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import threading
import time
import psutil
import platform
from datetime import datetime
import subprocess
import sys
from pathlib import Path

# Configure customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NeuralForgeGUI:
    """Modern GUI Dashboard for NeuralForge"""
    
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("NeuralForge - AI & Automation Toolkit")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        
        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        
        # Variables
        self.monitoring = False
        self.metrics_data = {
            'cpu': 0,
            'memory': 0,
            'neural_engine': 0,
            'temperature': 0,
            'power': 0
        }
        
        self.setup_ui()
        self.start_metrics_update()
    
    def setup_ui(self):
        """Setup the main UI"""
        # Main container
        main_frame = ctk.CTkFrame(self.root)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Header
        self.create_header(main_frame)
        
        # Content area
        content_frame = ctk.CTkFrame(main_frame)
        content_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Sidebar
        self.create_sidebar(content_frame)
        
        # Main content
        self.create_main_content(content_frame)
        
        # Footer
        self.create_footer(main_frame)
    
    def create_header(self, parent):
        """Create header section"""
        header_frame = ctk.CTkFrame(parent)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Logo and title
        logo_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        logo_frame.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        
        title_label = ctk.CTkLabel(
            logo_frame,
            text="🧠 NeuralForge",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.grid(row=0, column=0, sticky="w")
        
        subtitle_label = ctk.CTkLabel(
            logo_frame,
            text="AI & Automation Toolkit for Apple Silicon",
            font=ctk.CTkFont(size=14),
            text_color="gray"
        )
        subtitle_label.grid(row=1, column=0, sticky="w")
        
        # Status indicator
        status_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        status_frame.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="🟢 System Healthy",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="green"
        )
        self.status_label.grid(row=0, column=0, sticky="e")
        
        platform_label = ctk.CTkLabel(
            status_frame,
            text=f"{platform.system()} {platform.machine()}",
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        platform_label.grid(row=1, column=0, sticky="e")
    
    def create_sidebar(self, parent):
        """Create sidebar with tools"""
        sidebar_frame = ctk.CTkFrame(parent, width=250)
        sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)
        sidebar_frame.grid_propagate(False)
        
        # Tools title
        tools_title = ctk.CTkLabel(
            sidebar_frame,
            text="🛠️ Tools",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        tools_title.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        # Tools list
        tools = [
            ("🧠 Neural Monitor", self.launch_neural_monitor),
            ("💾 AI Memory", self.launch_ai_memory),
            ("📁 File Organizer", self.launch_file_organizer),
            ("🌐 Web Scraper", self.launch_web_scraper),
            ("📧 Email Auto", self.launch_email_automation),
            ("⏰ Schedule", self.launch_schedule_automation),
            ("📊 Analytics", self.show_analytics),
            ("⚙️ Settings", self.show_settings)
        ]
        
        for i, (name, command) in enumerate(tools):
            btn = ctk.CTkButton(
                sidebar_frame,
                text=name,
                command=command,
                height=40,
                font=ctk.CTkFont(size=14),
                anchor="w"
            )
            btn.grid(row=i+1, column=0, sticky="ew", padx=20, pady=5)
    
    def create_main_content(self, parent):
        """Create main content area"""
        main_content = ctk.CTkFrame(parent)
        main_content.grid(row=0, column=1, sticky="nsew", padx=(5, 10), pady=10)
        main_content.grid_columnconfigure(0, weight=1)
        main_content.grid_rowconfigure(1, weight=1)
        
        # Metrics section
        self.create_metrics_section(main_content)
        
        # Content area
        self.content_area = ctk.CTkFrame(main_content)
        self.content_area.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.content_area.grid_columnconfigure(0, weight=1)
        self.content_area.grid_rowconfigure(0, weight=1)
        
        # Default content
        self.show_dashboard_content()
    
    def create_metrics_section(self, parent):
        """Create system metrics section"""
        metrics_frame = ctk.CTkFrame(parent)
        metrics_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        metrics_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        # CPU
        self.cpu_frame = ctk.CTkFrame(metrics_frame)
        self.cpu_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.cpu_label = ctk.CTkLabel(self.cpu_frame, text="CPU", font=ctk.CTkFont(weight="bold"))
        self.cpu_label.grid(row=0, column=0, padx=10, pady=5)
        self.cpu_value = ctk.CTkLabel(self.cpu_frame, text="0%", font=ctk.CTkFont(size=16))
        self.cpu_value.grid(row=1, column=0, padx=10, pady=5)
        self.cpu_progress = ctk.CTkProgressBar(self.cpu_frame)
        self.cpu_progress.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        # Memory
        self.memory_frame = ctk.CTkFrame(metrics_frame)
        self.memory_frame.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.memory_label = ctk.CTkLabel(self.memory_frame, text="Memory", font=ctk.CTkFont(weight="bold"))
        self.memory_label.grid(row=0, column=0, padx=10, pady=5)
        self.memory_value = ctk.CTkLabel(self.memory_frame, text="0%", font=ctk.CTkFont(size=16))
        self.memory_value.grid(row=1, column=0, padx=10, pady=5)
        self.memory_progress = ctk.CTkProgressBar(self.memory_frame)
        self.memory_progress.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        # Neural Engine
        self.neural_frame = ctk.CTkFrame(metrics_frame)
        self.neural_frame.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        self.neural_label = ctk.CTkLabel(self.neural_frame, text="Neural Engine", font=ctk.CTkFont(weight="bold"))
        self.neural_label.grid(row=0, column=0, padx=10, pady=5)
        self.neural_value = ctk.CTkLabel(self.neural_frame, text="0%", font=ctk.CTkFont(size=16))
        self.neural_value.grid(row=1, column=0, padx=10, pady=5)
        self.neural_progress = ctk.CTkProgressBar(self.neural_frame)
        self.neural_progress.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        
        # Temperature
        self.temp_frame = ctk.CTkFrame(metrics_frame)
        self.temp_frame.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
        self.temp_label = ctk.CTkLabel(self.temp_frame, text="Temperature", font=ctk.CTkFont(weight="bold"))
        self.temp_label.grid(row=0, column=0, padx=10, pady=5)
        self.temp_value = ctk.CTkLabel(self.temp_frame, text="0°C", font=ctk.CTkFont(size=16))
        self.temp_value.grid(row=1, column=0, padx=10, pady=5)
        
        # Power
        self.power_frame = ctk.CTkFrame(metrics_frame)
        self.power_frame.grid(row=0, column=4, sticky="ew", padx=5, pady=5)
        self.power_label = ctk.CTkLabel(self.power_frame, text="Power", font=ctk.CTkFont(weight="bold"))
        self.power_label.grid(row=0, column=0, padx=10, pady=5)
        self.power_value = ctk.CTkLabel(self.power_frame, text="0W", font=ctk.CTkFont(size=16))
        self.power_value.grid(row=1, column=0, padx=10, pady=5)
    
    def create_footer(self, parent):
        """Create footer section"""
        footer_frame = ctk.CTkFrame(parent, fg_color="transparent")
        footer_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        
        footer_text = ctk.CTkLabel(
            footer_frame,
            text="NeuralForge Dashboard • Press Ctrl+C to exit • Last updated: " + datetime.now().strftime('%H:%M:%S'),
            font=ctk.CTkFont(size=12),
            text_color="gray"
        )
        footer_text.grid(row=0, column=0, sticky="w")
    
    def start_metrics_update(self):
        """Start updating metrics in background"""
        def update_metrics():
            while True:
                try:
                    # Get system metrics
                    cpu_percent = psutil.cpu_percent(interval=1)
                    memory = psutil.virtual_memory()
                    
                    # Update GUI (must be done in main thread)
                    self.root.after(0, self.update_metrics_display, {
                        'cpu': cpu_percent,
                        'memory': memory.percent,
                        'neural_engine': min(cpu_percent * 1.2, 100),
                        'temperature': 35 + (cpu_percent * 0.3),
                        'power': 10 + (cpu_percent * 0.2)
                    })
                    
                    time.sleep(2)
                except Exception as e:
                    print(f"Error updating metrics: {e}")
                    time.sleep(5)
        
        # Start metrics update in background thread
        metrics_thread = threading.Thread(target=update_metrics, daemon=True)
        metrics_thread.start()
    
    def update_metrics_display(self, metrics):
        """Update metrics display in main thread"""
        self.cpu_value.configure(text=f"{metrics['cpu']:.1f}%")
        self.cpu_progress.set(metrics['cpu'] / 100)
        
        self.memory_value.configure(text=f"{metrics['memory']:.1f}%")
        self.memory_progress.set(metrics['memory'] / 100)
        
        self.neural_value.configure(text=f"{metrics['neural_engine']:.1f}%")
        self.neural_progress.set(metrics['neural_engine'] / 100)
        
        self.temp_value.configure(text=f"{metrics['temperature']:.1f}°C")
        self.power_value.configure(text=f"{metrics['power']:.1f}W")
    
    def show_dashboard_content(self):
        """Show default dashboard content"""
        # Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        # Welcome message
        welcome_label = ctk.CTkLabel(
            self.content_area,
            text="Welcome to NeuralForge Dashboard",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        welcome_label.grid(row=0, column=0, pady=20)
        
        # Description
        desc_label = ctk.CTkLabel(
            self.content_area,
            text="Select a tool from the sidebar to get started with AI automation",
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        desc_label.grid(row=1, column=0, pady=10)
    
    def launch_neural_monitor(self):
        """Launch neural monitor"""
        self.show_tool_content("Neural Engine Monitor", "Starting neural engine monitoring...")
        # Here you would launch the actual neural monitor
    
    def launch_ai_memory(self):
        """Launch AI memory system"""
        self.show_tool_content("AI Memory System", "Accessing AI memory database...")
        # Here you would launch the actual AI memory system
    
    def launch_file_organizer(self):
        """Launch file organizer"""
        self.show_tool_content("File Organizer", "Analyzing file system...")
        # Here you would launch the actual file organizer
    
    def launch_web_scraper(self):
        """Launch web scraper"""
        self.show_tool_content("Web Scraper", "Initializing web scraping engine...")
        # Here you would launch the actual web scraper
    
    def launch_email_automation(self):
        """Launch email automation"""
        self.show_tool_content("Email Automation", "Setting up email workflows...")
        # Here you would launch the actual email automation
    
    def launch_schedule_automation(self):
        """Launch schedule automation"""
        self.show_tool_content("Schedule Automation", "Loading task scheduler...")
        # Here you would launch the actual schedule automation
    
    def show_analytics(self):
        """Show analytics dashboard"""
        self.show_tool_content("Analytics Dashboard", "Generating performance reports...")
        # Here you would show analytics
    
    def show_settings(self):
        """Show settings"""
        self.show_tool_content("Settings", "Opening configuration panel...")
        # Here you would show settings
    
    def show_tool_content(self, tool_name, message):
        """Show tool content in main area"""
        # Clear content area
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        # Tool title
        title_label = ctk.CTkLabel(
            self.content_area,
            text=tool_name,
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title_label.grid(row=0, column=0, pady=20)
        
        # Tool message
        message_label = ctk.CTkLabel(
            self.content_area,
            text=message,
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        message_label.grid(row=1, column=0, pady=10)
    
    def run(self):
        """Run the GUI application"""
        self.root.mainloop()

def main():
    """Main entry point"""
    app = NeuralForgeGUI()
    app.run()

if __name__ == "__main__":
    main()
