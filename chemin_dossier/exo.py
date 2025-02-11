import os
import sys
import json

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

# Chargement de la liste si le fichier existe
if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r", encoding="utf-8") as file:
        LISTE = json.load(file)
else:
    LISTE = []

while True:
    print("================================================================")
    print("\nActions :")
    print("\n")
    print("1 - Ajouter un élément")
    print("2 - Retirer un élément")
    print("3 - Afficher la liste")
    print("4 - Vider la liste")
    print("5 - Quitter")
    print("\n")

    user_input = input("Entrez un nombre correspondant à une action : ")

    if user_input == "1":
        element = input("Entrez l'élément à ajouter à la liste de courses: ")
        LISTE.append(element)
        print(f"L'élément '{element}' a été ajouté à la liste.")

    elif user_input == "2":
        if not LISTE:
            print("La liste de courses est vide.")
        else:
            element = input("Entrez l'élément à retirer de la liste de courses: ")
            if element in LISTE:
                LISTE.remove(element)
                print(f"L'élément '{element}' a été retiré de la liste.")
            else:
                print(f"L'élément '{element}' n'est pas dans la liste.")

    elif user_input == "3":
        if not LISTE:
            print("================================================================")
            print("La liste de courses est vide.")
        else:
            print("================================================================")
            print("Les éléments de la liste de courses sont:")
            for i, element in enumerate(LISTE, 1):
                print(f"{i}. {element}")

    elif user_input == "4":
        LISTE.clear()
        print("La liste de courses a été vidée.")

    elif user_input == "5":
        print("Merci de votre utilisation. Au revoir!")
        break  # Quitter la boucle proprement

    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")

    # Enregistrement de la liste après chaque modification
    with open(LISTE_PATH, "w", encoding="utf-8") as file:
        json.dump(LISTE, file, indent=4)
