"""FastAPI web application."""

from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from gen_ai_rag_langchain.config import get_config
from gen_ai_rag_langchain.core import RAGSystem

# Initialize configuration
config = get_config()

# Create FastAPI app
app = FastAPI(
    title="Gen AI RAG LangChain API",
    description="A comprehensive RAG system built with LangChain",
    version="0.1.0",
    docs_url="/docs" if config.debug else None,
    redoc_url="/redoc" if config.debug else None,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if config.debug else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG system
rag_system = RAGSystem(config.__dict__)


# Request/Response models
class QueryRequest(BaseModel):
    """Query request model."""

    query: str
    max_tokens: int = 4000
    temperature: float = 0.7


class QueryResponse(BaseModel):
    """Query response model."""

    query: str
    response: str
    sources: list
    metadata: Dict[str, Any]


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    version: str


# Routes
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    try:
        health_status = rag_system.health_check()
        return HealthResponse(**health_status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process a query through the RAG system."""
    try:
        result = rag_system.process_query(request.query)
        return QueryResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Gen AI RAG LangChain API",
        "version": "0.1.0",
        "docs": ("/docs" if config.debug else "Documentation disabled in production"),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "gen_ai_rag_langchain.api:app",
        host=config.api_host,
        port=config.api_port,
        reload=config.debug,
        workers=config.workers if not config.debug else 1,
    )
