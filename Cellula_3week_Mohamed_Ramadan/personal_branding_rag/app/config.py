from dataclasses import dataclass


@dataclass(frozen=True)
class RAGConfig:
    """
    Immutable configuration for the RAG system.
    """
    file_path: str
    persist_directory: str = "./vector_db"
    chunk_size: int = 700
    chunk_overlap: int = 100
    model_name: str = "mistralai/mistral-7b-instruct"
    temperature: float = 0.2
    top_k: int = 4