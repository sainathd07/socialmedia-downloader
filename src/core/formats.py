"""Video format detection and selection"""
from typing import List, Dict, Optional, Any
import yt_dlp
from ..utils.logger import logger


class FormatDetector:
    """Detect and manage available video formats"""
    
    QUALITY_PREFERENCES = {
        "Best Available": None,  # Let yt-dlp choose best
        "2160p (4K)": "2160",
        "1440p (2K)": "1440",
        "1080p (Full HD)": "1080",
        "720p (HD)": "720",
        "480p": "480",
        "360p": "360",
    }
    
    @staticmethod
    def get_video_info(url: str) -> Optional[Dict[str, Any]]:
        """
        Extract video information without downloading
        
        Args:
            url: Video URL
            
        Returns:
            Dictionary with video info or None if error
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'thumbnail': info.get('thumbnail', ''),
                    'uploader': info.get('uploader', 'Unknown'),
                    'formats': info.get('formats', []),
                    'id': info.get('id', ''),
                }
        except Exception as e:
            logger.error(f"Error extracting video info: {e}")
            return None
    
    @staticmethod
    def get_available_qualities(url: str) -> List[str]:
        """
        Get list of available quality options for a video
        
        Args:
            url: Video URL
            
        Returns:
            List of available quality strings
        """
        info = FormatDetector.get_video_info(url)
        if not info:
            return ["Best Available"]
        
        formats = info.get('formats', [])
        available_heights = set()
        
        for fmt in formats:
            height = fmt.get('height')
            if height:
                available_heights.add(height)
        
        # Filter quality preferences to only available ones
        available_qualities = ["Best Available"]
        
        for quality_name, height_str in FormatDetector.QUALITY_PREFERENCES.items():
            if height_str and int(height_str) in available_heights:
                available_qualities.append(quality_name)
        
        return available_qualities
    
    @staticmethod
    def get_format_selector(quality: str, download_type: str) -> str:
        """
        Get yt-dlp format selector string
        
        Args:
            quality: Quality preference
            download_type: "video" or "audio"
            
        Returns:
            Format selector string for yt-dlp
        """
        if download_type == "audio":
            return "bestaudio/best"
        
        # Video download
        if quality == "Best Available" or quality not in FormatDetector.QUALITY_PREFERENCES:
            return "bestvideo+bestaudio/best"
        
        height = FormatDetector.QUALITY_PREFERENCES[quality]
        if height:
            # Try to get video at specific height, fallback to best
            return f"bestvideo[height<={height}]+bestaudio/best[height<={height}]/best"
        
        return "bestvideo+bestaudio/best"
