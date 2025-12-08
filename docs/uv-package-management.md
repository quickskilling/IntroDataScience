# UV Package Management

Learn how to use UV, the fast Python package manager.

---

## 1. What is UV and Why Use It?

UV is a modern Python package manager written in Rust that's designed to be fast and reliable.

### Why UV?

**Speed ⚡**

- 10-100x faster than pip
- Installs packages in seconds, not minutes
- Parallel downloads and installations

**Reliability 🔒**

- Reproducible builds every time
- Automatic dependency resolution
- Clear error messages

**Simplicity 🎯**

- One tool for everything: packages, Python versions, virtual environments
- Works seamlessly with `pyproject.toml`
- No need for `pip`, `venv`, `pyenv` separately

### UV vs Traditional Tools

| Task          | Traditional                         | UV                        |
| ------------- | ----------------------------------- | ------------------------- |
| Create venv   | `python -m venv .venv`              | Automatic                 |
| Activate venv | `source .venv/bin/activate`         | Not needed                |
| Install deps  | `pip install -r requirements.txt`   | `uv sync`                 |
| Add package   | `pip install package && pip freeze` | `uv add package`          |
| Run script    | `python script.py`                  | `uv run python script.py` |

---

## 2. Basic Commands

### Initialize a New Project

```bash
uv init my-project
cd my-project
```

This creates:

- `pyproject.toml` - Project configuration
- `.python-version` - Python version specification
- `README.md` - Project readme

### Install/Sync Dependencies

```bash
uv sync
```

**What it does:**

- Reads `pyproject.toml`
- Creates/updates `.venv/` virtual environment
- Installs all dependencies
- Locks versions in `uv.lock`

**When to use:**

- First time setting up the project
- After cloning a repository
- After someone else updates dependencies
- If you delete `.venv/` folder

### Add a Package

```bash
uv add package-name
```

**Examples:**

```bash
uv add numpy              # Add latest version
uv add numpy >=2.0.0      # Add with version constraint
uv add numpy --dev     # Add as dev dependency
```

**What happens:**

- Package is downloaded and installed
- `pyproject.toml` is updated automatically
- Dependencies are resolved
- `uv.lock` is updated

### Remove a Package

```bash
uv remove package-name
```

**Example:**

```bash
uv remove numpy
```

**What happens:**

- Package is uninstalled
- Removed from `pyproject.toml`
- `uv.lock` is updated

### Run Python Scripts

```bash
uv run python script.py
```

**Why use `uv run`?**

- Automatically uses the virtual environment
- No need to activate/deactivate
- Works consistently across all platforms
- Ensures correct Python version

**Examples:**

```bash
uv run python analysis.py
uv run python -c "import polars; print(polars.__version__)"
uv run marimo edit notebook.py
```

---

## 3. Understanding `pyproject.toml`

The `pyproject.toml` file is the heart of your project configuration.

### Basic Structure

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
requires-python = ">=3.12"

dependencies = [
    "marimo>=0.9.0",
    "polars>=0.20.0",
    "plotly>=5.18.0",
]
```

### Sections Explained

**`[project]`** - Project metadata

- `name`: Your project name (lowercase, hyphens)
- `version`: Current version (semantic versioning)
- `description`: Short description
- `requires-python`: Minimum Python version

**`dependencies`** - Production packages

- Packages needed to run your code
- Format: `"package>=version"`
- Version constraints: `>=`, `<=`, `==`, `~=`

**`[project.optional-dependencies]`** - Optional packages

- `dev`: Development tools (linting, testing)
- `docs`: Documentation tools
- Custom groups for different use cases

### Version Constraints

```toml
dependencies = [
    "polars>=0.20.0",     # At least 0.20.0
    "plotly~=5.18.0",     # Compatible with 5.18.x
    "requests==2.31.0",   # Exactly 2.31.0
    "numpy>=1.24,<2.0",   # Between 1.24 and 2.0
]
```

**Recommendations:**

- Use `>=` for most packages (get bug fixes)
- Use `~=` when you need stability
- Use `==` only when absolutely necessary

---

## 4. Managing Multiple Python Versions

UV can manage Python installations for you!

### List Available Python Versions

```bash
uv python list
```

### Install a Specific Python Version

```bash
uv python install 3.12
uv python install 3.11
```

### Use a Specific Version for Your Project

Edit `pyproject.toml`:

```toml
[project]
requires-python = ">=3.12"
```

Or create `.python-version`:

```
3.12
```

UV will automatically use this version when you run `uv sync` or `uv run`.

---

## 5. Virtual Environments with UV

UV manages virtual environments automatically, but here's what's happening:

### Automatic Creation

When you run `uv sync`, UV creates `.venv/` in your project directory.

### Where is Everything?

```
IntroDataScience/
├── .venv/                # Virtual environment (auto-created)
│   ├── bin/             # Executables (python, pip, marimo)
│   ├── lib/             # Installed packages
│   └── pyvenv.cfg       # Configuration
├── pyproject.toml        # Your configuration
└── uv.lock              # Locked versions (auto-generated)
```

### Manual Virtual Environment Commands

Usually not needed, but available:

```bash
# Create new venv
uv venv

# Create with specific Python version
uv venv --python 3.12

# Create in custom location
uv venv /path/to/venv
```

---

## 6. Common Workflows

### Starting a New Project

```bash
uv init my-data-project
cd my-data-project
uv add polars plotly marimo
uv run marimo edit analysis.py
```

### Adding a Package Mid-Project

```bash
# Need seaborn for visualization
uv add seaborn

# Use it immediately
uv run python
>>> import seaborn
```

### Updating Dependencies

```bash
# Update all packages to latest compatible versions
uv sync --upgrade

# Update specific package
uv add package@latest
```

### Checking What's Installed

```bash
# List all installed packages
uv pip list

# Show dependency tree
uv pip show package-name

# Check for outdated packages
uv pip list --outdated
```

### Sharing Your Project

**To share:**

1. Commit `pyproject.toml` to git
2. Commit `uv.lock` to git (ensures same versions)
3. Don't commit `.venv/` (add to `.gitignore`)

**For others to use:**

```bash
git clone your-repo
cd your-repo
uv sync  # That's it!
```

### Creating a Requirements File (if needed)

Some tools still need `requirements.txt`:

```bash
uv pip freeze > requirements.txt
```

---

## 7. Comparison to pip/conda

### Coming from pip?

| pip Command                       | UV Equivalent    | Notes                       |
| --------------------------------- | ---------------- | --------------------------- |
| `pip install package`             | `uv add package` | Also updates pyproject.toml |
| `pip install -r requirements.txt` | `uv sync`        | Uses pyproject.toml         |
| `pip list`                        | `uv pip list`    | Same output                 |
| `pip freeze`                      | `uv pip freeze`  | Same output                 |
| `python -m venv .venv`            | `uv sync`        | Automatic                   |
| `source .venv/bin/activate`       | Use `uv run`     | No activation needed        |

### Coming from conda?

| conda Command           | UV Equivalent    | Notes                |
| ----------------------- | ---------------- | -------------------- |
| `conda create -n env`   | `uv sync`        | Automatic            |
| `conda activate env`    | Use `uv run`     | No activation needed |
| `conda install package` | `uv add package` |                      |
| `conda env export`      | `pyproject.toml` | Version controlled   |

**Key Difference:**

- Conda manages system libraries (C, R, etc.)
- UV focuses purely on Python
- UV is faster for Python-only projects

---

## Advanced Tips

### Working Offline

UV caches everything:

```bash
# Build cache
uv sync

# Later, work offline
uv sync --offline
```

### Cleaning Cache

```bash
# Clear download cache
uv cache clean

# See cache location
uv cache dir
```

### Custom Index (Corporate Networks)

```toml
[[tool.uv.index]]
url = "https://your-company-pypi.com/simple"
```

### Lock File

`uv.lock` contains exact versions of all dependencies:

- Always commit this file
- Ensures reproducible builds
- Update with `uv sync --upgrade`

---

## Quick Reference Card

```bash
# Project setup
uv init project-name        # New project
uv sync                     # Install dependencies

# Package management
uv add package-name         # Add package
uv remove package-name      # Remove package
uv add package --dev        # Add dev dependency

# Running code
uv run python script.py     # Run script
uv run marimo edit nb.py    # Run marimo notebook

# Information
uv pip list                 # List installed packages
uv python list              # List available Python versions
uv --version                # Check UV version

# Maintenance
uv sync --upgrade           # Update all packages
uv cache clean              # Clear cache
```

---

## Getting Help

```bash
# General help
uv --help

# Command-specific help
uv add --help
uv sync --help
uv run --help
```

**Official Documentation:**

- [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## Next Steps

- Read [Marimo Notebooks](./marimo-notebooks.md) to start coding
- Check [Setup Guide](./setup-guide.md) if you haven't installed UV yet
- See [Polars Data Wrangling](./polars-data-wrangling.md) for data manipulation

---

**UV makes Python package management simple and fast. Once you try it, you won't want to go back! 🚀**
