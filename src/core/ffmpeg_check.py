"""FFmpeg availability checker"""
import shutil
import os
import subprocess
from pathlib import Path
from ..utils.logger import logger


def is_ffmpeg_available() -> bool:
    """
    Check if FFmpeg is available in the system
    Checks both PATH and common installation locations
    
    Returns:
        True if FFmpeg is found, False otherwise
    """
    # First try using shutil.which (checks PATH)
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path:
        logger.info(f"FFmpeg found in PATH: {ffmpeg_path}")
        return True
    
    # If not in PATH, check common installation locations
    common_paths = [
        "/opt/homebrew/bin/ffmpeg",  # Homebrew on Apple Silicon
        "/usr/local/bin/ffmpeg",      # Homebrew on Intel Mac / Linux
        "/usr/bin/ffmpeg",             # System installation
        "/opt/local/bin/ffmpeg",       # MacPorts
        str(Path.home() / ".local/bin/ffmpeg"),  # User installation
    ]
    
    for path in common_paths:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            # Verify it's actually FFmpeg by running --version
            try:
                result = subprocess.run(
                    [path, "-version"],
                    capture_output=True,
                    timeout=2,
                    text=True
                )
                if result.returncode == 0 and "ffmpeg version" in result.stdout.lower():
                    logger.info(f"FFmpeg found at: {path}")
                    # Add to PATH for subprocess calls
                    os.environ['PATH'] = f"{os.path.dirname(path)}:{os.environ.get('PATH', '')}"
                    return True
            except (subprocess.TimeoutExpired, subprocess.SubprocessError, FileNotFoundError):
                continue
    
    logger.warning("FFmpeg not found in PATH or common locations")
    return False


def get_ffmpeg_install_message() -> str:
    """
    Get platform-specific FFmpeg installation instructions
    
    Returns:
        Installation instructions string
    """
    import platform
    
    system = platform.system()
    
    if system == "Darwin":  # macOS
        return (
            "FFmpeg is required for MP4/MP3 conversion.\n\n"
            "Install with Homebrew:\n"
            "  brew install ffmpeg\n\n"
            "After installing, restart the application.\n\n"
            "See FFMPEG_INSTALL.md for more details."
        )
    elif system == "Windows":
        return (
            "FFmpeg is required for MP4/MP3 conversion.\n\n"
            "Install with Winget (Windows 11):\n"
            "  winget install ffmpeg\n\n"
            "Or download from: https://www.gyan.dev/ffmpeg/builds/\n\n"
            "After installing, restart the application.\n\n"
            "See FFMPEG_INSTALL.md for more details."
        )
    else:  # Linux
        return (
            "FFmpeg is required for MP4/MP3 conversion.\n\n"
            "Install with your package manager:\n"
            "  Ubuntu/Debian: sudo apt install ffmpeg\n"
            "  Fedora: sudo dnf install ffmpeg\n"
            "  Arch: sudo pacman -S ffmpeg\n\n"
            "After installing, restart the application.\n\n"
            "See FFMPEG_INSTALL.md for more details."
        )
