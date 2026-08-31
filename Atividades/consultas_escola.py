from modelos_escola import Aluno, Turma
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    aluno_especifico = session.query(Aluno).get(1)
    
    if aluno_especifico:
        print(f"Encontramos: {aluno_especifico.nome} | {aluno_especifico.matricula}")
    else:
        print("Aluno não encontrado.")
    
    
    session.commit()