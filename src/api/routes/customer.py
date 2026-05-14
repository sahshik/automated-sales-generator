from fastapi import APIRouter
from src.db.neo4j_client import driver

router = APIRouter()

@router.get("/add-node")
def add_node():

    with driver.session() as session:

        session.run(
            """
            CREATE (c:Customer {
                name: 'Amazon',
                industry: 'Tech'
            })
            """
        )

    return {
        "status": "Node Created"
    }

@router.post("/customer")
def create_customer(name: str, industry: str):

    with driver.session() as session:

        session.run(
            """
            CREATE (c:Customer {
                name: $name,
                industry: $industry
            })
            """,
            name=name,
            industry=industry
        )

    return {
        "message": "Customer Created",
        "name": name,
        "industry": industry
    }

@router.get("/customers")
def get_customers():

    with driver.session() as session:

        result = session.run(
            """
            MATCH (c:Customer)
            RETURN c.name AS name,
                   c.industry AS industry
            """
        )

        customers = []

        for record in result:

            customers.append({
                "name": record["name"],
                "industry": record["industry"]
            })

    return {
        "customers": customers
    }