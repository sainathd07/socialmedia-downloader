# Quick Start Guide

## For End Users

### macOS
```bash
# Download the .dmg file, then:
1. Open VideoDownloader.dmg
2. Drag to Applications
3. Double-click to run
```

### Windows
```bat
1. Download VideoDownloader.exe
2. Run the installer
3. Launch from Start Menu
```

### Linux
```bash
# Download the .AppImage, then:
chmod +x VideoDownloader.AppImage
./VideoDownloader.AppImage
```

## For Developers

### Setup (First Time)

```bash
# 1. Clone repository
git clone <your-repo-url>
cd Downloader

# 2. Run the application (auto-installs dependencies)
./run.sh  # macOS/Linux
# or
python src\main.py  # Windows
```

### Daily Development

```bash
# Run the app
./run.sh

# Run tests
pytest tests/

# Build executable
./build.sh  # macOS/Linux
build_windows.bat  # Windows
```

## Installation Requirements

### Runtime Requirements (For Users)
- **macOS**: macOS 10.13+ (High Sierra or later)
- **Windows**: Windows 10 or later
- **Linux**: Any modern distribution
- **Optional**: FFmpeg (for audio downloads)

### Development Requirements
- Python 3.10 or higher
- pip (Python package manager)
- Git (for cloning repository)

### Installing Python

#### macOS
```bash
# Using Homebrew
brew install python@3.11

# Or download from python.org
```

#### Windows
```bat
REM Download from python.org
REM Make sure to check "Add Python to PATH" during installation
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.11 python3-pip python3-venv

# Fedora
sudo dnf install python3.11
```

### Installing FFmpeg (Optional)

FFmpeg is needed for audio-only downloads.

#### macOS
```bash
brew install ffmpeg
```

#### Windows
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg`
3. Add to PATH environment variable

#### Linux
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

## First Run

### Using the Application

1. **Launch the app**
2. **Paste a URL**: Copy any YouTube or Instagram video URL
3. **Choose options**: 
   - Video or Audio Only
   - Quality preference
   - Download location
4. **Click DOWNLOAD**
5. **Wait**: Progress bar shows status
6. **Done**: File saved to your chosen location

### Example URLs to Try

**YouTube:**
- `https://www.youtube.com/watch?v=jNQXAC9IVRw` (Me at the zoo)
- `https://youtu.be/dQw4w9WgXcQ`

**Instagram:**
- Any public Instagram post or reel URL

## Common First-Time Issues

### macOS: "App can't be opened"
```bash
# Solution 1: Right-click > Open
# Solution 2: Terminal command
xattr -cr /Applications/VideoDownloader.app
```

### Windows: SmartScreen Warning
```
Click "More info" → "Run anyway"
```

### Linux: Permission Denied
```bash
chmod +x VideoDownloader.AppImage
```

### Python Not Found
```bash
# Check Python installation
python3 --version

# Should show Python 3.10 or higher
```

## Project Structure (For Developers)

```
Downloader/
├── src/                    # Source code
│   ├── main.py            # Entry point
│   ├── gui/               # User interface
│   ├── core/              # Download logic
│   └── utils/             # Utilities
├── tests/                  # Test suite
├── requirements.txt        # Dependencies
├── build_macos.spec       # macOS build config
├── build_windows.spec     # Windows build config
├── run.sh                 # Quick run script
└── build.sh               # Build script
```

## Next Steps

### For Users
- Read [USER_GUIDE.md](USER_GUIDE.md) for detailed usage
- Check supported platforms and features
- Learn about keyboard shortcuts

### For Developers
- Read [DEVELOPMENT.md](DEVELOPMENT.md) for architecture
- Run tests: `pytest tests/`
- See [README.md](README.md) for contribution guidelines

## Getting Help

### For Users
1. Check [USER_GUIDE.md](USER_GUIDE.md)
2. Look at log files (`~/.video_downloader/logs/`)
3. Report issues with error messages

### For Developers
1. Read [DEVELOPMENT.md](DEVELOPMENT.md)
2. Check test output: `pytest tests/ -v`
3. Review logs for debugging
4. Open issues on GitHub

## Quick Commands Reference

```bash
# Development
./run.sh                    # Run app
pytest tests/               # Run tests
./build.sh                  # Build executable

# Virtual Environment
python3 -m venv venv        # Create venv
source venv/bin/activate    # Activate (Unix)
venv\Scripts\activate       # Activate (Windows)
deactivate                  # Deactivate

# Dependencies
pip install -r requirements.txt      # Install
pip install -r requirements-dev.txt  # Install with dev tools
pip list                             # List installed
```

## Support

- **Issues**: Check logs in `~/.video_downloader/logs/`
- **Documentation**: See README.md, USER_GUIDE.md, DEVELOPMENT.md
- **Updates**: Download latest version from releases

---

**Ready to start? Run `./run.sh` or `python src/main.py`!**
