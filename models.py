from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Estudante(Base):
    __tablename__ = 'estudantes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)