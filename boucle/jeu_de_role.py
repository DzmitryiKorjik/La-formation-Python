import random

utilisateur = 50
ennemi = 50

potion_max = 3

while True:
    try:
        print("----------------------------------------------------------------")
        start_jeu = int(input(f"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : "))

        if start_jeu == 1:
            attaque_aleatoire = random.randint(5, 10)
            attaque_ennemi = random.randint(5, 15)
            print(f"Vous avez infligé {attaque_aleatoire} points de dégats à l'ennemi ⚔️")
            ennemi -= attaque_aleatoire
            print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats ⚔️")
            utilisateur -= attaque_ennemi
            if utilisateur >=0:
                print(f"❤️ Il vous reste {utilisateur} points de dégats")
            else:
                print(f"❤️ Il vous reste 0 points de dégats")
            if ennemi >= 0:
                print(f"❤️ Il reste {ennemi} points de vie à l'ennemi.")
            else:
                print(f"❤️ Il reste 0 points de vie à l'ennemi.")
            if utilisateur <= 0:
                print("💀 Vous avez perdu! Game Over.")
                break
            elif ennemi <= 0:
                print("🎉 Vous avez gagné! Bravo!")
                break

        if start_jeu == 2:
            if potion_max > 0:
                nombre_vie_aleatoire = random.randint(15, 50)
                potion_max -= 1
                utilisateur += nombre_vie_aleatoire
                print(f"❤️ Vous avez utilisé une potion, vous avez maintenant {potion_max} potions.")
                print(f"Vous récupérez ❤️ {nombre_vie_aleatoire} points de vie. Total : {utilisateur}.")
                attaque_ennemi = random.randint(5, 15)
                print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats ⚔️")
                utilisateur -= attaque_ennemi
                print(f"❤️ Il vous reste {utilisateur} points de dégats")
                print(f"❤️ Il reste {ennemi} points de vie à l'ennemi.")
                if utilisateur <= 0:
                    print("💀 Vous avez perdu! Game Over.")
                    break
            else:
                print("❌ Vous n'avez plus de potions! Allez au combat")
                continue

    except ValueError:
        print("❌ Merci d'entrer un nombre valide.")

    