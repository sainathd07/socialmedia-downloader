# Development Guide

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Downloader
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

For development (includes testing tools):

```bash
pip install -r requirements-dev.txt
```

## Running the Application

### Development Mode

```bash
# Unix/macOS/Linux
./run.sh

# Or directly
python src/main.py
```

```bat
REM Windows
python src\main.py
```

## Project Structure

```
Downloader/
├── src/
│   ├── main.py                 # Entry point
│   ├── gui/                    # GUI components
│   │   ├── app.py             # Main application window
│   │   ├── theme.py           # Theme configuration
│   │   └── components/        # UI widgets
│   ├── core/                   # Core functionality
│   │   ├── downloader.py      # Download engine
│   │   ├── validator.py       # URL validation
│   │   └── formats.py         # Format detection
│   └── utils/                  # Utilities
│       ├── settings.py        # Settings management
│       ├── logger.py          # Logging
│       └── helpers.py         # Helper functions
├── tests/                      # Test suite
├── requirements.txt            # Dependencies
└── build_macos.spec           # PyInstaller config
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_validator.py -v
```

## Building Executables

### macOS

```bash
./build.sh
# Output: dist/VideoDownloader.app
```

Or manually:

```bash
pyinstaller build_macos.spec --clean
```

### Windows

```bat
build_windows.bat
REM Output: dist\VideoDownloader.exe
```

Or manually:

```bat
pyinstaller build_windows.spec --clean
```

### Linux

```bash
./build.sh
# Output: dist/VideoDownloader
```

## Configuration Files

### Settings Location

- **macOS/Linux**: `~/.video_downloader/settings.json`
- **Windows**: `%USERPROFILE%\.video_downloader\settings.json`

### Log Files

- **macOS/Linux**: `~/.video_downloader/logs/`
- **Windows**: `%USERPROFILE%\.video_downloader\logs\`

## Code Style

- Follow PEP 8
- Use type hints where possible
- Document functions with docstrings
- Keep functions focused and single-purpose

## Adding Features

### Adding a New Platform

1. Add URL patterns to `src/core/validator.py`
2. Test with existing URL validation
3. yt-dlp handles most platforms automatically

### Adding UI Components

1. Create component in `src/gui/components/`
2. Follow existing component patterns
3. Use CustomTkinter widgets
4. Maintain consistent styling

### Modifying Download Logic

1. Core logic is in `src/core/downloader.py`
2. Use progress callbacks for UI updates
3. Handle errors gracefully
4. Log important events

## Troubleshooting

### yt-dlp Issues

If downloads fail:

```bash
pip install --upgrade yt-dlp
```

### CustomTkinter Issues

If GUI looks wrong:

```bash
pip install --upgrade customtkinter
```

### FFmpeg Required

For audio downloads, FFmpeg must be installed:

- **macOS**: `brew install ffmpeg`
- **Ubuntu**: `sudo apt install ffmpeg`
- **Windows**: Download from ffmpeg.org

## Contributing

1. Create a feature branch
2. Write tests for new features
3. Ensure all tests pass
4. Update documentation
5. Submit pull request

## License

MIT License - see LICENSE file
