from dotenv import load_dotenv

from .config import RAGConfig
from .document_processor import DocumentProcessor
from .vector_store import VectorStoreService
from .rag_engine import RAGEngine
from .logging_config import setup_logging


class Application:
    """
    Application orchestrator.
    """

    def __init__(self, config: RAGConfig) -> None:
        load_dotenv()
        self.logger = setup_logging()
        self.config: RAGConfig = config

        self.document_processor = DocumentProcessor(config, self.logger)
        self.vector_service = VectorStoreService(config, self.logger)

        self.vector_store = self._initialize_vector_store()
        self.engine = RAGEngine(config, self.vector_store, self.logger)

    def _initialize_vector_store(self):
        existing = self.vector_service.load()
        if existing:
            return existing

        documents = self.document_processor.load()
        chunks = self.document_processor.split(documents)
        return self.vector_service.build(chunks)

    def run(self) -> None:
        print("\n Personal Branding RAG Ready")
        print("Type 'exit' to quit\n")

        while True:
            user_input: str = input("Ask: ")

            if user_input.lower() == "exit":
                self.engine.reset_session_memory()
                print("Session cleared.")
                break

            answer: str = self.engine.ask(user_input)
            print("\n" + answer + "\n")