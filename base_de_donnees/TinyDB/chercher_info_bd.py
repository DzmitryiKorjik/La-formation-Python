from xml.etree.ElementTree import indent

from tinydb import TinyDB, Query, where

from main import db

data_base = TinyDB('data.json', indent=4)

"""
db.insert({"name": "Patrice", "score": 50})

db.insert_multiple([
    {"name": "Oly", "score": 50},
    {"name": "Maks", "score": 45},
    {"name": "Dina", "score": 100}
])
"""

User = Query()
patrice = db.search(User.name == "Patrice")
print(patrice)

patrice_unique = db.get(User.name == "Patrice")
print(patrice_unique)

high_scores = db.search(where("score") > 0)
print(high_scores)

print(len(db))