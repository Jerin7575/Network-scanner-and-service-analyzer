from rich.console import Console
from rich.panel import Panel

console = Console()


def print_banner():
    banner = """
███╗   ██╗███████╗████████╗
████╗  ██║██╔════╝╚══██╔══╝
██╔██╗ ██║█████╗     ██║
██║╚██╗██║██╔══╝     ██║
██║ ╚████║███████╗   ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝

Network Scanner & Service Analyzer
"""

    console.print(
        Panel.fit(
            banner,
            title="[cyan]Python Cybersecurity Project[/cyan]",
            border_style="green"
        )
    )


def info(message):
    console.print(f"[cyan][*][/cyan] {message}")


def success(message):
    console.print(f"[green][+][/green] {message}")


def warning(message):
    console.print(f"[yellow][!][/yellow] {message}")


def error(message):
    console.print(f"[red][-][/red] {message}")
