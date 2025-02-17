# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer

app = typer.Typer()

def main(
    delete: bool = typer.Option(False, "--delete", "-d", help="Supprime les fichiers trouvés"),
    extension: str = typer.Argument("txt", help="Extension des fichiers à rechercher")):
    """
    This script demonstrates the usage of the Typer library for creating a command-line interface.
    """
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    if delete:  
        typer.echo("Suppression du fichiers")

@app.command("search")
def search_py():
    main(delete=False, extension="py")
@app.command("delete")
def delete_py():
    main(delete=True, extension="py")



if __name__  == "__main__":
    app()