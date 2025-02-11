from pathlib import Path

chemin = 'C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250204\\dossier_exerc'

dictionnaire = {
    "Films": ["Le seigneur des anneaux",
            "Harry Potter",
            "Moon",
            "Forrest Gump"],
    "Employes": ["Paul",
                "Pierre",
                "Marie"],
    "Exercices": ["les_variables",
                "les_fichiers",
                "les_boucles"]}

# Création du dossier

dossier = Path(chemin)
if not dossier.exists():
    dossier.mkdir(parents=True, exist_ok=True)

# Création des sous-dossiers
for categorie, sous_dossiers in dictionnaire.items():
    categorie_path = dossier / categorie
    categorie_path.mkdir(parents=True, exist_ok=True)

    for sous_dossier in sous_dossiers:
        sous_dossier_path = categorie_path / sous_dossier
        sous_dossier_path.mkdir(parents=True, exist_ok=True)






