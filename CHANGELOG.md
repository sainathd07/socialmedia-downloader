# Changelog - Social Media Downloader

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-05

### Added
- Initial release
- YouTube video download support
- Instagram post and reel download support
- MP4 video conversion with FFmpeg
- MP3 audio extraction
- Quality selection (4K, 1080p, 720p, 480p, 360p)
- Real-time progress tracking with speed and ETA
- Custom download folder selection
- Settings persistence (folder, quality, theme)
- Dark/Light mode toggle
- URL validation with visual feedback
- Comprehensive error handling
- FFmpeg detection with helpful installation guide
- Auto-update checker
- Version display in UI
- Cross-platform support (macOS, Windows, Linux)
- Build configurations for all platforms
- Comprehensive test suite (56 tests)
- Complete documentation (15+ guides)
- Professional icon design

### Technical
- Built with Python 3.10+
- CustomTkinter 5.2.2 for modern GUI
- yt-dlp 2026.2.4 for download engine
- PyInstaller 6.6.0 for executable building
- pytest for testing framework
- 88% core logic test coverage

### Documentation
- User Guide
- Development Guide
- Installation Guide
- Troubleshooting Guide
- Test Videos List
- FFmpeg Installation Guide
- Code Signing Guide
- Contributing Guidelines
- Production Readiness Assessment

### Known Limitations
- Age-restricted YouTube videos require authentication (not supported)
- Private Instagram accounts not supported
- Playlist downloads not supported (single videos only)
- Live streams not supported
- No download resume functionality

---

## [Unreleased]

### Planned Features
- Batch download support (multiple URLs)
- Download history with database
- Thumbnail preview before download
- Additional platform support (TikTok, Twitter, Vimeo)
- Playlist download support
- Resume interrupted downloads
- Subtitle download options
- Format conversion options
- Proxy settings

---

## Version History

- **1.0.0** (2026-02-05) - Initial production release

---

[1.0.0]: https://github.com/sainathd07/socialmedia-downloader/releases/tag/v1.0.0
[Unreleased]: https://github.com/sainathd07/socialmedia-downloader/compare/v1.0.0...HEAD
