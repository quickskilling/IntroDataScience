import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 2: Data Wrangling

    **Practice Polars!**

    **What you'll do:**

    - Load and explore real datasets
    - Filter and transform data
    - Answer questions with data

    **Instructions:**

    - Complete each TODO section
    - Run cells to see your results

    ---
    """)
    return


@app.cell
def _():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    from datetime import datetime
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Load and Explore Data
    """)
    return


@app.cell
def _():
    # TODO: Load the students.csv file using Polars
    # The file is at: ../data/raw/students.csv

    students = None  # Replace with pl.read_csv(...)

    # TODO: Display the first 10 rows
    return


@app.cell
def _():
    # TODO: Display basic information about the students dataset
    # - How many rows and columns?
    # - What are the column names?
    # - What are the data types?

    # Hint: Use students.shape, students.columns, students.dtypes, or students.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Filtering Practice
    """)
    return


@app.cell
def _():
    # TODO: Filter to find students who scored above 85 on their test

    high_scorers = None  # Use students.filter(...)

    print(f"Number of high scorers: {len(high_scorers) if high_scorers is not None else 0}")
    return


@app.cell
def _():
    # TODO: Filter to find students in grade_level 10 with attendance_rate > 90%

    grade_10_good_attendance = None  # Use multiple conditions with &
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Selecting and Creating Columns
    """)
    return


@app.cell
def _():
    # TODO: Select only the name, grade_level, and test_score columns

    subset = None  # Use students.select(...)
    return


@app.cell
def _():
    # TODO: Create a new column "performance_category" that categorizes students:
    # - "Excellent" if test_score >= 90
    # - "Good" if test_score >= 75
    # - "Needs Improvement" if test_score < 75
    # - Handle null values appropriately

    # Hint: Use pl.when().then().otherwise() chains

    students_categorized = None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Working with Sales Data
    """)
    return


@app.cell
def _():
    # TODO: Load the sales.json file
    # The file is at: ../data/raw/sales.json

    sales = None  # Replace with pl.read_json(...)
    return


@app.cell
def _():
    # TODO: Display basic info about the sales dataset
    # How many transactions? What's the date range?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Date Operations
    """)
    return


@app.cell
def _():
    # TODO: Convert the date column to datetime type
    # Then extract the month and create a new column "month"

    sales_with_month = None  # Use with_columns() and pl.col().str.to_date()
    return


@app.cell
def _():
    # TODO: Calculate total sales by month
    # Show which month had the highest revenue

    monthly_sales = None
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the data wrangling exercises!

    **What you practiced:**

    - ✅ Loading CSV and JSON data with Polars
    - ✅ Filtering and selecting data
    - ✅ Creating calculated columns
    - ✅ Date operations

    **What's next?**

    - Move on to Exercise 3: Plot

    **Pro Tips:**

    - Chain Polars operations for cleaner code
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
