# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer

def main(
    delete: bool = typer.Option(False, "--delete", "-d", help="Supprime les fichiers trouvés"),
    extension: str = typer.Argument("txt", help="Extension des fichiers à rechercher")):
    """
    This script demonstrates the usage of the Typer library for creating a command-line interface.
    """
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    if delete:
        confirm = typer.confirm("Êtes-vous sûr de vouloir supprimer ces fichiers ?")
        if not confirm:
            typer.echo("Opération annulée")
            raise typer.Abort()
    
    typer.echo("Suppression du fichiers")



if __name__  == "__main__":
    typer.run(main)