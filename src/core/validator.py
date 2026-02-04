"""URL validation for supported platforms"""
import re
from typing import Optional, Tuple
from enum import Enum


class Platform(Enum):
    """Supported download platforms"""
    YOUTUBE = "youtube"
    INSTAGRAM = "instagram"
    UNKNOWN = "unknown"


class URLValidator:
    """Validate and identify URLs from supported platforms"""
    
    # YouTube URL patterns
    YOUTUBE_PATTERNS = [
        r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=[\w-]+',
        r'(?:https?://)?(?:www\.)?youtu\.be/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/shorts/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/embed/[\w-]+',
        r'(?:https?://)?(?:www\.)?youtube\.com/v/[\w-]+',
    ]
    
    # Instagram URL patterns
    INSTAGRAM_PATTERNS = [
        r'(?:https?://)?(?:www\.)?instagram\.com/p/[\w-]+',
        r'(?:https?://)?(?:www\.)?instagram\.com/reel/[\w-]+',
        r'(?:https?://)?(?:www\.)?instagram\.com/tv/[\w-]+',
    ]
    
    @classmethod
    def validate(cls, url: str) -> Tuple[bool, Optional[Platform], Optional[str]]:
        """
        Validate a URL and identify its platform
        
        Args:
            url: URL string to validate
            
        Returns:
            Tuple of (is_valid, platform, error_message)
        """
        if not url or not isinstance(url, str):
            return False, None, "URL cannot be empty"
        
        url = url.strip()
        
        if not url:
            return False, None, "URL cannot be empty"
        
        # Check for basic URL structure
        if not re.match(r'^https?://', url, re.IGNORECASE):
            # Add https:// if missing
            url = 'https://' + url
        
        # Check YouTube
        for pattern in cls.YOUTUBE_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True, Platform.YOUTUBE, None
        
        # Check Instagram
        for pattern in cls.INSTAGRAM_PATTERNS:
            if re.match(pattern, url, re.IGNORECASE):
                return True, Platform.INSTAGRAM, None
        
        return False, Platform.UNKNOWN, "URL is not from a supported platform (YouTube or Instagram)"
    
    @classmethod
    def is_valid(cls, url: str) -> bool:
        """
        Quick check if URL is valid
        
        Args:
            url: URL string to validate
            
        Returns:
            True if valid, False otherwise
        """
        is_valid, _, _ = cls.validate(url)
        return is_valid
    
    @classmethod
    def get_platform(cls, url: str) -> Platform:
        """
        Get the platform for a URL
        
        Args:
            url: URL string
            
        Returns:
            Platform enum value
        """
        _, platform, _ = cls.validate(url)
        return platform or Platform.UNKNOWN
    
    @classmethod
    def normalize_url(cls, url: str) -> str:
        """
        Normalize URL (add https:// if missing, etc.)
        
        Args:
            url: URL string
            
        Returns:
            Normalized URL
        """
        url = url.strip()
        if not re.match(r'^https?://', url, re.IGNORECASE):
            url = 'https://' + url
        return url
