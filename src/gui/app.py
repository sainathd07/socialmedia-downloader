"""Main application window"""
import customtkinter as ctk
from pathlib import Path
import threading
from typing import Optional

from .theme import apply_theme
from .components.url_input import URLInput
from .components.options import DownloadOptions
from .components.folder_picker import FolderPicker
from .components.progress import ProgressDisplay

from ..core.downloader import VideoDownloader, DownloadProgress
from ..core.validator import URLValidator
from ..core.ffmpeg_check import is_ffmpeg_available, get_ffmpeg_install_message
from ..utils.settings import settings
from ..utils.logger import logger
from ..utils.version import get_current_version, check_for_updates


class VideoDownloaderApp(ctk.CTk):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Social Media Downloader")
        self.geometry("600x700")
        self.resizable(False, False)
        
        # Apply theme
        theme = settings.get("theme", "dark")
        apply_theme(theme)
        
        # State
        self.is_downloading = False
        self.current_url = ""
        self.url_is_valid = False
        self.downloader: Optional[VideoDownloader] = None
        self.download_thread: Optional[threading.Thread] = None
        
        # Create UI
        self._create_ui()
        
        # Load saved settings
        self._load_settings()
        
        # Check for FFmpeg
        self._check_ffmpeg()
        
        # Check for updates (async, non-blocking)
        self.after(2000, self._check_updates_silent)
        
        logger.info("Application started")
    
    def _create_ui(self):
        """Create the user interface"""
        # Main container with padding
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=24, pady=24)
        
        # Header
        self.header = ctk.CTkLabel(
            self.main_container,
            text="Video Downloader",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.header.pack(pady=(0, 24))
        
        # URL Input
        self.url_input = URLInput(
            self.main_container,
            on_change=self._on_url_change,
            fg_color="transparent"
        )
        self.url_input.pack(fill="x", pady=(0, 20))
        
        # Download Options
        self.options = DownloadOptions(
            self.main_container,
            on_type_change=self._on_type_change,
            on_quality_change=self._on_quality_change,
            fg_color="transparent"
        )
        self.options.pack(fill="x", pady=(0, 20))
        
        # Folder Picker
        default_folder = settings.get_output_directory()
        self.folder_picker = FolderPicker(
            self.main_container,
            default_folder=default_folder,
            on_folder_change=self._on_folder_change,
            fg_color="transparent"
        )
        self.folder_picker.pack(fill="x", pady=(0, 24))
        
        # Download Button
        self.download_button = ctk.CTkButton(
            self.main_container,
            text="DOWNLOAD",
            command=self._start_download,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#2fa572",
            hover_color="#258a5f"
        )
        self.download_button.pack(fill="x", pady=(0, 20))
        
        # Progress Display
        self.progress = ProgressDisplay(
            self.main_container,
            fg_color="transparent"
        )
        # Initially hidden, will be shown when download starts
        
        # Footer with settings and theme toggle
        self.footer = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.footer.pack(fill="x", pady=(16, 0), side="bottom")
        
        # Theme toggle
        self.theme_switch = ctk.CTkSwitch(
            self.footer,
            text="Dark Mode",
            command=self._toggle_theme,
            font=ctk.CTkFont(size=12)
        )
        self.theme_switch.pack(side="right")
        
        # Set initial theme switch state
        theme = settings.get("theme", "dark")
        if theme == "dark":
            self.theme_switch.select()
        else:
            self.theme_switch.deselect()
        
        # About label with version
        version = get_current_version()
        self.about_label = ctk.CTkLabel(
            self.footer,
            text=f"YouTube & Instagram Downloader v{version}",
            font=ctk.CTkFont(size=11),
            text_color="gray"
        )
        self.about_label.pack(side="left")
        
        # Check for updates button
        self.update_button = ctk.CTkButton(
            self.footer,
            text="Check Updates",
            command=self._check_updates,
            width=100,
            height=28,
            font=ctk.CTkFont(size=11),
            fg_color="transparent",
            border_width=1
        )
        self.update_button.pack(side="left", padx=(8, 0))
    
    def _load_settings(self):
        """Load saved settings into UI"""
        # Set download type
        download_type = settings.get("download_type", "video")
        self.options.set_download_type(download_type)
        
        # Set quality
        quality = settings.get("default_quality", "Best Available")
        self.options.set_quality(quality)
    
    def _check_ffmpeg(self):
        """Check if FFmpeg is available and show warning if not"""
        if not is_ffmpeg_available():
            logger.warning("FFmpeg not found")
            # Show warning dialog after a short delay to let UI render
            self.after(500, self._show_ffmpeg_warning)
    
    def _show_ffmpeg_warning(self):
        """Show FFmpeg installation warning dialog"""
        import tkinter.messagebox as messagebox
        
        message = get_ffmpeg_install_message()
        
        response = messagebox.showwarning(
            "FFmpeg Not Found",
            message + "\n\nWithout FFmpeg:\n• Videos will be WebM format (not MP4)\n• Audio extraction won't work\n\nInstall FFmpeg and restart the app for MP4/MP3 support.",
            parent=self
        )
        
        logger.info("FFmpeg warning shown to user")
    
    def _check_updates(self):
        """Manually check for updates"""
        import tkinter.messagebox as messagebox
        
        self.update_button.configure(state="disabled", text="Checking...")
        
        def check():
            available, version, url = check_for_updates()
            self.after(0, self._show_update_result, available, version, url)
        
        import threading
        threading.Thread(target=check, daemon=True).start()
    
    def _check_updates_silent(self):
        """Silently check for updates on startup"""
        def check():
            available, version, url = check_for_updates()
            if available:
                self.after(0, self._show_update_available, version, url)
        
        import threading
        threading.Thread(target=check, daemon=True).start()
    
    def _show_update_result(self, available, version, url):
        """Show update check result"""
        import tkinter.messagebox as messagebox
        
        self.update_button.configure(state="normal", text="Check Updates")
        
        if available:
            response = messagebox.showinfo(
                "Update Available",
                f"A new version is available!\n\nCurrent: {get_current_version()}\nLatest: {version}\n\nWould you like to download it?",
                parent=self
            )
            if url:
                import webbrowser
                webbrowser.open(url)
        else:
            messagebox.showinfo(
                "Up to Date",
                f"You're running the latest version ({get_current_version()})!",
                parent=self
            )
    
    def _show_update_available(self, version, url):
        """Show update available notification"""
        import tkinter.messagebox as messagebox
        
        response = messagebox.askyesno(
            "Update Available",
            f"Version {version} is available!\n\nYou're currently on {get_current_version()}.\n\nWould you like to download the update?",
            parent=self
        )
        
        if response and url:
            import webbrowser
            webbrowser.open(url)
    
    def _on_url_change(self, url: str, is_valid: bool):
        """Handle URL change"""
        self.current_url = url
        self.url_is_valid = is_valid
        
        # Enable/disable download button
        if is_valid and not self.is_downloading:
            self.download_button.configure(state="normal")
        else:
            self.download_button.configure(state="disabled")
    
    def _on_type_change(self, download_type: str):
        """Handle download type change"""
        settings.set("download_type", download_type)
    
    def _on_quality_change(self, quality: str):
        """Handle quality change"""
        settings.set("default_quality", quality)
    
    def _on_folder_change(self, folder: Path):
        """Handle folder change"""
        settings.set_output_directory(folder)
    
    def _toggle_theme(self):
        """Toggle between dark and light theme"""
        current_theme = settings.get("theme", "dark")
        new_theme = "light" if current_theme == "dark" else "dark"
        
        settings.set("theme", new_theme)
        apply_theme(new_theme)
        
        # Update switch text
        self.theme_switch.configure(text="Dark Mode" if new_theme == "dark" else "Light Mode")
        
        logger.info(f"Theme changed to {new_theme}")
    
    def _start_download(self):
        """Start the download process"""
        if not self.url_is_valid or self.is_downloading:
            return
        
        # Get download parameters
        url = self.current_url
        quality = self.options.get_quality()
        download_type = self.options.get_download_type()
        output_dir = self.folder_picker.get_folder()
        
        # Update UI state
        self.is_downloading = True
        self.download_button.configure(
            text="DOWNLOADING...",
            state="disabled",
            fg_color="gray"
        )
        self.url_input.set_enabled(False)
        self.options.set_enabled(False)
        self.folder_picker.set_enabled(False)
        
        # Show progress
        self.progress.show()
        self.progress.reset()
        self.progress.set_status("Initializing download...")
        
        logger.info(f"Starting download: {url} (type={download_type}, quality={quality})")
        
        # Start download in separate thread
        self.download_thread = threading.Thread(
            target=self._download_worker,
            args=(url, quality, download_type, output_dir),
            daemon=True
        )
        self.download_thread.start()
    
    def _download_worker(self, url: str, quality: str, download_type: str, output_dir: Path):
        """Worker function for downloading (runs in separate thread)"""
        try:
            # Create downloader
            self.downloader = VideoDownloader(output_dir)
            self.downloader.set_progress_callback(self._on_download_progress)
            
            # Perform download
            success, output_path, error_msg = self.downloader.download(
                url=url,
                quality=quality,
                download_type=download_type
            )
            
            # Update UI on main thread
            self.after(0, self._download_complete, success, output_path, error_msg)
            
        except Exception as e:
            logger.error(f"Download error: {e}", exc_info=True)
            self.after(0, self._download_complete, False, None, str(e))
    
    def _on_download_progress(self, progress: DownloadProgress):
        """Handle progress updates from downloader"""
        # Update UI on main thread
        self.after(0, self._update_progress_ui, progress)
    
    def _update_progress_ui(self, progress: DownloadProgress):
        """Update progress UI (runs on main thread)"""
        if progress.status == "downloading":
            status_text = f"Downloading: {progress.filename}" if progress.filename else "Downloading..."
            self.progress.update_progress(
                percentage=progress.percentage,
                speed=progress.speed,
                eta=progress.eta,
                status=status_text
            )
        elif progress.status == "processing":
            self.progress.set_status("Processing and converting to MP4...")
        elif progress.status == "converting":
            self.progress.set_status("Converting to MP3...")
    
    def _download_complete(self, success: bool, output_path: Optional[str], error_msg: Optional[str]):
        """Handle download completion (runs on main thread)"""
        self.is_downloading = False
        
        # Update UI state
        self.download_button.configure(
            text="DOWNLOAD",
            state="normal" if self.url_is_valid else "disabled",
            fg_color="#2fa572"
        )
        self.url_input.set_enabled(True)
        self.options.set_enabled(True)
        self.folder_picker.set_enabled(True)
        
        if success:
            filename = Path(output_path).name if output_path else "video"
            self.progress.show_success(f"✓ Download complete: {filename}")
            logger.info(f"Download successful: {output_path}")
            
            # Clear URL input
            self.url_input.clear()
        else:
            error_display = error_msg or "Download failed"
            self.progress.show_error(f"✗ {error_display}")
            logger.error(f"Download failed: {error_msg}")
    
    def on_closing(self):
        """Handle window closing"""
        logger.info("Application closing")
        
        # Save settings
        settings.save()
        
        # Stop any ongoing download
        if self.is_downloading and self.downloader:
            self.downloader.cancel()
        
        self.destroy()


def run():
    """Run the application"""
    app = VideoDownloaderApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
