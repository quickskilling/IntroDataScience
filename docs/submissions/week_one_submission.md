# Week 1 Learning Summary
## By Daniel Tobi Oyedepo

## Python
Python is a programming language designed to read and write almost like plain English, which makes it one of the best languages to learn for starters.

Python is used in various areas like data science and data analysis, automation and scripting, web development, machine learning and AI and areas relating to scientific research. 

Python is:
- Readable with clean syntax
- Contains huge standard library - many tasks have built-in tools
- Massive community support
- It's in great demand as a skill across data, tech, research, and more. 


## Marimo 
Marimo is a reactive python notebook that runs as pure Python files (`.py`) and not as JSON blobs (`.ipynb`).

### Key Features are:
- **Reaction Execution:** When you change one cell, dependent cells update automatically. 
- **Pure Python Files:*** Notebooks are regular `.py` files. Work with any Python tool and perfect for Git version control.
- **Reproducible:** Runs top-to-bottom and no hidden state.
- **Interactive:** Real time updates, interactive plots and built-in UI widgets. 

All these features makes it have greater advantages over Jupyter Notebook.


## Git Version Control 
Git is a distributed version control system that tracks changes to your code over time. 
Every developer has a full copy of the project history on their machine. 

### Core ideas:
- **Commit** - a saved snapshot of your changes.
- **Branch** - an independent line of development for experimenting safely
- **Merge** - combining branches back together.
- **Push/Pull** - syncing changes between your mahcine and a remote repo. 

The basic workflow: modify files --> stages changes --> commit --> push to a remote like GitHub. 

All these without affecting each others work and still having full history of it. 

Git is the tool; GitHub/GitLab are just platforms that host your Git repos online. 


## Plotly Visualization
Plotly is an interactive data visualization library available in Python, R, and JavaScritp. 

Plotly turns data into interactive charts and graphs where you can hover, zoom, pan, and filter directly in the browser. 

Common chart types are: Line, bar, scatter, pie, heatmaps, 3D plots, mpas, and more.

**Key Flavours:**
- **Plotly Express** -- quick, one-liner charts for fast exploration
- **Plotly Graph Objects** -- more verbose but fully customization 
- **Dash** -- Plotly's framework for building full data dashboards/web pages. 


## Polars Data Wrangling
Polars is a fast DataFrame library for data wrangling in Python, designed as a high-performance alternative to Pandas.

**Polars is:**
- extremely fast and memory efficient
- uses lazy evaluation by optimizing query before running it
- handles larger-than-memory datasets with ease.

Polars is best used when Pandas feels slow or dealing with large datasets. The syntax might have a learning curve but pays off. 

## VS Code
VS Code is a free, lightweight code editor by Microsoft. 

It is a fast, extensible editor that works for virtually any programming language, sitting between a simple text editor and a full IDE. 

**Key Features:**
- IntelliSense -- smart autocomplete, hints, and error detection
- Intergrated terminal -- run commands without leaving the editor
- Git integration -- built-in sorce control panel
- Extensions -- thousands of plugins for languages, themes, and tools
- Live Share -- real-time collaborative coding. 


## UV Package Management
uv is an extremely fast Python package and project manager designed as a drop-in replacement for `pip`, `pip-tools`, and `virtualenv`.

uv is 10-100x faster than `pip`, manages packages, virtual env, and Python versions all in one tool. 

**Key Features:**
- Auto virtual environments -- no need to manually create/activate vens
- Lockfile -- `uv.lock` ensures reproducible installs.
- Python verions management -- install and switch Python versions like `pyenv`
- Toolrunner -- run one-off tools without installing them globally (`uvx`)


## Data Science 
Data Science is the practice of extracting insights and value from data using statistics, programming, and domain knowledge.

**Key descipline areas includes:***
- Statistics -- for hypothesis testing, probability, distributions
- Mathematics -- linear algebra, calculus
- Programming -- automating analysis at scale
- Domain Knowledge -- knowing what the data means

**The workflow:***
1. Collect -- gather raw data from databases, APIs, files
2. Clean -- handle missing values, fix errors, reshape data
3. Explore (EDA) -- understand patterns, distributions, relationships
4. Model -- apply statistical or ML models to find insights or make predictions
5. Communicate -- visualize and present findings clearly. 

### Core toolkit (PYthon):
| **Task**         | **Libraries**       |
| ---------------- | ------------------- |
| Data wrangling   | Pandas, Polars      |
| Numerics         | Numpy               |
| Visualization    | Matplotlib, Plotyly |
| Machine Learning | Scikit-learn        |
| Deep Learning    | PyTorch, TensorFlow |
| Notebooks        | VS Code             |

Data science contributes across numerous domains like:
- Business and Commerce
- Scientific Research
- Public Sector
- Healthcare and Medicine
- Environmental and Climate Science


## Markdown Writing
Markdown is a lightweight markup language for formating plain text using simple symobls and it's designed to be readable as-is and  renderable as HTML.

Markdown's superpower is simplicity -- write in any text editor, render beautifully anywhere. It's the universal language of developer documentation. 

**Common Syntax are:**
````markdown
# Heading 1 
## Heading 2 - Chapter Heading
### Section Heading
### Sub-section

- bullet item
1. numbered item

[link text](https://url.com)
![alt text](image.png)

`inline code`
```python
code block
```

> blockquote

Tables
|  Col 1  |  Col 2  |
| ------- | ------- |
| cell    | cell    |

````

**Where it's used:**
- GitHub -- READMEs, issues, pull requests
- Jupyter Notebooks -- documentation cells 
- Docs sites -- MkDocs, Docusaurus, Notion
- Chat/forums -- Slack, Discord, Reddit
