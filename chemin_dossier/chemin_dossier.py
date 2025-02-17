chemin = "C:\\Users\\dmard\\Documents\\mes_modules\\fichier.txt"

with open(chemin, "r", encoding='utf-8') as f: # open the file for reading
    contenu = f.read().splitlines()
    print(contenu)

