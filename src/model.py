from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import OLLAMA_BASE_URL, LLM_MODEL, LOCAL_EMBEDDING_PATH

def get_llm():
    """Get the specific DeepSeek model via Ollama."""
    return ChatOllama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.6,
        streaming=True,
        # num_gpu=1, # Ollama handles this automatically usually
    )

def get_embeddings():
    """Get the BGE-M3 embedding model."""
    # Running on GPU if available, else CPU
    model_kwargs = {'device': 'cuda'} # or 'cpu'
    encode_kwargs = {'normalize_embeddings': True}
    print(f"Loading embedding model: {LOCAL_EMBEDDING_PATH}...")
    embeddings = HuggingFaceEmbeddings(
        model_name=LOCAL_EMBEDDING_PATH,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    print("Embedding model loaded.")
    return embeddings
