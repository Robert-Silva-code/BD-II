from datetime import date, datetime
from modelos_escola import Aluno, Turma
from sqlalchemy import create_engine, select, or_, exists, func
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///escola.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #aluno = Aluno(nome="Senior", matricula="202720400041", email="Senior@email.com", turma_id=3, data_nascimento=datetime(2008, 12, 12),)

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

    """
    tamanho_pagina = 10
    pagina_atual = 3


    total_alunos = session.query(Aluno).count()

    ordenados = session.query(Aluno).order_by(Aluno.nome.asc()).all()

    alunos_paginados = session.query(Aluno)\
        .limit(tamanho_pagina)\
        .offset((pagina_atual - 1) * tamanho_pagina)\
        .all()
    print(f"O total de alunos é igual a {total_alunos}")

    for estudante in alunos_paginados:
        print(f"Nome: {estudante.nome} | Matricula: {estudante.matricula}")
    
    for aluno in ordenados:
        print(aluno.nome)


    aluno_turma = session.query(Aluno, Turma)\
        .outerjoin(Turma, Aluno.turma_id == Turma.id)\
        .all()

    for aluno, turma in aluno_turma:
        nome_turma = turma.nome_turma if turma else "Sem Turma"
        print(f"Aluno: {aluno.nome} | Turma: {nome_turma}")


    aluno_sem_turma = session.query(Aluno)\
    .outerjoin(Turma, Aluno.turma_id == Turma.id)\
    .filter(Turma.id == None)\
    .all()


    for aluno in aluno_sem_turma:
        print(aluno.nome)


    relatorio_turma = session.query(
        Aluno.turma_id,
        func.count(Aluno.id)
        ).group_by(Aluno.turma_id)\
        .having(func.count(Aluno.id) > 30)\
        .all()

    for turma, total_aluno in relatorio_turma:
        print(f"A turma de Id {turma} tem {total_aluno} alunos")
    """


    consulta_aluno = session.query(Aluno).filter(
        Aluno.turma_id == 3,
        Aluno.data_nascimento != None
        )

    calculo_idade = consulta_aluno.add_columns(
        (date.today() - Aluno.data_nascimento).label('idade_aproximada')
    )

    #calculo_idade = consulta_aluno.add_columns(
    #    (func.extract('year', func.current_date()) - func.extract('year', Aluno.data_nascimento)).label('idade_aproximada')
    #)


    for aluno, idade in calculo_idade.all():
        print(f"Nome: {aluno.nome} | Data de nascimento: {aluno.data_nascimento} | Idade aproximada: {idade}")


    session.commit()