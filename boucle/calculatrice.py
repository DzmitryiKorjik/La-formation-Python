# nbr1 = input("Entrez un premier nombre : ")
# nbr2 = input("Entrez un deuxième nombre : ")

# if nbr1.isdigit() and nbr2.isdigit():
#     nbr1 = float(nbr1)
#     nbr2 = float(nbr2)
#     print(f"Le résultat de l'addition de {nbr1} avec {nbr2} est égal à {nbr1 + nbr2} ")
# else:
#     print("Veuillez entrer des nombres valides.")

while True:
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if all([a.isdigit(), b.isdigit()]):
        print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
        break
    else:
        print("Veuillez entrer deux nombres valides")  