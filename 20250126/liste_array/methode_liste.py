employes = ["Carlos", "Max", "Mertine", "Patrick", "Alex"]
resultat = employes.index("Max") #index 1
print(resultat)

resultat = employes.count("Max") #count 1
print(resultat)

employes.sort() #['Alex', 'Carlos', 'Max', 'Mertine', 'Patrick']
print("La meme liste avec sort(): ", employes)


liste_trie = sorted(employes) # nouveau liste
print("Nouvelle liste avec sorted(): ", liste_trie)

employes.reverse() # inverse la liste
print("La liste inversée: ", employes)

employes.insert(2, "Henri") # insert Henri à l'index 2
print("La liste avec Henri inséré: ", employes)

employes.remove("Mertine") # supprime Mertine de la liste
print("La liste sans Mertine: ", employes)

element = employes.pop(3) # supprime l'employé à l'index 3
print(element)
print(employes)

employes.clear()
print(employes) # clear liste