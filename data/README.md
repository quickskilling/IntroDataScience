# Dataset Documentation

This directory contains sample datasets for learning data science concepts.

---

## 📊 Available Datasets

### `students.csv`

**Description**: Student enrollment and performance data  
**Rows**: 15 students  
**Format**: CSV

**Columns**:

- `student_id` (int): Unique student identifier
- `name` (string): Student's full name
- `age` (int): Age in years
- `grade_level` (int): Grade level (8-12)
- `subject` (string): Primary subject of study
- `test_score` (float): Most recent test score out of 100 (some missing values)
- `attendance_rate` (float): Attendance percentage (0-100)
- `enrollment_date` (date): Date student enrolled (YYYY-MM-DD format)

**Use cases**:

- Practice basic filtering and sorting
- Handle missing values in `test_score`
- Calculate averages and statistics
- Group by grade level or subject

**Example questions**:

- Which students have perfect attendance?
- What's the average test score by subject?
- How many students are in each grade?

---

### `sales.json`

**Description**: E-commerce sales transactions  
**Rows**: 500 transactions  
**Format**: JSON (array of objects)

**Fields**:

- `transaction_id` (string): Unique transaction ID (format: TXN####)
- `date` (string): Transaction date (YYYY-MM-DD format)
- `customer_id` (string): Customer identifier (format: CUST###)
- `product_category` (string): Product category name
- `product_name` (string): Specific product name
- `quantity` (int): Number of items purchased
- `unit_price` (float): Price per unit in currency
- `total_amount` (float): Total transaction amount
- `payment_method` (string): Payment type used
- `region` (string): Geographic region (North, South, East, West, Central)

**Data quality notes**:

- Some category names have inconsistent capitalization (intentional for practice)
- Contains null values in some fields
- Real-world messiness for cleaning practice

**Use cases**:

- Time series analysis (sales over time)
- Category and regional analysis
- Customer behavior patterns
- Data cleaning practice

**Example questions**:

- Which product category generates the most revenue?
- What are monthly sales trends?
- Which region has the highest sales volume?

---

### `weather.parquet` / `weather.csv`

**Description**: Daily weather observations for one year  
**Rows**: 365 days  
**Format**: Parquet (or CSV fallback)

**Columns**:

- `date` (date): Observation date (YYYY-MM-DD)
- `temperature_high` (float): High temperature in °C
- `temperature_low` (float): Low temperature in °C
- `precipitation` (float): Rainfall in millimeters
- `humidity` (int): Humidity percentage (0-100)
- `wind_speed` (float): Wind speed in km/h
- `condition` (string): Weather description

**Use cases**:

- Time series visualization
- Seasonal pattern analysis
- Temperature range calculations
- Correlation analysis

**Example questions**:

- What's the average temperature by month?
- How many rainy days were there?
- What's the correlation between humidity and precipitation?

---

## 🔧 Data Generation

All datasets are **synthetically generated** for educational purposes. They contain:

- ✅ Realistic patterns and distributions
- ✅ Intentional data quality issues for learning
- ✅ No real personal information
- ✅ Free to use for educational purposes

**Data generator**: See `spec.md` for generation details.

---

## 📂 Directory Structure

```
data/
├── raw/              # Original, unmodified datasets
│   ├── students.csv
│   ├── sales.json
│   └── weather.parquet
│
└── processed/        # Cleaned/transformed data (generated during exercises)
    └── .gitkeep
```

**Note**: The `processed/` directory is for your output files and is ignored by git.

---

## 📖 Usage Examples

### Loading Data

```python
import polars as pl

# Load CSV
students = pl.read_csv("data/raw/students.csv")

# Load JSON
sales = pl.read_json("data/raw/sales.json")

# Load Parquet
weather = pl.read_parquet("data/raw/weather.parquet")
```

### Quick Exploration

```python
# First few rows
print(students.head())

# Data info
print(students.describe())

# Column names and types
print(students.schema)
```

---

## 🎓 Learning Progression

1. **Notebook 2**: Start with `students.csv` for basic operations
2. **Notebook 2**: Progress to `sales.json` for joining and grouping
3. **Notebook 3**: Use `weather.parquet` for time series visualization
4. **Exercise 2**: Practice with `students.csv` and `weather.parquet`
5. **Exercise 3**: Complete project with `sales.json`

---

## 📝 License

These datasets are created for the IntroDataScience course and are free to use for educational purposes.

**Terms of Use**:

- ✅ Use for learning and teaching
- ✅ Modify and adapt
- ✅ Share with attribution
- ❌ Do not use for commercial purposes without permission

---

## ❓ Questions?

If you find issues with the data or have questions, please open an issue on GitHub.
