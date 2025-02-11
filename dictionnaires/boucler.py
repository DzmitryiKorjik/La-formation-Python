liste = {
    "prenom" : "Paul",
    "profession": "Ingénieur",
    "ville": "Paris"
}
print(liste)
print(liste.keys())
print(liste.values())

for cle in liste:
    print(cle, ":", liste[cle])

for cle, valeur in liste.items():
    print("cle -", cle, ":  valeur -", valeur)
