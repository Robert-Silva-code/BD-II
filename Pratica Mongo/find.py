from conexao import AtlasConnection
from bson.decimal128 import Decimal128
db_name = 'cinema'


try:
    with AtlasConnection() as conexao:
        # 1. SOLICITANDO O BANCO DE DADOS
        # A classe retorna o objeto do banco de dados que queremos.
        db = conexao.get_database(db_name)
        collection = db['cinema']

        # --- Usando find_one ---
        # Busca o primeiro produto da marca "VisionMax"
        # produto = collection.find_one({"marca": "VisionMax"})
        # print(f"\nBusca com find_one:\n{produto}")

        # --- Usando find ---
        # Busca TODOS os produtos da marca "VisionMax"
        print("\nBusca com find (usando um loop):")
        cursor_cinema = collection.find({"ano_lancamento": {"$gt": Decimal128("2000")} })
        for doc in cursor_cinema:
            print(doc)
except (ValueError, ConnectionError) as e:
        # Captura erros de configuração ou conexão levantados pela nossa classe
        print(f"\nUm erro impediu a execução do programa: {e}")
except Exception as e:
    # Captura outros erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")