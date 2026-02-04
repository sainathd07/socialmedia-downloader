"""Core download functionality using yt-dlp"""
import os
from pathlib import Path
from typing import Callable, Optional, Dict, Any
import yt_dlp
from .formats import FormatDetector
from ..utils.logger import logger
from ..utils.helpers import sanitize_filename


class DownloadProgress:
    """Container for download progress information"""
    
    def __init__(self):
        self.status: str = "starting"
        self.percentage: float = 0.0
        self.speed: float = 0.0  # bytes per second
        self.eta: Optional[float] = None  # seconds
        self.downloaded_bytes: int = 0
        self.total_bytes: int = 0
        self.filename: str = ""
        self.error: Optional[str] = None


class VideoDownloader:
    """Handle video downloads with progress tracking"""
    
    def __init__(self, output_directory: Path):
        """
        Initialize downloader
        
        Args:
            output_directory: Directory to save downloads
        """
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)
        self.progress = DownloadProgress()
        self._progress_callback: Optional[Callable[[DownloadProgress], None]] = None
    
    def set_progress_callback(self, callback: Callable[[DownloadProgress], None]) -> None:
        """
        Set callback function for progress updates
        
        Args:
            callback: Function to call with progress updates
        """
        self._progress_callback = callback
    
    def _progress_hook(self, d: Dict[str, Any]) -> None:
        """
        Internal progress hook for yt-dlp
        
        Args:
            d: Progress dictionary from yt-dlp
        """
        if d['status'] == 'downloading':
            self.progress.status = 'downloading'
            
            # Extract progress information
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            
            self.progress.downloaded_bytes = downloaded
            self.progress.total_bytes = total
            
            if total > 0:
                self.progress.percentage = (downloaded / total) * 100
            
            self.progress.speed = d.get('speed', 0) or 0
            self.progress.eta = d.get('eta')
            
            # Extract filename
            filename = d.get('filename', '')
            if filename:
                self.progress.filename = Path(filename).name
            
        elif d['status'] == 'finished':
            self.progress.status = 'processing'
            self.progress.percentage = 100.0
            filename = d.get('filename', '')
            if filename:
                self.progress.filename = Path(filename).name
        
        elif d['status'] == 'error':
            self.progress.status = 'error'
            self.progress.error = "Download failed"
        
        # Call user callback if set
        if self._progress_callback:
            self._progress_callback(self.progress)
    
    def download(
        self,
        url: str,
        quality: str = "Best Available",
        download_type: str = "video",
        filename_template: Optional[str] = None
    ) -> tuple[bool, Optional[str], Optional[str]]:
        """
        Download a video
        
        Args:
            url: Video URL
            quality: Quality preference
            download_type: "video" or "audio"
            filename_template: Custom filename template (optional)
            
        Returns:
            Tuple of (success, output_path, error_message)
        """
        try:
            # Reset progress
            self.progress = DownloadProgress()
            self.progress.status = 'starting'
            
            # Get format selector
            format_selector = FormatDetector.get_format_selector(quality, download_type)
            
            # Set up output template
            if filename_template:
                output_template = str(self.output_directory / filename_template)
            else:
                output_template = str(self.output_directory / '%(title)s.%(ext)s')
            
            # Configure yt-dlp options
            ydl_opts = {
                'format': format_selector,
                'outtmpl': output_template,
                'progress_hooks': [self._progress_hook],
                'quiet': True,
                'no_warnings': True,
            }
            
            # Add format-specific options
            if download_type == "audio":
                # Audio: Extract and convert to MP3
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
                self.progress.status = 'converting'
            else:
                # Video: Ensure MP4 output
                ydl_opts['merge_output_format'] = 'mp4'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }]
            
            logger.info(f"Starting download: {url}")
            logger.debug(f"Format selector: {format_selector}")
            
            # Perform download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Get the output filename
                output_path = ydl.prepare_filename(info)
                if download_type == "audio":
                    # Audio files get .mp3 extension after conversion
                    output_path = Path(output_path).with_suffix('.mp3')
                else:
                    # Video files get .mp4 extension after conversion
                    output_path = Path(output_path).with_suffix('.mp4')
                
                self.progress.status = 'complete'
                self.progress.percentage = 100.0
                self.progress.filename = output_path.name
                
                if self._progress_callback:
                    self._progress_callback(self.progress)
                
                logger.info(f"Download complete: {output_path}")
                return True, str(output_path), None
                
        except yt_dlp.utils.DownloadError as e:
            error_msg = str(e)
            logger.error(f"Download error: {error_msg}")
            
            # Parse common errors for user-friendly messages
            if "Video unavailable" in error_msg:
                error_msg = "Video is unavailable or private. Try a different video."
            elif "Sign in" in error_msg or "login" in error_msg.lower() or "authentication" in error_msg.lower():
                error_msg = "This video requires authentication (age-restricted or private). Please try a different public video."
            elif "Copyright" in error_msg:
                error_msg = "Video unavailable due to copyright restrictions."
            elif "not available in your country" in error_msg.lower():
                error_msg = "Video not available in your region."
            elif "Private video" in error_msg:
                error_msg = "This is a private video. Try a public video instead."
            else:
                error_msg = f"Download failed: {error_msg}"
            
            self.progress.status = 'error'
            self.progress.error = error_msg
            
            if self._progress_callback:
                self._progress_callback(self.progress)
            
            return False, None, error_msg
            
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg, exc_info=True)
            
            self.progress.status = 'error'
            self.progress.error = error_msg
            
            if self._progress_callback:
                self._progress_callback(self.progress)
            
            return False, None, error_msg
    
    def cancel(self) -> None:
        """Cancel the current download (not fully implemented)"""
        logger.info("Download cancellation requested")
        self.progress.status = 'cancelled'
        # Note: yt-dlp doesn't have a clean cancellation mechanism
        # This would require running downloads in a separate process
