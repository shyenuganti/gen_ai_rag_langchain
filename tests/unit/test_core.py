"""Unit tests for the core module."""

from unittest.mock import patch

from gen_ai_rag_langchain.core import RAGSystem


class TestRAGSystem:
    """Test cases for RAGSystem class."""

    def test_init_default_config(self):
        """Test RAGSystem initialization with default config."""
        rag_system = RAGSystem()
        assert rag_system.config == {}

    def test_init_custom_config(self):
        """Test RAGSystem initialization with custom config."""
        config = {"key": "value", "debug": True}
        rag_system = RAGSystem(config)
        assert rag_system.config == config

    def test_process_query_basic(self):
        """Test basic query processing."""
        rag_system = RAGSystem()
        query = "What is artificial intelligence?"

        result = rag_system.process_query(query)

        assert "query" in result
        assert "response" in result
        assert "sources" in result
        assert "metadata" in result
        assert result["query"] == query
        assert query in result["response"]
        assert isinstance(result["sources"], list)
        assert isinstance(result["metadata"], dict)

    def test_process_query_empty(self):
        """Test query processing with empty string."""
        rag_system = RAGSystem()
        query = ""

        result = rag_system.process_query(query)

        assert result["query"] == query
        assert result["response"] is not None

    def test_health_check(self):
        """Test health check functionality."""
        rag_system = RAGSystem()

        health_status = rag_system.health_check()

        assert "status" in health_status
        assert "version" in health_status
        assert health_status["status"] == "healthy"
        assert health_status["version"] == "0.1.0"

    @patch("gen_ai_rag_langchain.core.logger")
    def test_logging_during_query_processing(self, mock_logger):
        """Test that logging occurs during query processing."""
        rag_system = RAGSystem()
        query = "test query"

        rag_system.process_query(query)

        # Check that logger.info was called
        assert mock_logger.info.call_count >= 2  # At least two log calls
