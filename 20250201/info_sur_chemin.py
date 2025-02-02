from pathlib import Path

chemin = Path("C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250131\\fichier.json")

print(chemin.name) # fichier.json
print(chemin.stem) # fichier
print(chemin.suffix) # .json
print(chemin.suffixes) # ['.json']
print(chemin.parts) # ('C:\\', 'Users', 'dmard', 'Desktop', 'Study', 'La formation Python', '20250131', 'fichier.json')
print(chemin.parent) # C:\Users\dmard\Desktop\Study\La formation Python\20250131
print(chemin.exists()) # True
print(chemin.is_dir()) # False
print(chemin.is_file()) # True
