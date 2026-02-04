"""User settings management"""
import json
from pathlib import Path
from typing import Any, Dict, Optional
from .logger import logger


class Settings:
    """Manage application settings with persistent storage"""
    
    DEFAULT_SETTINGS = {
        "output_directory": str(Path.home() / "Downloads" / "VideoDownloader"),
        "default_quality": "Best Available",
        "download_type": "video",  # "video" or "audio"
        "theme": "dark",  # "dark" or "light"
        "last_url": "",
        "window_size": {"width": 600, "height": 700},
    }
    
    def __init__(self):
        self.config_dir = Path.home() / ".video_downloader"
        self.config_file = self.config_dir / "settings.json"
        self._settings: Dict[str, Any] = {}
        self.load()
    
    def load(self) -> None:
        """Load settings from file or create with defaults"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    self._settings = json.load(f)
                logger.info("Settings loaded successfully")
            else:
                self._settings = self.DEFAULT_SETTINGS.copy()
                self.save()
                logger.info("Created default settings")
        except Exception as e:
            logger.error(f"Error loading settings: {e}")
            self._settings = self.DEFAULT_SETTINGS.copy()
    
    def save(self) -> None:
        """Save current settings to file"""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump(self._settings, f, indent=2)
            logger.debug("Settings saved successfully")
        except Exception as e:
            logger.error(f"Error saving settings: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a setting value
        
        Args:
            key: Setting key
            default: Default value if key not found
            
        Returns:
            Setting value or default
        """
        return self._settings.get(key, default)
    
    def set(self, key: str, value: Any, save_immediately: bool = True) -> None:
        """
        Set a setting value
        
        Args:
            key: Setting key
            value: New value
            save_immediately: Whether to save to disk immediately
        """
        self._settings[key] = value
        if save_immediately:
            self.save()
    
    def get_output_directory(self) -> Path:
        """Get output directory as Path object"""
        path_str = self.get("output_directory", self.DEFAULT_SETTINGS["output_directory"])
        path = Path(path_str)
        # Create directory if it doesn't exist
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def set_output_directory(self, path: Path) -> None:
        """Set output directory"""
        self.set("output_directory", str(path))
    
    def reset_to_defaults(self) -> None:
        """Reset all settings to defaults"""
        self._settings = self.DEFAULT_SETTINGS.copy()
        self.save()
        logger.info("Settings reset to defaults")


# Global settings instance
settings = Settings()
