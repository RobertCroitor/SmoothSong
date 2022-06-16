import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def getUserByUsername(username):
    cur = con.cursor()

    cur.execute("""SELECT * from users WHERE username = %s """, [username, ])
    rows = cur.fetchall()

    return rows
