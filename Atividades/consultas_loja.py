from modelos_loja import Produto, Categoria
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

Session = sessionmaker(bind=engine)


with Session() as session:
    '''
    # hardware = Categoria(nome="Hardware")
    # monitor = Produto(nome="AOC", codigo_barras="841655631", preco=400, categoria_id=1)

    # session.add(hardware)
    # session.add(monitor)
    '''
    query = select(Produto)

    produtos = session.execute(query).scalars().all()

    monitor_especifico = session.query(Produto).get(1)

    if monitor_especifico:
        print(f"Encontramos: {monitor_especifico.nome}")
    else:
        print("Produto não encontrado.")

    for produto in produtos:
        print(produto)

    session.commit()