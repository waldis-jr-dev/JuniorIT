import sqlite3

conn = sqlite3.connect('phones.sqlite')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                phone TEXT PRIMARY KEY,
                name TEXT,
                surname TEXT
                )''')

conn.commit()
cursor.close()
conn.close()
