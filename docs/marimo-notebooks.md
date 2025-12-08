# Marimo Notebooks

Learn how to use Marimo, the reactive Python notebook.

---

## 1. What is Marimo?

Marimo is a reactive Python notebook that runs as pure Python files (`.py`), not JSON blobs (`.ipynb`).

### Key Features

**Reactive Execution 🔄**

- When you change one cell, dependent cells update automatically
- No more stale outputs
- No more "run all cells" button

**Pure Python Files 📄**

- Notebooks are regular `.py` files
- Work with any Python tool
- Perfect for version control (Git)
- No merge conflicts

**Reproducible 🎯**

- Always runs top-to-bottom
- No hidden state
- Share with confidence

**Interactive 🎨**

- Built-in UI widgets (sliders, dropdowns)
- Interactive plots
- Real-time updates

---

## 2. Why Marimo vs. Jupyter?

### Marimo Advantages

| Feature         | Jupyter             | Marimo                 |
| --------------- | ------------------- | ---------------------- |
| File format     | `.ipynb` (JSON)     | `.py` (Python)         |
| Git-friendly    | ❌ Messy diffs      | ✅ Clean diffs         |
| Reactivity      | ❌ Manual re-runs   | ✅ Automatic updates   |
| Hidden state    | ⚠️ Common issue     | ✅ Impossible          |
| Execution order | ⚠️ Can be confusing | ✅ Always clear        |
| IDE support     | ⚠️ Limited          | ✅ Full Python support |
| Sharing         | `.ipynb` file       | `.py` file or HTML     |

### When to Use Each?

**Use Marimo when:**

- You want reproducible notebooks
- You're using Git for version control
- You want reactive updates
- You're learning data science (no hidden state!)

**Use Jupyter when:**

- You need widgets that only work in Jupyter
- Your team already uses Jupyter
- You're working with legacy `.ipynb` files

**For this course:** We use Marimo because it's better for learning and collaboration!

---

## 3. Starting Marimo

### Open an Existing Notebook

```bash
uv run marimo edit example_notebooks/01_python_basics.py
```

**What happens:**

1. Marimo starts a local server
2. Your browser opens automatically
3. The notebook loads in the browser

### Create a New Notebook

```bash
uv run marimo edit my_analysis.py
```

If the file doesn't exist, Marimo creates it for you.

### Run a Notebook (Non-Interactive)

```bash
uv run marimo run notebook.py
```

This executes the notebook and shows outputs, but you can't edit cells.

---

## 4. Marimo UI Overview

When you open a Marimo notebook, you'll see:

### Main Components

```
┌─────────────────────────────────────────┐
│ [▶] Run All    [+] Cell    [💾] Save   │  ← Toolbar
├─────────────────────────────────────────┤
│                                         │
│  Cell 1: Markdown                       │  ← Markdown cell
│  # My Data Analysis                     │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  Cell 2: Python Code                    │  ← Code cell
│  import polars as pl                    │
│  df = pl.read_csv("data.csv")          │
│                                         │
│  ┌───────────────────────┐             │
│  │ Output: 100 rows × 5  │             │  ← Cell output
│  └───────────────────────┘             │
├─────────────────────────────────────────┤
│                                         │
│  Cell 3: Interactive Plot               │  ← Another cell
│  ...                                    │
└─────────────────────────────────────────┘
│                                         │
│  📁 Files  📊 Variables  ⚙️ Settings   │  ← Sidebar
└─────────────────────────────────────────┘
```

### Toolbar Buttons

- **Run All**: Execute all cells
- **+ Cell**: Add new cell below
- **Save**: Save changes (auto-saves too!)
- **Export**: Export to HTML or other formats
- **Settings**: Notebook preferences

### Sidebar

- **Files**: File browser
- **Variables**: See all defined variables
- **Settings**: Theme, layout options

---

## 5. Creating and Running Cells

### Adding a Cell

- Click **+ Cell** in toolbar
- Or press `B` (below current cell) or `A` (above current cell)

### Types of Cells

**Code Cell:**

```python
import polars as pl
df = pl.read_csv("data/raw/students.csv")
df.head()
```

**Markdown Cell:**

```markdown
# My Analysis

This is a **markdown** cell with _formatting_.
```

To make a cell Markdown:

- Click the dropdown on the cell (shows `python` by default)
- Select `markdown`

### Running Cells

**Automatic execution:**

- Cells run automatically when you edit them
- Press `Shift + Enter` to force run and move to next cell
- Press `Ctrl/Cmd + Enter` to run and stay in current cell

**What gets re-run:**

- If you change cell A, any cells using variables from A re-run automatically
- This is reactivity in action!

### Cell Output

Outputs appear below the cell:

- Prints
- DataFrames (formatted tables)
- Plots
- Error messages

---

## 6. Reactive Execution Model

This is Marimo's superpower! Let's see it in action.

### Example: Reactivity

**Cell 1:**

```python
import marimo as mo
slider = mo.ui.slider(1, 100, value=50)
slider
```

**Cell 2:**

```python
number = slider.value
print(f"The number is: {number}")
```

**What happens:**

- Move the slider in Cell 1
- Cell 2 automatically updates!
- No need to manually re-run Cell 2

### How It Works

Marimo tracks dependencies:

```python
# Cell A
x = 10

# Cell B (depends on A)
y = x * 2

# Cell C (depends on B)
z = y + 5
```

If you change `x` in Cell A:

1. Cell B re-runs (depends on `x`)
2. Cell C re-runs (depends on `y`)
3. You always see current results!

### Benefits

- **No stale outputs**: Always see current results
- **No hidden state**: Can't have variable conflicts
- **Reproducible**: Anyone running your notebook gets same results

---

## 7. Exporting Notebooks

### Export to HTML

```bash
uv run marimo export html notebook.py -o output.html
```

**Result:**

- Standalone HTML file
- Contains all outputs
- Interactive plots work!
- Share with anyone (no Python needed)

### Export to Python Script

Marimo notebooks ARE Python files! Just run them:

```bash
uv run python notebook.py
```

### Share as Marimo App

Convert to standalone app:

```bash
uv run marimo run notebook.py
```

Others can view (but not edit) the notebook.

---

## 8. Best Practices for Organizing Code

### One Concept Per Cell

**Good:**

```python
# Cell 1: Load data
df = pl.read_csv("data.csv")

# Cell 2: Clean data
df_clean = df.filter(pl.col("age") > 0)

# Cell 3: Analyze
summary = df_clean.group_by("category").agg(pl.mean("value"))
```

**Avoid:**

```python
# Cell 1: Everything at once
df = pl.read_csv("data.csv")
df_clean = df.filter(pl.col("age") > 0)
summary = df_clean.group_by("category").agg(pl.mean("value"))
plot = px.bar(summary)
```

### Use Descriptive Variable Names

**Good:**

```python
student_df = pl.read_csv("students.csv")
high_scorers = student_df.filter(pl.col("score") > 85)
```

**Avoid:**

```python
df = pl.read_csv("students.csv")
df2 = df.filter(pl.col("score") > 85)
```

### Add Markdown Explanations

```python
# Cell 1 (Markdown)
"""
# Data Loading
Loading the sales dataset from Q4 2024.
"""

# Cell 2 (Python)
sales = pl.read_csv("sales_q4.csv")
```

### Group Related Cells

Use markdown headers to organize:

```markdown
# Data Loading

... cells for loading data ...

# Data Cleaning

... cells for cleaning ...

# Analysis

... cells for analysis ...

# Visualization

... cells for plots ...
```

---

## 9. Sharing and Version Control

### Git-Friendly

Marimo notebooks are `.py` files, so Git works perfectly!

**What to commit:**

```bash
git add my_analysis.py         # The notebook
git add data/raw/input.csv     # Input data
git add .gitignore             # Git configuration
```

**What NOT to commit:**

- `.venv/` - Virtual environment
- `data/processed/` - Generated outputs
- `.marimo_cache/` - Marimo cache

### Viewing Diffs

Git diffs are readable:

```diff
  import polars as pl

- df = pl.read_csv("old_data.csv")
+ df = pl.read_csv("new_data.csv")

  df.head()
```

Compare this to Jupyter's JSON mess!

### Collaborating

**Team workflow:**

1. Person A: Creates notebook, commits to Git
2. Person B: Pulls from Git, opens with `uv run marimo edit notebook.py`
3. Person B: Makes changes, commits
4. Person A: Pulls changes, sees readable diff
5. No merge conflicts! 🎉

---

## 10. Interactive Widgets and Sliders

Marimo makes interactive notebooks easy!

### Import Marimo UI

```python
import marimo as mo
```

### Slider

```python
# Create slider
age_slider = mo.ui.slider(0, 100, value=25, label="Age")
age_slider
```

```python
# Use slider value
selected_age = age_slider.value
print(f"Selected age: {selected_age}")
```

### Dropdown

```python
category_dropdown = mo.ui.dropdown(
    options=["Electronics", "Clothing", "Books"],
    value="Electronics",
    label="Category"
)
category_dropdown
```

### Text Input

```python
name_input = mo.ui.text(placeholder="Enter name", label="Name")
name_input
```

### Checkbox

```python
filter_checkbox = mo.ui.checkbox(label="Show high scorers only")
filter_checkbox
```

### Using Widgets in Analysis

```python
# Cell 1: Create slider
import marimo as mo
threshold = mo.ui.slider(0, 100, value=75, label="Score Threshold")
threshold
```

```python
# Cell 2: Filter based on slider (reactive!)
import polars as pl
df = pl.read_csv("data/raw/students.csv")
filtered = df.filter(pl.col("test_score") > threshold.value)
print(f"Students above {threshold.value}: {len(filtered)}")
```

Move the slider → Cell 2 updates automatically!

---

## Common Patterns

### Pattern 1: Load → Clean → Analyze → Visualize

```python
# Cell 1: Load
import polars as pl
df = pl.read_csv("data.csv")

# Cell 2: Clean
df_clean = df.drop_nulls()

# Cell 3: Analyze
summary = df_clean.group_by("category").agg(pl.mean("value"))

# Cell 4: Visualize
import plotly.express as px
fig = px.bar(summary, x="category", y="value")
fig
```

### Pattern 2: Interactive Exploration

```python
# Cell 1: Create widgets
import marimo as mo
category = mo.ui.dropdown(options=["A", "B", "C"], value="A")
threshold = mo.ui.slider(0, 100, value=50)
mo.hstack([category, threshold])

# Cell 2: Filter reactively
filtered = df.filter(
    (pl.col("category") == category.value) &
    (pl.col("score") > threshold.value)
)
filtered

# Cell 3: Plot reactively
fig = px.scatter(filtered, x="x", y="y")
fig
```

### Pattern 3: Parameterized Analysis

```python
# Cell 1: Parameters
import marimo as mo
params = mo.ui.dictionary({
    "data_file": mo.ui.text(value="data.csv"),
    "min_score": mo.ui.slider(0, 100, value=70),
    "group_by": mo.ui.dropdown(options=["A", "B"], value="A")
})
params

# Cell 2: Run analysis with parameters
df = pl.read_csv(params.value["data_file"])
result = df.filter(
    pl.col("score") > params.value["min_score"]
).group_by(params.value["group_by"]).count()
result
```

---

## Keyboard Shortcuts

| Action              | Shortcut              |
| ------------------- | --------------------- |
| Run cell            | `Shift + Enter`       |
| Run and stay        | `Ctrl/Cmd + Enter`    |
| New cell below      | `B`                   |
| New cell above      | `A`                   |
| Delete cell         | `D D` (press D twice) |
| Convert to Markdown | `M`                   |
| Convert to Code     | `Y`                   |
| Save                | `Ctrl/Cmd + S`        |
| Command palette     | `Ctrl/Cmd + K`        |

---

## Troubleshooting

### Notebook Won't Open

**Problem:** `uv run marimo edit notebook.py` shows error

**Solutions:**

1. Check you're in the right directory: `ls` should show `pyproject.toml`
2. Make sure dependencies are installed: `uv sync`
3. Try a different port: `uv run marimo edit --port 8080 notebook.py`

### Cell Won't Run

**Problem:** Cell doesn't execute when you change it

**Solutions:**

1. Check for syntax errors (red underlines)
2. Force run: Press `Shift + Enter`
3. Restart kernel: Click "Restart" in settings

### Reactivity Not Working

**Problem:** Changing one cell doesn't update others

**Solutions:**

1. Make sure you're referencing variables correctly
2. Check for variable name typos
3. Look at dependency graph (in sidebar)

### Can't Import Package

**Problem:** `ModuleNotFoundError: No module named 'package'`

**Solutions:**

1. Install the package: `uv add package-name`
2. Restart the notebook
3. Make sure you're using `uv run marimo edit`

---

## Next Steps

- Open `example_notebooks/01_python_basics.py` to see Marimo in action
- Read [Polars Data Wrangling](./polars-data-wrangling.md) to learn data manipulation
- Check [Plotly Visualization](./plotly-visualization.md) for interactive plots
- Experiment! Create your own notebook: `uv run marimo edit my_first_notebook.py`

---

**Official Resources:**

- [Marimo Documentation](https://docs.marimo.io/)
- [Marimo GitHub](https://github.com/marimo-team/marimo)
- [Marimo Examples](https://marimo.io/gallery)

---

**Marimo makes data analysis interactive, reproducible, and fun! Start coding! 🚀**
