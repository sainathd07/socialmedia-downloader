# Social Media Downloader - User Guide

## Overview

Video Downloader is a simple, modern application for downloading videos from YouTube and Instagram to your computer.

## Features

- Download videos from YouTube and Instagram
- Convert videos to MP3 audio files
- Choose video quality (up to 4K)
- Progress tracking with speed and time remaining
- Custom download folder selection
- Dark and light mode themes
- Remember your preferences

## Installation

### macOS

1. Download `VideoDownloader.dmg`
2. Open the DMG file
3. Drag "Video Downloader" to your Applications folder
4. Double-click to run

**Note**: If you see "cannot be opened because it is from an unidentified developer":
- Right-click the app and select "Open"
- Click "Open" in the dialog

### Windows

1. Download `VideoDownloader.exe` installer
2. Run the installer
3. Follow the installation wizard
4. Launch from Start Menu or Desktop shortcut

**Note**: Windows may show a SmartScreen warning. Click "More info" then "Run anyway"

### Linux

1. Download `VideoDownloader.AppImage`
2. Make it executable: `chmod +x VideoDownloader.AppImage`
3. Run: `./VideoDownloader.AppImage`

## How to Use

### Basic Download

1. **Copy Video URL**
   - Go to YouTube or Instagram
   - Copy the video URL from your browser

2. **Paste URL**
   - Paste the URL into the "Paste Video URL" field
   - You'll see a green checkmark if the URL is valid

3. **Choose Options**
   - Select "Video" or "Audio Only"
   - Choose quality (for video downloads)
   - Select where to save the file (optional)

4. **Download**
   - Click the "DOWNLOAD" button
   - Watch the progress bar
   - File will be saved when complete

### Supported URLs

**YouTube:**
- Standard videos: `youtube.com/watch?v=...`
- Short links: `youtu.be/...`
- Shorts: `youtube.com/shorts/...`

**Instagram:**
- Posts: `instagram.com/p/...`
- Reels: `instagram.com/reel/...`

### Download Types

#### Video Download
- Downloads the video file
- Choose quality: 4K, 1080p, 720p, etc.
- Saves as MP4 format

#### Audio Only
- Extracts audio from video
- Converts to MP3 format
- High quality (192 kbps)

### Download Folder

**Default Location:**
- `~/Downloads/VideoDownloader/`

**To Change:**
1. Click "Browse" button
2. Select your preferred folder
3. Your choice is remembered

### Dark/Light Mode

Toggle the switch in the bottom right corner to change themes.

## Troubleshooting

### "Video unavailable or private"
- The video may be private, deleted, or region-restricted
- Try opening the video in your browser first
- Some Instagram content requires login (not supported)

### "This video requires authentication"
- Some videos need you to be logged in
- These cannot be downloaded with this app

### "Download failed"
- Check your internet connection
- Verify the URL is correct
- Try updating the app

### Slow Downloads
- Speed depends on your internet connection
- Large videos (4K) take longer
- Server speed may vary

### Audio Downloads Not Working
- FFmpeg may not be installed
- Try downloading as video instead
- Check logs for specific error

## Tips

1. **Use "Best Available"** quality for automatic quality selection
2. **Keep URLs clean** - just copy from browser address bar
3. **Check disk space** before downloading large videos
4. **Organize downloads** by setting custom folders for different content
5. **Audio format** is perfect for music videos and podcasts

## Privacy

- **No data collection**: This app doesn't track you
- **No cloud storage**: Everything stays on your computer
- **No accounts**: No registration required
- **Local only**: All processing happens on your device

## File Locations

### Downloads
Default: `~/Downloads/VideoDownloader/`
Custom: As selected in the app

### Settings
- **macOS/Linux**: `~/.video_downloader/settings.json`
- **Windows**: `%USERPROFILE%\.video_downloader\settings.json`

### Logs
- **macOS/Linux**: `~/.video_downloader/logs/`
- **Windows**: `%USERPROFILE%\.video_downloader\logs\`

## Keyboard Shortcuts

- **⌘/Ctrl+V**: Paste URL (when input field is focused)
- **⌘/Ctrl+Q**: Quit application
- **Return/Enter**: Start download (when URL is valid)

## Limitations

- Instagram private accounts not supported
- Age-restricted YouTube videos may not work
- Some region-locked content unavailable
- No playlist downloads (single videos only)
- No live stream downloads

## Getting Help

If you encounter issues:

1. Check this guide first
2. Look at log files for error details
3. Ensure you have the latest version
4. Check if the video works in a web browser
5. Report bugs with:
   - URL you tried to download
   - Error message shown
   - Log file excerpt

## Updates

The app checks for yt-dlp updates automatically. For app updates:

- **macOS**: Download new DMG
- **Windows**: Run new installer
- **Linux**: Download new AppImage

## Legal Notice

- Only download content you have permission to download
- Respect copyright and terms of service
- This tool is for personal use only
- Users are responsible for their usage

## Credits

Built with:
- Python
- CustomTkinter (GUI)
- yt-dlp (Download engine)
- FFmpeg (Audio conversion)

## Version

Current version: 1.0.0

---

**Enjoy downloading your favorite videos!**
