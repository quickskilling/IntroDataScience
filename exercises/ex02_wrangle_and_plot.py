import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 2: Data Wrangling & Plotting 📊

    **Practice Polars and Plotly together!**

    **Estimated time:** 60 minutes

    **What you'll do:**
    - Load and explore real datasets
    - Filter and transform data
    - Create visualizations
    - Answer questions with data

    **Instructions:**
    - Complete each TODO section
    - Run cells to see your results
    - Solutions available in `solutions/ex02_wrangle_and_plot.py`

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
    ## Part 5: Aggregations and Grouping
    """)
    return


@app.cell
def _():
    # TODO: Calculate total sales by product_category
    # Sum up the total_amount for each category
    # Sort by total sales descending

    category_sales = None  # Use group_by() and agg()

    return


@app.cell
def _():
    # TODO: Find the average transaction amount by payment_method

    avg_by_payment = None

    return


@app.cell
def _():
    # TODO: Count how many transactions each region had
    # Also calculate the total revenue per region

    region_summary = None  # Group by region, count and sum

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 6: Date Operations
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
    ## Part 7: Your First Plot - Bar Chart
    """)
    return


@app.cell
def _():
    # TODO: Create a bar chart showing sales by category
    # Use plotly express (px.bar)
    # - x-axis: product_category
    # - y-axis: total sales
    # - Add a title
    # - Color the bars

    # Hint: Make sure category_sales is a valid dataframe first!

    fig1 = None  # Create your plot here

    # Uncomment when ready:
    # fig1.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 8: Line Chart - Sales Over Time
    """)
    return


@app.cell
def _():
    # TODO: Create a line chart showing sales trends by month
    # Use px.line
    # - x-axis: month
    # - y-axis: total revenue
    # - Add markers to the line
    # - Add a title

    fig2 = None

    # Uncomment when ready:
    # fig2.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 9: Scatter Plot - Exploring Relationships
    """)
    return


@app.cell
def _():
    # TODO: Create a scatter plot showing the relationship between
    # attendance_rate (x-axis) and test_score (y-axis)
    # - Color points by grade_level
    # - Add a trendline (trendline="ols")
    # - Add appropriate title and labels

    fig3 = None

    # Uncomment when ready:
    # fig3.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 10: Histogram - Distribution Analysis
    """)
    return


@app.cell
def _():
    # TODO: Create a histogram of transaction amounts (total_amount)
    # - Use 30 bins
    # - Add a title
    # - Label the axes
    # - Try adding nbins=30 parameter

    fig4 = None

    # Uncomment when ready:
    # fig4.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 11: Box Plot - Compare Distributions
    """)
    return


@app.cell
def _():
    # TODO: Create a box plot comparing total_amount across regions
    # This helps identify outliers and compare distributions
    # - x-axis: region
    # - y-axis: total_amount
    # - Add a title

    fig5 = None

    # Uncomment when ready:
    # fig5.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 12: Advanced - Multiple Subplots
    """)
    return


@app.cell
def _():
    # TODO: Create a dashboard with 2 subplots:
    # 1. Top plot: Bar chart of sales by category (reuse category_sales)
    # 2. Bottom plot: Bar chart of sales by region (reuse region_summary)

    # Hint: Use go.Figure() with make_subplots or add multiple traces
    # This is challenging - check the solution if you get stuck!

    fig6 = None

    # Uncomment when ready:
    # fig6.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 13: Challenge - Answer This Question
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Question:** What is the most popular product category in each region?

    **Your task:**
    1. Group the sales data by region AND product_category
    2. Count transactions for each combination
    3. For each region, find the category with the most transactions
    4. Create a bar chart showing the top category per region

    This combines multiple skills: grouping, filtering, and plotting!
    """)
    return


@app.cell
def _():
    # TODO: Write your analysis here

    # Step 1: Group by region and category, count transactions
    region_category_counts = None

    # Step 2: For each region, find the top category
    # Hint: You might need to use group_by, sort, and group_by().first()

    top_category_per_region = None

    return


@app.cell
def _():
    # TODO: Create a bar chart of your results

    fig7 = None

    # Uncomment when ready:
    # fig7.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Excellent Work!

    You've completed the data wrangling and plotting exercises!

    **What you practiced:**
    - ✅ Loading CSV and JSON data with Polars
    - ✅ Filtering and selecting data
    - ✅ Creating calculated columns
    - ✅ Grouping and aggregating
    - ✅ Date operations
    - ✅ Multiple chart types (bar, line, scatter, histogram, box)
    - ✅ Combining data analysis with visualization

    **What's next?**
    - Compare your solutions with `solutions/ex02_wrangle_and_plot.py`
    - Move on to Exercise 3: Mini Project
    - Try creating your own visualizations with the data!

    **Pro Tips:**
    - Plotly charts are interactive - hover, zoom, pan!
    - Chain Polars operations for cleaner code
    - Always explore your data before plotting
    """)
    return


if __name__ == "__main__":
    app.run()
