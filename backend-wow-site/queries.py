import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

url: str = os.getenv("URL")
key: str = os.getenv("KEY")
supabase: Client = create_client(url, key)

data, count = supabase.table('user').insert({"id": 1, "name": "Felipe de Pietro", "username": "feelp19", "email": "flp.pietro19@gmail.com", "senha":"sk8203040"}).execute()
data, count = supabase.table('user').insert({"id": 2, "name": "Many gold", "username":"lokokkx3", "email":"lokokkx3@gmail.com", "senha":"manylokko19"}).execute()

response = supabase.table('user').select("*").execute()

