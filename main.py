from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///escola.db", echo=True)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Olá, mundo!'"))
    print(result.scalar())