import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Data Wrangling with Polars 🐻‍❄️
        
        **Welcome!** Learn to load, explore, and transform data with Polars.
        
        **What you'll learn:**
        - Loading data (CSV, JSON, Parquet)
        - Exploring DataFrames
        - Filtering and selecting data
        - Creating new columns
        - Grouping and aggregation
        - Joining datasets
        
        **Estimated time:** 60 minutes
        
        ---
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 1. Loading Data""")
    return


@app.cell
def __():
    import polars as pl
    
    # Load CSV file
    students = pl.read_csv("../data/raw/students.csv")
    
    print("✓ Loaded students.csv")
    print(f"Shape: {students.shape[0]} rows × {students.shape[1]} columns")
    return pl, students


@app.cell
def __(students):
    # View first few rows
    students.head()
    return


@app.cell
def __(mo):
    mo.md(r"""### Loading JSON""")
    return


@app.cell
def __(pl):
    # Load JSON file
    sales = pl.read_json("../data/raw/sales.json")
    
    print("✓ Loaded sales.json")
    print(f"Shape: {sales.shape[0]} rows × {sales.shape[1]} columns")
    return (sales,)


@app.cell
def __(sales):
    sales.head()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 2. Exploring DataFrames""")
    return


@app.cell
def __(students):
    # DataFrame schema (column names and types)
    print("Schema:")
    print(students.schema)
    return


@app.cell
def __(students):
    # Summary statistics
    students.describe()
    return


@app.cell
def __(students):
    # Column names
    print("Columns:", students.columns)
    
    # Number of rows and columns
    print(f"Rows: {students.shape[0]}, Columns: {students.shape[1]}")
    
    # Check for nulls
    print("\nNull counts:")
    print(students.null_count())
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 3. Selecting Columns""")
    return


@app.cell
def __(students):
    # Select specific columns
    names_and_ages = students.select(["name", "age"])
    names_and_ages.head()
    return (names_and_ages,)


@app.cell
def __(students):
    # Select and rename
    result = students.select([
        pl.col("name"),
        pl.col("test_score").alias("score")
    ])
    result.head()
    return (result,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 4. Filtering Rows""")
    return


@app.cell
def __(pl, students):
    # Filter by condition
    high_scorers = students.filter(pl.col("test_score") > 85)
    
    print(f"Students with score > 85: {high_scorers.shape[0]}")
    high_scorers
    return (high_scorers,)


@app.cell
def __(pl, students):
    # Multiple conditions with & (and)
    good_attendance_high_score = students.filter(
        (pl.col("attendance_rate") >= 90) & 
        (pl.col("test_score") > 80)
    )
    
    print(f"Students with good attendance AND high scores: {good_attendance_high_score.shape[0]}")
    good_attendance_high_score
    return (good_attendance_high_score,)


@app.cell
def __(pl, students):
    # Filter by list of values
    math_or_science = students.filter(
        pl.col("subject").is_in(["Mathematics", "Science"])
    )
    
    print(f"Math or Science students: {math_or_science.shape[0]}")
    math_or_science
    return (math_or_science,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 5. Sorting Data""")
    return


@app.cell
def __(students):
    # Sort by column
    sorted_by_score = students.sort("test_score", descending=True)
    sorted_by_score.head()
    return (sorted_by_score,)


@app.cell
def __(students):
    # Sort by multiple columns
    sorted_multi = students.sort(["grade_level", "test_score"], descending=[False, True])
    sorted_multi.head(10)
    return (sorted_multi,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 6. Creating New Columns""")
    return


@app.cell
def __(pl, students):
    # Add calculated column
    students_with_grade = students.with_columns([
        # Convert score to letter grade
        pl.when(pl.col("test_score") >= 90)
          .then(pl.lit("A"))
          .when(pl.col("test_score") >= 80)
          .then(pl.lit("B"))
          .when(pl.col("test_score") >= 70)
          .then(pl.lit("C"))
          .when(pl.col("test_score") >= 60)
          .then(pl.lit("D"))
          .otherwise(pl.lit("F"))
          .alias("letter_grade")
    ])
    
    students_with_grade.select(["name", "test_score", "letter_grade"]).head()
    return (students_with_grade,)


@app.cell
def __(pl, students):
    # Multiple new columns at once
    enhanced_students = students.with_columns([
        (pl.col("test_score") / 10).round(1).alias("score_scaled"),
        (pl.col("attendance_rate") >= 95).alias("perfect_attendance"),
        pl.col("name").str.to_uppercase().alias("name_upper")
    ])
    
    enhanced_students.head()
    return (enhanced_students,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 7. Handling Missing Values""")
    return


@app.cell
def __(students):
    # Check for missing values
    print("Rows with missing test_score:")
    missing_scores = students.filter(pl.col("test_score").is_null())
    print(f"Count: {missing_scores.shape[0]}")
    missing_scores
    return (missing_scores,)


@app.cell
def __(pl, students):
    # Fill missing values
    students_filled = students.with_columns([
        pl.col("test_score").fill_null(pl.col("test_score").mean()).alias("test_score_filled")
    ])
    
    students_filled.select(["name", "test_score", "test_score_filled"]).head(10)
    return (students_filled,)


@app.cell
def __(pl, students):
    # Drop rows with nulls
    students_clean = students.drop_nulls(subset=["test_score"])
    
    print(f"Original: {students.shape[0]} rows")
    print(f"After dropping nulls: {students_clean.shape[0]} rows")
    return (students_clean,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 8. Grouping and Aggregation""")
    return


@app.cell
def __(students):
    # Group by and count
    by_grade = students.group_by("grade_level").agg([
        pl.count().alias("student_count")
    ]).sort("grade_level")
    
    by_grade
    return (by_grade,)


@app.cell
def __(pl, students):
    # Multiple aggregations
    by_subject = students.group_by("subject").agg([
        pl.count().alias("count"),
        pl.col("test_score").mean().alias("avg_score"),
        pl.col("test_score").max().alias("max_score"),
        pl.col("attendance_rate").mean().alias("avg_attendance")
    ]).sort("avg_score", descending=True)
    
    by_subject
    return (by_subject,)


@app.cell
def __(pl, sales):
    # Real-world example: Sales by category
    category_sales = sales.group_by("product_category").agg([
        pl.count().alias("transaction_count"),
        pl.col("total_amount").sum().alias("total_revenue"),
        pl.col("total_amount").mean().alias("avg_transaction"),
        pl.col("quantity").sum().alias("total_quantity")
    ]).sort("total_revenue", descending=True)
    
    category_sales
    return (category_sales,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 9. Working with Dates""")
    return


@app.cell
def __(pl, sales):
    # Parse dates and extract components
    sales_with_date = sales.with_columns([
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed")
    ]).with_columns([
        pl.col("date_parsed").dt.year().alias("year"),
        pl.col("date_parsed").dt.month().alias("month"),
        pl.col("date_parsed").dt.day().alias("day")
    ])
    
    sales_with_date.select(["date", "year", "month", "day"]).head()
    return (sales_with_date,)


@app.cell
def __(pl, sales_with_date):
    # Monthly sales trend
    monthly_sales = sales_with_date.group_by("month").agg([
        pl.col("total_amount").sum().alias("monthly_revenue"),
        pl.count().alias("transaction_count")
    ]).sort("month")
    
    monthly_sales
    return (monthly_sales,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 10. Joining DataFrames""")
    return


@app.cell
def __(pl):
    # Create a lookup table for grade levels
    grade_info = pl.DataFrame({
        "grade_level": [8, 9, 10, 11, 12],
        "grade_name": ["8th Grade", "9th Grade", "10th Grade", "11th Grade", "12th Grade"],
        "school_level": ["Middle", "High", "High", "High", "High"]
    })
    
    grade_info
    return (grade_info,)


@app.cell
def __(grade_info, students):
    # Left join students with grade info
    students_enriched = students.join(
        grade_info,
        on="grade_level",
        how="left"
    )
    
    students_enriched.select(["name", "grade_level", "grade_name", "school_level"]).head()
    return (students_enriched,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 11. Chaining Operations""")
    return


@app.cell
def __(pl, students):
    # Complex analysis in one chain
    analysis = (
        students
        .filter(pl.col("test_score").is_not_null())  # Remove nulls
        .with_columns([
            (pl.col("test_score") >= 80).alias("high_performer")
        ])
        .group_by("subject")
        .agg([
            pl.count().alias("total_students"),
            pl.col("high_performer").sum().alias("high_performers"),
            pl.col("test_score").mean().alias("avg_score")
        ])
        .with_columns([
            (pl.col("high_performers") / pl.col("total_students") * 100)
            .round(1)
            .alias("pct_high_performers")
        ])
        .sort("avg_score", descending=True)
    )
    
    analysis
    return (analysis,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 12. Data Cleaning Example
        
        Let's clean the sales data which has some quality issues:
        """
    )
    return


@app.cell
def __(pl, sales):
    # Clean and standardize the sales data
    sales_clean = (
        sales
        # Standardize category names (fix capitalization)
        .with_columns([
            pl.col("product_category")
            .str.to_titlecase()
            .alias("product_category")
        ])
        # Filter out invalid transactions
        .filter(
            (pl.col("quantity") > 0) & 
            (pl.col("total_amount") > 0)
        )
        # Add derived columns
        .with_columns([
            pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed"),
            (pl.col("total_amount") / pl.col("quantity")).round(2).alias("calculated_unit_price")
        ])
        .sort("date_parsed")
    )
    
    print(f"Original: {sales.shape[0]} rows")
    print(f"After cleaning: {sales_clean.shape[0]} rows")
    
    # Check unique categories
    print(f"\nUnique categories: {sales_clean['product_category'].n_unique()}")
    sales_clean.head()
    return (sales_clean,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 🎉 Great Job!
        
        You've learned data wrangling with Polars! You now know how to:
        - ✅ Load CSV, JSON, and Parquet files
        - ✅ Explore and understand your data
        - ✅ Filter and select data
        - ✅ Create new calculated columns
        - ✅ Handle missing values
        - ✅ Group and aggregate data
        - ✅ Work with dates
        - ✅ Join multiple datasets
        - ✅ Chain operations for complex analysis
        
        **Next step:** Open `03_plotting.py` to learn data visualization!
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
