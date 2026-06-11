"""
HackingTool Pro - Core Framework
Author: Kartikey Rai
"""

import os
import sys
import asyncio
import subprocess
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.layout import Layout
from rich.live import Live

from .database import DatabaseManager
from .config_manager import ConfigManager
from .plugin_manager import PluginManager
from utils.logger import get_logger


class ToolStatus(Enum):
    """Tool installation status."""
    NOT_INSTALLED = "not_installed"
    INSTALLING = "installing"
    INSTALLED = "installed"
    OUTDATED = "outdated"
    ERROR = "error"


@dataclass
class Tool:
    """Represents a hacking tool."""
    id: str
    name: str
    description: str
    category: str
    subcategory: Optional[str] = None
    install_cmd: Optional[str] = None
    update_cmd: Optional[str] = None
    uninstall_cmd: Optional[str] = None
    run_cmd: Optional[str] = None
    dependencies: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    version: str = "latest"
    author: str = ""
    github_url: str = ""
    website: str = ""
    status: ToolStatus = ToolStatus.NOT_INSTALLED
    is_favorite: bool = False
    last_used: Optional[str] = None
    usage_count: int = 0
    
    def __post_init__(self):
        if not self.id:
            self.id = self.name.lower().replace(" ", "_")


@dataclass
class Category:
    """Represents a tool category."""
    id: int
    name: str
    description: str
    icon: str
    color: str
    tools: List[Tool] = field(default_factory=list)


class HackingToolFramework:
    """
    Main framework class for HackingTool Pro.
    Manages tools, categories, and user interactions.
    """
    
    VERSION = "3.0.0"
    AUTHOR = "Kartikey Rai"
    GITHUB = "https://github.com/kartikey3205"
    
    CATEGORIES = [
        Category(1, "Information Gathering", "OSINT and reconnaissance tools", "🔍", "cyan"),
        Category(2, "Vulnerability Scanning", "Automated vulnerability scanners", "🔎", "red"),
        Category(3, "Exploitation", "Exploit frameworks and tools", "💥", "red"),
        Category(4, "Wireless Attacks", "WiFi and wireless security", "📡", "green"),
        Category(5, "Forensics", "Digital forensics tools", "🔬", "blue"),
        Category(6, "Post Exploitation", "Persistence and lateral movement", "🎯", "magenta"),
        Category(7, "Web Application", "Web app security testing", "🌐", "cyan"),
        Category(8, "Password Attacks", "Password cracking and recovery", "🔐", "yellow"),
        Category(9, "Sniffing & Spoofing", "Network traffic analysis", "👃", "green"),
        Category(10, "Reverse Engineering", "Binary analysis tools", "🔄", "blue"),
        Category(11, "Social Engineering", "Phishing and human factors", "🎭", "magenta"),
        Category(12, "Reporting", "Report generation tools", "📊", "white"),
        Category(13, "Cloud Security", "AWS, Azure, GCP security", "☁️", "cyan"),
        Category(14, "Active Directory", "AD enumeration and attacks", "🏢", "blue"),
        Category(15, "Mobile Security", "iOS and Android security", "📱", "green"),
        Category(16, "IoT Security", "Internet of Things security", "🔌", "yellow"),
        Category(17, "Blockchain", "Smart contract auditing", "⛓️", "white"),
        Category(18, "Steganography", "Data hiding techniques", "🖼️", "cyan"),
        Category(19, "DDoS Testing", "Stress testing tools", "⚡", "red"),
        Category(20, "Settings", "Configuration and preferences", "⚙️", "white"),
    ]
    
    def __init__(self, config: ConfigManager, db: DatabaseManager):
        self.config = config
        self.db = db
        self.console = Console()
        self.logger = get_logger()
        self.plugin_manager = PluginManager()
        self.tools_cache: Dict[str, Tool] = {}
        self.running = True
        
        self._init_tools()
    
    def _init_tools(self):
        """Initialize all tools from configuration."""
        # This would load from config files
        # For now, we'll have a sample implementation
        pass
    
    async def interactive_mode(self):
        """Run interactive menu system."""
        while self.running:
            self._display_main_menu()
            
            try:
                choice = IntPrompt.ask(
                    "\n[bold cyan]Select a category[/bold cyan]",
                    choices=[str(i) for i in range(0, 21)]
                )
                
                if choice == 0:
                    self.running = False
                    self.console.print("[yellow]Goodbye![/yellow]")
                    break
                
                await self.launch_category(choice)
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use option 0 to exit[/yellow]")
            except Exception as e:
                self.logger.error(f"Menu error: {e}")
                self.console.print(f"[red]Error: {e}[/red]")
    
    def _display_main_menu(self):
        """Display the main menu with categories."""
        self.console.clear()
        
        # Header
        header = Panel.fit(
            f"[bold cyan]HackingTool Pro[/bold cyan] [yellow]v{self.VERSION}[/yellow]\n"
            f"[dim]by {self.AUTHOR}[/dim]\n"
            f"[dim]{self.GITHUB}[/dim]",
            border_style="cyan"
        )
        self.console.print(header)
        
        # Categories table
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Icon")
        table.add_column("Category", style="bold")
        table.add_column("Description", style="dim")
        
        for cat in self.CATEGORIES:
            table.add_row(
                str(cat.id),
                cat.icon,
                f"[{cat.color}]{cat.name}[/{cat.color}]",
                cat.description
            )
        
        self.console.print(table)
        
        # Footer
        self.console.print("\n[dim]0. Exit | 99. Search | 100. Favorites | 101. Recent[/dim]")
    
    async def launch_category(self, category_id: int):
        """Launch a specific category menu."""
        category = next((c for c in self.CATEGORIES if c.id == category_id), None)
        
        if not category:
            self.console.print("[red]Invalid category[/red]")
            return
        
        self.console.clear()
        self.console.print(Panel.fit(
            f"{category.icon} [bold {category.color}]{category.name}[/bold {category.color}]",
            border_style=category.color
        ))
        
        # Get tools for this category
        tools = await self._get_tools_by_category(category_id)
        
        if not tools:
            self.console.print("[yellow]No tools available in this category[/yellow]")
            await asyncio.sleep(2)
            return
        
        # Display tools
        table = Table(show_header=True)
        table.add_column("#", style="cyan", justify="right")
        table.add_column("Name", style="bold")
        table.add_column("Description")
        table.add_column("Status")
        table.add_column("Version")
        
        for i, tool in enumerate(tools, 1):
            status_color = {
                ToolStatus.INSTALLED: "green",
                ToolStatus.NOT_INSTALLED: "red",
                ToolStatus.INSTALLING: "yellow",
                ToolStatus.OUTDATED: "orange",
                ToolStatus.ERROR: "red"
            }.get(tool.status, "white")
            
            table.add_row(
                str(i),
                tool.name,
                tool.description[:50] + "..." if len(tool.description) > 50 else tool.description,
                f"[{status_color}]{tool.status.value}[/{status_color}]",
                tool.version
            )
        
        self.console.print(table)
        
        # Tool selection
        choice = IntPrompt.ask(
            "\n[bold]Select a tool (0 to go back)[/bold]",
            choices=[str(i) for i in range(0, len(tools) + 1)]
        )
        
        if choice == 0:
            return
        
        selected_tool = tools[choice - 1]
        await self._tool_actions(selected_tool)
    
    async def _tool_actions(self, tool: Tool):
        """Display actions for a selected tool."""
        self.console.clear()
        self.console.print(Panel.fit(
            f"[bold cyan]{tool.name}[/bold cyan]\n"
            f"[dim]{tool.description}[/dim]",
            title="Tool Details",
            border_style="cyan"
        ))
        
        actions = []
        
        if tool.status == ToolStatus.INSTALLED:
            actions = [
                ("1", "Run Tool", self._run_tool),
                ("2", "Update Tool", self._update_tool),
                ("3", "Uninstall Tool", self._uninstall_tool),
                ("4", "View Documentation", self._view_docs),
                ("5", "Add to Favorites", self._toggle_favorite),
            ]
        else:
            actions = [
                ("1", "Install Tool", self._install_tool),
                ("2", "View Documentation", self._view_docs),
            ]
        
        for num, name, _ in actions:
            self.console.print(f"[cyan]{num}.[/cyan] {name}")
        
        self.console.print("[cyan]0.[/cyan] Back")
        
        choice = Prompt.ask("Select action", choices=[str(i) for i in range(0, 6)])
        
        if choice == "0":
            return
        
        action_map = {num: func for num, _, func in actions}
        if choice in action_map:
            await action_map[choice](tool)
    
    async def _run_tool(self, tool: Tool):
        """Execute a tool."""
        self.console.print(f"[green]Launching {tool.name}...[/green]")
        
        if tool.run_cmd:
            try:
                process = await asyncio.create_subprocess_shell(
                    tool.run_cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                
                stdout, stderr = await process.communicate()
                
                if stdout:
                    self.console.print(stdout.decode())
                if stderr:
                    self.console.print(f"[red]{stderr.decode()}[/red]")
                    
            except Exception as e:
                self.console.print(f"[red]Error running tool: {e}[/red]")
        
        Prompt.ask("\nPress Enter to continue")
    
    async def _install_tool(self, tool: Tool):
        """Install a tool."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console
        ) as progress:
            task = progress.add_task(f"Installing {tool.name}...", total=None)
            
            if tool.install_cmd:
                try:
                    process = await asyncio.create_subprocess_shell(
                        tool.install_cmd,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE
                    )
                    await process.communicate()
                    
                    tool.status = ToolStatus.INSTALLED
                    progress.update(task, description=f"[green]{tool.name} installed successfully![/green]")
                    
                except Exception as e:
                    tool.status = ToolStatus.ERROR
                    progress.update(task, description=f"[red]Installation failed: {e}[/red]")
            
            await asyncio.sleep(1)
        
        Prompt.ask("\nPress Enter to continue")
    
    async def _update_tool(self, tool: Tool):
        """Update a tool."""
        self.console.print(f"[yellow]Updating {tool.name}...[/yellow]")
        # Implementation similar to install
        Prompt.ask("\nPress Enter to continue")
    
    async def _uninstall_tool(self, tool: Tool):
        """Uninstall a tool."""
        if Confirm.ask(f"Are you sure you want to uninstall {tool.name}?"):
            self.console.print(f"[yellow]Uninstalling {tool.name}...[/yellow]")
            # Implementation
        Prompt.ask("\nPress Enter to continue")
    
    async def _view_docs(self, tool: Tool):
        """View tool documentation."""
        self.console.print(Panel(tool.description, title=f"{tool.name} Documentation"))
        if tool.github_url:
            self.console.print(f"\n[link={tool.github_url}]GitHub: {tool.github_url}[/link]")
        if tool.website:
            self.console.print(f"[link={tool.website}]Website: {tool.website}[/link]")
        Prompt.ask("\nPress Enter to continue")
    
    async def _toggle_favorite(self, tool: Tool):
        """Toggle favorite status."""
        tool.is_favorite = not tool.is_favorite
        status = "added to" if tool.is_favorite else "removed from"
        self.console.print(f"[green]{tool.name} {status} favorites[/green]")
        await asyncio.sleep(1)
    
    async def _get_tools_by_category(self, category_id: int) -> List[Tool]:
        """Get all tools in a category."""
        # This would query the database
        # Placeholder implementation
        return []
    
    async def search_tools(self, query: str):
        """Search for tools."""
        self.console.print(f"[cyan]Searching for: {query}[/cyan]")
        # Implementation
        Prompt.ask("\nPress Enter to continue")
    
    async def launch_tool(self, tool_name: str):
        """Launch a specific tool by name."""
        self.console.print(f"[cyan]Launching {tool_name}...[/cyan]")
        # Implementation