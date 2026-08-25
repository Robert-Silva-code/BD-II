from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo=True)

Session = sessionmaker(bind=engine)

with engine.connect() as connection:
    resultado = connection.execute(text("SELECT sqlite_version()"))
    print(resultado.scalar())