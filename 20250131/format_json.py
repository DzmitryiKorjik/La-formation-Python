import json

chemin = "C:\\Users\\dmard\\Desktop\\Study\\La formation Python\\20250131\\fichier.json"

# Création d'un fichier JSON
# with open(chemin, "w", encoding='utf-8') as f:
#     json.dump({"nom": "John Doe", "age": 30, "profession": "Ingénieur"}, f, indent=4)

    #json.dump(list(range(10)), f, indent=4)

# Lecture du fichier JSON
with open(chemin, "r", encoding='utf-8') as f:
    liste = json.load(f)

liste.append({"nom": "Dan Doe", "age":20, "profession": "UI"})

# Écriture du fichier modifié JSON
with open(chemin, "w", encoding='utf-8') as f:
    json.dump(liste, f, indent=4)

print(liste)
