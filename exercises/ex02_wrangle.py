# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.20.2",
#     "plotly>=6.6.0",
#     "polars>=1.39.3",
#     "pyzmq>=27.1.0",
# ]
# ///

import marimo

__generated_with = "0.20.4"
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

    return mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1: Load and Explore Data
    """)
    return


@app.cell
def _(pl):
    # TODO: Load the students.csv file using Polars
    # The file is at: ../data/raw/students.csv

    students = pl.read_csv("../data/raw/students.csv")  # Replace with pl.read_csv(...)

    # TODO: Display the first 10 rows
    students.head(10)
    return (students,)


@app.cell
def _(students):
    # TODO: Display basic information about the students dataset
    # - How many rows and columns?
    # - What are the column names?
    # - What are the data types?

    # Hint: Use students.shape, students.columns, students.dtypes, or students.describe()
    # Column names
    print("Students Columns:", students.columns)

    # Number of rows and columns)
    print(f"Rows: {students.shape[0]}, Columns: {students.shape[1]}")
    return


@app.cell
def _(students):
    students.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2: Filtering Practice
    """)
    return


@app.cell
def _(pl, students):
    # TODO: Filter to find students who scored above 85 on their test

    high_scorers = students.filter(pl.col("test_score") > 85)  # Use students.filter(...)

    print(f"Number of high scorers: {len(high_scorers) if high_scorers is not None else 0}")
    high_scorers.head()
    return


@app.cell
def _(pl, students):
    # TODO: Filter to find students in grade_level 10 with attendance_rate > 90%

    grade_10_good_attendance = students.filter(
        (pl.col("grade_level") == 10) &
        (pl.col("attendance_rate") >= 90)
    ) 

    print(f"Number of Grade 10 students with Attendance > 90%: {grade_10_good_attendance.shape[0]}")
    grade_10_good_attendance
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 3: Selecting and Creating Columns
    """)
    return


@app.cell
def _(students):
    # TODO: Select only the name, grade_level, and test_score columns

    subset = students.select(["name", "grade_level", "test_score"])
    subset.head()
    return


@app.cell
def _(pl, students):
    # TODO: Create a new column "performance_category" that categorizes students:
    # - "Excellent" if test_score >= 90
    # - "Good" if test_score >= 75
    # - "Needs Improvement" if test_score < 75
    # - Handle null values appropriately

    # Hint: Use pl.when().then().otherwise() chains

    students_categorized = students.with_columns([
        pl.when(pl.col("test_score") >= 90)
            .then(pl.lit("Excellent"))
            .when(pl.col("test_score") >= 75)
            .then(pl.lit("Good"))
            .when(pl.col("test_score") < 75)
            .then(pl.lit("Needs Improvement"))
            .otherwise(pl.lit("Unknown"))
            .alias("performance_category")
    ])

    students_categorized.select(["name", "test_score", "performance_category"]).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 4: Working with Sales Data
    """)
    return


@app.cell
def _(pl):
    # TODO: Load the sales.json file
    # The file is at: ../data/raw/sales.json

    sales = pl.read_json("../data/raw/sales.json")  # Replace with pl.read_json(...)
    return (sales,)


@app.cell
def _(sales):
    # TODO: Display basic info about the sales dataset
    # How many transactions? What's the date range?

    print(f"Number of transactions: {sales.shape[0]}")
    print(f"Date range: {sales['date'].min()} to {sales['date'].max()}")

    sales.head(10)
    return


@app.cell
def _(sales):
    sales.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 5: Date Operations
    """)
    return


@app.cell
def _(pl, sales):
    # TODO: Convert the date column to datetime type
    # Then extract the month and create a new column "month"

    sales_with_month = sales.with_columns(
        pl.col("date").str.to_date("%Y-%m-%d").alias("date_parsed")
        ).with_columns(
            pl.col("date_parsed").dt.month().alias("month")
        )

    sales_with_month.select(["date_parsed", "month"]).head()
    # Use with_columns() and pl.col().str.to_date()
    return (sales_with_month,)


@app.cell
def _(sales_with_month):
    sales_with_month.shape[0]
    return


@app.cell
def _(pl, sales_with_month):
    # TODO: Calculate total sales by month
    # Show which month had the highest revenue

    monthly_sales = (
        sales_with_month
        .group_by("month")
        .agg(pl.col("total_amount").sum()
        .alias("total_revenue"))
        .sort("total_revenue", descending=True)
    )

    # Month with highest revenue
    top_month = monthly_sales.select("month").row(0)

    print(monthly_sales)
    print(f"Month with highest revenue: {top_month}")
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
