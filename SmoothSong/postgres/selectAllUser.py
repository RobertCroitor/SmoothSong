import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def getAllUsers():
    print("Database opened successfully")
    cur = con.cursor()

    cur.execute("SELECT * from users  ")
    rows = cur.fetchall()

    for row in rows:
        print("id =", row[0])
        print("username =", row[1])
        print("password =", row[2])
        print("uuid =", row[3])
        print("isAdmin =", row[4], "\n")

    print("Operation done successfully")
    con.close()
    return rows


rows = getAllUsers()
for row in rows:
    print(row)
