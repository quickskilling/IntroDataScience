# Setup Guide

Complete environment setup for the Intro to Data Science course.

---

## 1. Installing VS Code

VS Code is a free, powerful code editor that works on all operating systems.

**Download VS Code:**

- Visit: [https://code.visualstudio.com/](https://code.visualstudio.com/)
- Click the big download button for your operating system
- Run the installer and follow the prompts

**Verify Installation:**

1. Open VS Code
2. You should see a welcome screen
3. Close any welcome tabs

---

## 2. Installing UV Package Manager

UV is a fast Python package manager that makes dependency management simple.

### macOS/Linux

Open Terminal and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Verify installation:**

```bash
uv --version
```

You should see something like: `uv 0.5.0` or higher

### Windows

Open PowerShell and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify installation:**

```powershell
uv --version
```

### Troubleshooting UV Installation

If `uv --version` doesn't work:

- **macOS/Linux**: Restart your terminal or run `source ~/.bashrc` (or `~/.zshrc`)
- **Windows**: Restart PowerShell
- If still not working, check that UV is in your PATH

---

## 3. Cloning the Repository

### Option A: Using Git (Recommended)

If you don't have Git installed:

- **macOS**: Open Terminal and run `git --version` (it will prompt you to install)
- **Windows**: Download from [https://git-scm.com/](https://git-scm.com/)
- **Linux**: Run `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (RHEL/CentOS)

**Clone the repository:**

```bash
git clone https://github.com/quickskilling/IntroDataScience.git
cd IntroDataScience
```

### Option B: Download ZIP

1. Go to the GitHub repository
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file
5. Open Terminal/PowerShell and navigate to the extracted folder:

```bash
cd path/to/IntroDataScience
```

---

## 4. Creating the Project Environment with UV

UV will automatically create a virtual environment and manage Python for you.

**Navigate to the project directory** (if you haven't already):

```bash
cd IntroDataScience
```

**Check that you're in the right place:**

```bash
ls
```

You should see files like `pyproject.toml`, `README.md`, etc.

---

## 5. Installing Dependencies

Run this single command to install all course dependencies:

```bash
uv sync
```

**What's happening:**

- UV reads `pyproject.toml`
- Creates a virtual environment in `.venv/`
- Installs Python 3.12+ if needed
- Installs Marimo, Polars, and Plotly

**Expected output:**

```
Resolved 29 packages in 401ms
Prepared 4 packages in 4.75s
Installed 26 packages in 191ms
 + marimo==0.18.3
 + polars==1.36.0
 + plotly==6.5.0
 ...
```

This might take 1-2 minutes on first run.

---

## 6. Verifying Installation

Let's make sure everything works!

**Check Python version:**

```bash
uv run python --version
```

You should see: `Python 3.12.x` or higher

**Check installed packages:**

```bash
uv run python -c "import marimo, polars, plotly; print('✓ All packages imported successfully!')"
```

You should see: `✓ All packages imported successfully!`

---

## 7. Launching Your First Marimo Notebook

Time to see Marimo in action!

**Start the Python basics notebook:**

```bash
uv run marimo edit example_notebooks/01_python_basics.py
```

**What happens:**

1. A browser window opens automatically
2. You see the Marimo notebook interface
3. The notebook is ready to use!

**Expected output in terminal:**

```
marimo server is running at http://localhost:2718
```

**Try it:**

- Click on any code cell
- Edit the code
- Press `Shift + Enter` to run
- Watch other cells update automatically (reactive!)

**To stop the notebook:**

- Press `Ctrl + C` in the terminal
- Or close the terminal window

---

## 8. VS Code Extensions to Install

Enhance your coding experience with these extensions.

### Essential Extensions

1. **Python Extension**

   - Open VS Code
   - Click the Extensions icon (or press `Ctrl/Cmd + Shift + X`)
   - Search for "Python"
   - Install the one by Microsoft

2. **Marimo Extension** (Optional but recommended)

   - Search for "Marimo"
   - Install to get syntax highlighting for Marimo notebooks

3. **GitHub Copilot** (Optional)
   - Search for "GitHub Copilot"
   - Requires GitHub account
   - Free for students and verified teachers
   - See [copilot-assisted-coding.md](./copilot-assisted-coding.md) for setup

### Recommended Extensions

- **Even Better TOML**: Better syntax for `pyproject.toml`
- **Path Intellisense**: Auto-complete file paths
- **Error Lens**: Inline error messages

---

## 9. Troubleshooting Common Issues

### Issue: "uv: command not found"

**Solution:**

- Restart your terminal
- Or run: `source ~/.bashrc` (Linux) or `source ~/.zshrc` (macOS)
- Windows: Restart PowerShell

### Issue: "Python version too old"

UV will automatically install Python 3.12+, but if you see this error:

**Solution:**

```bash
uv python install 3.12
```

### Issue: "Failed to resolve packages"

**Solution:**

1. Check your internet connection
2. Try again: `uv sync`
3. Clear cache: `uv cache clean` then `uv sync`

### Issue: Marimo notebook won't open in browser

**Solution:**

1. Check the terminal output for the URL (usually `http://localhost:2718`)
2. Manually open that URL in your browser
3. Try a different port: `uv run marimo edit --port 8080 example_notebooks/01_python_basics.py`

### Issue: Import errors in notebooks

**Solution:**

- Always run notebooks with `uv run marimo edit notebook.py`
- This ensures you're using the virtual environment
- Don't use `python` directly; use `uv run python`

### Issue: "Permission denied" on macOS/Linux

**Solution:**

- Don't use `sudo` with UV
- If you did, run: `sudo chown -R $USER:$USER ~/.local/share/uv`

### Issue: Windows antivirus blocking installation

**Solution:**

- Temporarily disable antivirus during installation
- Add UV installation directory to exclusions
- Re-enable antivirus after installation

---

## Quick Command Reference

Once you're set up, here are the commands you'll use most:

```bash
# Start a notebook
uv run marimo edit example_notebooks/01_python_basics.py

# Run a Python script
uv run python script.py

# Install a new package
uv add package-name

# Update all dependencies
uv sync

# Check what's installed
uv pip list
```

---

## Next Steps

You're all set! Here's what to do next:

1. **Start learning**: Open `example_notebooks/01_python_basics.py`
2. **Read the main README**: Go back to [README.md](../README.md) for the learning path
3. **Explore the tools**: Check out other docs:
   - [UV Package Management](./uv-package-management.md)
   - [Marimo Notebooks](./marimo-notebooks.md)
   - [Polars Data Wrangling](./polars-data-wrangling.md)
   - [Plotly Visualization](./plotly-visualization.md)

---

## Getting Help

**Stuck?**

- Read error messages carefully - they usually tell you what's wrong
- Check the troubleshooting section above
- Ask in your course forum or chat
- Use GitHub Copilot Chat if you have it installed

**Remember:** Everyone gets stuck sometimes. That's part of learning! Keep trying, read error messages, and ask for help when needed.

---

**Happy Coding! 🎉**
