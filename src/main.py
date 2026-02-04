"""Main entry point for Video Downloader application"""
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.gui.app import run
from src.utils.logger import logger


def main():
    """Main function"""
    try:
        logger.info("=" * 50)
        logger.info("Video Downloader Starting")
        logger.info("=" * 50)
        run()
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
