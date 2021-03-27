import psycopg2

DATABASE_URL = 'postgres://bolfhxflpnrgcm:38a1fa4078d935f4533b55d7bb68370e37832b15ebebe8e142a67b6b42bec6ea@ec2-54-157-12-250.compute-1.amazonaws.com:5432/d7drpahj1p2njo'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER UNIQUE PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            bd CHARACTER(10) NOT NULL,
                            zodiac_sign TEXT NOT NULL,
                            favourite_color TEXT NOT NULL)''')

cursor.close()
conn.commit()
conn.close()
