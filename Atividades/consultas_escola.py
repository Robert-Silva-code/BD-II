from datetime import date, datetime
from modelos_escola import Aluno, Turma
from sqlalchemy import create_engine, select, or_, exists
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #aluno = Aluno(nome="JuuNana", matricula="202720400017", email="JuuNana@email.com", turma_id=3, data_nascimento=datetime(2009, 10, 7),)

    #session.add(aluno)
    query = select(Aluno)
    aluno_especifico = session.query(Aluno).get(1)

    estudantes = session.execute(query).scalars().all()

    #for estudante in estudantes:
        #print(estudante)

    if aluno_especifico:
        print(f"Encontramos: {aluno_especifico.nome} | {aluno_especifico.matricula}")
    else:
        print("Aluno não encontrado.")

    #filtro = session.query(Turma).filter_by(nome_turma='3° Ano A').first()

    #print(filtro)
    
    # filtro_avancado = session.query(Aluno).filter(or_(
    #             Aluno.data_nascimento > 2006, 
    #             Aluno.email.like('%@escola.com')
    #         )
    #     ).all()

    # if filtro_avancado:
    #     for estudante in filtro_avancado:
    #         print(f"Encontramos o aluno: {estudante.nome}")
    # else:
    #     print(f"Aluno não encontrado")

    turma_id = 1

    existe_aluno = session.query(
        exists().where(Aluno.turma_id == turma_id)
    ).scalar()

    if existe_aluno:
        print("A turma possui alunos")
    else:
        print("A turma não possui alunos.")

    tamanho_pagina = 10
    pagina_atual = 3


    total_alunos = session.query(Aluno).count()

    ordenados = session.query(Aluno).order_by(Aluno.nome.asc()).all()

    alunos_paginados = session.query(Aluno)\
        .limit(tamanho_pagina)\
        .offset((pagina_atual - 1) * tamanho_pagina)\
        .all()
    print(f"O total de alunos é igual a {total_alunos}")
    print(ordenados)
    print(alunos_paginados)

    session.commit()