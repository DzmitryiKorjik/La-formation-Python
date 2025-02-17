
import json
import logging
import os

from constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("L'élément doit être une chaîne de caractères.")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste")
            return False
        
        self.append(element)
        return True
    
    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False
    
    def afficher(self):
        print(f"Ma liste de {self.nom} : ")
        for element in self:
            print(f" - {element}")

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        with open(chemin, "w", encoding="utf-8") as fiche:
            json.dump(self, fiche, ensure_ascii=False, indent=4)
        
        return True

    
if __name__ == "__main__":
    liste = Liste("Courses")
    liste.ajouter("Pain")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    liste.sauvegarder()

