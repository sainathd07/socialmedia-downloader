"""Integration tests for downloader"""
import pytest
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.downloader import VideoDownloader, DownloadProgress


class TestDownloadProgress:
    """Test DownloadProgress container"""
    
    def test_initialization(self):
        """Test progress initialization"""
        progress = DownloadProgress()
        assert progress.status == "starting"
        assert progress.percentage == 0.0
        assert progress.speed == 0.0
        assert progress.eta is None
        assert progress.downloaded_bytes == 0
        assert progress.total_bytes == 0
        assert progress.filename == ""
        assert progress.error is None


class TestVideoDownloader:
    """Test VideoDownloader class"""
    
    def test_initialization(self, tmp_path):
        """Test downloader initialization"""
        downloader = VideoDownloader(tmp_path)
        assert downloader.output_directory == tmp_path
        assert downloader.output_directory.exists()
        assert isinstance(downloader.progress, DownloadProgress)
    
    def test_set_progress_callback(self, tmp_path):
        """Test setting progress callback"""
        downloader = VideoDownloader(tmp_path)
        callback = Mock()
        downloader.set_progress_callback(callback)
        assert downloader._progress_callback == callback
    
    def test_progress_hook_downloading(self, tmp_path):
        """Test progress hook with downloading status"""
        downloader = VideoDownloader(tmp_path)
        callback = Mock()
        downloader.set_progress_callback(callback)
        
        hook_data = {
            'status': 'downloading',
            'downloaded_bytes': 1024000,
            'total_bytes': 10240000,
            'speed': 512000,
            'eta': 18,
            'filename': '/path/to/video.mp4'
        }
        
        downloader._progress_hook(hook_data)
        
        assert downloader.progress.status == 'downloading'
        assert downloader.progress.downloaded_bytes == 1024000
        assert downloader.progress.total_bytes == 10240000
        assert downloader.progress.speed == 512000
        assert downloader.progress.eta == 18
        assert downloader.progress.filename == 'video.mp4'
        callback.assert_called_once()
    
    def test_progress_hook_finished(self, tmp_path):
        """Test progress hook with finished status"""
        downloader = VideoDownloader(tmp_path)
        
        hook_data = {
            'status': 'finished',
            'filename': '/path/to/video.mp4'
        }
        
        downloader._progress_hook(hook_data)
        
        assert downloader.progress.status == 'processing'
        assert downloader.progress.percentage == 100.0
        assert downloader.progress.filename == 'video.mp4'
    
    def test_progress_hook_error(self, tmp_path):
        """Test progress hook with error status"""
        downloader = VideoDownloader(tmp_path)
        
        hook_data = {'status': 'error'}
        
        downloader._progress_hook(hook_data)
        
        assert downloader.progress.status == 'error'
        assert downloader.progress.error == "Download failed"
    
    @patch('src.core.downloader.yt_dlp.YoutubeDL')
    def test_download_video_success(self, mock_ydl_class, tmp_path):
        """Test successful video download"""
        # Setup mock
        mock_ydl = MagicMock()
        mock_ydl_class.return_value.__enter__.return_value = mock_ydl
        
        mock_info = {
            'title': 'Test Video',
            'ext': 'webm',
            'id': 'test123'
        }
        mock_ydl.extract_info.return_value = mock_info
        mock_ydl.prepare_filename.return_value = str(tmp_path / 'Test Video.webm')
        
        # Test
        downloader = VideoDownloader(tmp_path)
        success, output_path, error = downloader.download(
            url="https://youtube.com/watch?v=test123",
            quality="Best Available",
            download_type="video"
        )
        
        assert success is True
        assert output_path is not None
        assert error is None
        assert output_path.endswith('.mp4')
    
    @patch('src.core.downloader.yt_dlp.YoutubeDL')
    def test_download_audio_success(self, mock_ydl_class, tmp_path):
        """Test successful audio download"""
        # Setup mock
        mock_ydl = MagicMock()
        mock_ydl_class.return_value.__enter__.return_value = mock_ydl
        
        mock_info = {
            'title': 'Test Audio',
            'ext': 'm4a',
            'id': 'test456'
        }
        mock_ydl.extract_info.return_value = mock_info
        mock_ydl.prepare_filename.return_value = str(tmp_path / 'Test Audio.m4a')
        
        # Test
        downloader = VideoDownloader(tmp_path)
        success, output_path, error = downloader.download(
            url="https://youtube.com/watch?v=test456",
            quality="Best Available",
            download_type="audio"
        )
        
        assert success is True
        assert output_path is not None
        assert error is None
        assert output_path.endswith('.mp3')
    
    def test_cancel(self, tmp_path):
        """Test download cancellation"""
        downloader = VideoDownloader(tmp_path)
        downloader.cancel()
        assert downloader.progress.status == 'cancelled'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
