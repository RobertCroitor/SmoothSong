import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Songs:
    @staticmethod
    def getAllSongs():
        cur = con.cursor()
        cur.execute("SELECT * from songs ")
        rows = cur.fetchall()
        return rows

    @staticmethod
    def insertSong(title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO songs (title,singer,genre,image,url) VALUES (%s,%s,%s,%s,%s)"
        record_to_insert = (title, singer, genre, imgURL, songURL)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    @staticmethod
    def getSongsByTitle(title):
        cur = con.cursor()
        cur.execute("""SELECT * from songs WHERE title = %s """, [title, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def deleteSong(songID):
        cur = con.cursor()
        stringSongID = str(songID)
        cur.execute("""DELETE FROM songs WHERE id = %s """, [stringSongID, ])
        con.commit()
        return True
