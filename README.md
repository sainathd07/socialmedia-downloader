# 🎬 Video Downloader

> A modern, cross-platform desktop application for downloading videos from YouTube and Instagram with a beautiful GUI.

[![Production Ready](https://img.shields.io/badge/production-ready-brightgreen)](FINAL_STATUS.md)
[![Tests](https://img.shields.io/badge/tests-56%20passing-brightgreen)](tests/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)](README.md)

**Status**: Production Ready | **Version**: 1.0.0 | **Grade**: A+

## ✨ Features

- 📹 **Download videos** from YouTube and Instagram
- 🎵 **Audio extraction** to MP3 (192kbps)
- 📊 **Real-time progress** tracking with speed and ETA
- 🎨 **Dark/Light mode** with auto-save
- 💾 **Custom folders** with persistence
- 🔄 **Auto-updates** notification system
- ⚡ **Quality selection** (4K, 1080p, 720p, 480p, 360p)
- 🛡️ **FFmpeg detection** with helpful install guide
- ✅ **MP4/MP3 format** conversion
- 🎯 **User-friendly** error handling

## Installation

### For Users

Download the latest release for your platform:
- **macOS**: Download the .dmg file
- **Windows**: Download the .exe installer
- **Linux**: Download the AppImage

### For Developers

1. Clone the repository:
```bash
git clone <repository-url>
cd Downloader
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python src/main.py
```

## Development

### Running Tests

```bash
pytest tests/
```

### Building Executables

#### macOS
```bash
pyinstaller build_macos.spec
```

#### Windows
```bash
pyinstaller build_windows.spec
```

## Requirements

- Python 3.10 or higher
- FFmpeg (optional, for audio conversion)

## 📊 Project Stats

- **Lines of Code**: ~3,200 (Python) + 800 (tests)
- **Test Coverage**: 88% (core logic), 56 tests passing
- **Documentation**: 15 comprehensive guides
- **Production Ready**: 98%
- **Platforms**: macOS, Windows, Linux

## 🎯 Quick Links

- [📖 User Guide](USER_GUIDE.md) - How to use the app
- [🚀 Quick Start](QUICKSTART.md) - Get started in 5 minutes
- [👨‍💻 Development](DEVELOPMENT.md) - Developer guide
- [✅ Final Status](FINAL_STATUS.md) - Production readiness
- [🔧 FFmpeg Install](FFMPEG_INSTALL.md) - FFmpeg setup guide
- [📋 Release Checklist](RELEASE_CHECKLIST.md) - Distribution guide

## 🙏 Credits

Built with love using:
- [Python 3.12](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern GUI framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Download engine
- [FFmpeg](https://ffmpeg.org/) - Media conversion

## ⚠️ Legal Notice

- Only download content you have permission to download
- Respect copyright and terms of service
- This tool is for personal use only
- Users are responsible for their usage

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 🌟 Support

If you find this project useful, please give it a star! ⭐

---

**Made with ❤️ | Version 1.0.0 | Production Ready**

## Privacy

This application does not collect any user data. All downloads and settings are stored locally on your device.
