# 🪟 Building Windows Version for Release

You have **3 options** to create the Windows version:

---

## ⚡ Option 1: Automated with GitHub Actions (RECOMMENDED)

This is the easiest way - GitHub will automatically build for Windows, macOS, and Linux!

### How It Works

I've created `.github/workflows/release.yml` that will:
- Build for macOS, Windows, and Linux automatically
- Create a release with all 3 versions
- Trigger when you push a tag like `v1.0.1`

### Steps

1. **Update version** (if needed):
   ```bash
   # Edit src/utils/version.py
   __version__ = "1.0.1"
   ```

2. **Commit and push**:
   ```bash
   git add .
   git commit -m "chore: bump version to 1.0.1"
   git push
   ```

3. **Create and push tag**:
   ```bash
   git tag v1.0.1
   git push origin v1.0.1
   ```

4. **Watch the magic**:
   - Go to: https://github.com/sainathd07/socialmedia-downloader/actions
   - Wait ~10 minutes for builds to complete
   - A new release will be created automatically with all 3 versions!

### Manual Trigger

You can also trigger builds manually:
1. Go to: https://github.com/sainathd07/socialmedia-downloader/actions
2. Click "Build Release Binaries"
3. Click "Run workflow"
4. Choose the branch
5. Click "Run workflow"

---

## 🖥️ Option 2: Build on Windows Machine

If you have access to a Windows computer:

### Steps

1. **Clone repository**:
   ```batch
   git clone https://github.com/sainathd07/socialmedia-downloader.git
   cd socialmedia-downloader
   ```

2. **Create virtual environment**:
   ```batch
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```batch
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Build**:
   ```batch
   build_windows.bat
   ```

5. **Create release archive**:
   ```batch
   cd dist
   powershell Compress-Archive -Path SocialMediaDownloader.exe -DestinationPath SocialMediaDownloader-Windows-v1.0.0.zip
   ```

6. **Upload to GitHub**:
   - Go to: https://github.com/sainathd07/socialmedia-downloader/releases
   - Edit your existing release
   - Upload the Windows .zip file

---

## ☁️ Option 3: Cloud Windows VM

Use a free cloud Windows machine:

### GitHub Codespaces (Free)

1. Go to: https://github.com/sainathd07/socialmedia-downloader
2. Click "Code" → "Codespaces" → "Create codespace on main"
3. Wait for environment to load
4. Run:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   pyinstaller build_windows.spec --clean --noconfirm
   ```
5. Download the built file from `dist/`

### AWS/Azure/GCP Free Tier

1. Create a free Windows VM
2. Connect via RDP
3. Follow Option 2 steps above

---

## 🎯 Recommended Approach

**Use Option 1 (GitHub Actions)** because:
- ✅ Automatic builds for all platforms
- ✅ No Windows machine needed
- ✅ Consistent build environment
- ✅ Builds on every release
- ✅ Free (included with GitHub)

---

## 📋 For Your Current v1.0.0 Release

Since you already released v1.0.0 with macOS only, you have 2 choices:

### Choice A: Add Windows to Existing v1.0.0 Release
```bash
# Push the workflow file
git add .github/workflows/release.yml
git commit -m "ci: add automated release builds for all platforms"
git push

# Manually trigger the workflow for v1.0.0
# Go to Actions → Build Release Binaries → Run workflow
# Then download the artifacts and manually add them to the v1.0.0 release
```

### Choice B: Create v1.0.1 with All Platforms (RECOMMENDED)
```bash
# Push the workflow file
git add .github/workflows/release.yml WINDOWS_RELEASE.md
git commit -m "ci: add automated release builds for all platforms"
git push

# Create new version
git tag v1.0.1
git push origin v1.0.1

# Wait for automatic build and release creation!
```

---

## 🔍 What the Workflow Does

The GitHub Actions workflow will:

1. **Build macOS**: Creates `.app` bundle → zips it
2. **Build Windows**: Creates `.exe` → zips it
3. **Build Linux**: Creates executable → tar.gz it
4. **Create Release**: Automatically creates GitHub release with all files
5. **Add Description**: Auto-generates release notes

All automatically when you push a tag! 🚀

---

## 🆘 Troubleshooting

### "Build Failed on Windows"

Check the Actions log for errors. Common issues:
- Missing dependencies (already fixed in workflow)
- Icon file issues (workflow handles this)

### "No Release Created"

Make sure you:
- Pushed a tag starting with `v` (e.g., `v1.0.1`)
- Have workflows enabled in Settings → Actions

### "Want to Test First"

Use manual workflow trigger:
1. Go to Actions tab
2. Select "Build Release Binaries"
3. Click "Run workflow"
4. Download artifacts to test before creating actual release

---

## ✅ Next Steps

1. **Commit the workflow file** (already created)
2. **Choose** between updating v1.0.0 or creating v1.0.1
3. **Let GitHub Actions do the work** automatically!

No Windows machine needed! 🎉
