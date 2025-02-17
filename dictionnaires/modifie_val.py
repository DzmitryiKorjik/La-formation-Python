liste = {
    "prenom" : "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}
print(liste)
print("Prenom est :",liste.get("prenom"))

liste["prenom"] = "Dzmitryi"
liste["ville"] = "Lyon"

print(liste)

liste["age"] = 30
print(liste)

if "age" in liste:
    del liste["age"]
print(liste)
