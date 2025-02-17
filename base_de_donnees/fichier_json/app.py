import json

fichier = "settings.json"

with open(fichier, "r", encoding="utf-8") as fiche:
    settings = json.load(fiche)

    settings["fontSize"] = 15

with open(fichier, "w", encoding="utf-8") as fiche:
    json.dump(settings, fiche, indent=4)