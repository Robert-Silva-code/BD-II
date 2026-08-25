from sqlalchemy import Column, Integer, String, Numeric, Float, Boolean
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    codigo_barras = Column(String(30), nullable=False, unique=True)
    preco = Column(Float, nullable=False)
    em_estoque = Column(Boolean, default=True)

    def __repr__(self):
        return f"Produto(id={self.id}, Nome='{self.nome}', Preço='{self.preco}', Está em estoque:'{self.em_estoque}')"
