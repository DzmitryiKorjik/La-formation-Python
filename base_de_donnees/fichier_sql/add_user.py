import sqlite3  # Importation du module SQLite


# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Liste des nouveaux utilisateurs à ajouter
nouveaux_utilisateurs = [
    ('admin', 'password123'),
    ('user2', 'user2pass'),
    ('user3', 'user3pass'),
    ('user4', 'user4pass'),
    ('user5', 'user5pass')
]

# Ajout des utilisateurs dans la table "users"
c.executemany("INSERT INTO users (username, password) VALUES (?, ?)", nouveaux_utilisateurs)


# Récupération et affichage de tous les utilisateurs après l'insertion
c.execute("SELECT * FROM users")
donnees = c.fetchall()
print("Liste des utilisateurs :", donnees)

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()
