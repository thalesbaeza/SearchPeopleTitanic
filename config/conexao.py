import psycopg2
<<<<<<< HEAD

class Conexao():
    def __init__(self, localhost="34.151.225.250", db="postgres", user="postgres", password="admin", port=5432):
        self.conn = psycopg2.connect(host=localhost, database=db, user=user , password=password, port=port)
=======
import os

class Conexao():
    def __init__(self, 
                B_HOST = os.getenv("DB_HOST"),
                DB_PORT = os.getenv("DB_PORT"),
                DB_NAME = os.getenv("DB_NAME"),
                DB_USER = os.getenv("DB_USER"),
                DB_PASSWORD = os.getenv("DB_PASSWORD")
                 ):
        self.conn = psycopg2.connect(host=B_HOST, database=DB_NAME, user=DB_USER , password=DB_PASSWORD, port=DB_PORT)
>>>>>>> 0d55d2b9960df81e6e961bdfa63d8d9dc1d7c3be
        self.cur = self.conn.cursor()

    def criar(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def inserir(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()

    def sair(self):
        self.cur.close()
<<<<<<< HEAD
        self.conn.close()

   
=======
        self.conn.close()
>>>>>>> 0d55d2b9960df81e6e961bdfa63d8d9dc1d7c3be
