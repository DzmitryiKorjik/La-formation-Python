import json
import os
import time
from faker import Faker

fake = Faker(locale="fr_FR")
users_data = []

users = 0
while users < 100:
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "company": fake.company(),
        "job": fake.job(),
        "birthdate": str(fake.date_this_year())
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


    