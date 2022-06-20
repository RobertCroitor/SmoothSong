import psycopg2
from functions import cryptingManagement

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class Users:
    # INSERT FUNCTIONS
    # CHANGE THE ADMIN FLAG OF A USER TO TRUE
    @staticmethod
    def insertAdmin(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        postgres_insert_query = "UPDATE users SET isAdmin =True WHERE id= %s"
        record_to_insert = (stringUserID,)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    # INSERT A NEW USER IN THE USERS TABLE
    @staticmethod
    def insertUser(username, password):
        encPass = cryptingManagement.encrypt(password)
        uuid = cryptingManagement.generateUuid(username)
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO users (username,password,uuid,isAdmin) VALUES (%s,%s,%s,%s)"
        record_to_insert = (username, encPass, uuid, False)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    # INSERT FUNCTIONS END

    # GET FUNCTIONS
    # GET ALL USERS FROM USERS TABLE
    @staticmethod
    def getAllUsers():
        cur = con.cursor()
        cur.execute("SELECT * from users  ")
        rows = cur.fetchall()
        return rows

    # GET A USER DATA BY SEARCHING HIS USERNAME
    @staticmethod
    def getUserByUsername(username):
        cur = con.cursor()
        cur.execute("""SELECT * from users WHERE username = %s """, [username, ])
        rows = cur.fetchall()
        return rows

    # GET A USER DATA BY SEARCHING HIS ID
    @staticmethod
    def getAdminByID(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""SELECT isAdmin from users WHERE id = %s """, [stringUserID, ])
        rows = cur.fetchall()
        return rows

    # GET USERS COUNT BY SEARCHING THE USERNAME
    @staticmethod
    def getCountUserByUsername(username):
        cur = con.cursor()
        cur.execute("""SELECT COUNT (*) from users WHERE username = %s """, [username, ])
        rows = cur.fetchall()
        return rows

    # GET FUNCTIONS END

    # DELETE FUNCTIONS
    # DELETE A USER USING HIS ID
    @staticmethod
    def deleteUser(userID):
        cur = con.cursor()
        stringUserID = str(userID)
        cur.execute("""DELETE FROM users WHERE id = %s """, [stringUserID, ])
        con.commit()
        return True
    # DELETE FUNCTIONS END
