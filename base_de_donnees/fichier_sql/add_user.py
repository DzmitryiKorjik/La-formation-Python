import sqlite3  # Importation du module SQLite


# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Liste des nouveaux utilisateurs à ajouter
nouveaux_utilisateurs = [
    ('admin', 'password123'),
    ('Dima', 'user2pass'),
    ('Ksu', 'user3pass'),
    ('Maksim', 'user4pass'),
    ('Pavel', 'user5pass'),
    ('Rania', 'user6pass')
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
