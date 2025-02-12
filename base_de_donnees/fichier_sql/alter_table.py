import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Ajout d'une colonne email si elle n'existe pas déjà
c.execute("ALTER TABLE users ADD COLUMN email TEXT")

# Validation et fermeture de la connexion
conn.commit()
conn.close()

print("La colonne 'email' a été ajoutée avec succès!")
