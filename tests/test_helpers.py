"""Tests for helper utilities"""
import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.helpers import (
    sanitize_filename,
    format_bytes,
    format_speed,
    format_eta,
    truncate_path
)


class TestHelpers:
    """Test helper utility functions"""
    
    def test_sanitize_filename_basic(self):
        """Test basic filename sanitization"""
        filename = "my_video.mp4"
        result = sanitize_filename(filename)
        assert result == "my_video.mp4"
    
    def test_sanitize_filename_dangerous_chars(self):
        """Test removal of dangerous characters"""
        filename = 'test<>:"/\\|?*.mp4'
        result = sanitize_filename(filename)
        assert '<' not in result
        assert '>' not in result
        assert ':' not in result
        assert '"' not in result
        assert '/' not in result
        assert '\\' not in result
        assert '|' not in result
        assert '?' not in result
        assert '*' not in result
    
    def test_sanitize_filename_long(self):
        """Test truncation of long filenames"""
        filename = "a" * 250 + ".mp4"
        result = sanitize_filename(filename)
        assert len(result) <= 200
    
    def test_format_bytes(self):
        """Test byte formatting"""
        assert format_bytes(500) == "500.0 B"
        assert format_bytes(1500) == "1.5 KB"
        assert format_bytes(1500000) == "1.4 MB"
        assert format_bytes(1500000000) == "1.4 GB"
    
    def test_format_speed(self):
        """Test speed formatting"""
        result = format_speed(1500000)
        assert "MB/s" in result
    
    def test_format_eta_seconds(self):
        """Test ETA formatting for seconds"""
        assert format_eta(30) == "30s"
        assert format_eta(59) == "59s"
    
    def test_format_eta_minutes(self):
        """Test ETA formatting for minutes"""
        result = format_eta(90)
        assert "1m" in result
        assert "30s" in result
    
    def test_format_eta_hours(self):
        """Test ETA formatting for hours"""
        result = format_eta(3661)
        assert "1h" in result
    
    def test_format_eta_none(self):
        """Test ETA formatting with None"""
        assert format_eta(None) == "Unknown"
    
    def test_format_eta_negative(self):
        """Test ETA formatting with negative value"""
        assert format_eta(-10) == "Unknown"
    
    def test_truncate_path_short(self):
        """Test path truncation with short path"""
        path = "/home/user/file.txt"
        result = truncate_path(path, 50)
        assert result == path
    
    def test_truncate_path_long(self):
        """Test path truncation with long path"""
        path = "/home/user/very/long/path/to/some/file/that/is/very/long.txt"
        result = truncate_path(path, 30)
        assert len(result) == 30
        assert "..." in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
