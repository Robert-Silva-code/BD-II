#robertvinicius_db_user
#bOB3roQmNSjv1kfj

# uri = "mongodb+srv://robertvinicius_db_user:bOB3roQmNSjv1kfj@cluster0.t6y1ytg.mongodb.net/"
# client = MongoClient(uri)
# try:
#     client.admin.command("ping")
#     print("Connected successfully")
#     client.close()

from pymongo import MongoClient
from conexao import AtlasConnection


db_name = 'cinema'


try:
    with AtlasConnection() as conexao:
        # 1. SOLICITANDO O BANCO DE DADOS
        # A classe retorna o objeto do banco de dados que queremos.
        db = conexao.get_database(db_name)
        collection = db['cinema']

        # --- Usando insert_one ---
        produto_unico = {"titulo": "Project Hail Mary", "ano_lancamento": 2026, "diretor": "Christoper Miller e Phil Lord", "generos": "Sci-Fi, Drama"}
        resultado_one = collection.insert_one(produto_unico)
        print(f"Documento único inserido com o ID: {resultado_one.inserted_id}")

        # --- Usando insert_many ---
        lista_produtos = [
            {"titulo": "Saltburn", "ano_lancamento": 2023, "diretor": "Emerald Fennel", "generos": "Suspense, Comédia"},
            {"titulo": "Under the Silver Lake", "ano_lancamento": 2019, "diretor": "David Robert Mitchell", "generos": "Mistério, Comédia"},
            {"titulo": "NightCrawler", "ano_lancamento": 2014, "diretor": "Dan Gilroy", "generos": "Suspense, Crime"}
        ]
        resultado_many = collection.insert_many(lista_produtos)
        print(f"IDs dos documentos inseridos: {resultado_many.inserted_ids}")
except (ValueError, ConnectionError) as e:
        # Captura erros de configuração ou conexão levantados pela nossa classe
        print(f"\nUm erro impediu a execução do programa: {e}")
except Exception as e:
    # Captura outros erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)