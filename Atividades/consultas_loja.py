from modelos_loja import Produto, Categoria
from sqlalchemy import create_engine, select, exists
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #jogo = Produto(nome="Rain World", codigo_barras="5661954898", preco=59.99, categoria_id=3, em_estoque=True)
    #session.add(jogo)
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
    """
    tamanho_pagina = 5
    pagina_atual = 2


    total_produtos = session.query(Produto).count()

    produtos_unicos = session.query(Produto.categoria_id).distinct().all()

    produtos_paginados = session.query(Produto)\
        .order_by(Produto.preco.desc())\
        .limit(tamanho_pagina)\
        .offset((pagina_atual - 1) * tamanho_pagina)\
        .all()


    produtos_com_categoria = session.query(Produto).join(Categoria).first() #Retornar para esse ponto depois, não entendi o join direito, talvez perguntar mais a Jales?



    produtos_agrupados = session.query(Produto.categoria_id).group_by(categora_id) #Procurar mais depois




    session.commit()