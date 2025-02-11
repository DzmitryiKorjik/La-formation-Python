user = ["Paul", "John", "Pierre", "Marie"]
if "Paul" in user: # opérateurs d'appartenance
    user.remove("Paul")
    user.append("Bruce")

print(user)

liste = [1, 2, 3, 4, 5]
liste.append(6)
if 6 in liste:
    print("Le nombre 6 a bien été ajouté à la liste.")