class Voiture:
    def __init__(self, essence=100):
        self.essence = essence

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence:.2f} litres d'essence.")

    def roule(self, km):
        consommation = (km * 5) / 100
        if self.essence > consommation:
            self.essence -= consommation
            print(f"La voiture roule {km} km et a maintenant {self.essence} litres d'essence.")
        elif self.essence <= 10:
            print("Vous n'avez bientôt plus d'essence !")
        else:
            print("Vous n'avez plus d'essence, faites le plein !")

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")

# Test du code
ma_voiture = Voiture()
ma_voiture.afficher_reservoir()
ma_voiture.roule(150)
ma_voiture.afficher_reservoir()
ma_voiture.faire_le_plein()
ma_voiture.afficher_reservoir()