liste = [-6, -3, -2, -1, -10, 0, 1, 2, 3, 4, 5, 6]

# Calcul du nombre d'entier positif
nombres_positifs = [i for i in liste if i > 0]
print(nombres_positifs) #[1, 2, 3, 4, 5, 6]
# Calcul du nombre d'entier négatif
nombre_negatifs = [i for i in liste if i < 0]
print(nombre_negatifs) #[-6, -3, -2, -1, -10]