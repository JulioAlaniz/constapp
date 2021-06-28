from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_text_basic():
    with open("README.md") as readme:
        markdown = Markdown(readme.read())

    console.print(markdown)
    console.print(":smiley:")
    console.print(
        "This a [b dark_red]text example [/b dark_red][b dark_goldenrod]with console  [/b dark_goldenrod][i][u light_sea_green] output[/u light_sea_green][/i]"
    )

print_text_basic()