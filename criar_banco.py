from sqlalchemy import create_engine
from models import Base

engine = create_engine("sqlite:///biblioteca.db", echo=True)

print("Gerando o schema do banco de dados...")
Base.metadata.create_all(engine)
print("Schema gerado com sucesso!")