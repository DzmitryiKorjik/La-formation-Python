import sqlite3  # Importation du module SQLite

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Remove des users - WHERE username='admin'
c.execute("DELETE FROM users")
c.execute("DELETE FROM sqlite_sequence")

# Commit les modifications
conn.commit()

# Fermeture de la connexion
conn.close()