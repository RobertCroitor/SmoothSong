import psycopg2
from utils import crypt
from utils import uuidGenerator

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Users:

    @staticmethod
    def getAllUsers():
        cur = con.cursor()
        cur.execute("SELECT * from users  ")
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getUserByUsername(username):
        cur = con.cursor()
        cur.execute("""SELECT * from users WHERE username = %s """, [username, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getAdminByID(id):
        cur = con.cursor()
        stringUserID = str(id)
        cur.execute("""SELECT isAdmin from users WHERE id = %s """, [stringUserID, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def getCountUserByUsername(username):
        cur = con.cursor()
        cur.execute("""SELECT COUNT (*) from users WHERE username = %s """, [username, ])
        rows = cur.fetchall()
        return rows

    @staticmethod
    def insertAdmin(userID):
        cur = con.cursor()
        stringUserID = str(userID)

        postgres_insert_query = "UPDATE users SET isAdmin =True WHERE id= %s"
        record_to_insert = (stringUserID,)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    @staticmethod
    def insertUser(username, password):
        encPass = crypt.encrypt(password)
        uuid = uuidGenerator.generateUuid(username)

        cur = con.cursor()
        postgres_insert_query = "INSERT INTO users (username,password,uuid,isAdmin) VALUES (%s,%s,%s,%s)"
        record_to_insert = (username, encPass, uuid, False)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    @staticmethod
    def deleteUser(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""DELETE FROM users WHERE id = %s """, [stringUserID, ])
        con.commit()
        return True
