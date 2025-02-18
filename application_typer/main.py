# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "typer"
# ]
# ///

import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()
@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Directory to search in."),
         delete: bool = typer.Option(False, help="Delete the files found.")):
    """
    affiche les fichiers trouvés l'extension donnée.
    """

    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(f"Le répertoire {directory} n'existe pas.", fg=typer.colors.RED)
        raise typer.Exit()
    
    files = list(directory.rglob(f"*.{extension}"))
    count = len(files)

    if count == 0:
        typer.secho(f"Aucun fichier trouvé avec l'extension {extension}.", fg=typer.colors.YELLOW)
        return
    
    typer.secho(f"Fichiers trouvés avec l'extension {extension}: {count}", fg=typer.colors.GREEN)


    if delete:
        typer.confirm("Voulez-vous vraiment supprimer ces fichiers ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Fichier supprimé : {file}", fg=typer.colors.YELLOW)
    else:
        for file in files:
            typer.echo(file)

@app.command()
def search(extension: str):
    """Recherche les fichiers avec l'extension donnée."""
    main(extension=extension, directory=None, delete=False)

@app.command()
def delete(extension: str):
    """Supprime les fichiers avec l'extension donnée."""
    main(extension=extension, directory=None, delete=True)

if __name__ == "__main__":
    app()