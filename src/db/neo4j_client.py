from neo4j import GraphDatabase

uri = "bolt://neo4j:7687"

driver = GraphDatabase.driver(
    uri,
    auth=("neo4j", "password")
)