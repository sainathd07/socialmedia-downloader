# Installation Instructions for macOS

## Quick Install (Copy & Paste)

Run these commands in your terminal:

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate virtual environment
source venv/bin/activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python src/main.py
```

## Detailed Steps

### Step 1: Create Virtual Environment
```bash
python3 -m venv venv
```
This creates an isolated Python environment in the `venv` folder.

### Step 2: Activate Virtual Environment
```bash
source venv/bin/activate
```
You should see `(venv)` appear at the start of your terminal prompt.

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
**Note**: Inside the virtual environment, you use `pip` (not `pip3`).

### Step 4: Run the App
```bash
python src/main.py
```

## Common Issues

### "pip: command not found"
- **Outside venv**: Use `pip3` instead of `pip`
- **Inside venv**: Make sure you activated it with `source venv/bin/activate`

### "python: command not found"
- Use `python3` instead of `python`

### "requirements.tx not found"
- Make sure you type `requirements.txt` (with `.txt` extension)

## Verify Installation

After installing, verify everything works:

```bash
# Check Python version
python --version  # Should show Python 3.12.x

# Check installed packages
pip list

# Run verification script
python verify.py
```

## Quick Run Script

For convenience, just use:

```bash
./run.sh
```

This script automatically:
- Creates venv if needed
- Activates it
- Installs dependencies
- Runs the app

## Deactivate Virtual Environment

When you're done:

```bash
deactivate
```

---

**Next**: After installation, read `USER_GUIDE.md` to learn how to use the app.
