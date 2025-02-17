fichier = input("Entrez un fichier à ouvrir : ")

try:
    file = open(fichier, "r")
    print(file.read())
except FileNotFoundError:
    print(f"Le fichier '{fichier}' n'existe pas.")
except UnicodeDecodeError:
    print(f"Le fichier '{fichier}' contient des caractères non-codés.")
else:
    file.close() # ferme le fichier quand il n'y a pas eu d'erreur