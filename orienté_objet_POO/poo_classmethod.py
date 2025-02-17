class Voiture:
    voiture_crees = 0
    def __init__(self, marque, vitesse, prix):
        Voiture.voiture_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    def __str__(self) -> str:
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse} et avec le prix {self.prix}."

    @classmethod
    def bmw(cls):
        return cls("BMW", 250, 30000)
    
    @classmethod
    def audi(cls):
        return cls("Audi", 220, 35000)
    
    @staticmethod
    def get_total_voitures_crees():
        print(f"Vous avez {Voiture.voiture_crees} voitures dans votre garage.")
    
bmw = Voiture.bmw()
audi = Voiture.audi()
Voiture.get_total_voitures_crees()

print(bmw)
print(audi)

