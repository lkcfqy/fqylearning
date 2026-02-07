from typing import List, Dict, Any
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from src.graph_db import get_graph_client, query_graph
from src.model import get_llm, get_embeddings

# Define the structure for extracted entities and relationships
class Entity(BaseModel):
    name: str = Field(description="Name of the entity")
    type: str = Field(description="Type of the entity")
    description: str = Field(description="Description of the entity")

class Relation(BaseModel):
    source: str = Field(description="Name of the source entity")
    target: str = Field(description="Name of the target entity")
    type: str = Field(description="Type of the relationship")
    description: str = Field(description="Description of the relationship")

class KnowledgeGraph(BaseModel):
    entities: List[Entity] = Field(description="List of entities")
    relations: List[Relation] = Field(description="List of relationships")

def extract_knowledge(text: str) -> Dict[str, Any]:
    """Extract entities and relations from text using LLM."""
    llm = get_llm()
    parser = JsonOutputParser(pydantic_object=KnowledgeGraph)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a knowledge graph extractor. Extract entities and relationships from the text. \n{format_instructions}"),
        ("human", "{text}"),
    ])
    
    chain = prompt | llm | parser
    return chain.invoke({"text": text, "format_instructions": parser.get_format_instructions()})

def save_to_memory(text: str, session_id: str = "default"):
    """Extract knowledge from text and save to Neo4j."""
    try:
        data = extract_knowledge(text)
        graph = get_graph_client()
        
        # Add entities
        for entity in data.get("entities", []):
            query = """
            MERGE (e:Entity {name: $name})
            ON CREATE SET e.type = $type, e.description = $description, e.created_at = timestamp()
            ON MATCH SET e.last_seen = timestamp()
            """
            graph.query(query, params=entity)
            
        # Add relations
        for rel in data.get("relations", []):
            query = """
            MATCH (s:Entity {name: $source})
            MATCH (t:Entity {name: $target})
            MERGE (s)-[r:RELATION {type: $type}]->(t)
            ON CREATE SET r.description = $description, r.created_at = timestamp()
            """
            graph.query(query, params=rel)
            
        print(f"Saved {len(data.get('entities', []))} entities and {len(data.get('relations', []))} relations.")
    except Exception as e:
        print(f"Error saving to memory: {e}")

def retrieve_memory(query: str, limit: int = 5) -> str:
    """Retrieve relevant context from the graph."""
    # Simple keyword/vector search simulation using purely graph traversal for now
    # Ideally, use vector index here.
    # For now, let's just find entities mentioned in the query and get their neighbors.
    
    # 1. Extract potential entities from query (simplified)
    # real implementation would use LLM or NER
    
    cypher_query = """
    CALL db.index.fulltext.queryNodes("entity_index", $query) YIELD node, score
    RETURN node.name, node.description, collect([(node)-[r]-(other) | {rel: type(r), target: other.name}]) as connections
    LIMIT $limit
    """
    
    # Note: Requires a fulltext index. 
    # We will need to create it first.
    
    return "Context from graph..."

def init_indexes():
    """Create necessary indexes in Neo4j."""
    graph = get_graph_client()
    try:
        graph.query("CREATE FULLTEXT INDEX entity_index IF NOT EXISTS FOR (n:Entity) ON EACH [n.name, n.description]")
    except Exception as e:
        print(f"Index creation failed (might already exist): {e}")

if __name__ == "__main__":
    init_indexes()
