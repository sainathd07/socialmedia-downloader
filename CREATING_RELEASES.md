# 🚀 Creating GitHub Releases for Non-Technical Users

This guide shows you how to build and release executables so users can download and run the app without installing Python or building from source.

---

## 📦 What Users Will Download

After following this guide, users can download:
- **macOS**: `SocialMediaDownloader-macOS-v1.0.0.zip` (double-click to install)
- **Windows**: `SocialMediaDownloader-Windows-v1.0.0.zip` (extract and run .exe)
- **Linux**: `SocialMediaDownloader-Linux-v1.0.0.tar.gz` (extract and run)

---

## 🛠️ Step 1: Build the Application

### Build for macOS

On your macOS machine:

```bash
# Navigate to project
cd /path/to/socialmedia-downloader

# Activate virtual environment
source venv/bin/activate

# Install build dependencies if not already installed
pip install -r requirements-dev.txt

# Build the app
./build.sh

# This creates: dist/SocialMediaDownloader.app
```

**Create the release archive:**
```bash
cd dist
zip -r SocialMediaDownloader-macOS-v1.0.0.zip SocialMediaDownloader.app
cd ..
```

### Build for Windows

On a Windows machine (or use GitHub Actions):

```batch
# Navigate to project
cd C:\path\to\socialmedia-downloader

# Activate virtual environment
venv\Scripts\activate

# Install build dependencies
pip install -r requirements-dev.txt

# Build the app
build_windows.bat

# This creates: dist\SocialMediaDownloader.exe
```

**Create the release archive:**
```batch
cd dist
powershell Compress-Archive -Path SocialMediaDownloader.exe -DestinationPath SocialMediaDownloader-Windows-v1.0.0.zip
cd ..
```

### Build for Linux

On a Linux machine:

```bash
# Navigate to project
cd /path/to/socialmedia-downloader

# Activate virtual environment
source venv/bin/activate

# Install build dependencies
pip install -r requirements-dev.txt

# Build the app
./build.sh

# This creates: dist/SocialMediaDownloader
```

**Create the release archive:**
```bash
cd dist
tar -czf SocialMediaDownloader-Linux-v1.0.0.tar.gz SocialMediaDownloader
cd ..
```

---

## 📝 Step 2: Create Release Notes

Create a file `release-notes-v1.0.0.md` with this content:

```markdown
# 🎉 Social Media Downloader v1.0.0

First official release! A modern, cross-platform desktop application for downloading videos from YouTube and Instagram.

## ✨ Features

- 📹 Download videos from YouTube and Instagram
- 🎵 Audio extraction to MP3 (192kbps)
- 📊 Real-time progress tracking with speed and ETA
- 🎨 Dark/Light mode with auto-save
- 💾 Custom download folders with persistence
- 🔄 Auto-update notifications
- ⚡ Quality selection (4K, 1080p, 720p, 480p, 360p)
- ✅ MP4/MP3 format conversion
- 🎯 User-friendly error handling
- 🛡️ Cross-platform support (macOS, Windows, Linux)

## 📥 Downloads

Choose the right version for your operating system:

### macOS
- Download: `SocialMediaDownloader-macOS-v1.0.0.zip`
- Requirements: macOS 10.13 or later
- Installation:
  1. Download and extract the zip file
  2. Move `SocialMediaDownloader.app` to your Applications folder
  3. Install FFmpeg: `brew install ffmpeg`
  4. Double-click the app to run

### Windows
- Download: `SocialMediaDownloader-Windows-v1.0.0.zip`
- Requirements: Windows 10 or later
- Installation:
  1. Download and extract the zip file
  2. Install FFmpeg (see [FFmpeg Installation Guide](FFMPEG_INSTALL.md))
  3. Run `SocialMediaDownloader.exe`

### Linux
- Download: `SocialMediaDownloader-Linux-v1.0.0.tar.gz`
- Requirements: Ubuntu 20.04+ or equivalent
- Installation:
  1. Extract: `tar -xzf SocialMediaDownloader-Linux-v1.0.0.tar.gz`
  2. Install FFmpeg: `sudo apt install ffmpeg`
  3. Run: `./SocialMediaDownloader`

## ⚠️ Important: FFmpeg Required

This app requires FFmpeg for MP4/MP3 conversion. See the [FFmpeg Installation Guide](https://github.com/sainathd07/socialmedia-downloader/blob/main/FFMPEG_INSTALL.md) for detailed instructions.

## 📖 Documentation

- [User Guide](https://github.com/sainathd07/socialmedia-downloader/blob/main/USER_GUIDE.md)
- [Troubleshooting](https://github.com/sainathd07/socialmedia-downloader/blob/main/TROUBLESHOOTING.md)
- [Test Videos](https://github.com/sainathd07/socialmedia-downloader/blob/main/TEST_VIDEOS.md)

## 🐛 Known Limitations

- Age-restricted YouTube videos require authentication (not supported)
- Instagram private accounts not supported
- Single video downloads only (no playlists yet)
- FFmpeg must be installed separately

## 🆕 What's New

This is the first release with all core features:
- YouTube and Instagram video downloads
- MP4/MP3 conversion
- Quality selection
- Dark/Light themes
- Progress tracking
- Auto-update checker
- Comprehensive error handling

## 📊 Technical Details

- Built with Python 3.10+
- CustomTkinter 5.2.2 for GUI
- yt-dlp 2026.2.4 for downloads
- 88% test coverage
- Production-ready code

## 🙏 Support

If you encounter any issues:
1. Check the [Troubleshooting Guide](https://github.com/sainathd07/socialmedia-downloader/blob/main/TROUBLESHOOTING.md)
2. Search [existing issues](https://github.com/sainathd07/socialmedia-downloader/issues)
3. [Open a new issue](https://github.com/sainathd07/socialmedia-downloader/issues/new/choose)

## ⭐ Like this project?

Give it a star on [GitHub](https://github.com/sainathd07/socialmedia-downloader) and share it with others!

---

**Full Changelog**: https://github.com/sainathd07/socialmedia-downloader/blob/main/CHANGELOG.md
```

---

## 🎯 Step 3: Create the GitHub Release

### Via GitHub Website (Easiest)

1. **Go to your repository**:
   - Navigate to https://github.com/sainathd07/socialmedia-downloader

2. **Click on "Releases"**:
   - On the right sidebar, click "Releases" (or go to `/releases`)

3. **Click "Create a new release"** or "Draft a new release"

4. **Fill in the release details**:
   - **Choose a tag**: `v1.0.0`
     - Click "Choose a tag" → Type `v1.0.0` → Click "Create new tag: v1.0.0 on publish"
   
   - **Release title**: `v1.0.0 - Initial Release`
   
   - **Description**: Copy the content from `release-notes-v1.0.0.md`

5. **Upload the binaries**:
   - Drag and drop or click "Attach binaries by dropping them here or selecting them"
   - Upload these files:
     - `SocialMediaDownloader-macOS-v1.0.0.zip`
     - `SocialMediaDownloader-Windows-v1.0.0.zip`
     - `SocialMediaDownloader-Linux-v1.0.0.tar.gz`

6. **Options**:
   - ✅ Check "Set as the latest release"
   - ⬜ Don't check "Set as a pre-release" (it's stable)

7. **Click "Publish release"** 🎉

### Via GitHub CLI (Alternative)

If you have GitHub CLI installed:

```bash
# Create the release
gh release create v1.0.0 \
  --title "v1.0.0 - Initial Release" \
  --notes-file release-notes-v1.0.0.md \
  dist/SocialMediaDownloader-macOS-v1.0.0.zip \
  dist/SocialMediaDownloader-Windows-v1.0.0.zip \
  dist/SocialMediaDownloader-Linux-v1.0.0.tar.gz
```

---

## 📱 Step 4: Update Your README

Update the installation section in `README.md`:

```markdown
## 📥 Installation

### For Non-Technical Users (Recommended)

Download the latest release for your platform:

**[📦 Download Latest Release](https://github.com/sainathd07/socialmedia-downloader/releases/latest)**

- **macOS**: Download the `.zip` file, extract, and move to Applications
- **Windows**: Download the `.zip` file, extract, and run the `.exe`
- **Linux**: Download the `.tar.gz` file, extract, and run the executable

**Note**: FFmpeg is required. See [installation guide](FFMPEG_INSTALL.md).

### For Developers

See [Development Guide](DEVELOPMENT.md) for building from source.
```

Commit and push:
```bash
git add README.md
git commit -m "docs: add release download links to README"
git push
```

---

## 🔄 For Future Releases

When you make updates and want to release v1.1.0:

1. **Update version** in `src/utils/version.py`:
   ```python
   __version__ = "1.1.0"
   ```

2. **Update CHANGELOG.md** with new features/fixes

3. **Commit the changes**:
   ```bash
   git add .
   git commit -m "chore: bump version to 1.1.0"
   git push
   ```

4. **Build the application** (repeat Step 1 for all platforms)

5. **Create new release** (repeat Step 3 with new version number)

---

## 🤖 Optional: Automate with GitHub Actions

You can automate building for all platforms using GitHub Actions. Create `.github/workflows/release.yml`:

```yaml
name: Build and Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build-macos:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Build
        run: ./build.sh
      - name: Create archive
        run: |
          cd dist
          zip -r SocialMediaDownloader-macOS-${{ github.ref_name }}.zip SocialMediaDownloader.app
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: macos-build
          path: dist/*.zip

  build-windows:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Build
        run: .\build_windows.bat
      - name: Create archive
        run: |
          cd dist
          Compress-Archive -Path SocialMediaDownloader.exe -DestinationPath SocialMediaDownloader-Windows-${{ github.ref_name }}.zip
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: windows-build
          path: dist/*.zip

  build-linux:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt
      - name: Build
        run: ./build.sh
      - name: Create archive
        run: |
          cd dist
          tar -czf SocialMediaDownloader-Linux-${{ github.ref_name }}.tar.gz SocialMediaDownloader
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: linux-build
          path: dist/*.tar.gz

  release:
    needs: [build-macos, build-windows, build-linux]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Download all artifacts
        uses: actions/download-artifact@v3
      - name: Create Release
        uses: softprops/action-gh-release@v1
        with:
          files: |
            macos-build/*.zip
            windows-build/*.zip
            linux-build/*.tar.gz
          generate_release_notes: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**To use automation**:
1. Create the workflow file
2. Push a tag: `git tag v1.0.0 && git push --tags`
3. GitHub will automatically build and create the release!

---

## 📊 What Users Will See

After creating the release, users visiting your repository will see:

1. **On the main page**: A "Latest Release" badge on the right sidebar
2. **In the Releases section**: All downloadable files with clear instructions
3. **Download counts**: GitHub shows how many times each file was downloaded

Users can simply:
1. Click "Releases"
2. Click the download link for their OS
3. Follow the installation instructions
4. Start using the app immediately!

---

## ✅ Checklist Before Release

- [ ] Built app for macOS (tested it works)
- [ ] Built app for Windows (tested it works)
- [ ] Built app for Linux (tested it works)
- [ ] Created release archives (.zip, .tar.gz)
- [ ] Wrote release notes with clear instructions
- [ ] Updated README with download links
- [ ] Tested FFmpeg detection in built apps
- [ ] Verified all download links work

---

## 🎉 You're Done!

Your app is now available for non-technical users to download and use without any coding knowledge required!

**Questions?** Check the [GitHub Releases documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
