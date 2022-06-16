from utils import crypt
from utils import uuidGenerator
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


def insertUser(username, password):
    encPass = crypt.encrypt(password)
    uuid = uuidGenerator.generateUuid(username)

    cur = con.cursor()
    postgres_insert_query = "INSERT INTO users (username,password,uuid,isAdmin) VALUES (%s,%s,%s,%s)"
    record_to_insert = (username, encPass, uuid, False)
    cur.execute(postgres_insert_query, record_to_insert)
    con.commit()
    return True
