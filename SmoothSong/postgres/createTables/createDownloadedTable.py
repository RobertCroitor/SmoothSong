import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def createDownloaded():
    cur = con.cursor()
    cur.execute('''CREATE TABLE favorites
          (id SERIAL PRIMARY KEY     NOT NULL,
          title           TEXT    NOT NULL,
          singer            TEXT    NOT NULL,
          genre        TEXT,
          image        TEXT,
          url        TEXT);''')
    con.commit()
