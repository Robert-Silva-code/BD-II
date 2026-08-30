from sqlalchemy import create_engine
from modelos_escola import Base

engine = create_engine("sqlite:///escola.db", echo=True)

print("Gerando o schema do banco de dados...")
Base.metadata.create_all(engine)
print("Schema gerado com sucesso!")