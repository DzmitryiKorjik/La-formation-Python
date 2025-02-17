import re
import string
from tinydb import TinyDB
from pathlib import Path

class User:

    DB = TinyDB(Path(__file__).resolve().parent / 'dara.json', indent=4)

    def __init__(self, first_name: str, last_name: str, email: str="", password: str="", phone_number: str="", address: str=""):
        self.first_name = self._check(first_name, "name")
        self.last_name = self._check(last_name, "name")
        self.email = email
        self.password = password
        self.address = address
        self.phone_number = self._check(phone_number, "phone")

    def __str__(self):
        return f"{self.full_name}\n{self.email}\n{self.password}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def _check(self, value: str, type_: str) -> str:
        if type_ == "phone":
            return self._check_phone_number(value)
        elif type_ == "name":
            return self._check_names(value)
        return value

        
    def _check_phone_number(self, phone_number: str) -> str:
        phone_number = re.sub(r'[ \+\(\)]', "", phone_number)
        pattern = r'^[0-9]{10}$'  
        
        if re.match(pattern, phone_number):
            return phone_number
        return f"Phone number {phone_number} invalid"
    
    def _check_names(self, name: str) -> str:
        allowed_characters = string.ascii_letters + " -" + "'"

        if not name:
            return("First and last names are required")
        if any(char not in allowed_characters for char in name):
            return(f"Name: {name} contains invalid characters.")
        return name
    
    def save(self):
        return User.DB.insert(self.__dict__)
        
def get_all_users():
    users = [User(**user) for user in User.DB.all()]
    return "\n\n".join(str(user) for user in users)

    
if __name__ == '__main__':
    print(get_all_users())
    # from faker import Faker
    # fake = Faker(locale="fr_FR")

    # for i in range(20):
    #     user = User(fake.first_name(),
    #                 fake.last_name(),
    #                 fake.email(),
    #                 fake.password(),
    #                 fake.phone_number(),
    #                 fake.address())
    #     print(user.save())
    #     print("_" * 10)
