"""Configuration management."""

import os
from typing import Any, Dict
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class Config:
    """Application configuration."""
    
    # Environment
    environment: str = os.getenv("ENVIRONMENT", "development")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    workers: int = int(os.getenv("WORKERS", "1"))
    
    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # Database Configuration
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./gen_ai_rag.db")
    
    # AWS Configuration
    aws_region: str = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    
    # ECS Configuration
    ecs_cluster_name: str = os.getenv("ECS_CLUSTER_NAME", "gen-ai-rag-cluster")
    ecs_service_name: str = os.getenv("ECS_SERVICE_NAME", "gen-ai-rag-service")
    ecs_task_definition: str = os.getenv("ECS_TASK_DEFINITION", "gen-ai-rag-task")
    
    # Vector Database Configuration
    vector_db_path: str = os.getenv("VECTOR_DB_PATH", "./data/vectordb")
    chroma_persist_directory: str = os.getenv("CHROMA_PERSIST_DIRECTORY", "./data/chroma")
    
    # Application specific settings
    max_tokens: int = int(os.getenv("MAX_TOKENS", "4000"))
    temperature: float = float(os.getenv("TEMPERATURE", "0.7"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "1000"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP", "200"))


def get_config() -> Config:
    """Get application configuration.
    
    Returns:
        Config instance
    """
    return Config()


def get_settings() -> Dict[str, Any]:
    """Get application settings as dictionary.
    
    Returns:
        Dictionary of application settings
    """
    config = get_config()
    return {
        "environment": config.environment,
        "debug": config.debug,
        "log_level": config.log_level,
        "api_host": config.api_host,
        "api_port": config.api_port,
        "workers": config.workers,
        "max_tokens": config.max_tokens,
        "temperature": config.temperature,
        "chunk_size": config.chunk_size,
        "chunk_overlap": config.chunk_overlap,
    }
