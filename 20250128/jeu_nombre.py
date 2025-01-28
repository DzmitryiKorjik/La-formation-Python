import random

nombre_aleatoire = random.randint(1, 100)

nombre_essais = 0
max_essais = 5

print("Bienvenue dans le jeu du nombre mystère !")
print(f"Vous avez {max_essais} essais pour deviner un nombre entre 1 et 100.")

while nombre_essais < max_essais:
    try:
        user_essai = int(input("Entrez votre nombre... (1 à 100) :"))
        
        if (user_essai == nombre_aleatoire):
            print(f"Bravo! Vous avez trouvé le nombre {nombre_aleatoire}")
            break
        elif (user_essai < nombre_aleatoire):
            print("Nombre est plus grand")
            nombre_essais += 1
            print(f"Il vous reste : {max_essais - nombre_essais} tentatives")
        elif (user_essai > nombre_aleatoire):
            print("Nombre est plus petit")
            nombre_essais += 1
            print(f"Il vous reste : {max_essais - nombre_essais} tentatives")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

print(f"Perdu ! Le nombre mystère était {nombre_aleatoire}.")