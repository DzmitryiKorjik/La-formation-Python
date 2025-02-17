# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer

def main(extension: str = typer.Argument(..., help="Extension des fichiers à rechercher")):
    """
    This script demonstrates the usage of the Typer library for creating a command-line interface.
    """
    if not extension:
        typer.echo("Veuillez fournir une extension de fichier.")
        return

    typer.echo(f"Recherches des fichiers avec l'extension {extension}.")


if __name__  == "__main__":
    typer.run(main)