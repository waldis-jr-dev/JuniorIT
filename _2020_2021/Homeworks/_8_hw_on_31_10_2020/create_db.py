import sqlite3

conn = sqlite3.connect('customers.sqlite3')
cursor = conn.cursor()

cursor.executescript('''CREATE TABLE IF NOT EXISTS customers (
                            note_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            birth_year TEXT NOT NULL,
                            start_location TEXT NOT NULL,
                            end_location TEXT NOT NULL,
                            distance REAL NOT NULL)''')

cursor.executescript('''CREATE TABLE IF NOT EXISTS cost (
                            ticket_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                            customer_id INTEGER NOT NULL, 
                            cost  TEXT NOT NULL,
                            FOREIGN KEY(customer_id) REFERENCES customers(note_id))''')

cursor.close()
conn.close()
