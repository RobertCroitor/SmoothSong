import connect as conn

con = conn.conn()

print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE songs
      (id SERIAL PRIMARY KEY     NOT NULL,
      title           TEXT    NOT NULL,
      singer            TEXT    NOT NULL,
      genre        TEXT,
      image        TEXT,
      url        TEXT);''')
print("Table created successfully")

con.commit()
con.close()
