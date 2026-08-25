from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True)
    matricula = Column(String(20), nullable=False, unique=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True)
    data_nascimento = Column(Date)