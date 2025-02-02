from pathlib import Path

chemin = Path("C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250201")

chemin = chemin / "DossierTest"

if not chemin.exists():
    chemin.mkdir()
    print(f"Le dossier {chemin} a été créé.")
else:
    print(f"Le dossier {chemin} existe déjà.")
    chemin.rmdir() # Supprimer le dossier
