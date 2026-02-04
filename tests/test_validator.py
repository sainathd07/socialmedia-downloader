"""Tests for URL validation"""
import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.validator import URLValidator, Platform


class TestURLValidator:
    """Test URL validation functionality"""
    
    def test_youtube_standard_url(self):
        """Test standard YouTube URL"""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.YOUTUBE
        assert error is None
    
    def test_youtube_short_url(self):
        """Test YouTube short URL"""
        url = "https://youtu.be/dQw4w9WgXcQ"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.YOUTUBE
    
    def test_youtube_shorts(self):
        """Test YouTube Shorts URL"""
        url = "https://www.youtube.com/shorts/xyz123"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.YOUTUBE
    
    def test_youtube_without_protocol(self):
        """Test YouTube URL without https://"""
        url = "youtube.com/watch?v=dQw4w9WgXcQ"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.YOUTUBE
    
    def test_instagram_post(self):
        """Test Instagram post URL"""
        url = "https://www.instagram.com/p/ABC123xyz"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.INSTAGRAM
    
    def test_instagram_reel(self):
        """Test Instagram reel URL"""
        url = "https://www.instagram.com/reel/XYZ789abc"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is True
        assert platform == Platform.INSTAGRAM
    
    def test_invalid_url(self):
        """Test invalid URL"""
        url = "https://www.example.com/video"
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is False
        assert platform == Platform.UNKNOWN
        assert error is not None
    
    def test_empty_url(self):
        """Test empty URL"""
        url = ""
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is False
        assert error == "URL cannot be empty"
    
    def test_none_url(self):
        """Test None URL"""
        url = None
        is_valid, platform, error = URLValidator.validate(url)
        assert is_valid is False
    
    def test_is_valid_method(self):
        """Test is_valid convenience method"""
        assert URLValidator.is_valid("https://youtube.com/watch?v=test") is True
        assert URLValidator.is_valid("https://example.com") is False
    
    def test_get_platform_method(self):
        """Test get_platform method"""
        platform = URLValidator.get_platform("https://youtube.com/watch?v=test")
        assert platform == Platform.YOUTUBE
        
        platform = URLValidator.get_platform("https://instagram.com/p/test")
        assert platform == Platform.INSTAGRAM
        
        platform = URLValidator.get_platform("https://example.com")
        assert platform == Platform.UNKNOWN
    
    def test_normalize_url(self):
        """Test URL normalization"""
        url = "youtube.com/watch?v=test"
        normalized = URLValidator.normalize_url(url)
        assert normalized.startswith("https://")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
