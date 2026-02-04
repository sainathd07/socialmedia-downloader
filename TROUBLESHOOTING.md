# Troubleshooting Guide

Common issues and solutions for Social Media Downloader.

---

## ❌ "This video requires authentication"

### What It Means:
The video is age-restricted, private, or requires YouTube login.

### Why It Happens:
- Video is marked 18+ (age-restricted)
- Video is private or unlisted with restrictions
- Video requires channel membership
- Video has premium content

### Solution:
✅ **Try a different public video**

Test with this guaranteed-working video:
```
https://www.youtube.com/watch?v=jNQXAC9IVRw
```

### How to Check:
Open the video in **incognito/private browsing mode**:
- ✅ Plays without login → Will download
- ❌ Asks to sign in → Won't download

---

## ❌ "Video is unavailable or private"

### What It Means:
The video was deleted, made private, or doesn't exist.

### Solution:
- Check if video plays in browser
- Try a different video
- Verify the URL is correct

---

## ❌ "FFmpeg Not Found" Warning

### What It Means:
FFmpeg isn't installed, so MP4/MP3 conversion won't work.

### Solution:

#### macOS:
```bash
brew install ffmpeg
```

#### Check if already installed:
```bash
ffmpeg -version
```

### After Installing:
1. Close the Video Downloader app completely
2. Reopen it
3. The warning should be gone!

---

## ❌ App Won't Open (macOS)

### Solution 1: Right-Click Method
1. Right-click `VideoDownloader.app`
2. Select "Open"
3. Click "Open" in the dialog

### Solution 2: Terminal Method
```bash
xattr -cr dist/VideoDownloader.app
open dist/VideoDownloader.app
```

### Solution 3: System Preferences
1. Try opening the app
2. System Preferences → Security & Privacy
3. Click "Open Anyway"

---

## ❌ Download Gets Stuck at 0%

### Possible Causes:
1. No internet connection
2. Video is processing
3. Server is slow

### Solutions:
- Check internet connection
- Wait 30 seconds
- Try a different video
- Check logs: `~/.video_downloader/logs/`

---

## ❌ "Download Failed" Generic Error

### Steps to Debug:

1. **Check internet connection**
2. **Try in browser**: Does the video play?
3. **Check URL format**: YouTube or Instagram only
4. **Check logs**:
   ```bash
   cat ~/.video_downloader/logs/*.log | tail -50
   ```
5. **Try a different video**

---

## ❌ Downloaded File Won't Play

### WebM Instead of MP4?

**Cause**: FFmpeg not installed

**Solution**:
```bash
brew install ffmpeg
```

Then download again - will be MP4!

### File Corrupted?

**Solution**:
1. Delete the partial file
2. Download again
3. Check disk space
4. Try different quality

---

## ❌ "URL is not from a supported platform"

### Supported Platforms:
- ✅ YouTube (`youtube.com` or `youtu.be`)
- ✅ Instagram (`instagram.com`)
- ❌ Others not supported yet

### Common Mistakes:
- ❌ `https://facebook.com/...` → Not supported
- ❌ `https://tiktok.com/...` → Not supported
- ❌ `https://twitter.com/...` → Not supported

---

## ⚠️ Slow Download Speed

### Normal Speeds:
- Depends on your internet connection
- Server speed varies
- Large videos (4K) take longer

### Not Actually Slow:
- 4K 10-minute video = ~500MB = 2-5 minutes on good connection
- This is normal!

### If Truly Slow:
1. Check your internet speed
2. Close other downloads
3. Try different time of day
4. YouTube/Instagram server may be slow

---

## ❌ "Insufficient Disk Space"

### Solution:
1. Check available space:
   ```bash
   df -h ~
   ```
2. Free up space
3. Choose different download folder
4. Try lower quality

---

## ❌ Can't Select Download Folder

### Solution:
1. Click "Browse" button
2. Navigate to desired folder
3. Click "Select"
4. App will remember your choice

### Permissions Issue:
If you can't select certain folders:
1. Grant Full Disk Access to Terminal (if running from terminal)
2. Or choose a folder in your home directory

---

## 🔧 Advanced Troubleshooting

### Check Logs
```bash
# View today's log
cat ~/.video_downloader/logs/$(date +%Y%m%d).log

# View last 50 lines
tail -50 ~/.video_downloader/logs/*.log

# Search for errors
grep ERROR ~/.video_downloader/logs/*.log
```

### Reset Settings
```bash
# Remove settings file
rm ~/.video_downloader/settings.json

# Reopen app - will create fresh settings
```

### Clean Reinstall
```bash
# Remove all app data
rm -rf ~/.video_downloader

# Rebuild from source
cd /Users/sainathdushatti/projects/Tools/Downloader
./build.sh

# Open fresh app
open dist/VideoDownloader.app
```

---

## 📞 Getting Help

### Before Reporting Issues:

1. ✅ Try a different video (use test videos from TEST_VIDEOS.md)
2. ✅ Check if FFmpeg is installed
3. ✅ Read error message carefully
4. ✅ Check logs
5. ✅ Try the video in browser (incognito mode)

### When Reporting Issues:

Include:
- Video URL you tried
- Error message shown
- Log file excerpt
- macOS version
- Whether FFmpeg is installed

---

## ✨ Success Checklist

Your app is working if:
- ✅ Opens without errors
- ✅ Validates URLs (green checkmark)
- ✅ Shows progress when downloading
- ✅ Downloads complete successfully
- ✅ Files are in MP4 or MP3 format
- ✅ Can switch dark/light mode
- ✅ Settings persist after restart

---

## 🎯 Quick Fix Guide

| Problem | Quick Fix |
|---------|-----------|
| Authentication error | Try public video |
| FFmpeg warning | `brew install ffmpeg` |
| App won't open | Right-click → Open |
| Download stuck | Wait or try different video |
| WebM format | Install FFmpeg |
| Slow speed | Normal for large files |

---

## 📚 Related Guides

- **TEST_VIDEOS.md** - Videos guaranteed to work
- **USER_GUIDE.md** - Complete user manual
- **FFMPEG_INSTALL.md** - FFmpeg installation
- **FAQ** (below)

---

## ❓ FAQ

### Q: Why do some videos fail?
**A**: Age-restricted, private, or region-locked videos require authentication. Try public videos only.

### Q: How do I know if a video will work?
**A**: Open it in incognito browser mode. If it plays without login, it will download!

### Q: Can I download age-restricted videos?
**A**: No, the app doesn't support authentication. This is by design for privacy.

### Q: What video format do I get?
**A**: MP4 for videos, MP3 for audio (if FFmpeg installed). WebM otherwise.

### Q: Why is FFmpeg needed?
**A**: For converting to MP4 and extracting MP3 audio. Without it, videos stay as WebM.

### Q: Is my data safe?
**A**: Yes! No data is collected, everything stays on your computer.

---

**Most Common Issue**: Trying to download age-restricted or private videos. Use public videos only! ✅
