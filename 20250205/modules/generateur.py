from random import uniform

def generer_nombre_aleatoire():
    """Génère un nombre aléatoire entre 1 et 100."""
    return round(uniform(1, 100))

print(generer_nombre_aleatoire())