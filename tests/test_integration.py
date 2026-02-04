"""Integration tests for complete workflows"""
import pytest
import sys
from pathlib import Path
from unittest.mock import patch, Mock

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.validator import URLValidator, Platform
from src.core.formats import FormatDetector
from src.utils.settings import Settings


class TestIntegrationWorkflows:
    """Test complete user workflows"""
    
    def test_youtube_url_validation_flow(self):
        """Test complete YouTube URL validation"""
        # Test various YouTube URL formats
        urls = [
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "https://youtu.be/dQw4w9WgXcQ",
            "youtube.com/watch?v=dQw4w9WgXcQ",
            "https://www.youtube.com/shorts/abc123",
        ]
        
        for url in urls:
            is_valid, platform, error = URLValidator.validate(url)
            assert is_valid is True
            assert platform == Platform.YOUTUBE
            assert error is None
    
    def test_instagram_url_validation_flow(self):
        """Test complete Instagram URL validation"""
        urls = [
            "https://www.instagram.com/p/ABC123/",
            "https://www.instagram.com/reel/XYZ789/",
            "instagram.com/p/TEST123/",
        ]
        
        for url in urls:
            is_valid, platform, error = URLValidator.validate(url)
            assert is_valid is True
            assert platform == Platform.INSTAGRAM
            assert error is None
    
    def test_invalid_url_flow(self):
        """Test invalid URL handling"""
        urls = [
            "https://www.example.com",
            "not a url",
            "",
            "https://facebook.com/video",
        ]
        
        for url in urls:
            is_valid, platform, error = URLValidator.validate(url)
            assert is_valid is False
            assert error is not None
    
    def test_format_selector_generation(self):
        """Test format selector generation for different types"""
        # Video download
        selector = FormatDetector.get_format_selector("Best Available", "video")
        assert "bestvideo" in selector or "best" in selector
        
        # Audio download
        selector = FormatDetector.get_format_selector("Best Available", "audio")
        assert "bestaudio" in selector or "best" in selector
        
        # Specific quality
        selector = FormatDetector.get_format_selector("1080p (Full HD)", "video")
        assert "1080" in selector
    
    def test_settings_persistence_flow(self, tmp_path):
        """Test complete settings workflow"""
        # Create settings with custom config dir
        settings = Settings()
        
        # Set values
        settings.set("test_key", "test_value")
        settings.set("download_type", "audio")
        settings.set("default_quality", "720p (HD)")
        
        # Verify values
        assert settings.get("test_key") == "test_value"
        assert settings.get("download_type") == "audio"
        assert settings.get("default_quality") == "720p (HD)"
        
        # Test output directory
        output_dir = settings.get_output_directory()
        assert isinstance(output_dir, Path)
        assert output_dir.exists()
    
    def test_quality_options_workflow(self):
        """Test quality options availability"""
        qualities = FormatDetector.QUALITY_PREFERENCES
        
        assert "Best Available" in qualities
        assert "1080p (Full HD)" in qualities
        assert "720p (HD)" in qualities
        assert "480p" in qualities
        
        # Test all qualities have valid selectors
        for quality in qualities.keys():
            selector = FormatDetector.get_format_selector(quality, "video")
            assert isinstance(selector, str)
            assert len(selector) > 0


class TestErrorHandlingIntegration:
    """Test error handling in integrated scenarios"""
    
    def test_empty_url_handling(self):
        """Test handling of empty URL"""
        is_valid, platform, error = URLValidator.validate("")
        assert is_valid is False
        assert "empty" in error.lower()
    
    def test_none_url_handling(self):
        """Test handling of None URL"""
        is_valid, platform, error = URLValidator.validate(None)
        assert is_valid is False
        assert error is not None
    
    def test_malformed_url_handling(self):
        """Test handling of malformed URLs"""
        urls = [
            "http://",
            "youtube",
            "www.",
            "://youtube.com",
        ]
        
        for url in urls:
            is_valid, platform, error = URLValidator.validate(url)
            assert is_valid is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
