import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


# CREATE FAVORITES TABLE
def createQuizzGameTable():
    cur = con.cursor()
    cur.execute('''CREATE TABLE quizzGame
          (id SERIAL PRIMARY KEY     NOT NULL,
          question            TEXT NOT NULL,
          answers           TEXT    NOT NULL,
          correctAnswer            TEXT    NOT NULL
          );''')
    con.commit()
    con.close()
