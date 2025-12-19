# Introduction to Data Science 📊

> A beginner-friendly, hands-on introduction to modern data science tools and techniques

**For**: First-time coders learning data science  
**Location**: Johannesburg SA 2026 Trainings  
**Duration**: ~4 hours

---

## 🎯 What You'll Learn

By the end of this course, you'll be able to:

- Write Python code for data analysis
- Load and manipulate data with Polars
- Create interactive visualizations with Plotly
- Complete a full data analysis project
- Use AI tools (GitHub Copilot) to help you code

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites

- **Required**: None! This course is designed for complete beginners
- **Equipment**: Computer with internet (Mac, Windows, or Linux)

### Setup Steps

1. **Install VS Code** (if you haven't already)

   - Download from [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install UV** (Python package manager)

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Clone this repository**

   ```bash
   git clone https://github.com/quickskilling/IntroDataScience.git
   cd IntroDataScience
   ```

4. **Add UV to PATH**

   ```bash
   # macOS/Linux
   source $HOME/.local/bin/env

   # Windows (PowerShell)
   # Should be added to PATH already, but in case
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Users\$env:USERNAME\.cargo\bin", "User")
   ```

5. **Verify UV Installation**
   ```bash
   uv --version
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

### Setup (30 minutes)

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
- Grouping and aggregation
- Joining datasets

**📓 Notebook 3: Plotting** (20 min)

- Line charts and bar charts
- Scatter plots and histograms
- Customizing visualizations
- Interactive features

### Phase 2: Practice (2 hours)

**✏️ Exercise 1: Fundamentals** (30 min)

- Practice Python basics
- 8-10 hands-on exercises

**✏️ Exercise 2: Wrangle and Plot** (30 min)

- Load and manipulate real datasets
- Create visualizations from data
- 10-12 practical exercises

**✏️ Exercise 3: Mini Project** (60 min)

- Complete end-to-end sales analysis
- Answer business questions with data
- Build your first portfolio piece!

**Total Time**: ~4 hours 

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
├── ✅ solutions/           → Exercise solutions (try first!)
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
- [ ] Install UV and dependencies
- [ ] Run first notebook successfully

### Learn (Example Notebooks)

- [ ] 01: Python Basics (20 min)
- [ ] 02: Data Wrangling (20 min)
- [ ] 03: Plotting (20 min)

### Practice (Exercises)

- [ ] Exercise 1: Fundamentals (30 min)
- [ ] Exercise 2: Wrangle and Plot (60 min)
- [ ] Exercise 3: Mini Project (60 min)

### You're Done! 🎉

- [ ] Share your mini project
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
