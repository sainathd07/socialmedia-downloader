"""Version management and update checking"""
import requests
from typing import Optional, Tuple
from .logger import logger

__version__ = "1.0.0"
GITHUB_REPO = "yourusername/video-downloader"  # TODO: Update with your actual GitHub repo
UPDATE_CHECK_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"


def get_current_version() -> str:
    """
    Get current application version
    
    Returns:
        Version string (e.g., "1.0.0")
    """
    return __version__


def check_for_updates() -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Check if a newer version is available on GitHub
    
    Returns:
        Tuple of (update_available, latest_version, download_url)
    """
    try:
        response = requests.get(UPDATE_CHECK_URL, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        latest_version = data.get("tag_name", "").lstrip("v")
        download_url = data.get("html_url", "")
        
        if latest_version and is_newer_version(latest_version, __version__):
            logger.info(f"Update available: {latest_version} (current: {__version__})")
            return True, latest_version, download_url
        
        logger.info(f"Up to date: {__version__}")
        return False, None, None
        
    except requests.RequestException as e:
        logger.debug(f"Update check failed: {e}")
        return False, None, None
    except Exception as e:
        logger.error(f"Update check error: {e}")
        return False, None, None


def is_newer_version(latest: str, current: str) -> bool:
    """
    Compare version strings
    
    Args:
        latest: Latest version string
        current: Current version string
        
    Returns:
        True if latest is newer than current
    """
    try:
        latest_parts = [int(x) for x in latest.split(".")]
        current_parts = [int(x) for x in current.split(".")]
        
        # Pad to same length
        while len(latest_parts) < len(current_parts):
            latest_parts.append(0)
        while len(current_parts) < len(latest_parts):
            current_parts.append(0)
        
        return latest_parts > current_parts
    except (ValueError, AttributeError):
        return False
