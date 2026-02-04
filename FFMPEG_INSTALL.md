# Installing FFmpeg for Format Conversion

## Why FFmpeg?

FFmpeg is required to convert videos to MP4 and extract audio to MP3. Without it:
- Videos will download as WebM or other formats ❌
- Audio extraction won't work ❌

## Check If Already Installed

```bash
ffmpeg -version
```

If you see version information, you're good! ✅

## Install FFmpeg on macOS

### Option 1: Homebrew (Recommended)

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg
brew install ffmpeg

# Verify installation
ffmpeg -version
```

### Option 2: MacPorts

```bash
sudo port install ffmpeg
```

### Option 3: Download Binary

1. Visit: https://evermeet.cx/ffmpeg/
2. Download the latest version
3. Extract and move to `/usr/local/bin/`
4. Make executable: `chmod +x /usr/local/bin/ffmpeg`

## Install FFmpeg on Windows

### Option 1: Winget (Windows 11)

```powershell
winget install ffmpeg
```

### Option 2: Chocolatey

```powershell
choco install ffmpeg
```

### Option 3: Manual Install

1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to PATH
4. Restart terminal/IDE

## Install FFmpeg on Linux

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Fedora

```bash
sudo dnf install ffmpeg
```

### Arch Linux

```bash
sudo pacman -S ffmpeg
```

## Verify Installation

After installing, verify:

```bash
ffmpeg -version
```

You should see something like:
```
ffmpeg version 6.1.1
```

## Restart the App

After installing FFmpeg:

1. Close the Video Downloader app
2. Restart it
3. Try downloading again

Your videos will now be MP4 and audio will be MP3! 🎉

## Troubleshooting

### "ffmpeg not found"

Make sure FFmpeg is in your PATH:

```bash
# Check where ffmpeg is
which ffmpeg

# Should show a path like /usr/local/bin/ffmpeg or /opt/homebrew/bin/ffmpeg
```

If empty, FFmpeg isn't in PATH. Add it:

```bash
# For Homebrew on Apple Silicon Mac
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For Homebrew on Intel Mac
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Still not working?

1. Completely close terminal
2. Reopen terminal
3. Run: `ffmpeg -version`
4. If it works, restart the Video Downloader app

---

**Quick Install for macOS**: `brew install ffmpeg` ✅
