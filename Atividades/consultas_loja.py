from modelos_loja import Produto, Categoria
from sqlalchemy import create_engine, select, exists, func
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #jogo = Produto(nome="Rain World", codigo_barras="5661954898", preco=59.99, categoria_id=3, em_estoque=True)
    #session.add(sem_ideia)
    query = select(Produto)

    produtos = session.execute(query).scalars().all()

    monitor_especifico = session.query(Produto).get(1)

    if monitor_especifico:
        print(f"Encontramos: {monitor_especifico.nome}")
    else:
        print("Produto não encontrado.")

    #for produto in produtos:
        #print(produto)
    """
    
    filtro = session.query(Produto).filter_by(em_estoque=True).all()

    filtro_avancado = session.query(Produto).filter(Produto.preco > 100, Produto.nome.like('%gamer')).first()

    if filtro_avancado:
        print(f"Encontramos: {filtro_avancado.nome}")
    else:
        print("Produto não encontrado.")

    # print(filtro)

    existe_produto = exists().where(Produto.categoria_id == Categoria.id)

    produto_com_categoria = session.query(Categoria).filter(existe_produto).all()

    for categoria in produto_com_categoria:
        print(f"A categoria de nome: '{categoria.nome}' possui produtos")
    tamanho_pagina = 5
    pagina_atual = 2


    total_produtos = session.query(Produto).count()

    produtos_unicos = session.query(Produto.categoria_id).distinct().all()

    produtos_paginados = session.query(Produto)\
        .order_by(Produto.preco.desc())\
        .limit(tamanho_pagina)\
        .offset((pagina_atual - 1) * tamanho_pagina)\
        .all()


    produtos_com_categoria = session.query(Produto.nome, Categoria.nome).join(Categoria).all()

    for nome_produto, nome_categoria in produtos_com_categoria:
        print(f"Produto - {nome_produto} | Categoria - {nome_categoria}")

    categoria_orfa = session.query(Categoria)\
    .outerjoin(Produto, Categoria.id == Produto.categoria_id)\
    .filter(Produto.id == None)\
    .all()

    for categoria in categoria_orfa:
        print(categoria.nome)
    """

    relatorio_vendas = session.query(
        Produto.categoria_id,
        func.avg(Produto.preco).label('media_preco'),
        func.count(Produto.id).label('total_produto')
        ).group_by(Produto.categoria_id)\
        .having(func.avg(Produto.preco) > 250)\
        .all()

    for id_categoria, media_preco , estoque in relatorio_vendas:
        print(f"Id Categoria: {id_categoria} | Estoque: {estoque} | Média de preços: {media_preco:.2f}")
    


    session.commit()