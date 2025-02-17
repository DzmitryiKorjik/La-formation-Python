from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    gender: str

user1 = User("John Doe", 25, "male")

print(user1) # User(name='John Doe', age=25, gender='male')

