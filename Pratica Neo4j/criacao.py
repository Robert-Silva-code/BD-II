from neo4j import GraphDatabase

uri = "neo4j+s://58331087.databases.neo4j.io"
user="58331087"
password = "XL0UTmwP0_-P4dlNwOxt81kfdtuip9ngt0tUbmoXGT4"

driver = GraphDatabase.driver(uri, auth=(user, password))

def criar_dados(tx):
    tx.run("CREATE (:Usuario {nome: 'Robert'})")
    tx.run("CREATE (:Usuario {nome: 'Samuel'})")
    tx.run("CREATE (:Usuario {nome: 'Davi'})")
    tx.run("CREATE (:Usuario {nome: 'Danilo'})")
    tx.run("CREATE (:Grupo {nome: 'BD2'})")
    tx.run("CREATE (:Postagem {id: 1, conteudo: 'Olá, Pythonistas!'})")

with driver.session() as session:
    session.execute_write(criar_dados)

driver.close()