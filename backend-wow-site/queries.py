from connection import Connection

class Query(Connection):
    def __init__(self):
        connection_status = self.conectar()
        if connection_status != 'Conectado':
            raise Exception(connection_status)
    
    def selecionar(self, table, attr):
        try:
            response = self.supabase.table(table).select(attr).execute()
            return response
        except Exception as e:
            return f'Erro ao executar a consulta: {str(e)}'
    
    def inserir_usuario(self, name, username, email, senha):
        try:
            response = self.supabase.table('user').insert({"name": name, "username":username, "email": email, "password": senha}).execute()
            return f'Inserido com sucesso'
        except Exception as e:
            return f'Erro ao executar a Query: {str(e)}'

    def inserir_news(self, name, description, likes):
        try:
            response = self.supabase.table('news').insert({"name": name, "description": description, "likes": likes}).execute()
            return f'Inserido com sucesso'
        except Exception as e:
            return f'Erro ao executar a Query: {str(e)}'