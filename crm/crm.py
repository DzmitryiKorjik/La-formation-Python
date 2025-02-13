
class User:
    def __init__(self, first_name: str, last_name: str, email: str="", password: str="", phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.full_name}\n{self.email}\n{self.password}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

if __name__ == '__main__':
    from faker import Faker
    fake = Faker(locale="fr_FR")
    for i in range(10):
        user = User(fake.first_name(),
                    fake.last_name(),
                    fake.email(),
                    fake.password(),
                    fake.phone_number(),
                    fake.address())
        print(user)
        print("_" * 10)
        #print(user.__dict__)