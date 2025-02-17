import json
import os
import time
from faker import Faker

fake = Faker(locale="fr_FR")
users_data = []

users = 0
while users < 100:
    user = {
        "name": fake.unique.name(),
        "age": fake.random_int(18, 99),
        "gender": fake.random_element(["male", "female"]),
        "address": fake.unique.address(),
        "city": fake.unique.city(),
        "country": fake.unique.country(),
        "email": fake.unique.email(),
        "phone_number": fake.unique.phone_number(),
        "company": fake.unique.company(),
        "job": fake.unique.job(),
        "birthdate": str(fake.date_this_year()),
        "credit_card": fake.credit_card_number(),
        "credit_cerd_expire": fake.credit_card_expire(),
        "credit_card_security_code": fake.credit_card_security_code(),
        "social_security_number": fake.ssn(),
    }    

    users_data.append(user)
    users += 1
    
def save_users(data):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'data_users.json')

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"✅ {len(data)} users saved in data_users.json")
    except IOError as e:
        print(f"❌ Erreur d'écriture: {e}")
        print("Nouvelle tentative dans 2 secondes...")
        time.sleep(2)
        save_users(data)  # repeat once

save_users(users_data)


    