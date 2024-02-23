from rich.console import Console
from rich.markdown import Markdown
import sys

console = Console()

def display(fd):
    with open(fd, "r+") as xfile:
        console.print(Markdown(xfile.read()))
    sys.exit(0)
   
display(sys.argv[1])
