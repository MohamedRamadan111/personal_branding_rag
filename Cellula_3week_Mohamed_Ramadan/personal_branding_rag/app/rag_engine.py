import os
from typing import List, Tuple

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
#from langchain_chat_models import ChatOpenAI

from .config import RAGConfig
from .prompt_factory import PromptFactory


class RAGEngine:
    """
    Core Retrieval-Augmented Generation engine.
    """

    def __init__(
        self,
        config: RAGConfig,
        vector_store: Chroma,
        logger
    ) -> None:
        self.config: RAGConfig = config
        self.logger = logger
        self.vector_store: Chroma = vector_store

        self.llm: ChatOpenAI = ChatOpenAI(
            model=config.model_name,
            temperature=config.temperature,
            base_url=os.getenv("OPENROUTER_BASE_URL"),
            api_key=os.getenv("OPENROUTER_API_KEY"),
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "Personal Branding RAG"
            }
        )

        self.retriever = vector_store.as_retriever(
            search_kwargs={"k": config.top_k}
        )

        self.chat_history: List[Tuple[str, str]] = []

        self.prompt = PromptFactory.build()
        self.chain = self._build_chain()

    def _build_chain(self):
        return (
            {
                "context": self.retriever,
                "question": RunnablePassthrough(),
                "history": lambda _: self._format_history(),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def _format_history(self) -> str:
        return "\n".join(
            f"User: {question}\nAssistant: {answer}"
            for question, answer in self.chat_history[-5:]
        )

    def ask(self, question: str) -> str:
        """
        Process user question through RAG pipeline.
        """
        response: str = self.chain.invoke(question)
        self.chat_history.append((question, response))
        return response

    def reset_session_memory(self) -> None:
        """
        Clear in-memory session history.
        """
        self.chat_history.clear()