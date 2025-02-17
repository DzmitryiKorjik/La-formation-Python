chemin = "C:\\Users\\dmard\\Documents\\mes_modules\\fichier.txt"

# with open(chemin, "w", encoding='utf-8') as f: # open the file for writes
#     f.write("Hello, world!")
#     f.write("\nCeci est un exemple de texte.")

with open(chemin, "a", encoding='utf-8') as f: # open the file for writes with append
    f.write("\nCeci est encore un exemple de texte avec append.")