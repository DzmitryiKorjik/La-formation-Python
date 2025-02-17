from tinydb import TinyDB, Query, where

from main import db

data_base = TinyDB('data.json', indent=4)

# db.update({"score": 10}, where("score") == 0)

# db.update({"role": ["junior"]})

# db.upsert({"name": "Pierre", "score": 0, "role": ["senior"]}, where("name") == "Pierre")

# db.remove(where("score") == 10)

# db.truncate()
