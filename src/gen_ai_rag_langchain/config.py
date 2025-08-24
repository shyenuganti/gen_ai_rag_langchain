"""Configuration management."""

import os
from dataclasses import dataclass
from typing import Any, Dict

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


@dataclass
class Config:
    """Application configuration."""

    # Default values will be set in __post_init__
    environment: str = ""
    debug: bool = False
    log_level: str = ""
    api_host: str = ""
    api_port: int = 0
    workers: int = 0
    openai_api_key: str = ""
    database_url: str = ""
    aws_region: str = ""
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    ecs_cluster_name: str = ""
    ecs_service_name: str = ""
    ecs_task_definition: str = ""
    vector_db_path: str = ""
    chroma_persist_directory: str = ""
    max_tokens: int = 0
    temperature: float = 0.0
    chunk_size: int = 0
    chunk_overlap: int = 0

    def __post_init__(self) -> None:
        """Initialize configuration from environment variables."""
        # Environment
        self.environment = os.getenv("ENVIRONMENT", "development")
        self.debug = os.getenv("DEBUG", "False").lower() == "true"
        self.log_level = os.getenv("LOG_LEVEL", "INFO")

        # API Configuration
        # nosec B104: Bind to all interfaces for containerized deployment
        self.api_host = os.getenv("API_HOST", "0.0.0.0")  # nosec
        self.api_port = int(os.getenv("API_PORT", "8000"))
        self.workers = int(os.getenv("WORKERS", "1"))

        # OpenAI Configuration
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "")

        # Database Configuration
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./gen_ai_rag.db")

        # AWS Configuration
        self.aws_region = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID", "")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", "")

        # ECS Configuration
        self.ecs_cluster_name = os.getenv("ECS_CLUSTER_NAME", "gen-ai-rag-cluster")
        self.ecs_service_name = os.getenv("ECS_SERVICE_NAME", "gen-ai-rag-service")
        self.ecs_task_definition = os.getenv("ECS_TASK_DEFINITION", "gen-ai-rag-task")

        # Vector Database Configuration
        self.vector_db_path = os.getenv("VECTOR_DB_PATH", "./data/vectordb")
        self.chroma_persist_directory = os.getenv(
            "CHROMA_PERSIST_DIRECTORY", "./data/chroma"
        )

        # Application specific settings
        self.max_tokens = int(os.getenv("MAX_TOKENS", "4000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.chunk_size = int(os.getenv("CHUNK_SIZE", "1000"))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "200"))


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
