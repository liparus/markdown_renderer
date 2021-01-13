#
# Markdown render example
# -----------------------
#
# Render README.md file (markdown files)
#
# Dependency: Rich (pip install rich)
# https://github.com/willmcgugan/ric
#


from rich.console import Console
from rich.markdown import Markdown
import sys

file = sys.argv[1]

console = Console()
with open(file) as readme:
    markdown = Markdown(readme.read())
console.print(markdown)
