# Code Signing Guide

Complete guide to signing your Video Downloader application for distribution.

---

## Why Code Signing?

### Without Signing:
- ❌ macOS: "App can't be opened because it is from an unidentified developer"
- ❌ Windows: SmartScreen warning appears
- ⚠️ Users must right-click → Open (works but not ideal)

### With Signing:
- ✅ macOS: Opens without warnings
- ✅ Windows: No SmartScreen warnings
- ✅ Professional appearance
- ✅ User trust

---

## macOS Code Signing

### Prerequisites

1. **Apple Developer Account**
   - Cost: $99/year
   - Sign up: https://developer.apple.com/programs/

2. **Developer Certificate**
   - "Developer ID Application" certificate
   - For apps distributed outside App Store

### Step 1: Get Certificate

1. Log in to Apple Developer portal
2. Go to Certificates, Identifiers & Profiles
3. Create new certificate → Developer ID Application
4. Download and install in Keychain Access

### Step 2: Sign the App

```bash
# After building with PyInstaller
cd dist

# Sign the app
codesign --force --deep --sign "Developer ID Application: Your Name (TEAM_ID)" VideoDownloader.app

# Verify signature
codesign --verify --deep --strict VideoDownloader.app
codesign -dv VideoDownloader.app
```

### Step 3: Notarize (macOS 10.14.5+)

```bash
# Create a ZIP for notarization
ditto -c -k --keepParent VideoDownloader.app VideoDownloader.zip

# Upload for notarization
xcrun notarytool submit VideoDownloader.zip \
  --apple-id "your@email.com" \
  --team-id "TEAM_ID" \
  --password "app-specific-password" \
  --wait

# If successful, staple the ticket
xcrun stapler staple VideoDownloader.app

# Verify
xcrun stapler validate VideoDownloader.app
```

### Step 4: Create DMG (Optional)

```bash
# Install create-dmg
brew install create-dmg

# Create DMG
create-dmg \
  --volname "Video Downloader" \
  --window-pos 200 120 \
  --window-size 600 400 \
  --icon-size 100 \
  --icon "VideoDownloader.app" 175 190 \
  --hide-extension "VideoDownloader.app" \
  --app-drop-link 425 190 \
  "VideoDownloader-v1.0.0.dmg" \
  "VideoDownloader.app"

# Sign the DMG
codesign --sign "Developer ID Application: Your Name (TEAM_ID)" VideoDownloader-v1.0.0.dmg
```

### Automated Signing Script

```bash
#!/bin/bash
# sign_macos.sh

APP_NAME="VideoDownloader"
IDENTITY="Developer ID Application: Your Name (TEAM_ID)"
APPLE_ID="your@email.com"
TEAM_ID="TEAM_ID"

# Sign
codesign --force --deep --sign "$IDENTITY" dist/$APP_NAME.app

# Verify
codesign --verify --deep --strict dist/$APP_NAME.app

# Create ZIP
cd dist
ditto -c -k --keepParent $APP_NAME.app $APP_NAME.zip

# Notarize
xcrun notarytool submit $APP_NAME.zip \
  --apple-id "$APPLE_ID" \
  --team-id "$TEAM_ID" \
  --password "@keychain:AC_PASSWORD" \
  --wait

# Staple
xcrun stapler staple $APP_NAME.app

echo "✅ Signing complete!"
```

---

## Windows Code Signing

### Prerequisites

1. **Code Signing Certificate**
   - Purchase from: DigiCert, Sectigo, SSL.com
   - Cost: $80-400/year
   - Options:
     - Standard Code Signing (~$200)
     - EV Code Signing (~$300, instant SmartScreen reputation)

2. **SignTool**
   - Included with Windows SDK
   - Download: https://developer.microsoft.com/windows/downloads/windows-sdk/

### Step 1: Install Certificate

```powershell
# Import PFX certificate
Import-PfxCertificate -FilePath "certificate.pfx" -CertStoreLocation Cert:\CurrentUser\My
```

### Step 2: Sign the Executable

```powershell
# Sign with SignTool
signtool sign /f "certificate.pfx" /p "password" /t http://timestamp.digicert.com /fd SHA256 dist\VideoDownloader.exe

# Verify signature
signtool verify /pa dist\VideoDownloader.exe
```

### Step 3: Create Installer (Optional)

Using Inno Setup:

```iss
; installer.iss
[Setup]
AppName=Video Downloader
AppVersion=1.0.0
DefaultDirName={pf}\VideoDownloader
DefaultGroupName=Video Downloader
OutputDir=dist
OutputBaseFilename=VideoDownloader-Setup
Compression=lzma
SolidCompression=yes
SignTool=mysigntool

[Files]
Source: "dist\VideoDownloader.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\Video Downloader"; Filename: "{app}\VideoDownloader.exe"
Name: "{commondesktop}\Video Downloader"; Filename: "{app}\VideoDownloader.exe"
```

Compile and sign:
```powershell
# Compile installer
iscc installer.iss

# Sign installer
signtool sign /f "certificate.pfx" /p "password" /t http://timestamp.digicert.com dist\VideoDownloader-Setup.exe
```

### Automated Signing Script

```powershell
# sign_windows.ps1
$CERT_PATH = "certificate.pfx"
$CERT_PASSWORD = "your-password"
$TIMESTAMP_URL = "http://timestamp.digicert.com"

# Sign executable
signtool sign /f $CERT_PATH /p $CERT_PASSWORD /t $TIMESTAMP_URL /fd SHA256 dist\VideoDownloader.exe

# Verify
signtool verify /pa dist\VideoDownloader.exe

Write-Host "✅ Signing complete!"
```

---

## Linux

Linux doesn't require code signing in the same way, but you can:

1. **GPG Sign AppImage**
   ```bash
   gpg --detach-sign --armor VideoDownloader.AppImage
   ```

2. **Create checksums**
   ```bash
   sha256sum VideoDownloader.AppImage > VideoDownloader.AppImage.sha256
   ```

---

## Distribution Without Signing

If you can't afford certificates, users can still install:

### macOS Workaround

**Option 1**: Right-click → Open
```
1. Right-click VideoDownloader.app
2. Select "Open"
3. Click "Open" in dialog
```

**Option 2**: Terminal command
```bash
xattr -cr /Applications/VideoDownloader.app
```

**Option 3**: System Preferences
```
1. System Preferences → Security & Privacy
2. Click "Open Anyway" after first attempt
```

### Windows Workaround

**Option 1**: Click "More info"
```
1. Windows Defender SmartScreen appears
2. Click "More info"
3. Click "Run anyway"
```

**Option 2**: Unblock in Properties
```
1. Right-click VideoDownloader.exe
2. Properties → General
3. Check "Unblock"
4. Click OK
```

### Document in README

Add to your README:

```markdown
## Installation Security Warnings

### macOS
If you see "App can't be opened" warning:
1. Right-click the app → Select "Open"
2. Click "Open" in the dialog

### Windows
If you see SmartScreen warning:
1. Click "More info"
2. Click "Run anyway"

This is normal for unsigned applications. The app is safe!
```

---

## Cost Comparison

| Platform | Certificate Type | Annual Cost | Instant Reputation |
|----------|-----------------|-------------|-------------------|
| macOS | Developer Account | $99 | No |
| Windows | Standard Code Signing | $200-300 | No (takes time) |
| Windows | EV Code Signing | $300-500 | Yes |
| **Total** | Both platforms | **$300-600/year** | - |

---

## Recommendations

### For Personal/Free Distribution
- **Skip signing** initially
- Document workarounds clearly
- Add security FAQ to website
- Build trust through:
  - Open source code
  - GitHub verification
  - User reviews

### For Commercial Distribution
- **Invest in signing**
- Start with macOS Developer ($99)
- Add Windows EV cert if sales justify ($300+)
- Professional appearance = more downloads

### For Open Source Projects
- **Apply for free signing**
- macOS: Contact Apple Developer Relations
- Windows: Look into SignPath (free for OSS)
- Document build process

---

## Testing Signed Apps

### macOS
```bash
# Verify signature
codesign --verify --deep --strict VideoDownloader.app

# Check certificate
codesign -dv --verbose=4 VideoDownloader.app

# Verify notarization
spctl -a -vvv -t install VideoDownloader.app

# Check stapling
stapler validate VideoDownloader.app
```

### Windows
```powershell
# Verify signature
signtool verify /pa VideoDownloader.exe

# View certificate details
signtool verify /v /pa VideoDownloader.exe
```

---

## Troubleshooting

### macOS: "Code object is not signed at all"
```bash
# Re-sign with correct identity
codesign --force --deep --sign "Developer ID Application: ..." VideoDownloader.app
```

### macOS: "Notarization failed"
```bash
# Check logs
xcrun notarytool log <submission-id> --apple-id your@email.com

# Common issues:
# - Hardened runtime not enabled
# - Entitlements missing
# - Info.plist issues
```

### Windows: "SignTool not found"
```powershell
# Find SignTool
where signtool

# If not found, install Windows SDK
# Or use full path:
"C:\Program Files (x86)\Windows Kits\10\bin\x64\signtool.exe"
```

---

## Conclusion

**Without Signing**: App works but requires user workarounds
**With Signing**: Professional, seamless experience

**Start Without Signing**:
- Document workarounds
- Build user base
- Gather feedback

**Add Signing Later**:
- When revenue justifies cost
- For professional distribution
- To improve conversion rate

---

**For most developers starting out: Skip signing, focus on features!**

Your app is excellent - signing is just polish. 🎨
