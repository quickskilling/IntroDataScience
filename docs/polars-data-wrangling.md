# Polars Data Wrangling

Master data manipulation with Polars, the blazing-fast DataFrame library.

---

## 1. What is Polars?

Polars is a DataFrame library for Python that's designed for speed and efficiency.

### Key Features

**Fast ⚡**

- Written in Rust
- Parallel execution by default
- 5-10x faster than Pandas

**Memory Efficient 💾**

- Uses Arrow memory format
- Efficient data types
- Handles larger-than-RAM datasets (lazy mode)

**Expressive API 🎯**

- Clear, readable syntax
- Method chaining
- Powerful expression language

**Type-Safe ✅**

- Strong typing
- Catches errors early
- Better IDE support

---

## 2. Why Polars?

### Polars vs Pandas

| Feature        | Pandas          | Polars                        |
| -------------- | --------------- | ----------------------------- |
| Speed          | Good            | Excellent (5-10x faster)      |
| Memory         | Higher          | Lower                         |
| Syntax         | Method chaining | Method chaining + expressions |
| Parallel       | Limited         | Full parallelism              |
| Type safety    | Weak            | Strong                        |
| Learning curve | Gentle          | Moderate                      |

**For this course:** We use Polars because it's the modern standard and teaches good data habits!

---

## 3. Reading Data

### Reading CSV Files

```python
import polars as pl

# Basic read
df = pl.read_csv("data/raw/students.csv")

# With options
df = pl.read_csv(
    "data/raw/students.csv",
    null_values=["NA", ""],           # Treat these as null
    dtypes={"student_id": pl.Int64},  # Specify column types
    n_rows=100                         # Read only first 100 rows
)
```

### Reading JSON Files

```python
# JSON array of objects
df = pl.read_json("data/raw/sales.json")

# Newline-delimited JSON
df = pl.read_ndjson("data/raw/logs.ndjson")
```

### Reading Parquet Files

```python
# Parquet (efficient binary format)
df = pl.read_parquet("data/raw/weather.parquet")
```

### Reading from URLs

```python
df = pl.read_csv("https://example.com/data.csv")
```

---

## 4. DataFrame Basics

### Structure and Schema

```python
import polars as pl
df = pl.read_csv("data/raw/students.csv")

# View first rows
df.head()         # First 5 rows
df.head(10)       # First 10 rows

# View last rows
df.tail()         # Last 5 rows

# Get shape
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

# Get column names
df.columns        # ['student_id', 'name', 'age', ...]

# Get data types
df.dtypes         # Schema with types
df.schema         # Dictionary of column → type

# Summary statistics
df.describe()     # Count, mean, std, min, max, etc.
```

### Inspecting Data

```python
# Basic info
print(df)         # Shows first few rows

# Detailed schema
df.schema
# {'student_id': Int64, 'name': String, 'age': Int64, ...}

# Sample random rows
df.sample(n=5)    # 5 random rows
df.sample(fraction=0.1)  # 10% of data

# Check for nulls
df.null_count()   # Nulls per column
```

---

## 5. Selecting Columns

### Select Specific Columns

```python
# Single column (returns DataFrame)
df.select("name")

# Multiple columns
df.select("name", "age", "grade_level")

# Using a list
columns = ["name", "age"]
df.select(columns)

# Using pl.col() expression
df.select(
    pl.col("name"),
    pl.col("test_score")
)
```

### Select by Pattern

```python
# All columns starting with 'test'
df.select(pl.col("^test.*$"))

# All numeric columns
df.select(pl.col(pl.Int64, pl.Float64))

# Everything except one column
df.select(pl.exclude("student_id"))
```

### Rename Columns

```python
# Rename while selecting
df.select(
    pl.col("name").alias("student_name"),
    pl.col("test_score").alias("score")
)

# Rename in place
df.rename({"name": "student_name", "age": "student_age"})
```

---

## 6. Filtering Rows

### Basic Filtering

```python
# Single condition
df.filter(pl.col("age") > 15)

# Multiple conditions with &
df.filter(
    (pl.col("age") > 15) &
    (pl.col("test_score") > 80)
)

# Multiple conditions with |
df.filter(
    (pl.col("grade_level") == 10) |
    (pl.col("grade_level") == 11)
)
```

### Filter Methods

```python
# Greater than
df.filter(pl.col("test_score") > 75)

# Less than or equal
df.filter(pl.col("age") <= 16)

# Equal to
df.filter(pl.col("subject") == "Mathematics")

# Not equal
df.filter(pl.col("subject") != "Art")

# In a list
df.filter(pl.col("grade_level").is_in([10, 11, 12]))

# Null values
df.filter(pl.col("test_score").is_null())
df.filter(pl.col("test_score").is_not_null())

# String operations
df.filter(pl.col("name").str.contains("John"))
df.filter(pl.col("name").str.starts_with("A"))
```

### Complex Filtering

```python
# Between values
df.filter(
    pl.col("test_score").is_between(70, 90)
)

# Not in list
df.filter(
    ~pl.col("subject").is_in(["Art", "Music"])
)

# Multiple AND conditions
df.filter(
    (pl.col("age") > 14) &
    (pl.col("attendance_rate") > 90) &
    (pl.col("test_score") > 85)
)
```

---

## 7. Sorting Data

### Basic Sorting

```python
# Sort by one column (ascending)
df.sort("test_score")

# Sort descending
df.sort("test_score", descending=True)

# Sort by multiple columns
df.sort(["grade_level", "test_score"])

# Mixed sorting
df.sort(
    "grade_level",              # Ascending
    "test_score",               # Ascending
    descending=[False, True]    # test_score descending
)
```

### Sort with Expressions

```python
# Sort by calculated value
df.sort(pl.col("test_score") / pl.col("attendance_rate"))

# Sort nulls first
df.sort("test_score", nulls_last=False)
```

---

## 8. Adding/Modifying Columns

### With Columns

```python
# Add new column
df.with_columns(
    pl.col("test_score").alias("score_copy")
)

# Calculate new column
df.with_columns(
    (pl.col("test_score") * 1.1).alias("bonus_score")
)

# Multiple new columns
df.with_columns(
    pl.col("test_score").round(0).alias("rounded_score"),
    (pl.col("age") + 1).alias("next_year_age"),
    pl.lit("2024").alias("year")  # Literal value
)
```

### Conditional Columns

```python
# If-else logic with when/then/otherwise
df.with_columns(
    pl.when(pl.col("test_score") >= 90)
    .then(pl.lit("A"))
    .when(pl.col("test_score") >= 80)
    .then(pl.lit("B"))
    .when(pl.col("test_score") >= 70)
    .then(pl.lit("C"))
    .otherwise(pl.lit("F"))
    .alias("grade")
)
```

### String Operations

```python
# Uppercase
df.with_columns(
    pl.col("name").str.to_uppercase().alias("name_upper")
)

# Extract parts
df.with_columns(
    pl.col("name").str.split(" ").list.get(0).alias("first_name")
)

# Replace
df.with_columns(
    pl.col("subject").str.replace("Math", "Mathematics").alias("subject_full")
)
```

---

## 9. Grouping and Aggregation

### Basic Grouping

```python
# Count by group
df.group_by("grade_level").count()

# Single aggregation
df.group_by("subject").agg(
    pl.mean("test_score")
)

# Multiple aggregations
df.group_by("grade_level").agg(
    pl.mean("test_score").alias("avg_score"),
    pl.max("test_score").alias("max_score"),
    pl.count().alias("num_students")
)
```

### Common Aggregations

```python
df.group_by("subject").agg(
    pl.count().alias("count"),                    # Count rows
    pl.sum("test_score").alias("total"),          # Sum
    pl.mean("test_score").alias("average"),       # Mean
    pl.median("test_score").alias("median"),      # Median
    pl.std("test_score").alias("std_dev"),        # Standard deviation
    pl.min("test_score").alias("minimum"),        # Minimum
    pl.max("test_score").alias("maximum"),        # Maximum
    pl.first("test_score").alias("first"),        # First value
    pl.last("test_score").alias("last")           # Last value
)
```

### Group by Multiple Columns

```python
df.group_by(["grade_level", "subject"]).agg(
    pl.mean("test_score").alias("avg_score"),
    pl.count().alias("num_students")
)
```

### Filtering After Grouping

```python
# Group, aggregate, then filter
(
    df.group_by("subject")
    .agg(pl.mean("test_score").alias("avg_score"))
    .filter(pl.col("avg_score") > 80)
)
```

---

## 10. Joining DataFrames

### Load Example Data

```python
students = pl.read_csv("data/raw/students.csv")
grades = pl.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "semester": ["Fall", "Fall", "Spring", "Fall", "Spring"],
    "gpa": [3.5, 3.8, 3.2, 3.9, 3.6]
})
```

### Inner Join

```python
# Keep only matching rows from both
students.join(grades, on="student_id", how="inner")
```

### Left Join

```python
# Keep all rows from left, add matching from right
students.join(grades, on="student_id", how="left")
```

### Types of Joins

```python
# Inner: Only matching rows
students.join(grades, on="student_id", how="inner")

# Left: All from left, matching from right
students.join(grades, on="student_id", how="left")

# Outer: All rows from both
students.join(grades, on="student_id", how="outer")

# Cross: Cartesian product (every combination)
students.join(grades, how="cross")
```

### Join on Different Column Names

```python
# When column names differ
students.join(
    grades,
    left_on="student_id",
    right_on="id",
    how="left"
)
```

---

## 11. Handling Missing Values

### Detect Nulls

```python
# Count nulls per column
df.null_count()

# Filter rows with nulls
df.filter(pl.col("test_score").is_null())

# Filter rows without nulls
df.filter(pl.col("test_score").is_not_null())
```

### Remove Nulls

```python
# Drop rows with any null
df.drop_nulls()

# Drop rows with null in specific column
df.drop_nulls(subset=["test_score"])

# Drop rows with null in multiple columns
df.drop_nulls(subset=["test_score", "attendance_rate"])
```

### Fill Nulls

```python
# Fill with a value
df.with_columns(
    pl.col("test_score").fill_null(0).alias("test_score")
)

# Fill with mean
mean_score = df.select(pl.mean("test_score")).item()
df.with_columns(
    pl.col("test_score").fill_null(mean_score)
)

# Forward fill (use previous value)
df.with_columns(
    pl.col("test_score").fill_null(strategy="forward")
)

# Backward fill (use next value)
df.with_columns(
    pl.col("test_score").fill_null(strategy="backward")
)
```

---

## 12. Expression Syntax

Polars expressions are powerful and composable!

### Column Expressions

```python
# Reference a column
pl.col("age")

# Multiple columns
pl.col("age", "test_score")

# All columns
pl.all()

# Columns matching pattern
pl.col("^test_.*$")  # Regex pattern
```

### Chaining Operations

```python
# Chain multiple operations
df.select(
    pl.col("test_score")
    .fill_null(0)           # Fill nulls
    .clip(0, 100)           # Clip to range
    .round(1)               # Round to 1 decimal
    .alias("clean_score")   # Rename
)
```

### Window Functions

```python
# Rank within groups
df.with_columns(
    pl.col("test_score")
    .rank()
    .over("grade_level")
    .alias("rank_in_grade")
)

# Running sum
df.with_columns(
    pl.col("test_score")
    .cum_sum()
    .alias("cumulative_score")
)
```

---

## 13. Method Chaining

Polars is designed for readable method chains!

### Good Chain Example

```python
result = (
    pl.read_csv("data/raw/students.csv")
    .filter(pl.col("age") > 14)                          # Filter young students
    .with_columns(
        (pl.col("test_score") * 1.1).alias("bonus_score")  # Add bonus
    )
    .group_by("grade_level")                             # Group by grade
    .agg(
        pl.mean("bonus_score").alias("avg_bonus"),
        pl.count().alias("num_students")
    )
    .sort("avg_bonus", descending=True)                  # Sort by average
    .head(5)                                             # Top 5
)
```

### Why Chain?

- **Readable**: Each step is clear
- **Efficient**: Polars optimizes the entire chain
- **Maintainable**: Easy to add/remove steps

---

## 14. Lazy Evaluation

For large datasets, use lazy mode for better performance!

### Lazy API

```python
# Start lazy
lazy_df = pl.scan_csv("large_file.csv")

# Build query (doesn't execute yet)
lazy_query = (
    lazy_df
    .filter(pl.col("age") > 18)
    .group_by("category")
    .agg(pl.sum("value"))
)

# Execute when ready
result = lazy_query.collect()
```

### Benefits

- **Optimization**: Polars optimizes the entire query
- **Memory**: Processes data in chunks
- **Speed**: Only reads needed columns

### When to Use Lazy

- Large CSV files (> 1GB)
- Complex chains of operations
- When you want maximum performance

---

## 15. Common Operations Cheat Sheet

```python
import polars as pl

# Reading
df = pl.read_csv("file.csv")
df = pl.read_json("file.json")
df = pl.read_parquet("file.parquet")

# Viewing
df.head()
df.tail()
df.describe()
df.schema

# Selecting
df.select("col1", "col2")
df.select(pl.col("col1"))

# Filtering
df.filter(pl.col("age") > 18)
df.filter((pl.col("a") > 5) & (pl.col("b") < 10))

# Sorting
df.sort("col1")
df.sort("col1", descending=True)

# Adding columns
df.with_columns(
    (pl.col("a") * 2).alias("a_doubled")
)

# Grouping
df.group_by("category").agg(pl.mean("value"))

# Joining
df1.join(df2, on="id", how="left")

# Writing
df.write_csv("output.csv")
df.write_json("output.json")
df.write_parquet("output.parquet")
```

---

## 16. Polars vs Pandas Comparison

### Syntax Comparison

| Operation  | Pandas                            | Polars                                            |
| ---------- | --------------------------------- | ------------------------------------------------- |
| Read CSV   | `pd.read_csv()`                   | `pl.read_csv()`                                   |
| Filter     | `df[df['age'] > 18]`              | `df.filter(pl.col("age") > 18)`                   |
| Add column | `df['new'] = df['a'] * 2`         | `df.with_columns((pl.col("a") * 2).alias("new"))` |
| Group by   | `df.groupby('cat')['val'].mean()` | `df.group_by("cat").agg(pl.mean("val"))`          |
| Sort       | `df.sort_values('col')`           | `df.sort("col")`                                  |

---

## 17. Performance Tips

### Do's ✅

- Use lazy evaluation for large files
- Chain operations instead of intermediate variables
- Use expressions instead of apply/map
- Filter early in the chain
- Select only needed columns

### Don'ts ❌

- Don't use Python loops on DataFrames
- Don't convert to Pandas unless necessary
- Don't load entire file if you only need part
- Don't use mutable operations (Polars is immutable)

---

## Practice Exercise

Try this on the students dataset:

```python
import polars as pl

# Load data
df = pl.read_csv("data/raw/students.csv")

# Challenge: Find the average test score by grade level,
# but only for students with > 85% attendance

result = (
    df
    # Your code here!
)
```

**Solution:**

```python
result = (
    df
    .filter(pl.col("attendance_rate") > 85)
    .group_by("grade_level")
    .agg(pl.mean("test_score").alias("avg_score"))
    .sort("grade_level")
)
```

---

## Next Steps

- Practice with `example_notebooks/02_data_wrangling.py`
- Try exercises in `exercises/ex02_wrangle_and_plot.py`
- Read [Plotly Visualization](./plotly-visualization.md) to visualize your data
- Check [official Polars docs](https://pola-rs.github.io/polars/) for advanced features

---

**Official Resources:**

- [Polars Documentation](https://pola-rs.github.io/polars/)
- [Polars GitHub](https://github.com/pola-rs/polars)
- [Polars Cheat Sheet](https://franzdiebold.github.io/polars-cheat-sheet/Polars_cheat_sheet.pdf)

---

**Polars makes data wrangling fast and elegant. Happy analyzing! 🐻‍❄️**
