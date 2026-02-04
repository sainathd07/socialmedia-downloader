#!/bin/bash
# Build script for Video Downloader

set -e

echo "================================"
echo "Video Downloader Build Script"
echo "================================"
echo ""

# Detect platform
PLATFORM=$(uname)
echo "Platform detected: $PLATFORM"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements-dev.txt
echo "✓ Dependencies installed"
echo ""

# Run tests
echo "Running tests..."
pytest tests/ -v
echo "✓ Tests passed"
echo ""

# Build application
echo "Building application for $PLATFORM..."
if [ "$PLATFORM" = "Darwin" ]; then
    # macOS
    echo "Building macOS application..."
    pyinstaller build_macos.spec --clean
    echo "✓ macOS build complete!"
    echo "Application: dist/VideoDownloader.app"
elif [ "$PLATFORM" = "Linux" ]; then
    # Linux
    echo "Building Linux application..."
    pyinstaller build_windows.spec --clean --name VideoDownloader
    echo "✓ Linux build complete!"
    echo "Application: dist/VideoDownloader"
else
    echo "⚠️  Unsupported platform for this script. Please use build_windows.bat on Windows."
    exit 1
fi

echo ""
echo "================================"
echo "Build Complete!"
echo "================================"
