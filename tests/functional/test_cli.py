"""Functional tests for the CLI module."""

import pytest
from unittest.mock import patch, Mock
import sys
from io import StringIO

from gen_ai_rag_langchain.cli import main


class TestCLI:
    """Test cases for CLI functionality."""
    
    def test_no_command_shows_help(self, capsys):
        """Test that running without command shows help."""
        result = main([])
        
        assert result == 1
        captured = capsys.readouterr()
        assert "Available commands" in captured.out or "usage:" in captured.out
    
    def test_version_command(self, capsys):
        """Test version command."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "0.1.0" in captured.out
    
    @patch('gen_ai_rag_langchain.cli.RAGSystem')
    def test_query_command(self, mock_rag_system, capsys):
        """Test query command."""
        # Mock the RAG system
        mock_instance = Mock()
        mock_instance.process_query.return_value = {
            "query": "test query",
            "response": "test response",
            "sources": [],
            "metadata": {"processing_time": 0.1}
        }
        mock_rag_system.return_value = mock_instance
        
        result = main(["query", "test query"])
        
        assert result == 0
        captured = capsys.readouterr()
        assert "Query: test query" in captured.out
        assert "Response: test response" in captured.out
    
    @patch('gen_ai_rag_langchain.cli.RAGSystem')
    def test_health_command(self, mock_rag_system, capsys):
        """Test health command."""
        # Mock the RAG system
        mock_instance = Mock()
        mock_instance.health_check.return_value = {
            "status": "healthy",
            "version": "0.1.0"
        }
        mock_rag_system.return_value = mock_instance
        
        result = main(["health"])
        
        assert result == 0
        captured = capsys.readouterr()
        assert "Status: healthy" in captured.out
        assert "Version: 0.1.0" in captured.out
    
    @patch('gen_ai_rag_langchain.cli.uvicorn')
    @patch('gen_ai_rag_langchain.cli.RAGSystem')
    def test_server_command(self, mock_rag_system, mock_uvicorn):
        """Test server command."""
        mock_instance = Mock()
        mock_rag_system.return_value = mock_instance
        mock_uvicorn.run = Mock()
        
        result = main(["server", "--host", "localhost", "--port", "9000"])
        
        assert result == 0
        mock_uvicorn.run.assert_called_once()
        call_args = mock_uvicorn.run.call_args
        assert call_args[1]["host"] == "localhost"
        assert call_args[1]["port"] == 9000
    
    @patch('gen_ai_rag_langchain.cli.RAGSystem')
    def test_error_handling(self, mock_rag_system, capsys):
        """Test error handling in CLI."""
        # Mock the RAG system to raise an exception
        mock_instance = Mock()
        mock_instance.health_check.side_effect = Exception("Test error")
        mock_rag_system.return_value = mock_instance
        
        result = main(["health"])
        
        assert result == 1
        captured = capsys.readouterr()
        assert "Error: Test error" in captured.err
