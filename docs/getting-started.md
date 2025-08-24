# Getting Started

This guide will help you set up and run the Gen AI RAG LangChain project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11 or higher** - [Download Python](https://www.python.org/downloads/)
- **UV** - Fast Python package installer and resolver
- **Git** - Version control system
- **direnv** (optional) - Environment variable management

### Installing UV

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip
pip install uv
```

### Installing direnv (Optional but Recommended)

```bash
# On macOS
brew install direnv

# On Ubuntu/Debian
sudo apt install direnv

# On Arch Linux
sudo pacman -S direnv
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shyenuganti/gen_ai_rag_langchain.git
cd gen_ai_rag_langchain
```

### 2. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your configuration
# At minimum, you'll want to set:
# - OPENAI_API_KEY (if using OpenAI)
# - DATABASE_URL (if using a database)
```

### 3. Environment Setup

#### Option A: Using direnv (Recommended)

```bash
# Allow direnv to load the .envrc file
direnv allow
```

This will automatically set up your Python path and load environment variables.

#### Option B: Manual Setup

```bash
# Set Python path manually
export PYTHONPATH="${PWD}/src:${PYTHONPATH}"

# Load environment variables
source .env
```

### 4. Install Dependencies

```bash
# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # On Linux/macOS
# or
.venv\Scripts\activate     # On Windows

# Install the project with all dependencies
uv pip install -e ".[dev,test,docs]"
```

### 5. Install Pre-commit Hooks

```bash
uv run pre-commit install
```

## Verification

Verify your installation by running:

```bash
# Check if the package is installed correctly
uv run python -c "from gen_ai_rag_langchain import __version__; print(__version__)"

# Run health check
uv run gen-ai-rag health

# Run a simple test
uv run pytest tests/unit/test_core.py -v
```

## First Steps

### 1. Start the API Server

```bash
# Start the development server
uv run gen-ai-rag server --reload

# Or use the Python module directly
uv run python -m gen_ai_rag_langchain.api
```

The API will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### 2. Try the CLI

```bash
# Process a query via CLI
uv run gen-ai-rag query "What is artificial intelligence?"

# Get help
uv run gen-ai-rag --help
```

### 3. Use the Python API

```python
from gen_ai_rag_langchain.core import RAGSystem
from gen_ai_rag_langchain.config import get_config

# Initialize the system
config = get_config()
rag_system = RAGSystem(config.__dict__)

# Process a query
result = rag_system.process_query("Explain machine learning")
print(f"Response: {result['response']}")
```

## Development Workflow

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test categories
uv run pytest tests/unit/ -m "unit"
uv run pytest tests/integration/ -m "integration"
uv run pytest tests/functional/ -m "functional"

# Run with coverage
uv run pytest --cov=src/gen_ai_rag_langchain --cov-report=html
```

### Code Quality Checks

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

# Documentation will be available at http://localhost:8000
```

## Docker Development

If you prefer to use Docker for development:

```bash
# Build and run with Docker Compose
docker-compose up --build

# The API will be available at http://localhost:8000
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure `PYTHONPATH` is set correctly:
   ```bash
   export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
   ```

2. **UV Not Found**: Ensure UV is installed and in your PATH:
   ```bash
   uv --version
   ```

3. **Permission Denied**: On Unix systems, make sure scripts are executable:
   ```bash
   chmod +x deployment/deploy.sh
   ```

4. **Environment Variables Not Loaded**: If using direnv, ensure it's hooked into your shell:
   ```bash
   eval "$(direnv hook bash)"  # For bash
   eval "$(direnv hook zsh)"   # For zsh
   ```

### Getting Help

- Check the [GitHub Issues](https://github.com/shyenuganti/gen_ai_rag_langchain/issues) for known problems
- Review the [API documentation](api/core.md) for detailed usage information
- Look at the [test files](../tests/) for usage examples

## Next Steps

Now that you have the project set up:

1. Explore the [API Reference](api/core.md) to understand the available functionality
2. Check out the [Testing Guide](testing.md) to understand the test structure
3. Review the [Deployment Options](deployment/local.md) for production deployment
4. Read the [Contributing Guidelines](contributing.md) if you want to contribute
