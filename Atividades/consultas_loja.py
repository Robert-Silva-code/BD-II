from modelos_loja import Produto, Categoria
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    #notebook = Produto(nome="Notebook Positivo", codigo_barras="849755633", preco=400, categoria_id=1, em_estoque=False)

    query = select(Produto)

    produtos = session.execute(query).scalars().all()

    monitor_especifico = session.query(Produto).get(1)

    if monitor_especifico:
        print(f"Encontramos: {monitor_especifico.nome}")
    else:
        print("Produto não encontrado.")

    for produto in produtos:
        print(produto)

    filtro = session.query(Produto).filter_by(em_estoque=True).all()

    print(filtro)
    session.commit()

