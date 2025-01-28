# for element in list:
#     print(element)

# for i in [1, 2, 3]:
#     print(i) 

# for l in range(10):
#     print("Bonjour") # Bonjor 10 fois

# prenoms = ["Pierre", "Patrick", "Jean", "Marc"]
# for prenom in prenoms:
#     if prenom == "Dima": 
#         print("Jean a été trouvé !")
#         break
# else: 
#     print("Jean n'a pas été trouvé dans la liste.")

# mot = "Python"
# for lettre in mot[::-1]:
#     print(lettre)

# mot = "Python"
# for i in range(len(mot)):
#     print(i)

# nombre = 7
# i = 0
# for i in range(11):
#     print(f"{i} x {nombre} = {i * nombre}")
#     i += 1


# nombres = [1, 21, 5, 44, 9, 5, 83, 29, 31, 25, 38]
# nombres_pairs = []
# nombres_impairs = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_pairs.append(i)
# print(nombres_pairs)

# for i in nombres:
#     if i % 2 != 0:
#         nombres_impairs.append(i)
# print(nombres_impairs)


# nombres = [1, 21, 5, 44, 9, 5, 83, 29, 31, 25, 38]
# nombres_pairs = [i for i in nombres if i % 2 == 0]
# print(nombres_pairs)
# nombres_impairs = [i for i in nombres if i % 2 != 0]
# print(nombres_impairs)

nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)
