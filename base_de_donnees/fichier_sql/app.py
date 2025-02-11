import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             password TEXT NOT NULL)''')

c.execute("INSERT INTO users VALUES (1, 'admin', 'password123')")

conn.commit()

conn.close()