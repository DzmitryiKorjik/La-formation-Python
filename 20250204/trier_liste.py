from pathlib import Path
import re

chemin = Path('C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250204\\prenoms.txt')
chemin_final = Path('C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250204\\prenoms_final.txt')

# Lire le contenu du fichier
with chemin.open('r', encoding='utf-8') as f:
    contenu = f.read()

# Extraire et nettoyer les prénoms en une seule étape
prenoms = sorted(set(prenom.strip("., ") for prenom in re.split(r'\s+', contenu)))

# Écriture dans le fichier final
with chemin_final.open('w', encoding='utf-8') as f:
    f.write("\n".join(prenoms))

print(f"Les prénoms ont été écrits dans {chemin_final}")
