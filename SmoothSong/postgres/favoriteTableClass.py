import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Favorites:
    # CREATE FAVORITES TABLE
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

    # DELETE FAVORITES TABLE
    @staticmethod
    def deleteTable():
        cur = con.cursor()
        postgres_insert_query = "DROP TABLE favorites"
        cur.execute(postgres_insert_query)
        con.commit()
        return True

    # INSERT FUNCTIONS
    # INSERT ONE SONG IN THE FAVORITES TABLE
    @staticmethod
    def insertSong(userID, title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO favorites (userID,title,singer,genre,image,url) VALUES (%s,%s,%s,%s,%s,%s)"
        record_to_insert = (userID, title, singer, genre, imgURL, songURL)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    # INSERT FUNCTIONS END

    # GET FUNCTIONS
    # GET ALL SONGS FROM FAVORITES TABLE
    @staticmethod
    def getAllSongs():
        cur = con.cursor()
        cur.execute("SELECT * from favorites ")
        rows = cur.fetchall()
        return rows

    # GET SONG DATA BY FILTERING IT USING THE USER ID
    @staticmethod
    def getSongsByUserID(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""SELECT * from favorites WHERE userID = %s """, [stringUserID, ])
        rows = cur.fetchall()
        return rows

    # GET SONG COUNT BY FILTERING IT USING THE SONG TITLE AND SINGER
    @staticmethod
    def getSongsCountByTitle(title, singer, userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""SELECT  COUNT(*) from favorites WHERE title = %s AND singer= %s AND userID=%s """,
                    [title, singer, stringUserID, ])
        rows = cur.fetchall()
        return rows

    # GET SONG DATA FILTERING IT USING THE SONG TITLE AND SINGER
    @staticmethod
    def getSongData(title, singer):
        cur = con.cursor()
        cur.execute("""SELECT * from favorites WHERE title = %s AND singer=%s """, [title, singer, ])
        rows = cur.fetchall()
        return rows

    # GET FUNCTIONS END

    # DELETE FUNCTIONS
    # DELETE A SONG USING THE SONG ID
    @staticmethod
    def deleteSongByID(songID):
        cur = con.cursor()
        stringSongID = str(songID)
        cur.execute("""DELETE FROM favorites WHERE id = %s """, [stringSongID, ])
        con.commit()
        return True

    # DELETE A SONG USING THE SONG TITLE AND SINGER
    @staticmethod
    def deleteSongByTitleAndSinger(title, singer):
        cur = con.cursor()
        cur.execute("""DELETE FROM favorites WHERE title = %s AND singer=%s""", [title, singer, ])
        con.commit()
        return True
