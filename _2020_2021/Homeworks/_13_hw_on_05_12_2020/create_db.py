import sqlite3

conn = sqlite3.connect('fighters.sqlite3')
cursor = conn.cursor()

cursor.executescript('''CREATE TABLE IF NOT EXISTS fighters (
                            fighter_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            damage INTEGER NOT NULL,
                            hp INTEGER NOT NULL,
                            MAX_HP INTEGER NOT NULL,
                            strength INTEGER NOT NULL,
                            agility INTEGER NOT NULL,
                            wins INTEGER DEFAULT 0,
                            losses INTEGER DEFAULT 0)''')

cursor.executescript('''CREATE TABLE IF NOT EXISTS battles (
                            battle_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                            winner INTEGER DEFAULT 0,
                            loser INTEGER DEFAULT 0,
                            FOREIGN KEY (winner) REFERENCES fighters(fighter_id) 
                            ON DELETE SET DEFAULT ON UPDATE CASCADE,
                            FOREIGN KEY (loser) REFERENCES fighters(fighter_id) 
                            ON DELETE SET DEFAULT ON UPDATE CASCADE)''')

cursor.close()
conn.close()
