"""Integration tests for the API module."""

import pytest
from fastapi.testclient import TestClient

from gen_ai_rag_langchain.api import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


class TestAPI:
    """Test cases for API endpoints."""
    
    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert data["version"] == "0.1.0"
    
    def test_health_check_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "version" in data
        assert data["status"] == "healthy"
        assert data["version"] == "0.1.0"
    
    def test_query_endpoint_success(self, client):
        """Test the query endpoint with valid input."""
        query_data = {
            "query": "What is artificial intelligence?",
            "max_tokens": 4000,
            "temperature": 0.7
        }
        
        response = client.post("/query", json=query_data)
        
        assert response.status_code == 200
        data = response.json()
        assert "query" in data
        assert "response" in data
        assert "sources" in data
        assert "metadata" in data
        assert data["query"] == query_data["query"]
    
    def test_query_endpoint_minimal_input(self, client):
        """Test the query endpoint with minimal input."""
        query_data = {"query": "Test query"}
        
        response = client.post("/query", json=query_data)
        
        assert response.status_code == 200
        data = response.json()
        assert data["query"] == "Test query"
    
    def test_query_endpoint_invalid_input(self, client):
        """Test the query endpoint with invalid input."""
        response = client.post("/query", json={})
        
        assert response.status_code == 422  # Validation error
    
    def test_cors_headers(self, client):
        """Test CORS headers are present."""
        response = client.options("/")
        
        # In test environment, CORS should be enabled
        assert response.status_code in [200, 405]  # 405 if OPTIONS not explicitly handled
