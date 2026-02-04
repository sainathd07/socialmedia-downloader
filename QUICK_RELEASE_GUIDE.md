# ⚡ Quick Release Guide - TL;DR

## For Your First Release Right Now

### Step 1: Build the macOS App (5 minutes)

```bash
cd /Users/sainathdushatti/projects/Tools/Downloader
source venv/bin/activate
./build.sh
cd dist
zip -r SocialMediaDownloader-macOS-v1.0.0.zip SocialMediaDownloader.app
cd ..
```

You now have: `dist/SocialMediaDownloader-macOS-v1.0.0.zip`

### Step 2: Create GitHub Release (3 minutes)

1. Go to: https://github.com/sainathd07/socialmedia-downloader/releases/new

2. Fill in:
   - **Tag**: `v1.0.0` (create new tag)
   - **Title**: `v1.0.0 - Initial Release`
   - **Description**:
   ```
   # 🎉 Social Media Downloader v1.0.0
   
   Download videos from YouTube and Instagram with a beautiful GUI!
   
   ## Features
   - 📹 YouTube & Instagram downloads
   - 🎵 MP3 audio extraction
   - 📊 Real-time progress tracking
   - 🎨 Dark/Light mode
   - ⚡ Quality selection (4K to 360p)
   
   ## Installation
   
   ### macOS
   1. Download `SocialMediaDownloader-macOS-v1.0.0.zip`
   2. Extract and move to Applications
   3. Install FFmpeg: `brew install ffmpeg`
   4. Double-click to run
   
   **Note**: FFmpeg is required for MP4/MP3 conversion.
   
   ## Documentation
   - [User Guide](https://github.com/sainathd07/socialmedia-downloader/blob/main/USER_GUIDE.md)
   - [Troubleshooting](https://github.com/sainathd07/socialmedia-downloader/blob/main/TROUBLESHOOTING.md)
   
   ## Support
   [Report Issues](https://github.com/sainathd07/socialmedia-downloader/issues/new/choose)
   ```

3. **Upload file**: Drag `SocialMediaDownloader-macOS-v1.0.0.zip` to the upload area

4. **Check**: ✅ "Set as the latest release"

5. **Click**: "Publish release" 🚀

### Done! 🎉

Users can now download from:
https://github.com/sainathd07/socialmedia-downloader/releases/latest

---

## Add Windows/Linux Later

When you have access to Windows/Linux machines:
- Follow the same build steps for each platform
- Upload the additional files to the same release
- Edit the release description to include all platforms

---

**See `CREATING_RELEASES.md` for the complete guide with automation options.**
