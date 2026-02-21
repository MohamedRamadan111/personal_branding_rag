import os
from typing import List, Optional

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from .config import RAGConfig


class VectorStoreService:
    """
    Manages vector database lifecycle.
    """

    def __init__(self, config: RAGConfig, logger) -> None:
        self.config: RAGConfig = config
        self.logger = logger

        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )

    def load(self) -> Optional[Chroma]:
        """
        Load existing vector database if available.
        """
        if os.path.exists(self.config.persist_directory):
            self.logger.info("Loading existing vector database...")
            return Chroma(
                persist_directory=self.config.persist_directory,
                embedding_function=self.embeddings
            )
        return None

    def build(self, documents: List[Document]) -> Chroma:
        """
        Build vector database (persists automatically to persist_directory)
        """
        self.logger.info("Building vector database...")

        os.makedirs(self.config.persist_directory, exist_ok=True)

        vector_store: Chroma = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.config.persist_directory
        )
        
        return vector_store