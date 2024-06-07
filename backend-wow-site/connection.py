import mysql.connector

class Connection:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        try:
            conn = mysql.connector.connect(self.host, self.user, self.password, self.db)
            if conn:
                return f'Conectado'
            else:
                return f'Nao foi possivel conectar'

        except mysqlError as Error:
            return f'Nao foi possivel conectar {Error}'


