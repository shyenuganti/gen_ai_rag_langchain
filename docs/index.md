# Gen AI RAG LangChain

Welcome to Gen AI RAG LangChain - a comprehensive Python project for building Retrieval-Augmented Generation (RAG) systems using LangChain.

## Overview

This project provides a complete, production-ready foundation for building RAG applications with modern Python tooling, comprehensive testing, and deployment automation.

## Key Features

- **Modern Python Stack**: Python 3.11+, UV package manager, FastAPI
- **RAG Implementation**: Powered by LangChain for state-of-the-art retrieval-augmented generation
- **Development Excellence**: Pre-commit hooks, linting, type checking, security scanning
- **Testing Suite**: Unit, integration, and functional tests with pytest
- **Deployment Ready**: Docker containers, AWS ECS deployment, CI/CD pipelines
- **Documentation**: Automatic API documentation generation

## Getting Started

See the [Getting Started Guide](getting-started.md) for detailed installation and setup instructions.

## API Reference

- [Core Module](api/core.md) - Main RAG functionality
- [Configuration](api/config.md) - Environment and settings management
- [Web API](api/api.md) - FastAPI REST endpoints
- [CLI](api/cli.md) - Command line interface

## Deployment

- [Local Development](deployment/local.md)
- [Docker Deployment](deployment/docker.md)
- [AWS ECS Deployment](deployment/aws-ecs.md)

## Development

- [Testing Guide](testing.md)
- [Contributing Guidelines](contributing.md)

## Architecture

The project follows a clean architecture pattern with clear separation of concerns:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web API       │    │   CLI           │    │   Core Logic    │
│   (FastAPI)     │────▶   (argparse)    │────▶   (RAG System)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                              ┌─────────────────┐
                                              │   Configuration │
                                              │   (Environment) │
                                              └─────────────────┘
```

## Quick Example

```python
from gen_ai_rag_langchain.core import RAGSystem
from gen_ai_rag_langchain.config import get_config

# Initialize the RAG system
config = get_config()
rag_system = RAGSystem(config.__dict__)

# Process a query
result = rag_system.process_query("What is machine learning?")
print(result["response"])
```

## Support

For issues, questions, or contributions, please visit our [GitHub repository](https://github.com/shyenuganti/gen_ai_rag_langchain).
