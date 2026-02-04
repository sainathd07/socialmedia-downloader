"""Helper utility functions"""
import re
from pathlib import Path
from typing import Optional


def sanitize_filename(filename: str) -> str:
    """
    Remove or replace dangerous characters from filename
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename safe for all platforms
    """
    # Remove or replace dangerous characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    # Limit length
    if len(filename) > 200:
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        filename = name[:200 - len(ext) - 1] + '.' + ext if ext else name[:200]
    return filename


def format_bytes(bytes_value: int) -> str:
    """
    Format bytes to human-readable string
    
    Args:
        bytes_value: Number of bytes
        
    Returns:
        Formatted string (e.g., "5.2 MB")
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} PB"


def format_speed(bytes_per_second: float) -> str:
    """
    Format download speed to human-readable string
    
    Args:
        bytes_per_second: Download speed in bytes per second
        
    Returns:
        Formatted string (e.g., "5.2 MB/s")
    """
    return f"{format_bytes(int(bytes_per_second))}/s"


def format_eta(seconds: Optional[float]) -> str:
    """
    Format ETA in seconds to human-readable string
    
    Args:
        seconds: Time in seconds
        
    Returns:
        Formatted string (e.g., "2m 30s" or "Unknown")
    """
    if seconds is None or seconds < 0:
        return "Unknown"
    
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"


def get_available_space(path: Path) -> int:
    """
    Get available disk space for given path
    
    Args:
        path: Directory path to check
        
    Returns:
        Available space in bytes
    """
    import shutil
    stat = shutil.disk_usage(path)
    return stat.free


def truncate_path(path: str, max_length: int = 40) -> str:
    """
    Truncate path string to fit in UI
    
    Args:
        path: Full path string
        max_length: Maximum length
        
    Returns:
        Truncated path with ellipsis if needed
    """
    if len(path) <= max_length:
        return path
    
    # Try to show beginning and end
    if max_length > 10:
        start_len = (max_length - 3) // 2
        end_len = max_length - 3 - start_len
        return f"{path[:start_len]}...{path[-end_len:]}"
    
    return path[:max_length]
