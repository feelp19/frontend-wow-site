from connection import Connection
from queries import Query

if __name__ == "__main__":
    connect = Connection()
    print(connect.conectar())
    query = Query()
    resultado_inserir_news = query.inserir_news('Breaking News', 'Descrição da notícia', 100)
    print(resultado_inserir_news)
    resultado_inserir_usuario = query.inserir_usuario("Many", "manyx", "lokokkx33@gmail.com", "binholoko")
    print(resultado_inserir_usuario)

    resultado_select = query.selecionar('user', 'name')
    print(resultado_select)