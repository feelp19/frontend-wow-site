import os
from supabase import create_client, Client
from dotenv import load_dotenv

class Connection:
    def __init__(self):
        self.load_dotenv()

    def conectar(self):
        self.url: str = os.getenv("URL")
        self.key: str = os.getenv("KEY")
