import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Downloaded:

    @staticmethod
    def createDownloaded():
        cur = con.cursor()
        cur.execute('''CREATE TABLE downloaded
              (id SERIAL PRIMARY KEY     NOT NULL,
              modified  bool DEFAULT false,
              title           TEXT    NOT NULL,
              singer            TEXT    NOT NULL,
              genre        TEXT,
              image        TEXT,
              url        TEXT);''')
        con.commit()

    @staticmethod
    def deleteDownloaded():
        cur = con.cursor()
        cur.execute('''DROP TABLE IF EXISTS downloaded;''')
        con.commit()

    @staticmethod
    def getAllSongs():
        cur = con.cursor()
        cur.execute("SELECT * from downloaded ")
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getSongData(title, singer):
        cur = con.cursor()
        cur.execute("""SELECT * from songs WHERE title = %s AND singer=%s """, [title, singer, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def insertSong(title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO downloaded (title,singer,genre,image,url) " \
                                "VALUES (%s,%s,%s,%s,%s)"
        record_to_insert = (title, singer, genre, imgURL, songURL)

        cur.execute(postgres_insert_query, record_to_insert)

        con.commit()
        return True

    @staticmethod
    def insertDownloaded(title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        modified = True

        postgres_insert_query = "INSERT INTO downloaded " \
                                "(modified,title,singer,genre,image,url) " \
                                "VALUES (%s,%s,%s,%s,%s,%s)"
        record_to_insert = (modified, title, singer, genre, imgURL, songURL)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    @staticmethod
    def getSongsCount():
        cur = con.cursor()

        cur.execute("""SELECT COUNT (*) from downloaded """)
        rows = cur.fetchall()
        return rows


def initialiseDownloadedTable():
    downloaded = Downloaded()
    downloaded.deleteDownloaded()
    downloaded.createDownloaded()
    return True
