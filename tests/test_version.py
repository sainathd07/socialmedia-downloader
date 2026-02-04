"""Tests for version checking"""
import pytest
import sys
from pathlib import Path
from unittest.mock import patch, Mock

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.version import (
    get_current_version,
    is_newer_version,
    check_for_updates
)


class TestVersion:
    """Test version utilities"""
    
    def test_get_current_version(self):
        """Test getting current version"""
        version = get_current_version()
        assert isinstance(version, str)
        assert len(version.split('.')) == 3
    
    def test_is_newer_version_major(self):
        """Test major version comparison"""
        assert is_newer_version("2.0.0", "1.0.0") is True
        assert is_newer_version("1.0.0", "2.0.0") is False
    
    def test_is_newer_version_minor(self):
        """Test minor version comparison"""
        assert is_newer_version("1.1.0", "1.0.0") is True
        assert is_newer_version("1.0.0", "1.1.0") is False
    
    def test_is_newer_version_patch(self):
        """Test patch version comparison"""
        assert is_newer_version("1.0.1", "1.0.0") is True
        assert is_newer_version("1.0.0", "1.0.1") is False
    
    def test_is_newer_version_equal(self):
        """Test equal versions"""
        assert is_newer_version("1.0.0", "1.0.0") is False
    
    def test_is_newer_version_invalid(self):
        """Test invalid version strings"""
        assert is_newer_version("invalid", "1.0.0") is False
        assert is_newer_version("1.0.0", "invalid") is False
    
    @patch('src.utils.version.requests.get')
    def test_check_for_updates_available(self, mock_get):
        """Test update check when update is available"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "tag_name": "v2.0.0",
            "html_url": "https://github.com/user/repo/releases/tag/v2.0.0"
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        available, version, url = check_for_updates()
        
        assert available is True
        assert version == "2.0.0"
        assert "github.com" in url
    
    @patch('src.utils.version.requests.get')
    def test_check_for_updates_current(self, mock_get):
        """Test update check when already up to date"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "tag_name": "v1.0.0",
            "html_url": "https://github.com/user/repo/releases/tag/v1.0.0"
        }
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        
        available, version, url = check_for_updates()
        
        assert available is False
        assert version is None
    
    @patch('src.utils.version.requests.get')
    def test_check_for_updates_network_error(self, mock_get):
        """Test update check with network error"""
        mock_get.side_effect = Exception("Network error")
        
        available, version, url = check_for_updates()
        
        assert available is False
        assert version is None
        assert url is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
