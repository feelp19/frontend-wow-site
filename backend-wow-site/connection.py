import os
from supabase import create_client, Client
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        load_dotenv()
    
    def conectar(self):
        self.url: str = os.getenv("URL")
        self.key: str = os.getenv("KEY")

        if not self.url or not self.key:
            return f"URL ou KEY nao encontradas"
        try:
            self.supabase: Client = create_client(self.url, self.key)
            return f'Conectado'
        except Exception as e:
            return f'Nao foi possivel conectar {str(e)}'
