#  Personal Branding RAG System

A production-grade **Retrieval-Augmented Generation (RAG)** system designed to function as an AI-powered **Personal Branding Strategist**.

This project demonstrates enterprise-level software engineering principles applied to LLM systems — combining Clean Architecture, modular design, semantic retrieval, and strict grounding to eliminate hallucinations.

It is intentionally built as a showcase of:

- Clean Code
- SOLID Principles
- Dependency Injection
- Modular System Design
- Production-Oriented AI Engineering

---

##  Key Highlights

###  Enterprise-Grade Architecture
Built with clear separation of concerns:
- Configuration Layer
- Infrastructure Layer
- Application Orchestration
- Core RAG Engine
- API-ready integration support

Designed for scalability and maintainability.

---

###  Advanced Retrieval Pipeline
- Vector storage powered by **ChromaDB**
- Semantic embeddings via **HuggingFace** (`sentence-transformers/all-MiniLM-L6-v2`)
- Top-K similarity retrieval for high precision context injection

---

###  Session-Aware Context
Implements lightweight in-memory session tracking:
- Maintains conversational continuity
- No external memory overhead
- Fully resettable per session

---

###  LangChain Expression Language (LCEL)
Uses LCEL pipelines to chain:

Retriever → Prompt Template → LLM → Output Parser

This ensures:
- Composability
- Clean orchestration
- Clear data flow

---

###  Cost & Latency Optimized
- Detects existing persisted vector database before rebuilding
- Avoids unnecessary embedding recomputation
- Reduces API cost footprint

---

###  Strict Anti-Hallucination Design
Prompt constraints enforce:
- Context-only answers
- No fabrication
- Explicit fallback message when information is unavailable

---

##  Technical Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.11+ |
| LLM Orchestration | LangChain (Core & Community) |
| Vector Database | Chroma |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| LLM Provider | OpenRouter API |
| Configuration | `dataclasses` + `python-dotenv` |
| Logging | Structured Python logging |

Default LLM configuration:

meta-llama/llama-3-70b-instruct


(Provider configurable via environment variables)

---

##  System Architecture Overview

### 1 Document Processing
- Loads `about_me.txt`
- Splits text using `RecursiveCharacterTextSplitter`
- Preserves semantic overlap

### 2 Embedding & Persistence
- Generates embeddings locally
- Stores vectors in ChromaDB
- Persists to disk for reuse

### 3 Retrieval-Augmented Generation
Pipeline flow:

```pash
User Question
↓
Retriever (Top-K)
↓
Prompt Template (Persona + Constraints)
↓
LLM
↓
Final Answer
```

---

##  Getting Started

### 1 Prerequisites

- Python 3.11+
- OpenRouter (or OpenAI-compatible) API Key

---

### 2 Installation

```bash
git clone https://github.com/mohamedramadanm1/personal-branding-rag.git
cd personal-branding-rag
pip install -r requirements.txt
```
### 3 Environment Variables


Create a .env file in the root directory:
```pash
OPENAI_API_KEY=your_openrouter_key_here
OPENAI_BASE_URL=https://openrouter.ai/api/v1
```

### 4 Run the System
```pash
python main.py
```

You can now interact with the assistant via terminal.
