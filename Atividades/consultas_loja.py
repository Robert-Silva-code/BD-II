from modelos_loja import Produto, Categoria
from sqlalchemy import create_engine, select, exists
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #gabinete = Produto(nome="Gabinete Gamer", codigo_barras="8497745733", preco=500, categoria_id=1, em_estoque=False)

    query = select(Produto)

    produtos = session.execute(query).scalars().all()

    monitor_especifico = session.query(Produto).get(1)

    if monitor_especifico:
        print(f"Encontramos: {monitor_especifico.nome}")
    else:
        print("Produto não encontrado.")

    #for produto in produtos:
        #print(produto)

    filtro = session.query(Produto).filter_by(em_estoque=True).all()

    filtro_avancado = session.query(Produto).filter(Produto.preco > 100, Produto.nome.like('%gamer')).first()

    # if filtro_avancado:
    #     print(f"Encontramos: {filtro_avancado.nome}")
    # else:
    #     print("Produto não encontrado.")

    # print(filtro)

    existe_produto = exists().where(Produto.categoria_id == Categoria.id)

    produto_com_categoria = session.query(Categoria).filter(existe_produto).all()

    for categoria in produto_com_categoria:
        print(f"A categoria de nome: '{categoria.nome}' possui produtos")




    session.commit()