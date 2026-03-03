# Introduction to Data Science 📊

> A beginner-friendly, hands-on introduction to modern data science tools and techniques

**For**: First-time coders learning data science  
**Location**: Johannesburg SA 2026 Trainings  
**Duration**: ~3 hours

---
## What you'll learn (by the end of this class)
- Load and explore a dataset with Python
- Perform basic data cleaning and transformations with Polars
- Create simple visualizations with Plotly
- Use GitHub Copilot responsibly to speed up learning

## Dataset note
The datasets in this repository are provided for learning purposes.  

## Common setup issues (quick fixes)
- **`uv` command not found**: close and reopen your terminal after installing UV (or restart VS Code).
- **Install/Sync fails**: run `uv sync` again from the project folder (where `pyproject.toml` is).
- **Marimo won't start / port in use**: stop other running notebooks/apps, then rerun the start command.
- **Permission issues on Windows**: try running PowerShell as Administrator.
---

## 🚀 Quick Start (5 Minutes)

### Prerequisites

- **Required**: None! This course is designed for complete beginners
- **Equipment**: Computer with internet (Mac, Windows, or Linux)

### Setup Steps

1. **Install VS Code** (if you haven't already)

   - Download and Install VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
   - Install Marimo extension from [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
   


2. **Install UV and add to PATH** (Python package manager)

   ```bash
   # macOS/Linux (Ubuntu or Debian)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   source $HOME/.local/bin/env

   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Should be added to PATH already, but in case
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\.cargo\bin", "User")
   ```

   ```bash
   # Verify Installation
   uv --version
   ```

3. **Install Python with UV**
   ```bash
   uv python install
   ```

   ```bash
   # Verify Installation
   python --version
   ```


4. **Install Git and verify installation**
   ```bash
   # Windows (Powershell)
   winget install --id Git.Git -e --source winget
   
   # macOS
   brew install git

   # Linux (Ubuntu or Debian)
   apt-get install git
   ```

   ```bash
   # Verify Installation
   git --version
   ```


5. **Clone this repository**

   ```bash
   git clone https://github.com/quickskilling/IntroDataScience.git
   cd IntroDataScience
   ```

6. **Sync dependencies**

   ```bash
   uv sync
   ```

7. **Launch your first notebook**
   ```bash
   uv run marimo edit example_notebooks/01_python_basics.py
   ```

📖 **Need more help?** Check out the [detailed setup guide](docs/setup-guide.md)

---

## 📚 Learning Path

### Overview and Setup (40 minutes)

✓ Overview of Data Science and Tools
✓ Install VS Code and UV  
✓ Clone repository and sync dependencies  
✓ Launch first notebook

### Phase 1: Learn the Basics (1 hour)

**📓 Notebook 1: Python Basics** (20 min)

- Variables, data types, and operations
- Lists and dictionaries
- Control flow (if/else, loops)
- Functions

**📓 Notebook 2: Data Wrangling** (20 min)

- Loading data (CSV, JSON, Parquet)
- Exploring DataFrames with Polars
- Filtering, selecting, and transforming data
- Joining datasets

**📓 Notebook 3: Plotting** (20 min)

- Line charts and bar charts
- Scatter plots and histograms
- Customizing visualizations
- Subplots

### Phase 2: Practice (1 hour)

**✏️ Exercise 1: Fundamentals** (20 min)

- Practice Python basics
- 8-10 hands-on exercises

**✏️ Exercise 2: Basic Data Wrangling with Polars** (20 min)

- Load and manipulate real datasets
- Answer questions with data

**✏️ Exercise 3: Basic Plotting with Plotly** (20 min)

- Create visualizations from data
- Hands-on exercises

**Total Time**: ~3 hours 

---

## 🛠️ Technology Stack

Our modern, industry-standard tools:

- **[Python](docs/setup-guide.md)** - The most popular data science language
- **[UV](docs/uv-package-management.md)** ⚡ - Lightning-fast package manager
- **[Marimo](docs/marimo-notebooks.md)** 📓 - Reactive Python notebooks
- **[Polars](docs/polars-data-wrangling.md)** 🐻‍❄️ - Blazing-fast data manipulation
- **[Plotly](docs/plotly-visualization.md)** 📊 - Interactive visualizations
- **[GitHub Copilot](docs/copilot-assisted-coding.md)** 🤖 - AI coding assistant

---

## 📁 Repository Structure

```
📦 IntroDataScience/
├── 📓 example_notebooks/  → Learning notebooks (start here!)
│   ├── 01_python_basics.py
│   ├── 02_data_wrangling.py
│   └── 03_plotting.py
│
├── ✏️ exercises/           → Practice problems
│   ├── ex01_fundamentals.py
│   ├── ex02_wrangle_and_plot.py
│   └── ex03_mini_project.py
│
│
├── 📊 data/                → Sample datasets
│   └── raw/
│       ├── students.csv
│       ├── sales.json
│       └── weather.parquet
│
└── 📚 docs/                → Tool guides and documentation
```

---

## ✅ Progress Tracker

Track your journey through the course:

### Setup

- [ ] Install VS Code and extensions
- [ ] Install Python
- [ ] Install UV and dependencies
- [ ] Install Git and clone repository
- [ ] Run first notebook successfully

### Learn (Example Notebooks)

- [ ] 01: Python Basics (20 min)
- [ ] 02: Data Wrangling (20 min)
- [ ] 03: Plotting (20 min)

### Practice (Exercises)

- [ ] Exercise 1: Fundamentals (20 min)
- [ ] Exercise 2: Basic Data Wrangling with Polars (20 min)
- [ ] Exercise 3: Basic Plotting with Plotly (20 min)

### You're Done! 🎉

- [ ] Share your work
- [ ] Keep learning with your own data

---

## 💡 Getting Help

- **Read error messages carefully** - They often tell you exactly what's wrong!
- **Check the docs** - Each tool we use has a guide in the `/docs` folder
- **Ask your neighbor** - Pair programming can improve efficancy and help you learn
- **Ask GitHub Copilot** - If you have it installed, use Copilot Chat for help
- **Raise your hand** - A DataThink representative will be happy to help if you get stuck

---


**Ready to start?** Jump to [example_notebooks/01_python_basics.py](example_notebooks/01_python_basics.py) 🚀
