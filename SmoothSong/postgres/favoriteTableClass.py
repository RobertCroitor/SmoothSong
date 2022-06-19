import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Favorites:
    @staticmethod
    def deleteTable():
        cur = con.cursor()
        postgres_insert_query = "DROP TABLE favorites"
        cur.execute(postgres_insert_query)
        con.commit()
        return True

    @staticmethod
    def createTable():
        cur = con.cursor()
        cur.execute('''CREATE TABLE favorites
              (id SERIAL PRIMARY KEY     NOT NULL,
              userID text NOT NULL,
              title           TEXT    NOT NULL,
              singer            TEXT    NOT NULL,
              genre        TEXT,
              image        TEXT,
              url        TEXT);''')
        con.commit()
        return True

    @staticmethod
    def insertSong(userID, title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO favorites (userID,title,singer,genre,image,url) VALUES (%s,%s,%s,%s,%s,%s)"
        record_to_insert = (userID, title, singer, genre, imgURL, songURL)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    @staticmethod
    def getAllSongs():
        cur = con.cursor()
        cur.execute("SELECT * from favorites ")
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getSongsByUserID(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""SELECT * from favorites WHERE userID = %s """, [stringUserID, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getSongsCountByTitle(title, userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""SELECT COUNT (*) from favorites WHERE title = %s AND userID=%s """, [title, stringUserID, ])
        rows = cur.fetchall()
        return rows
