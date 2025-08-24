#!/usr/bin/env bash

# Setup script for Gen AI RAG LangChain project
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_step() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main setup function
setup_project() {
    log_info "Setting up Gen AI RAG LangChain project..."
    
    # Check Python version
    log_step "Checking Python version..."
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
        
        if [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -ge 11 ]; then
            log_info "Python $PYTHON_VERSION found ✓"
        else
            log_error "Python 3.11+ required, found $PYTHON_VERSION"
            exit 1
        fi
    else
        log_error "Python 3 not found. Please install Python 3.11+."
        exit 1
    fi
    
    # Check/Install UV
    log_step "Checking UV package manager..."
    if ! command_exists uv; then
        log_warn "UV not found. Installing UV..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
        
        if ! command_exists uv; then
            log_error "Failed to install UV. Please install manually."
            exit 1
        fi
    fi
    log_info "UV found ✓"
    
    # Set up environment file
    log_step "Setting up environment configuration..."
    if [ ! -f .env ]; then
        cp .env.example .env
        log_info "Created .env from .env.example"
        log_warn "Please edit .env file with your configuration"
    else
        log_info ".env file already exists"
    fi
    
    # Set up Python path
    log_step "Setting up Python path..."
    export PYTHONPATH="${PWD}/src:${PYTHONPATH}"
    log_info "PYTHONPATH set to: $PYTHONPATH"
    
    # Create virtual environment
    log_step "Creating virtual environment..."
    uv venv
    log_info "Virtual environment created"
    
    # Install dependencies
    log_step "Installing dependencies..."
    uv pip install -e ".[dev,test,docs]"
    log_info "Dependencies installed ✓"
    
    # Set up pre-commit hooks
    log_step "Installing pre-commit hooks..."
    uv run pre-commit install
    log_info "Pre-commit hooks installed ✓"
    
    # Run initial tests
    log_step "Running initial tests..."
    if uv run pytest tests/unit/test_core.py -v; then
        log_info "Initial tests passed ✓"
    else
        log_warn "Some tests failed. This might be expected if external dependencies are not configured."
    fi
    
    # Make scripts executable
    log_step "Making scripts executable..."
    chmod +x deployment/deploy.sh
    log_info "Scripts made executable ✓"
    
    # Final verification
    log_step "Verifying installation..."
    if uv run python -c "from gen_ai_rag_langchain import __version__; print(f'Version: {__version__}')"; then
        log_info "Package import successful ✓"
    else
        log_error "Package import failed"
        exit 1
    fi
    
    # Success message
    echo
    log_info "🎉 Setup completed successfully!"
    echo
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Edit .env file with your configuration"
    echo "2. Activate virtual environment: source .venv/bin/activate"
    echo "3. Start development server: uv run gen-ai-rag server"
    echo "4. Visit API docs: http://localhost:8000/docs"
    echo
    echo -e "${BLUE}Useful commands:${NC}"
    echo "• Run tests: uv run pytest"
    echo "• Format code: uv run black src/ tests/"
    echo "• Lint code: uv run flake8 src/ tests/"
    echo "• Start server: uv run gen-ai-rag server"
    echo "• CLI help: uv run gen-ai-rag --help"
    echo
}

# Run setup
setup_project
