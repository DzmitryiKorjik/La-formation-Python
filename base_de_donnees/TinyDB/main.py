from xml.etree.ElementTree import indent
from tinydb import TinyDB

db = TinyDB('data.json', indent=4)

"""
db.insert_multiple([
    {"name": "Oly", "score": 50, "roles": ["junior"]},
    {"name": "Maks", "score": 45, "roles": ["junior"]},
    {"name": "Dina", "score": 100, "roles": ["junior"]}
])
"""




