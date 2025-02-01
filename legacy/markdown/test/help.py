from rich.console import Console
from rich.markdown import Markdown
import sys

console = Console()


def display_help():
    with open("help.md", "r+") as help_file:
        console.print(Markdown(help_file.read()))
    sys.exit(0)
   

if len(sys.argv) >= 2:
    if sys.argv[1].lower() == "help":
            display_help()
