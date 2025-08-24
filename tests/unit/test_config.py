"""Unit tests for configuration module."""

import os
from unittest.mock import patch

from gen_ai_rag_langchain.config import Config, get_config, get_settings


class TestConfig:
    """Test cases for Config class."""

    def test_config_defaults(self):
        """Test default configuration values."""
        config = Config()

        assert config.environment == "test"  # Set in conftest.py
        assert config.debug is True
        assert config.log_level == "DEBUG"
        assert config.api_host == "0.0.0.0"
        assert config.api_port == 8000
        assert config.workers == 1
        assert config.max_tokens == 4000
        assert config.temperature == 0.7
        assert config.chunk_size == 1000
        assert config.chunk_overlap == 200

    @patch.dict(
        os.environ,
        {
            "ENVIRONMENT": "production",
            "DEBUG": "false",
            "API_PORT": "9000",
            "MAX_TOKENS": "2000",
            "TEMPERATURE": "0.5",
        },
        clear=False,
    )
    def test_config_from_environment(self):
        """Test configuration loading from environment variables."""
        # Create config after patching environment
        config = Config()

        assert config.environment == "production"
        assert config.debug is False
        assert config.api_port == 9000
        assert config.max_tokens == 2000
        assert config.temperature == 0.5

    def test_get_config(self):
        """Test get_config function."""
        config = get_config()
        assert isinstance(config, Config)

    def test_get_settings(self):
        """Test get_settings function."""
        settings = get_settings()

        assert isinstance(settings, dict)
        assert "environment" in settings
        assert "debug" in settings
        assert "log_level" in settings
        assert "api_host" in settings
        assert "api_port" in settings
        assert "workers" in settings
        assert "max_tokens" in settings
        assert "temperature" in settings
        assert "chunk_size" in settings
        assert "chunk_overlap" in settings

    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}, clear=False)
    def test_openai_api_key_loading(self):
        """Test OpenAI API key loading from environment."""
        config = Config()
        assert config.openai_api_key == "test-key"

    @patch.dict(os.environ, {"AWS_DEFAULT_REGION": "us-west-2"}, clear=False)
    def test_aws_region_loading(self):
        """Test AWS region loading from environment."""
        config = Config()
        assert config.aws_region == "us-west-2"
