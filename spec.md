# IntroDataScience Repository Specification

**Target Audience**: First-time coders learning data science  
**Location**: Johannesburg SA 2026 Trainings  
**Last Updated**: December 8, 2025

## Overview

This repository provides a beginner-friendly introduction to data science using modern Python tooling. The curriculum is designed to be digestible for first-time coders with hands-on examples, progressive exercises, and comprehensive tool documentation.

## Tech Stack

- **Python**: Core programming language
- **VS Code**: Development environment
- **UV**: Fast Python package manager
- **Marimo**: Reactive notebook environment
- **Polars**: High-performance data wrangling
- **Plotly**: Interactive data visualization
- **GitHub Copilot**: AI-assisted coding companion

---

## Directory Structure

```
IntroDataScience/
├── README.md                          # Main entry point with learning path
├── spec.md                            # This specification document
├── pyproject.toml                     # UV project configuration
├── .python-version                    # Python version specification
├── .gitignore                         # Git ignore patterns
│
├── docs/                              # Tool-specific documentation
│   ├── setup-guide.md                 # Complete environment setup
│   ├── uv-package-management.md       # UV package manager guide
│   ├── marimo-notebooks.md            # Marimo notebook basics
│   ├── polars-data-wrangling.md       # Polars fundamentals
│   ├── plotly-visualization.md        # Plotly plotting guide
│   └── copilot-assisted-coding.md     # Coding with GitHub Copilot
│
├── example_notebooks/                 # Progressive learning notebooks
│   ├── 01_python_basics.py            # Python fundamentals (Marimo)
│   ├── 02_data_wrangling.py           # Polars basics and operations
│   └── 03_plotting.py                 # Plotly visualizations
│
├── data/                              # Sample datasets
│   ├── raw/                           # Original unprocessed data
│   │   ├── students.csv               # Student records dataset
│   │   ├── sales.json                 # Sales transactions dataset
│   │   └── weather.parquet            # Weather observations dataset
│   ├── processed/                     # Cleaned/transformed data
│   └── README.md                      # Data dictionary and sources
│
├── exercises/                         # Practice exercises
│   ├── ex01_fundamentals.py           # Python basics practice
│   ├── ex02_wrangle_and_plot.py       # Data wrangling + plotting practice
│   └── ex03_mini_project.py           # Small end-to-end analysis project
│
├── solutions/                         # Exercise solutions
│   ├── ex01_fundamentals.py           # Solutions for fundamentals
│   ├── ex02_wrangle_and_plot.py       # Solutions for wrangle and plot
│   └── ex03_mini_project.py           # Solutions for mini project
│
└──
```

---

## Detailed File Specifications

### Root Level Files

#### `README.md`

**Purpose**: Main entry point for learners  
**Content Structure**:

- Welcome section introducing the course and goals
- Prerequisites (none! designed for beginners)
- Quick start guide (5-minute setup)
- Learning path overview with estimated time per section
- Technology stack overview with links to docs
- How to get help and contribute
- Links to all tool-specific documentation
- Progress tracking checklist

**Tone**: Friendly, encouraging, non-technical language

#### `pyproject.toml`

**Purpose**: UV project configuration  
**Contains**:

- Project metadata (name, version, description)
- Python version requirement (3.11+)
- Dependencies: `marimo`, `polars`, `plotly`, `jupyter` (for compatibility)
- Dev dependencies: `ruff` (linting), `pytest` (testing)
- UV-specific configuration settings

#### `.python-version`

**Purpose**: Specify Python version for UV  
**Content**: `3.11` or `3.12`

#### `.gitignore`

**Purpose**: Exclude unnecessary files from version control  
**Includes**:

- Python cache files (`__pycache__`, `*.pyc`)
- Virtual environments (`venv/`, `.venv/`)
- Marimo cache (`.marimo/`)
- IDE settings (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Data output files (`*.log`, `*.tmp`)

---

### `/docs` Directory

#### `setup-guide.md`

**Purpose**: Complete environment setup walkthrough  
**Sections**:

1. Installing VS Code (with download links)
2. Installing UV package manager (OS-specific instructions)
3. Cloning the repository
4. Creating the project environment with UV
5. Installing dependencies
6. Verifying installation
7. Launching your first Marimo notebook
8. VS Code extensions to install (Python, Marimo, Copilot)
9. Troubleshooting common issues

**Format**: Step-by-step with numbered instructions, code blocks, and expected output examples

#### `uv-package-management.md`

**Purpose**: Understanding UV for dependency management  
**Sections**:

1. What is UV and why use it? (speed, reliability)
2. Basic commands:
   - `uv init` - Initialize a project
   - `uv add <package>` - Add a dependency
   - `uv remove <package>` - Remove a dependency
   - `uv sync` - Sync dependencies
   - `uv run <command>` - Run scripts
3. Understanding `pyproject.toml`
4. Managing multiple Python versions
5. Virtual environments with UV
6. Common workflows (adding packages, updating)
7. Comparison to pip/conda (for context)

**Format**: Command reference with examples, use cases, and explanations

#### `marimo-notebooks.md`

**Purpose**: Introduction to Marimo reactive notebooks  
**Sections**:

1. What is Marimo? (reactive Python notebooks)
2. Why Marimo vs. Jupyter? (reproducibility, reactivity, Git-friendly)
3. Starting Marimo: `uv run marimo edit notebook.py`
4. Marimo UI overview (cell structure, sidebar, output)
5. Creating and running cells
6. Reactive execution model (cells auto-update)
7. Exporting notebooks to HTML/static sites
8. Best practices for organizing code in cells
9. Sharing and version control (it's just Python!)
10. Interactive widgets and sliders

**Format**: Tutorial style with screenshots (placeholders noted), code examples

#### `polars-data-wrangling.md`

**Purpose**: Data manipulation with Polars  
**Sections**:

1. What is Polars? (fast DataFrame library)
2. Why Polars? (speed, memory efficiency, expressive API)
3. Reading data: `pl.read_csv()`, `pl.read_json()`, `pl.read_parquet()`
4. DataFrame basics:
   - Structure and schema
   - Selecting columns
   - Filtering rows
   - Sorting data
5. Data transformations:
   - Adding/modifying columns with `with_columns()`
   - Grouping and aggregation with `group_by()`
   - Joining DataFrames
6. Expression syntax (lazy evaluation)
7. Common operations cheat sheet
8. Polars vs Pandas (comparison for reference)
9. Performance tips

**Format**: Concept + code example pattern, building complexity progressively

#### `plotly-visualization.md`

**Purpose**: Creating interactive visualizations  
**Sections**:

1. What is Plotly? (interactive plotting library)
2. Plotly Express vs Plotly Graph Objects
3. Basic plot types:
   - Line charts: `px.line()`
   - Bar charts: `px.bar()`
   - Scatter plots: `px.scatter()`
   - Histograms: `px.histogram()`
4. Customization:
   - Colors and themes
   - Labels and titles
   - Legends and annotations
5. Interactive features (hover, zoom, pan)
6. Subplots and multiple charts
7. Integrating with Polars DataFrames
8. Exporting plots (HTML, PNG)
9. Gallery of examples

**Format**: Visual guide with code snippets and rendered plot examples (placeholders)

#### `copilot-assisted-coding.md`

**Purpose**: Learning to code with AI assistance  
**Sections**:

1. What is GitHub Copilot?
2. Setting up Copilot in VS Code
3. How Copilot works (code suggestions, completion)
4. Effective prompting:
   - Writing clear comments
   - Descriptive function names
   - Breaking down problems
5. Copilot features:
   - Inline suggestions (Tab to accept)
   - Copilot Chat (asking questions)
   - Explaining code
   - Fixing errors
   - Generating tests
6. Best practices:
   - Review all suggestions
   - Learn from the code
   - Don't blindly accept
   - Use as a learning tool
7. Example workflow: Building a data analysis with Copilot
8. When to use Copilot vs. when to think independently
9. Ethical considerations (understanding your code)

**Format**: Practical guide with tips, examples, and learning strategies

---

### `/example_notebooks` Directory

All notebooks use **Marimo format** (`.py` files, not `.ipynb`). Each notebook is self-contained and focused on core concepts.

#### `01_python_basics.py`

**Purpose**: Essential Python fundamentals for data science  
**Estimated Time**: 20 minutes

**Topics**:

- Variables and data types (strings, numbers, booleans, lists, dictionaries)
- Basic operations (math, string methods)
- Control flow (if/else, for loops)
- Functions (defining, calling, parameters, return values)
- List comprehensions

**Structure**:

- 6-8 interactive cells
- Each cell demonstrates one core concept
- Includes quick practice examples
- Focus on what's needed for data work

**Learning Objectives**: Write basic Python code, understand data structures, use functions for data tasks

#### `02_data_wrangling.py`

**Purpose**: Data manipulation with Polars  
**Estimated Time**: 20 minutes

**Topics**:

- Loading data (CSV, JSON, Parquet) with `pl.read_csv()`, `pl.read_json()`, `pl.read_parquet()`
- Exploring DataFrames (head, shape, columns, describe, schema)
- Selecting columns and filtering rows
- Creating new columns with `with_columns()`
- Grouping and aggregation with `group_by()`
- Sorting data
- Handling missing values
- Joining DataFrames

**Data Used**: `students.csv`, `sales.json`

**Structure**:

- 10-12 cells covering essential operations
- Progressive examples from simple to complex
- Real-world data wrangling patterns
- Focus on practical techniques

**Learning Objectives**: Load and clean data, transform DataFrames, combine datasets, prepare data for analysis

#### `03_plotting.py`

**Purpose**: Creating visualizations with Plotly  
**Estimated Time**: 20 minutes

**Topics**:

- Line charts with `px.line()` (time series)
- Bar charts with `px.bar()` (categorical data)
- Scatter plots with `px.scatter()` (relationships)
- Histograms with `px.histogram()` (distributions)
- Customizing (colors, labels, titles, themes)
- Interactive features (hover, zoom)
- Subplots for multiple charts

**Data Used**: `weather.parquet`, `sales.json`

**Structure**:

- 8-10 cells covering main chart types
- Create and customize approach
- Integration with Polars DataFrames
- Focus on telling stories with data

**Learning Objectives**: Create effective visualizations, customize plots for clarity, choose appropriate chart types

---

### `/data` Directory

#### `data/raw/` - Original Datasets

##### `students.csv`

**Description**: Student enrollment and performance data  
**Rows**: ~150 students  
**Columns**:

- `student_id` (int): Unique identifier
- `name` (string): Student name
- `age` (int): Age in years
- `grade_level` (int): Grade (8-12)
- `subject` (string): Primary subject
- `test_score` (float): Score out of 100
- `attendance_rate` (float): Percentage 0-100
- `enrollment_date` (date): Date enrolled

**Purpose**: Practice basic filtering, sorting, aggregation  
**Data Quality**: Clean with a few intentional missing values in `test_score`

##### `sales.json`

**Description**: E-commerce sales transactions  
**Format**: JSON array of objects  
**Rows**: ~500 transactions  
**Fields**:

- `transaction_id` (string): Unique ID
- `date` (string): ISO date format
- `customer_id` (string): Customer identifier
- `product_category` (string): Category name
- `product_name` (string): Product name
- `quantity` (int): Items purchased
- `unit_price` (float): Price per unit
- `total_amount` (float): Total sale amount
- `payment_method` (string): Payment type
- `region` (string): Geographic region

**Purpose**: Practice JSON loading, grouping, time series, joining  
**Data Quality**: Real-world messiness - some null values, inconsistent capitalization

##### `weather.parquet`

**Description**: Daily weather observations  
**Rows**: ~365 days (one year)  
**Columns**:

- `date` (date): Observation date
- `temperature_high` (float): High temp °C
- `temperature_low` (float): Low temp °C
- `precipitation` (float): Rainfall in mm
- `humidity` (int): Humidity percentage
- `wind_speed` (float): Wind speed km/h
- `condition` (string): Weather description

**Purpose**: Practice Parquet files, time series, visualization  
**Data Quality**: Complete, realistic weather patterns

#### `data/processed/`

**Description**: Cleaned or transformed datasets created during analysis  
**Purpose**: Demonstrate data pipeline outputs  
**Contents**: Generated by notebooks, not committed to git (in .gitignore)

#### `data/README.md`

**Purpose**: Data dictionary and documentation  
**Sections**:

- Overview of each dataset
- Column descriptions and data types
- Data sources (synthetic/generated for educational use)
- Known issues and limitations
- Suggested analyses for each dataset
- Terms of use (open for educational purposes)

---

### `/exercises` Directory

Exercises are structured as Marimo notebooks (`.py` files) with TODO comments and starter code.

#### `exercises/ex01_fundamentals.py`

**Purpose**: Practice Python basics  
**Format**: Marimo notebook with 8-10 exercises
**Estimated Time**: 30 minutes

**Topics Covered**:

1. Variables and basic operations (3 exercises)
2. Lists and dictionaries (2 exercises)
3. Control flow - loops and conditionals (2 exercises)
4. Functions (2-3 exercises)

**Difficulty**: ⭐ Easy  
**Data Used**: None (pure Python practice)  
**Hints Provided**: Yes, with clear TODO instructions

**Learning Objectives**:

- Write basic Python code confidently
- Work with essential data structures
- Create simple functions

#### `exercises/ex02_wrangle_and_plot.py`

**Purpose**: Practice data wrangling and visualization together  
**Format**: Marimo notebook with 10-12 exercises
**Estimated Time**: 30 minutes

**Topics Covered**:

1. **Data Wrangling** (6-7 exercises)

   - Load CSV and JSON data
   - Filter and select data
   - Create new columns
   - Group and aggregate
   - Handle missing values
   - Join two datasets

2. **Plotting** (5-6 exercises)
   - Create line chart from data
   - Create bar chart for categories
   - Create scatter plot
   - Customize colors and labels
   - Create subplot with 2 charts

**Difficulty**: ⭐⭐ Medium  
**Data Used**: `students.csv`, `weather.parquet`  
**Hints Provided**: Moderate, with pointers to documentation

**Learning Objectives**:

- Manipulate real datasets with Polars
- Create meaningful visualizations
- Connect data wrangling to visual output

#### `exercises/ex03_mini_project.py`

**Purpose**: Complete a small end-to-end analysis  
**Format**: Marimo notebook with structured project template
**Estimated Time**: 60 minutes

**Project Brief**:
Analyze sales data to answer business questions:

1. Which product categories sell best?
2. What are the sales trends over time?
3. Which regions have the highest revenue?

**Structure**:

1. **Introduction** (provided) - Project goals and questions
2. **Load Data** (TODO) - Read `sales.json`
3. **Explore** (TODO) - Basic exploration and data quality checks
4. **Transform** (TODO) - Create calculated fields, filter, aggregate
5. **Visualize** (TODO) - Create 3 charts to answer questions
6. **Conclusions** (TODO) - Write brief findings

**Difficulty**: ⭐⭐⭐ Moderate Challenge  
**Data Used**: `sales.json`  
**Hints Provided**: Minimal - structured template with section guidance only

**Learning Objectives**:

- Execute full analysis workflow
- Make decisions about data processing
- Answer questions with data and visualizations
- Present findings clearly

---

### `/solutions` Directory

**Structure**: Mirrors `/exercises` directory with three solution files  
**Format**: Complete, working Marimo notebooks with detailed comments

**Files**:

- `ex01_fundamentals.py` - Complete solutions for Python basics
- `ex02_wrangle_and_plot.py` - Complete solutions for wrangling and plotting
- `ex03_mini_project.py` - One complete solution for the mini project

**Content Standards**:

- Fully commented code explaining logic
- Best practices demonstrated
- Clear, idiomatic code
- Links to relevant documentation

**Access Strategy**:

- README note: "Try exercises first! Solutions are for learning and reference."
- Consider separate branch for classroom settings

---

## Main `README.md` Structure

The main README serves as the landing page and navigation hub for learners.

### Sections

#### 1. Hero Section

- Repository title and tagline
- Brief description (2-3 sentences)
- Target audience clarification
- Key outcomes learners will achieve

#### 2. Why This Course?

- Modern tools used in industry (2024+)
- Beginner-friendly approach
- Hands-on from day one
- Portfolio-building projects
- AI-assisted learning with Copilot

#### 3. Prerequisites

- **Required**: None! Complete beginners welcome
- **Helpful but not required**: Basic computer literacy
- **Equipment needed**: Computer with internet (Mac/Windows/Linux)

#### 4. Quick Start (5 Minutes)

Step-by-step instructions to get running:

1. Install VS Code (link)
2. Install UV (one command)
3. Clone this repository
4. Run setup: `uv sync`
5. Launch first notebook: `uv run marimo edit example_notebooks/01_python_basics.py`
6. Link to detailed setup guide

#### 5. Learning Path

Visual representation (diagram or table) of the curriculum:

**Setup** (30 minutes)

- Install VS Code and UV
- Clone repository and sync dependencies
- Launch first notebook

**Phase 1: Learn the Basics** (1 hours)

- Notebook 1: Python Basics (20 min)
- Notebook 2: Data Wrangling with Polars (20 min)
- Notebook 3: Plotting with Plotly (20 min)

**Phase 2: Practice** (2 hours)

- Exercise 1: Python Fundamentals (30 min)
- Exercise 2: Wrangle and Plot (30 min)
- Exercise 3: Mini Project (60 min)

**Phase 3: Share Your Work** (30 minutes)

- Review solutions
- Disscussion

**Total Time**: ~4 hours

#### 6. Technology Stack

Brief overview with links to detailed guides:

- **[Python](docs/setup-guide.md)** - Programming language
- **[UV](docs/uv-package-management.md)** - Package manager ⚡ Fast!
- **[Marimo](docs/marimo-notebooks.md)** - Reactive notebooks 📓
- **[Polars](docs/polars-data-wrangling.md)** - Data wrangling 🐻‍❄️ Blazing fast!
- **[Plotly](docs/plotly-visualization.md)** - Interactive plots 📊
- **[GitHub Copilot](docs/copilot-assisted-coding.md)** - AI coding assistant 🤖

Each bullet links to respective `/docs/*.md` file

#### 7. Repository Structure

```
📦 IntroDataScience/
├── 📓 example_notebooks/ - Learning notebooks (start here!)
├── 📚 docs/              - Tool guides and documentation
├── 📊 data/              - Sample datasets
├── ✏️ exercises/         - Practice problems (3 progressive files)
└── ✅ solutions/         - Exercise solutions (try first!)
```

#### 8. Getting Help

- How to read error messages
- Copilot Chat for coding help

#### 9. Progress Tracking

Checklist format:

**Setup**

- [ ] Install VS Code and extensions
- [ ] Install UV and dependencies
- [ ] Run first notebook successfully

**Learn (Example Notebooks)**

- [ ] 01: Python Basics (20 min)
- [ ] 02: Data Wrangling (20 min)
- [ ] 03: Plotting (20 min)

**Practice (Exercises)**

- [ ] Exercise 1: Fundamentals (30 min)
- [ ] Exercise 2: Wrangle and Plot (30 min)
- [ ] Exercise 3: Mini Project (60 min)

**You're Done! 🎉**

- [ ] Share your mini project
- [ ] Keep learning with your own data

---

## Implementation Guidelines

### Code Style Standards

- **Python**: Follow PEP 8
- **Comments**: Explain "why" not just "what"
- **Variable names**: Descriptive and clear (`student_scores` not `ss`)
- **Function names**: Verb-based (`calculate_average` not `average`)

### Documentation Standards

- **Markdown**: Use proper headings hierarchy
- **Code blocks**: Always specify language for syntax highlighting
- **Links**: Descriptive text, not "click here"
- **Examples**: Always include expected output

### Notebook Standards (Marimo)

- **Cell order**: Logical progression, top to bottom
- **Cell length**: Keep cells focused (one concept per cell)
- **Markdown cells**: Use for narrative and section headers
- **Interactivity**: Use sliders/widgets where appropriate
- **Reproducibility**: All cells should run without errors

### Dataset Standards

- **Size**: Keep files under 1MB each (CSV/JSON ~500 rows, Parquet efficient)
- **Quality**: Intentionally include common data issues for learning
- **Realism**: Use realistic but synthetic data (no real PII)
- **Documentation**: Every dataset fully documented in data/README.md

### Exercise Standards

- **Progressive difficulty**: Each exercise slightly harder than previous
- **Starter code**: Provide structure, not full solution
- **TODO comments**: Clear instructions for what learners should do
- **Tests**: Where appropriate, include simple assertions to check answers
- **Time estimates**: Realistic for target audience

---

## Development Roadmap

### Phase 1: Repository Structure ✅

- Create directory structure
- Add .gitignore and base config files
- Initialize with UV

### Phase 2: Documentation 📝

- Write all `/docs/*.md` files
- Create main README.md
- Add data dictionary

### Phase 3: Datasets 📊

- Generate/curate sample datasets
- Validate data quality
- Document all datasets

### Phase 4: Notebooks 📓

- Create 3 focused learning notebooks
- Test all code for correctness
- Add interactivity with Marimo features
- Keep content concise and practical

### Phase 5: Exercises ✏️

- Write 3 exercise notebooks
- Create corresponding solutions
- Test time estimates (30-45 min each)

---

## Notes for Instructors

- **Pacing**: 4-hour workshop format with breaks
  - 30 min: Setup and introductions
  - 1 hours: Work through notebooks together
  - 2 hours: Guided exercise time
  - 30 min: Share mini projects and wrap-up
- **Teaching Approach**: Live coding along with notebooks
- **Assessments**: Review completed mini projects (Exercise 3)
- **Engagement**: Encourage pair programming on exercises

---

**End of Specification Document**

_This document is a living specification and will be updated as the repository evolves._
