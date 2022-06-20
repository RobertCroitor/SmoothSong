import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


# CREATE SONG TABLE
def createSongsTable():
    cur = con.cursor()
    cur.execute('''CREATE TABLE songs
          (id SERIAL PRIMARY KEY     NOT NULL,
          title           TEXT    NOT NULL,
          singer            TEXT    NOT NULL,
          genre        TEXT,
          image        TEXT,
          url        TEXT);''')
    con.commit()
    con.close()
