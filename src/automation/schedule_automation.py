"""
Schedule automation module for NeuralForge
"""
import schedule
import time
import threading
from datetime import datetime, timedelta
from rich.console import Console
from typing import Callable, Dict, Any
import json

console = Console()

class ScheduleAutomation:
    """
    Schedule automation for NeuralForge.
    
    Features:
    - Schedule tasks at specific times
    - Recurring tasks (daily, weekly, monthly)
    - Task management and monitoring
    - Background execution
    """
    
    def __init__(self):
        self.tasks = {}
        self.running = False
        self.scheduler_thread = None
    
    def add_task(self, task_id: str, func: Callable, schedule_time: str, **kwargs) -> bool:
        """
        Add a scheduled task.
        
        Args:
            task_id: Unique identifier for the task
            func: Function to execute
            schedule_time: When to run (e.g., "10:30", "daily", "weekly")
            **kwargs: Additional arguments for the function
        """
        try:
            if schedule_time == "daily":
                schedule.every().day.at("00:00").do(self._execute_task, task_id, func, **kwargs)
            elif schedule_time == "weekly":
                schedule.every().monday.do(self._execute_task, task_id, func, **kwargs)
            elif schedule_time == "monthly":
                schedule.every().month.do(self._execute_task, task_id, func, **kwargs)
            elif ":" in schedule_time:
                schedule.every().day.at(schedule_time).do(self._execute_task, task_id, func, **kwargs)
            else:
                console.print(f"[red]❌ Invalid schedule time: {schedule_time}[/red]")
                return False
            
            self.tasks[task_id] = {
                "func": func,
                "schedule_time": schedule_time,
                "last_run": None,
                "status": "scheduled",
                "kwargs": kwargs
            }
            
            console.print(f"[green]✅ Task '{task_id}' scheduled for {schedule_time}[/green]")
            return True
            
        except Exception as e:
            console.print(f"[red]❌ Failed to schedule task: {e}[/red]")
            return False
    
    def _execute_task(self, task_id: str, func: Callable, **kwargs):
        """Execute a scheduled task."""
        try:
            console.print(f"[blue]🔄 Executing task: {task_id}[/blue]")
            self.tasks[task_id]["last_run"] = datetime.now()
            self.tasks[task_id]["status"] = "running"
            
            # Execute the function
            result = func(**kwargs)
            
            self.tasks[task_id]["status"] = "completed"
            console.print(f"[green]✅ Task '{task_id}' completed successfully[/green]")
            
        except Exception as e:
            self.tasks[task_id]["status"] = "failed"
            console.print(f"[red]❌ Task '{task_id}' failed: {e}[/red]")
    
    def start_scheduler(self):
        """Start the scheduler in background thread."""
        if self.running:
            console.print("[yellow]⚠️ Scheduler already running[/yellow]")
            return
        
        self.running = True
        self.scheduler_thread = threading.Thread(target=self._run_scheduler, daemon=True)
        self.scheduler_thread.start()
        console.print("[green]✅ Scheduler started[/green]")
    
    def _run_scheduler(self):
        """Run the scheduler loop."""
        while self.running:
            schedule.run_pending()
            time.sleep(1)
    
    def stop_scheduler(self):
        """Stop the scheduler."""
        self.running = False
        if self.scheduler_thread:
            self.scheduler_thread.join()
        console.print("[yellow]⏹️ Scheduler stopped[/yellow]")
    
    def get_task_status(self, task_id: str = None) -> Dict[str, Any]:
        """Get status of tasks."""
        if task_id:
            return self.tasks.get(task_id, {})
        return self.tasks
    
    def remove_task(self, task_id: str) -> bool:
        """Remove a scheduled task."""
        if task_id in self.tasks:
            del self.tasks[task_id]
            console.print(f"[green]✅ Task '{task_id}' removed[/green]")
            return True
        else:
            console.print(f"[red]❌ Task '{task_id}' not found[/red]")
            return False

def example_task():
    """Example task function."""
    console.print("🔄 Running example task...")
    time.sleep(2)
    console.print("✅ Example task completed")

def main():
    """Example usage of ScheduleAutomation."""
    console.print("⏰ Schedule Automation Module")
    console.print("=" * 40)
    
    # Create scheduler
    scheduler = ScheduleAutomation()
    
    # Add example tasks
    scheduler.add_task("daily_cleanup", example_task, "daily")
    scheduler.add_task("hourly_check", example_task, "10:30")
    
    # Start scheduler
    scheduler.start_scheduler()
    
    # Show status
    console.print("📊 Task Status:")
    for task_id, task_info in scheduler.get_task_status().items():
        console.print(f"  {task_id}: {task_info['status']} (scheduled for {task_info['schedule_time']})")
    
    # Keep running for demonstration
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        scheduler.stop_scheduler()

if __name__ == "__main__":
    main()
