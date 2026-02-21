import os
from typing import List

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import RAGConfig


class DocumentProcessor:
    """
    Handles document loading and splitting.
    """

    def __init__(self, config: RAGConfig, logger) -> None:
        self.config: RAGConfig = config
        self.logger = logger

    def load(self) -> List[Document]:
        """
        Load source document from disk.
        """
        if not os.path.exists(self.config.file_path):
            raise FileNotFoundError(f"{self.config.file_path} not found.")

        self.logger.info("Loading source document...")
        loader: TextLoader = TextLoader(
            self.config.file_path,
            encoding="utf-8"
        )
        return loader.load()

    def split(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks.
        """
        self.logger.info("Splitting document into chunks...")
        splitter: RecursiveCharacterTextSplitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=self.config.chunk_size,
                chunk_overlap=self.config.chunk_overlap,
            )
        )
        return splitter.split_documents(documents)