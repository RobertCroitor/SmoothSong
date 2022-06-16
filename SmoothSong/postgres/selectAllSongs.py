import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def getAllSongs():
    cur = con.cursor()

    cur.execute("SELECT * from songs  ")
    rows = cur.fetchall()

    return rows
