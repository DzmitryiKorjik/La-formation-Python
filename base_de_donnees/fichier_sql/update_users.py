import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Données à mettre à jour
dictionary = {
    "password": "new_secure_password",  # Nouveau mot de passe
}

username = "admin"  # Nom d'utilisateur cible

# Construction dynamique de la requête SQL
columns = ", ".join(f"{key} = ?" for key in dictionary.keys())
values = list(dictionary.values()) + [username]  # Ajouter username à la fin pour la condition WHERE

sql = f"UPDATE users SET {columns} WHERE username = ?"

# Exécution de la requête avec les valeurs
c.execute(sql, values)

# Validation et fermeture de la connexion
conn.commit()
conn.close()

print("Données mises à jour avec succès!")
