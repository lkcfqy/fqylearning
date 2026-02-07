from langchain_neo4j import Neo4jGraph
from src.config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD

def get_graph_client() -> Neo4jGraph:
    """Initialize and return a Neo4jGraph client."""
    return Neo4jGraph(
        url=NEO4J_URI,
        username=NEO4J_USERNAME,
        password=NEO4J_PASSWORD,
        refresh_schema=False
    )

def query_graph(query: str, params: dict = None):
    """Execute a Cypher query on the graph database."""
    graph = get_graph_client()
    return graph.query(query, params)
