import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Liste des nouveaux utilisateurs sous forme de dictionnaire
nouveaux_utilisateurs = [
    {"username": "admin", "password": "password123"},
    {"username": "Dima", "password": "user2pass"},
    {"username": "Ksu", "password": "user3pass"},
    {"username": "Maksim", "password": "user4pass"},
    {"username": "Pavel", "password": "user5pass"},
    {"username": "Rania", "password": "user6pass"}
]

# Génération dynamique des colonnes et valeurs
columns = ", ".join(nouveaux_utilisateurs[0].keys())  # "username, password"
placeholders = ", ".join(["?" for _ in nouveaux_utilisateurs[0]])  # "?, ?"
values = [tuple(user.values()) for user in nouveaux_utilisateurs]  # Liste de tuples

# Requête SQL dynamique
sql = f"INSERT INTO users ({columns}) VALUES ({placeholders})"

# Exécution de l'insertion
c.executemany(sql, values)

# Récupération et affichage de tous les utilisateurs après l'insertion
c.execute("SELECT * FROM users")
donnees = c.fetchall()
print("Liste des utilisateurs :", donnees)

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()
