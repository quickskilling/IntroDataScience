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

4. **Sync dependencies**

   ```bash
   uv sync
   ```

5. **Launch your first notebook**
   ```bash
   uv run marimo edit example_notebooks/01_python_basics.py
   ```

📖 **Need more help?** Check out the [detailed setup guide](docs/setup-guide.md)

---

## 📚 Learning Path

### Setup (15 minutes)

✓ Install VS Code and UV  
✓ Clone repository and sync dependencies  
✓ Launch first notebook

### Phase 1: Learn the Basics (2.5 hours)

**📓 Notebook 1: Python Basics** (45 min)

- Variables, data types, and operations
- Lists and dictionaries
- Control flow (if/else, loops)
- Functions

**📓 Notebook 2: Data Wrangling** (60 min)

- Loading data (CSV, JSON, Parquet)
- Exploring DataFrames with Polars
- Filtering, selecting, and transforming data
- Grouping and aggregation
- Joining datasets

**📓 Notebook 3: Plotting** (45 min)

- Line charts and bar charts
- Scatter plots and histograms
- Customizing visualizations
- Interactive features

### Phase 2: Practice (2.5 hours)

**✏️ Exercise 1: Fundamentals** (30 min)

- Practice Python basics
- 8-10 hands-on exercises

**✏️ Exercise 2: Wrangle and Plot** (60 min)

- Load and manipulate real datasets
- Create visualizations from data
- 10-12 practical exercises

**✏️ Exercise 3: Mini Project** (60 min)

- Complete end-to-end sales analysis
- Answer business questions with data
- Build your first portfolio piece!

**Total Time**: ~4 hours (excluding setup)

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

- [ ] 01: Python Basics (45 min)
- [ ] 02: Data Wrangling (60 min)
- [ ] 03: Plotting (45 min)

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
- **Use GitHub Issues** - Ask questions or report problems
- **Ask GitHub Copilot** - If you have it installed, use Copilot Chat for help
- **Check the docs** - Each tool has a guide in the `/docs` folder

---

## 🤝 Contributing

Found a typo? Have a suggestion? We welcome contributions!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This course is released under the MIT License for educational purposes.

---

## 🙏 Acknowledgments

Built with amazing open-source tools:

- [Marimo](https://marimo.io/) - Reactive Python notebooks
- [Polars](https://pola.rs/) - Fast DataFrames
- [Plotly](https://plotly.com/) - Interactive visualizations
- [UV](https://astral.sh/uv) - Python package management

**Training developed for Johannesburg SA 2026**

---

## 📞 Contact & Support

**Issues**: [GitHub Issues](https://github.com/quickskilling/IntroDataScience/issues)  
**Discussions**: [GitHub Discussions](https://github.com/quickskilling/IntroDataScience/discussions)  
**Training Year**: 2026  
**Location**: Johannesburg, South Africa

---

**Ready to start?** Jump to [example_notebooks/01_python_basics.py](example_notebooks/01_python_basics.py) 🚀
