from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

#Codigo Slides

class Curso(Base):
    __tablename__ = 'cursos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, unique=True)


class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    curso_id = Column(Integer, ForeignKey('cursos.id'), nullable=False)

    def __repr__(self):
        return f"Estudante(id={self.id}, nome='{self.nome}')"


#Exercicio 1 - Aula 4 - ORM
class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Numeric(10, 2))
    em_estoque = Column(Boolean, default=True)


#Exercicio 2 - Aula 4 - ORM
class Autor(Base):
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)


class Livro(Base):
    __tablename__ = 'livros'

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    autor_id = Column(Integer, ForeignKey('autores.id'))