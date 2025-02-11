# Classe des parents
# Heritage / Inheritance  
class Animal:  
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Il y a un bruit")

class Dog(Animal): 
    def make_sound(self):  
        print(f"{self.name} Gav-Gav!")

class Cat(Animal): 
    def make_sound(self):
        print(f"{self.name} May-May!")

# Polymorphism
animals = [Dog("Doggi"), Cat("Myrka")]

for animal in animals:
    animal.make_sound()

    # Tentative de modification de la méthode make_sound()
    animal.sound = "Woof!"
    animal.make_sound()


