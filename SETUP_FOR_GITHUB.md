# Setting Up for GitHub

This guide will help you publish this project to GitHub and make it open source.

## 1. Update Repository Information

Before pushing to GitHub, update these files with your actual repository information:

### `src/utils/version.py`
```python
GITHUB_REPO = "yourusername/video-downloader"  # Change to your actual repo
```

### `CHANGELOG.md`
Update the URLs at the bottom:
```markdown
[1.0.0]: https://github.com/yourusername/video-downloader/releases/tag/v1.0.0
[Unreleased]: https://github.com/yourusername/video-downloader/compare/v1.0.0...HEAD
```

### `README.md`
Update any example URLs or references to match your GitHub username.

## 2. Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository:
   - **Name**: `video-downloader` (or your preferred name)
   - **Description**: "A modern, cross-platform desktop application for downloading videos from YouTube and Instagram"
   - **Visibility**: Public (for open source)
   - **Do NOT** initialize with README, .gitignore, or license (we already have these)

## 3. Push to GitHub

After creating the repository on GitHub:

```bash
# Add the remote (replace with your actual URL)
git remote add origin https://github.com/yourusername/video-downloader.git

# Push the code
git push -u origin main
```

## 4. Configure Repository Settings

On GitHub, go to your repository settings:

### About Section
- Description: "A modern, cross-platform desktop application for downloading videos from YouTube and Instagram"
- Website: (optional - add if you have one)
- Topics: `python`, `video-downloader`, `youtube-downloader`, `instagram-downloader`, `customtkinter`, `yt-dlp`, `desktop-app`, `cross-platform`

### GitHub Pages (optional)
If you want to host documentation:
- Go to Settings > Pages
- Source: Deploy from a branch
- Branch: main, /docs folder (if you add docs)

### Discussions (optional)
- Enable Discussions for community Q&A

### Issues Templates
Already set up in `.github/ISSUE_TEMPLATE/`

### Pull Request Template
Already set up in `.github/pull_request_template.md`

## 5. Add Badges (Optional)

You can add additional badges to `README.md`:

### Build Status
```markdown
[![Build Status](https://github.com/yourusername/video-downloader/workflows/Build%20and%20Test/badge.svg)](https://github.com/yourusername/video-downloader/actions)
```

### Code Coverage
If you set up Codecov:
```markdown
[![codecov](https://codecov.io/gh/yourusername/video-downloader/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/video-downloader)
```

### Downloads
```markdown
[![GitHub Downloads](https://img.shields.io/github/downloads/yourusername/video-downloader/total)](https://github.com/yourusername/video-downloader/releases)
```

### Stars
```markdown
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/video-downloader?style=social)](https://github.com/yourusername/video-downloader/stargazers)
```

## 6. Create First Release

### Prepare Release Assets

1. **Build for all platforms**:
   ```bash
   # macOS
   ./build.sh
   
   # Windows (on Windows machine)
   build_windows.bat
   
   # Linux (on Linux machine)
   ./build.sh
   ```

2. **Create release archives**:
   ```bash
   # macOS
   cd dist
   zip -r VideoDownloader-macOS-v1.0.0.zip VideoDownloader.app
   
   # Windows
   zip VideoDownloader-Windows-v1.0.0.zip VideoDownloader.exe
   
   # Linux
   tar -czf VideoDownloader-Linux-v1.0.0.tar.gz VideoDownloader
   ```

### Create GitHub Release

1. Go to your repository on GitHub
2. Click "Releases" > "Create a new release"
3. Set tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Description (copy from CHANGELOG.md):
   ```markdown
   # Video Downloader v1.0.0
   
   First production-ready release! 🎉
   
   ## Features
   - ✅ YouTube video downloads
   - ✅ Instagram post/reel downloads
   - ✅ MP4/MP3 conversion
   - ✅ Quality selection (4K to 360p)
   - ✅ Real-time progress tracking
   - ✅ Dark/Light themes
   - ✅ Custom download folders
   - ✅ Auto-update checker
   
   ## Downloads
   - **macOS**: VideoDownloader-macOS-v1.0.0.zip
   - **Windows**: VideoDownloader-Windows-v1.0.0.zip
   - **Linux**: VideoDownloader-Linux-v1.0.0.tar.gz
   
   ## Requirements
   - FFmpeg (see [installation guide](FFMPEG_INSTALL.md))
   
   ## Documentation
   - [User Guide](USER_GUIDE.md)
   - [Installation Instructions](INSTALL.md)
   - [Troubleshooting](TROUBLESHOOTING.md)
   
   ## Known Limitations
   - Age-restricted videos require authentication
   - Private accounts not supported
   - Single video downloads only (no playlists)
   ```
6. Upload the release archives
7. Check "Set as the latest release"
8. Click "Publish release"

## 7. Post-Release Tasks

### Update README
Add installation instructions for the release:

```markdown
## Quick Install

### macOS
1. Download `VideoDownloader-macOS-v1.0.0.zip`
2. Extract and move `VideoDownloader.app` to Applications
3. Install FFmpeg: `brew install ffmpeg`
4. Open the app

### Windows
1. Download `VideoDownloader-Windows-v1.0.0.zip`
2. Extract `VideoDownloader.exe`
3. Install FFmpeg (see [guide](FFMPEG_INSTALL.md))
4. Run the executable

### Linux
1. Download `VideoDownloader-Linux-v1.0.0.tar.gz`
2. Extract: `tar -xzf VideoDownloader-Linux-v1.0.0.tar.gz`
3. Install FFmpeg: `sudo apt install ffmpeg`
4. Run: `./VideoDownloader`
```

### Social Media Announcement (Optional)

Share your project:
- Reddit: r/Python, r/opensource, r/software
- Twitter/X: #Python #OpenSource #VideoDownloader
- Dev.to: Write a blog post about the project
- Hacker News: Submit your project

Example announcement:
```
🎉 Just released Video Downloader v1.0.0!

A modern, cross-platform desktop app for downloading videos from YouTube & Instagram.

✨ Features:
- Clean CustomTkinter GUI
- MP4/MP3 conversion
- Quality selection
- Dark/Light themes
- Real-time progress

🛠 Built with Python, yt-dlp, CustomTkinter
📦 56 tests, 88% coverage
📄 MIT Licensed

Check it out: https://github.com/yourusername/video-downloader

Feedback welcome! 🚀
```

## 8. Set Up Continuous Integration (Optional)

The GitHub Actions workflow is already set up in `.github/workflows/build.yml`.

To enable it:
1. Make sure your repository has Actions enabled (Settings > Actions)
2. Push a commit to trigger the workflow
3. Check the Actions tab to see build status

### Add Codecov (Optional)

For code coverage reporting:
1. Go to [codecov.io](https://codecov.io)
2. Sign in with GitHub
3. Add your repository
4. Get the upload token
5. Add it to GitHub Secrets: Settings > Secrets > New repository secret
   - Name: `CODECOV_TOKEN`
   - Value: (your token)

## 9. Community Guidelines

### Responding to Issues
- Be welcoming and helpful
- Ask for more details if needed
- Refer to documentation when applicable
- Label issues appropriately (bug, enhancement, question, etc.)

### Reviewing Pull Requests
- Check that tests pass
- Review code for quality
- Test the changes locally if possible
- Provide constructive feedback
- Thank contributors!

### Keeping the Project Active
- Respond to issues within 1-2 days
- Review PRs within 1 week
- Update dependencies regularly
- Release updates when fixes accumulate

## 10. Maintenance Checklist

### Weekly
- [ ] Check and respond to new issues
- [ ] Review open pull requests
- [ ] Test with latest yt-dlp version

### Monthly
- [ ] Update dependencies
- [ ] Check for security vulnerabilities
- [ ] Review and update documentation
- [ ] Consider new feature requests

### When YouTube/Instagram Changes
- [ ] Test downloads still work
- [ ] Update yt-dlp if needed
- [ ] Release patch version if broken

## Questions?

If you need help setting up GitHub or have questions, feel free to:
- Check GitHub's [documentation](https://docs.github.com)
- Ask in GitHub Discussions
- Open an issue

---

**Ready to go open source? Let's do this! 🚀**
