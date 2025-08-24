# Makefile for Gen AI RAG LangChain project

.PHONY: help install install-dev test test-unit test-integration test-functional \
        lint format type-check security-check clean build docs docs-serve \
        docker-build docker-run docker-clean setup pre-commit-install \
        pre-commit-run coverage

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON := uv run python
PYTEST := uv run pytest
BLACK := uv run black
ISORT := uv run isort
FLAKE8 := uv run flake8
MYPY := uv run mypy
BANDIT := uv run bandit
SAFETY := uv run safety
MKDOCS := uv run mkdocs
PRECOMMIT := uv run pre-commit

# Source and test directories
SRC_DIR := src
TEST_DIR := tests
DOCS_DIR := docs

help: ## Show this help message
	@echo "Gen AI RAG LangChain - Available commands:"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

# Setup and installation
setup: ## Run the complete project setup
	@echo "🚀 Setting up Gen AI RAG LangChain project..."
	./setup.sh

install: ## Install project dependencies
	uv venv
	uv pip install -e .

install-dev: ## Install project with development dependencies
	uv venv
	uv pip install -e ".[dev,test,docs]"

pre-commit-install: ## Install pre-commit hooks
	$(PRECOMMIT) install

pre-commit-run: ## Run pre-commit on all files
	$(PRECOMMIT) run --all-files

# Testing
test: ## Run all tests
	$(PYTEST) -v

test-unit: ## Run unit tests only
	$(PYTEST) tests/unit/ -v -m "unit"

test-integration: ## Run integration tests only
	$(PYTEST) tests/integration/ -v -m "integration"

test-functional: ## Run functional tests only
	$(PYTEST) tests/functional/ -v -m "functional"

test-watch: ## Run tests in watch mode
	$(PYTEST) -f -v

coverage: ## Run tests with coverage report
	$(PYTEST) --cov=$(SRC_DIR)/gen_ai_rag_langchain --cov-report=html --cov-report=term-missing

coverage-xml: ## Generate XML coverage report
	$(PYTEST) --cov=$(SRC_DIR)/gen_ai_rag_langchain --cov-report=xml

# Code quality
lint: ## Run all linters
	$(FLAKE8) $(SRC_DIR)/ $(TEST_DIR)/
	$(MYPY) $(SRC_DIR)/

format: ## Format code with black and isort
	$(BLACK) $(SRC_DIR)/ $(TEST_DIR)/
	$(ISORT) $(SRC_DIR)/ $(TEST_DIR)/

format-check: ## Check code formatting without making changes
	$(BLACK) --check --diff $(SRC_DIR)/ $(TEST_DIR)/
	$(ISORT) --check-only --diff $(SRC_DIR)/ $(TEST_DIR)/

type-check: ## Run type checking with mypy
	$(MYPY) $(SRC_DIR)/

security-check: ## Run security checks
	$(BANDIT) -r $(SRC_DIR)/ -f json
	$(SAFETY) check

# Documentation
docs: ## Build documentation
	$(MKDOCS) build

docs-serve: ## Serve documentation locally
	$(MKDOCS) serve

docs-clean: ## Clean documentation build
	rm -rf site/

# Building and packaging
build: ## Build the package
	$(PYTHON) -m build

build-clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/

# Docker
docker-build: ## Build Docker image
	docker build -t gen-ai-rag-langchain .

docker-run: ## Run Docker container
	docker run -p 8000:8000 --env-file .env gen-ai-rag-langchain

docker-compose-up: ## Start services with docker-compose
	docker-compose up --build

docker-compose-down: ## Stop services with docker-compose
	docker-compose down

docker-clean: ## Clean Docker artifacts
	docker system prune -f

# Development servers
serve: ## Start the development server
	uv run gen-ai-rag server --reload

serve-prod: ## Start the production server
	uv run gen-ai-rag server

# CLI commands
cli-query: ## Run a test query via CLI (usage: make cli-query QUERY="your query")
	uv run gen-ai-rag query "$(QUERY)"

cli-health: ## Check system health via CLI
	uv run gen-ai-rag health

# Cleaning
clean: ## Clean all build artifacts and caches
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf site/

# CI/CD helpers
ci-test: ## Run tests suitable for CI
	$(PYTEST) --cov=$(SRC_DIR)/gen_ai_rag_langchain --cov-report=xml --cov-report=term-missing

ci-quality: ## Run all quality checks for CI
	$(FLAKE8) $(SRC_DIR)/ $(TEST_DIR)/ --count --select=E9,F63,F7,F82 --show-source --statistics
	$(BLACK) --check --diff $(SRC_DIR)/ $(TEST_DIR)/
	$(ISORT) --check-only --diff $(SRC_DIR)/ $(TEST_DIR)/
	$(MYPY) $(SRC_DIR)/
	$(BANDIT) -r $(SRC_DIR)/ -f json

ci-security: ## Run security checks for CI
	$(BANDIT) -r $(SRC_DIR)/ -f json
	$(SAFETY) check --json

# Release helpers
version: ## Show current version
	@$(PYTHON) -c "from gen_ai_rag_langchain import __version__; print(__version__)"

# Development helpers
install-uv: ## Install UV package manager
	curl -LsSf https://astral.sh/uv/install.sh | sh

check-deps: ## Check for outdated dependencies
	uv pip list --outdated

# All-in-one commands
dev-setup: install-dev pre-commit-install ## Complete development setup
	@echo "✅ Development environment ready!"

check-all: format-check lint type-check security-check test ## Run all checks
	@echo "✅ All checks passed!"

# AWS/Cloud deployment
deploy: ## Deploy to AWS ECS
	./deployment/deploy.sh

# Example usage targets
example-api: ## Show example API usage
	@echo "Example API usage:"
	@echo "curl -X POST http://localhost:8000/query -H 'Content-Type: application/json' -d '{\"query\": \"What is AI?\"}'"

example-cli: ## Show example CLI usage
	@echo "Example CLI usage:"
	@echo "uv run gen-ai-rag query 'What is machine learning?'"
	@echo "uv run gen-ai-rag server --host 0.0.0.0 --port 8000"
	@echo "uv run gen-ai-rag health"
