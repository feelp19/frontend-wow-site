import mysql.connector
from mysql.connector import errorcode
import os

class Connection:
    def __init__(self):
        self.conexao = None
    
    def connect(self):
        try:
            if not self.conexao:
                host = os.getenv('HOST')
                user = os.getenv('USER')
                password = os.getenv('PASSWORD')
                database = os.getenv('DATABASE')

                self.conexao = mysql.connector.connect(host = host, user = user, password = password, database = database)

                return f'Conectado'
            else:
                return f'Conexao ja estabelecida'
        except mysql.connector.Error as err:
            return f'Nao foi possivel conectar: {err}'