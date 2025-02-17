import os

chemin = "/Users/dmard/Desktop/Study/La formation Python/20250126"

dossier = os.path.join(chemin, "dossier")

if not os.path.exists(dossier):
    os.makedirs(dossier) # Create directory
    print(f"Le dossier {dossier} a ete cree.")
else:
    print(f"Le dossier {dossier} existe et deja supprimer.")
    os.removedirs(dossier)

