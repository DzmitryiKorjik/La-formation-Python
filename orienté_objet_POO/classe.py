class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Bonjour, je m'appelle {self.name} et j'ai {self.age} ans."

# Создание экземпляров (объектов) класса
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.introduce())  # Bonjour, je m'appelle Alice et j'ai 25 ans.
print(p2.introduce())  # Bonjour, je m'appelle Bob et j'ai 30 ans.
