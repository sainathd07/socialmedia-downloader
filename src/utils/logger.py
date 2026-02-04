"""Logging configuration and utilities"""
import logging
import os
from pathlib import Path
from datetime import datetime


def setup_logger(name: str = "video_downloader") -> logging.Logger:
    """
    Set up and configure logger for the application
    
    Args:
        name: Logger name
        
    Returns:
        Configured logger instance
    """
    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Try to set up file logging, but continue if it fails (e.g., in tests)
    try:
        # Create logs directory
        log_dir = Path.home() / ".video_downloader" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Create log file with timestamp
        log_file = log_dir / f"{datetime.now().strftime('%Y%m%d')}.log"
        
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    except (PermissionError, OSError):
        # File logging not available (e.g., in sandboxed tests)
        pass
    
    # Console handler (always add this)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    return logger


# Create default logger
logger = setup_logger()
