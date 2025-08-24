#!/usr/bin/env python3
"""Test config manually"""

import os
from unittest.mock import patch
import sys
sys.path.insert(0, 'src')

from gen_ai_rag_langchain.config import Config

# Test 1: Default values
print("Test 1: Default values")
config1 = Config()
print(f"Environment: {config1.environment}")
print(f"Debug: {config1.debug}")
print(f"API Port: {config1.api_port}")

# Test 2: With environment variables
print("\nTest 2: With environment variables")
with patch.dict(os.environ, {
    "ENVIRONMENT": "production", 
    "DEBUG": "false",
    "API_PORT": "9000"
}, clear=False):
    config2 = Config()
    print(f"Environment: {config2.environment}")
    print(f"Debug: {config2.debug}")
    print(f"API Port: {config2.api_port}")

print("\nDone!")
