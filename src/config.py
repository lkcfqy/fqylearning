import os

# Neo4j Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# LLM Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
LLM_MODEL = "deepseek-r1:8b"
EMBEDDING_MODEL = "BAAI/bge-m3"

# HuggingFace / Local Model Paths
# If using local weights directly instead of Ollama for embeddings
LOCAL_EMBEDDING_PATH = os.getenv("LOCAL_EMBEDDING_PATH", "BAAI/bge-m3")

# LangSmith / LangFuse
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "pk-lf-...")
LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "sk-lf-...")
LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "http://localhost:3000")
