"""
Email automation module for NeuralForge
"""
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from rich.console import Console
from typing import List, Dict, Optional
import os

console = Console()

class EmailAutomation:
    """
    Email automation for NeuralForge.
    
    Features:
    - Send emails with attachments
    - Bulk email sending
    - Email templates
    - SMTP configuration
    """
    
    def __init__(self, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = os.getenv("SMTP_USERNAME")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.connection = None
    
    def connect(self) -> bool:
        """Connect to SMTP server."""
        try:
            self.connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.connection.starttls()
            self.connection.login(self.smtp_username, self.smtp_password)
            console.print("[green]✅ Connected to SMTP server[/green]")
            return True
        except Exception as e:
            console.print(f"[red]❌ Failed to connect: {e}[/red]")
            return False
    
    def send_email(self, to: str, subject: str, body: str, attachments: List[str] = None) -> bool:
        """Send a single email."""
        if not self.connection:
            if not self.connect():
                return False
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_username
            msg['To'] = to
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Add attachments
            if attachments:
                for file_path in attachments:
                    if os.path.isfile(file_path):
                        with open(file_path, "rb") as attachment:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(attachment.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename= {os.path.basename(file_path)}'
                            )
                            msg.attach(part)
            
            self.connection.send_message(msg)
            console.print(f"[green]✅ Email sent to {to}[/green]")
            return True
            
        except Exception as e:
            console.print(f"[red]❌ Failed to send email: {e}[/red]")
            return False
    
    def send_bulk_emails(self, recipients: List[Dict[str, str]], template: str) -> Dict[str, int]:
        """Send bulk emails using template."""
        results = {"success": 0, "failed": 0}
        
        for recipient in recipients:
            personalized_body = template.format(**recipient)
            if self.send_email(recipient["email"], recipient["subject"], personalized_body):
                results["success"] += 1
            else:
                results["failed"] += 1
        
        console.print(f"[blue]📊 Bulk email results: {results['success']} sent, {results['failed']} failed[/blue]")
        return results
    
    def disconnect(self):
        """Disconnect from SMTP server."""
        if self.connection:
            self.connection.quit()
            console.print("[yellow]🔌 Disconnected from SMTP server[/yellow]")

def main():
    """Example usage of EmailAutomation."""
    console.print("📧 Email Automation Module")
    console.print("=" * 40)
    
    # Example usage
    email_automation = EmailAutomation()
    
    if email_automation.connect():
        # Send test email
        email_automation.send_email(
            to="test@example.com",
            subject="NeuralForge Test Email",
            body="This is a test email from NeuralForge automation module."
        )
        email_automation.disconnect()

if __name__ == "__main__":
    main()
