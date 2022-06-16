import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def selectSongsByUsername(title):
    print("Database opened successfully")

    cur = con.cursor()
    title = "testSongTitle"
    cur.execute("""SELECT * from songs WHERE title = %s """, [title, ]
                )
    rows = cur.fetchall()

    for row in rows:
        print("id =", row[0])
        print("title =", row[1])
        print("singer =", row[2])
        print("genre =", row[3])
        print("url =", row[4], "\n")

    print("Operation done successfully")
    con.close()
    return rows
