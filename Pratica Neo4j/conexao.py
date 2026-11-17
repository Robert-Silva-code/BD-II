from neo4j import GraphDatabase

URI = "neo4j+s://58331087.databases.neo4j.io"
AUTH = ("58331087", "XL0UTmwP0_-P4dlNwOxt81kfdtuip9ngt0tUbmoXGT4")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    print('Conexão bem-sucedida!')
