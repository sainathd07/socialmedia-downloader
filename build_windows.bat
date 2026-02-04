@echo off
REM Build script for Video Downloader on Windows

echo ================================
echo Video Downloader Build Script
echo ================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/upgrade dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
echo Dependencies installed
echo.

REM Run tests
echo Running tests...
pytest tests\ -v
echo Tests passed
echo.

REM Build application
echo Building Windows application...
pyinstaller build_windows.spec --clean
echo Windows build complete!
echo Application: dist\VideoDownloader.exe

echo.
echo ================================
echo Build Complete!
echo ================================
pause
