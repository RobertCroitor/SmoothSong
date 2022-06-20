import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


# CREATE USERS TABLE
def createUsersTable():
    cur = con.cursor()
    cur.execute('''CREATE TABLE users
          (id SERIAL PRIMARY KEY     NOT NULL,
          username           TEXT    NOT NULL UNIQUE,
          password        TEXT,
          uuid            TEXT    ,
          isAdmin        bool DEFAULT false)
          ;''')
    con.commit()
    con.close()
