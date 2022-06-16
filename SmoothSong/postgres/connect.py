import psycopg2


def conn():
    return psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost", port="5432")
