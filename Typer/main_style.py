# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer

def main():
    name = typer.style("Python", bold=True, fg=typer.colors.RED)
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)