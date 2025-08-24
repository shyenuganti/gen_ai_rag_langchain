# Gen AI RAG LangChain

A comprehensive Python project for building Retrieval-Augmented Generation (RAG) systems using LangChain.

## Features

- 🚀 **Modern Python Setup**: Built with Python 3.11+, UV package manager, and modern tooling
- 🔧 **Development Tools**: Pre-commit hooks, linting, type checking, and code formatting
- 🧪 **Comprehensive Testing**: Unit, integration, and functional tests with pytest
- 🐳 **Containerization**: Docker and Docker Compose support
- ☁️ **Cloud Deployment**: AWS ECS deployment with GitHub Actions CI/CD
- 📚 **Documentation**: Automatic documentation generation with MkDocs
- 🔒 **Security**: Built-in security scanning with Bandit and Safety
- 🌟 **Modern RAG**: Powered by LangChain for state-of-the-art RAG implementations

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [UV](https://github.com/astral-sh/uv) package manager
- [direnv](https://direnv.net/) (optional but recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/shyenuganti/gen_ai_rag_langchain.git
cd gen_ai_rag_langchain
```

2. Set up the environment:
```bash
# If using direnv
direnv allow

# Otherwise, set up manually
export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
```

3. Install dependencies with UV:
```bash
uv venv
uv pip install -e ".[dev,test,docs]"
```

4. Copy environment file:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Install pre-commit hooks:
```bash
uv run pre-commit install
```

### Usage

#### Command Line Interface

```bash
# Process a query
gen-ai-rag query "What is artificial intelligence?"

# Start the API server
gen-ai-rag server --host 0.0.0.0 --port 8000

# Health check
gen-ai-rag health
```

#### Python API

```python
from gen_ai_rag_langchain.core import RAGSystem
from gen_ai_rag_langchain.config import get_config

# Initialize the system
config = get_config()
rag_system = RAGSystem(config.__dict__)

# Process a query
result = rag_system.process_query("What is machine learning?")
print(result["response"])
```

#### REST API

Start the server:
```bash
uv run python -m gen_ai_rag_langchain.api
```

Then make requests:
```bash
# Health check
curl http://localhost:8000/health

# Process a query
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is deep learning?"}'
```

## Development

### Running Tests

```bash
# All tests
uv run pytest

# Unit tests only
uv run pytest tests/unit/ -m "unit"

# Integration tests
uv run pytest tests/integration/ -m "integration"

# Functional tests
uv run pytest tests/functional/ -m "functional"

# With coverage
uv run pytest --cov=src/gen_ai_rag_langchain --cov-report=html
```

### Code Quality

```bash
# Format code
uv run black src/ tests/
uv run isort src/ tests/

# Lint code
uv run flake8 src/ tests/
uv run mypy src/

# Security scan
uv run bandit -r src/
uv run safety check
```

### Documentation

```bash
# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```

## Deployment

### Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t gen-ai-rag-langchain .
docker run -p 8000:8000 gen-ai-rag-langchain
```

### AWS ECS

1. Configure AWS credentials and update `deployment/task-definition.json`
2. Run the deployment script:
```bash
./deployment/deploy.sh
```

### GitHub Actions

The project includes a complete CI/CD pipeline that:
- Runs tests on multiple Python versions
- Performs security scanning
- Builds and pushes Docker images to ECR
- Deploys to AWS ECS automatically on main branch pushes

## Project Structure

```
gen_ai_rag_langchain/
├── src/gen_ai_rag_langchain/     # Main package
│   ├── __init__.py
│   ├── core.py                   # Core RAG functionality
│   ├── config.py                 # Configuration management
│   ├── api.py                    # FastAPI web application
│   └── cli.py                    # Command line interface
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── functional/               # Functional tests
├── deployment/                   # Deployment configurations
│   ├── task-definition.json      # ECS task definition
│   └── deploy.sh                 # Deployment script
├── docs/                         # Documentation
├── .github/workflows/            # GitHub Actions
├── pyproject.toml               # Project configuration
├── Dockerfile                   # Container configuration
├── docker-compose.yml           # Local development
└── mkdocs.yml                   # Documentation configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the test suite: `uv run pytest`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Project Summary

This project provides a **complete, production-ready foundation** for building RAG (Retrieval-Augmented Generation) applications with modern Python tooling, comprehensive testing, and deployment automation.

### ✅ Features Implemented

#### **🚀 Modern Python Setup**
- **UV Package Manager**: Fast, modern Python package installer and resolver
- **Python 3.11+**: Support for the latest Python features and performance improvements
- **Virtual Environment Management**: Automated virtual environment setup and management
- **TOML Configuration**: Modern `pyproject.toml` configuration following Python standards

#### **🔧 Development Environment**
- **direnv Integration**: Automatic environment variable loading and PYTHONPATH setup
- **Environment Templates**: `.env.example` with comprehensive configuration options
- **Development Scripts**: Automated setup scripts and Makefile for common tasks
- **IDE Support**: Pre-configured for VS Code and other modern IDEs

#### **🧪 Comprehensive Testing Suite**
- **Unit Tests**: Fast, isolated tests for individual components (`tests/unit/`)
- **Integration Tests**: Tests for component interactions (`tests/integration/`)
- **Functional Tests**: End-to-end testing of complete workflows (`tests/functional/`)
- **Coverage Reporting**: HTML and XML coverage reports with configurable thresholds
- **Test Markers**: Organized test categories for selective test execution
- **Pytest Configuration**: Advanced pytest setup with fixtures and custom markers

#### **🔒 Code Quality & Security**
- **Pre-commit Hooks**: Automated code quality checks before commits
- **Code Formatting**: Black for consistent Python code formatting
- **Import Sorting**: isort for organized import statements
- **Linting**: flake8 for code style and error detection
- **Type Checking**: mypy for static type analysis
- **Security Scanning**: Bandit for security vulnerability detection
- **Dependency Security**: Safety for checking known vulnerabilities in dependencies
- **Git Hooks**: GitGuardian for secrets detection

#### **🐳 Containerization & Local Development**
- **Multi-stage Dockerfile**: Optimized for production with security best practices
- **Docker Compose**: Complete local development environment with services
- **Health Checks**: Built-in container health monitoring
- **Non-root User**: Security-hardened container configuration
- **Environment Variables**: Flexible configuration through environment variables

#### **☁️ Cloud Deployment (AWS ECS)**
- **ECS Task Definition**: Production-ready AWS ECS configuration
- **Fargate Compatibility**: Serverless container deployment
- **Load Balancer Support**: Application Load Balancer integration
- **Auto Scaling**: Configurable CPU and memory-based scaling
- **Secrets Management**: AWS Secrets Manager integration for sensitive data
- **CloudWatch Logging**: Centralized logging and monitoring
- **Deployment Script**: Automated deployment with error handling and rollback

#### **🔄 CI/CD Pipeline (GitHub Actions)**
- **Multi-Python Testing**: Matrix testing across Python 3.11 and 3.12
- **Quality Gates**: Automated code quality checks and security scanning
- **Test Reporting**: Detailed test results with coverage reporting
- **Security Scanning**: Comprehensive security analysis in CI pipeline
- **Docker Build & Push**: Automated container image building and ECR deployment
- **Blue-Green Deployment**: Safe production deployments with rollback capability
- **Release Automation**: Automatic PyPI package publishing on releases
- **Artifact Management**: Build artifacts and test reports storage

#### **📚 Documentation System**
- **MkDocs**: Modern documentation site generation
- **Material Theme**: Beautiful, responsive documentation theme
- **API Documentation**: Automatic API reference generation with mkdocstrings
- **Code Examples**: Interactive code examples and usage guides
- **Search Functionality**: Full-text search across documentation
- **Multi-format Output**: HTML, PDF, and other output formats

#### **🖥️ Application Architecture**
- **FastAPI Web API**: Modern, fast web framework with automatic OpenAPI docs
- **CLI Interface**: Comprehensive command-line interface with argparse
- **Core RAG System**: Extensible RAG implementation with LangChain
- **Configuration Management**: Centralized configuration with environment variable support
- **Structured Logging**: Professional logging with structlog
- **Health Monitoring**: Built-in health check endpoints and monitoring

#### **🛠️ Developer Experience**
- **Make Commands**: Comprehensive Makefile with 30+ development commands
- **Setup Automation**: One-command project setup with dependency installation
- **Development Server**: Hot-reloading development server for rapid iteration
- **Code Formatting**: Automatic code formatting on save
- **Type Safety**: Full type hints and mypy integration
- **Error Handling**: Comprehensive error handling and logging
- **Development Tools**: Integration with modern Python development tools

## 🛠️ Make Commands Reference

The project includes a comprehensive Makefile with commands for all development tasks:

### **Setup & Installation**
```bash
make help              # Show all available commands
make setup             # Complete project setup (recommended first step)
make install           # Install project dependencies only
make install-dev       # Install with development dependencies
make dev-setup         # Complete development environment setup
```

### **Code Quality**
```bash
make format            # Format code with black and isort
make format-check      # Check formatting without changes
make lint              # Run flake8 linting
make type-check        # Run mypy type checking
make security-check    # Run bandit and safety security checks
make check-all         # Run all quality checks
```

### **Testing**
```bash
make test              # Run all tests
make test-unit         # Run unit tests only
make test-integration  # Run integration tests only
make test-functional   # Run functional tests only
make test-watch        # Run tests in watch mode
make coverage          # Generate HTML coverage report
make coverage-xml      # Generate XML coverage report
make ci-test          # Run tests with CI configuration
```

### **Development Server**
```bash
make serve             # Start development server with auto-reload
make serve-prod        # Start production server
make cli-health        # Test CLI health check
make cli-query QUERY="your question"  # Test CLI query
```

### **Documentation**
```bash
make docs              # Build documentation
make docs-serve        # Serve documentation locally (http://localhost:8000)
make docs-clean        # Clean documentation build files
```

### **Docker & Containers**
```bash
make docker-build      # Build Docker image
make docker-run        # Run Docker container
make docker-compose-up # Start all services with docker-compose
make docker-compose-down # Stop docker-compose services
make docker-clean      # Clean Docker artifacts
```

### **Building & Packaging**
```bash
make build             # Build Python package
make build-clean       # Clean build artifacts
make version           # Show current version
```

### **Cloud Deployment**
```bash
make deploy            # Deploy to AWS ECS
```

### **Maintenance**
```bash
make clean             # Clean all build artifacts and caches
make check-deps        # Check for outdated dependencies
make install-uv        # Install UV package manager
```

### **Examples & Help**
```bash
make example-api       # Show API usage examples
make example-cli       # Show CLI usage examples
```

## 🔧 Key Tools & Technologies

### **Core Technologies**
- **[Python 3.11+](https://www.python.org/)**: Modern Python with latest features and performance
- **[UV](https://github.com/astral-sh/uv)**: Ultra-fast Python package installer and resolver
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast web framework with automatic API docs
- **[LangChain](https://github.com/langchain-ai/langchain)**: Framework for developing LLM applications
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Data validation using Python type annotations

### **Development Environment**
- **[direnv](https://direnv.net/)**: Automatic environment variable loading
- **[pre-commit](https://pre-commit.com/)**: Git hook scripts for code quality
- **[pytest](https://pytest.org/)**: Advanced Python testing framework
- **[Docker](https://www.docker.com/)**: Containerization platform
- **[Docker Compose](https://docs.docker.com/compose/)**: Multi-container application management

### **Code Quality Tools**
- **[Black](https://black.readthedocs.io/)**: Uncompromising Python code formatter
- **[isort](https://pycqa.github.io/isort/)**: Python import statement organizer
- **[flake8](https://flake8.pycqa.org/)**: Python code linting tool
- **[mypy](https://mypy.readthedocs.io/)**: Static type checker for Python
- **[Bandit](https://bandit.readthedocs.io/)**: Security linter for Python
- **[Safety](https://pyup.io/safety/)**: Vulnerability scanner for Python dependencies

### **Testing & Coverage**
- **[pytest-cov](https://pytest-cov.readthedocs.io/)**: Coverage plugin for pytest
- **[pytest-asyncio](https://pytest-asyncio.readthedocs.io/)**: Async testing support
- **[pytest-mock](https://pytest-mock.readthedocs.io/)**: Mocking utilities for pytest
- **[requests-mock](https://requests-mock.readthedocs.io/)**: HTTP request mocking

### **Documentation**
- **[MkDocs](https://www.mkdocs.org/)**: Static site generator for documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)**: Material Design theme
- **[mkdocstrings](https://mkdocstrings.github.io/)**: Automatic API documentation generation

### **Cloud & Deployment**
- **[AWS ECS](https://aws.amazon.com/ecs/)**: Container orchestration service
- **[AWS Fargate](https://aws.amazon.com/fargate/)**: Serverless container platform
- **[AWS ECR](https://aws.amazon.com/ecr/)**: Container registry service
- **[GitHub Actions](https://github.com/features/actions)**: CI/CD automation platform

### **Monitoring & Logging**
- **[structlog](https://www.structlog.org/)**: Structured logging for Python
- **[Uvicorn](https://www.uvicorn.org/)**: Lightning-fast ASGI server

### **Configuration & Environment**
- **[python-dotenv](https://python-dotenv.readthedocs.io/)**: Environment variable loading
- **[TOML](https://toml.io/)**: Configuration file format (pyproject.toml)

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the RAG framework
- [UV](https://github.com/astral-sh/uv) for fast Python package management
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework
- [Pytest](https://pytest.org/) for the testing framework
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for beautiful documentation
- [Astral](https://astral.sh/) for modern Python tooling