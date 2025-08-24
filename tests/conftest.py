"""Test configuration for pytest."""

import os
import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Set test environment
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "True"
os.environ["LOG_LEVEL"] = "DEBUG"
