"""Tests for settings management"""
import pytest
import sys
import tempfile
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.settings import Settings


class TestSettings:
    """Test settings management"""
    
    def test_default_settings(self):
        """Test default settings are loaded"""
        settings = Settings()
        assert settings.get("theme") in ["dark", "light"]
        assert settings.get("default_quality") is not None
    
    def test_get_set(self):
        """Test getting and setting values"""
        settings = Settings()
        settings.set("test_key", "test_value", save_immediately=False)
        assert settings.get("test_key") == "test_value"
    
    def test_get_default(self):
        """Test getting non-existent key with default"""
        settings = Settings()
        result = settings.get("nonexistent_key", "default_value")
        assert result == "default_value"
    
    def test_get_output_directory(self):
        """Test output directory retrieval"""
        settings = Settings()
        output_dir = settings.get_output_directory()
        assert isinstance(output_dir, Path)
    
    def test_set_output_directory(self):
        """Test output directory setting"""
        settings = Settings()
        test_path = Path("/tmp/test_downloads")
        settings.set_output_directory(test_path)
        assert settings.get("output_directory") == str(test_path)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
