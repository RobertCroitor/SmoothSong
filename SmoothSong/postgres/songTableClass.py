import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Songs:
    # INSERT ONE SONG IN THE SONGS TABLE
    @staticmethod
    def insertSong(title, singer, genre, imgURL, songURL):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO songs (title,singer,genre,image,url) VALUES (%s,%s,%s,%s,%s)"
        record_to_insert = (title, singer, genre, imgURL, songURL)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    # GET FUNCTIONS
    # GET ALL SONGS IN THE SONGS TABLE
    @staticmethod
    def getAllSongs():
        cur = con.cursor()
        cur.execute("SELECT * from songs ")
        rows = cur.fetchall()
        return rows

    # GET SONG DATA FROM SONG TABLE FILTERING THE RESULTS BY SONG TITLE AND SINGER
    @staticmethod
    def getSongData(title, singer):
        cur = con.cursor()
        cur.execute("""SELECT * from songs WHERE title = %s AND singer=%s """, [title, singer, ])
        rows = cur.fetchall()
        return rows

        # GET SONG DATA FROM SONG TABLE FILTERING THE RESULTS BY SONG TITLE AND SINGER

    @staticmethod
    def getSongCountByTitleAndSinger(title, singer):
        cur = con.cursor()
        cur.execute("""SELECT COUNT(*) from songs WHERE title = %s AND singer=%s """, [title, singer, ])
        rows = cur.fetchall()
        return rows

    # GET SONG DATA FROM SONG TABLE FILTERING THE RESULTS BY SONG ID
    @staticmethod
    def getSongByID(songID):
        cur = con.cursor()
        stringSongID = str(songID)
        cur.execute("""SELECT * from songs WHERE id = %s  """, [stringSongID])
        rows = cur.fetchall()
        return rows

    # GET FUNCTIONS END

    # DELETE FUNCTIONS
    # DELETE A SONG USING THE SONG ID
    @staticmethod
    def deleteSong(songID):
        cur = con.cursor()
        stringSongID = str(songID)
        cur.execute("""DELETE FROM songs WHERE id = %s """, [stringSongID, ])
        con.commit()
        return True
    # DELETE FUNCTIONS END
