from modelos_escola import Aluno, Turma
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    """
    tsi = Turma(nome_turma="TSI", ano_letivo=2)
    samuel = Aluno(nome="Samuel", matricula="202512040017", email="samuel@teste.com", turma_id=1)
    """
    query = select(Aluno)
    aluno_especifico = session.query(Aluno).get(1)

    estudantes = session.execute(query).scalars().all()

    for estudante in estudantes:
        print(estudante)

    if aluno_especifico:
        print(f"Encontramos: {aluno_especifico.nome} | {aluno_especifico.matricula}")
    else:
        print("Aluno não encontrado.")
    
    
    session.commit()