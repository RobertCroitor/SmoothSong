import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")


class QuizzGame:
    # GET FUNCTIONS
    # Get ALL QUESTIONS DATA
    @staticmethod
    def getAllQuestionsData():
        cur = con.cursor()
        cur.execute("SELECT * from quizzGame ")
        rows = cur.fetchall()
        return rows

    # GET THE SIZE OF QUIZZ TABLE
    @staticmethod
    def getAllQuestionsCount():
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) from quizzGame ")
        rows = cur.fetchall()
        return rows

    # GET QUESTION DATA BY ID
    @staticmethod
    def getQuestionDataByID(questionID):
        cur = con.cursor()
        stringQuestionID = str(questionID)
        cur.execute("""SELECT * from quizzGame WHERE id = %s  """, [stringQuestionID])
        rows = cur.fetchall()
        return rows

    # GET FUNCTIONS END

    # INSERT FUNCTIONS
    @staticmethod
    def insertSong(question, answers, correctAnswer):
        cur = con.cursor()
        postgres_insert_query = "INSERT INTO quizzGame (question,answers,correctAnswer) VALUES (%s,%s,%s)"
        record_to_insert = (question, answers, correctAnswer)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True

    # INSERT FUNCTIONS END

    # UPDATE FUNCTIONS
    @staticmethod
    def updateQuestion(question, answers, correctAnswer):
        cur = con.cursor()
        postgres_insert_query = "UPDATE quizzGame SET question=%s,answers=%s,correctAnswer=%s WHERE id=14"
        record_to_insert = (question, answers, correctAnswer)
        cur.execute(postgres_insert_query, record_to_insert)
        con.commit()
        return True
    # UPDATE FUNCTIONS END
