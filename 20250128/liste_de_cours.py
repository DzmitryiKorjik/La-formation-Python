courses = []

while True:
    print("\nActions :")
    print("1 - Ajouter un élément")
    print("2 - Retirer un élément")
    print("3 - Afficher la liste")
    print("4 - Vider la liste")
    print("5 - Quitter")

    user_input = input("Entres un nombre de la liste de courses :")
    
    if user_input == "1":
        element = input("Entrez l'élément à ajouter à la liste de courses: ")
        courses.append(element)
        print(f"L'élément {element} a été ajouté à la liste.")
    elif user_input == "2":
        if len(courses) == 0:
            print("La liste de courses est vide.")
        else:
            element = input("Entrez l'élément à retirer de la liste de courses: ")
            if element in courses:
                courses.remove(element)
                print(f"L'élément {element} a été retiré de la liste.")
            else:
                print(f"L'élément {element} n'est pas dans la liste.")
    elif user_input == "3":
        if len(courses) == 0:
            print("La liste de courses est vide.")
        else:
            print("Les éléments de la liste de courses sont:")
            for element in courses:
                print(element)
    elif user_input == "4":
        courses.clear()
        print("La liste de courses a été vide.")
    elif user_input == "5":
        print("Merci de votre utilisation. Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")