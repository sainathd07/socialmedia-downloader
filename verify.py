#!/usr/bin/env python3
"""
Quick verification script to check project structure and dependencies
Run this before building to ensure everything is properly set up
"""

import sys
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def check_mark(condition, message):
    """Print check mark or X based on condition"""
    if condition:
        print(f"{GREEN}✓{RESET} {message}")
        return True
    else:
        print(f"{RED}✗{RESET} {message}")
        return False

def warning(message):
    """Print warning message"""
    print(f"{YELLOW}⚠{RESET}  {message}")

print(f"\n{BOLD}Video Downloader - Project Verification{RESET}")
print("=" * 50)

# Check Python version
print(f"\n{BOLD}Python Environment:{RESET}")
py_version = sys.version_info
version_ok = py_version.major == 3 and py_version.minor >= 10
check_mark(version_ok, f"Python {py_version.major}.{py_version.minor}.{py_version.micro}")
if not version_ok:
    warning("Python 3.10 or higher recommended")

# Check project structure
print(f"\n{BOLD}Project Structure:{RESET}")
required_files = [
    "src/main.py",
    "src/core/downloader.py",
    "src/core/validator.py",
    "src/core/formats.py",
    "src/gui/app.py",
    "src/utils/settings.py",
    "src/utils/logger.py",
    "src/utils/helpers.py",
    "requirements.txt",
    "README.md",
]

all_files_exist = True
for file_path in required_files:
    exists = Path(file_path).exists()
    check_mark(exists, file_path)
    all_files_exist = all_files_exist and exists

# Check test files
print(f"\n{BOLD}Test Suite:{RESET}")
test_files = [
    "tests/test_validator.py",
    "tests/test_helpers.py",
    "tests/test_settings.py",
]

all_tests_exist = True
for test_file in test_files:
    exists = Path(test_file).exists()
    check_mark(exists, test_file)
    all_tests_exist = all_tests_exist and exists

# Check build files
print(f"\n{BOLD}Build Configuration:{RESET}")
build_files = [
    "build_macos.spec",
    "build_windows.spec",
    "build.sh",
    "run.sh",
]

for build_file in build_files:
    exists = Path(build_file).exists()
    check_mark(exists, build_file)

# Check dependencies
print(f"\n{BOLD}Dependencies:{RESET}")
try:
    import customtkinter
    check_mark(True, "customtkinter installed")
except ImportError:
    check_mark(False, "customtkinter (not installed)")
    warning("Run: pip install -r requirements.txt")

try:
    import yt_dlp
    check_mark(True, "yt-dlp installed")
except ImportError:
    check_mark(False, "yt-dlp (not installed)")
    warning("Run: pip install -r requirements.txt")

try:
    from PIL import Image
    check_mark(True, "Pillow installed")
except ImportError:
    check_mark(False, "Pillow (not installed)")
    warning("Run: pip install -r requirements.txt")

# Check optional dependencies
print(f"\n{BOLD}Optional Dependencies:{RESET}")
try:
    import pytest
    check_mark(True, "pytest installed (for testing)")
except ImportError:
    check_mark(False, "pytest (not installed)")
    warning("Run: pip install -r requirements-dev.txt")

# Summary
print(f"\n{BOLD}Summary:{RESET}")
print("=" * 50)

if all_files_exist and all_tests_exist:
    print(f"{GREEN}✓ Project structure is complete!{RESET}")
else:
    print(f"{RED}✗ Some files are missing{RESET}")

print(f"\n{BOLD}Next Steps:{RESET}")
print("1. Install dependencies: pip install -r requirements.txt")
print("2. Run the application: ./run.sh or python src/main.py")
print("3. Run tests: pytest tests/")
print("4. Build executable: ./build.sh")
print(f"\n{BOLD}Documentation:{RESET}")
print("- Quick start: QUICKSTART.md")
print("- User guide: USER_GUIDE.md")
print("- Development: DEVELOPMENT.md")
print("- Summary: PROJECT_SUMMARY.md")
print()
