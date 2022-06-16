import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def insertSong(title, singer, genre, imgURL, songURL):
    print("Database opened successfully")

    cur = con.cursor()
    postgres_insert_query = "INSERT INTO songs (title,singer,genre,image,url) VALUES (%s,%s,%s,%s,%s)"
    record_to_insert = (title, singer, genre, imgURL, songURL)
    cur.execute(postgres_insert_query, record_to_insert)

    con.commit()
    print("Record inserted successfully")
