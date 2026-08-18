from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Curso, Estudante, Base

engine = create_engine("sqlite:///escola.db", echo=True)

print("Gerando o schema do banco de dados...")
Base.metadata.create_all(engine)
print("Schema gerado com sucesso!")

Session = sessionmaker(bind=engine)


with Session() as session:
    curso_eng_comp = Curso(nome="Engenharia de Computação")
    estudante_ana = Estudante(nome="Ana", email="ana@email.com", curso_id=1)

    session.add(curso_eng_comp)
    session.add(estudante_ana)

    session.commit()