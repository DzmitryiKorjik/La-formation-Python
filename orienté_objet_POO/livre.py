class Livre:
    def __init__(self, nom, nombre_de_pages, prix):
        self.nom = nom
        self.nombre_de_pages = nombre_de_pages
        self.prix = prix
    
    def afficher_info(self):
        print(f"Livre : {self.nom}")
        print(f"Nombre de pages : {self.nombre_de_pages}")
        print(f"Prix : {self.prix} euros")
        print("-------------------")
        
livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le Seigneur des Anneaux", 400, 13.99)

livre_HP.afficher_info()
livre_LOTR.afficher_info() 