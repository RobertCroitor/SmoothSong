from postgres import connect as conn

con = conn.conn()

print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE users
      (id SERIAL PRIMARY KEY     NOT NULL,
      username           TEXT    NOT NULL UNIQUE,
      password        TEXT,
      uuid            TEXT    ,
      isAdmin        bool DEFAULT false)
      ;''')
print("Table created successfully")

con.commit()
con.close()
