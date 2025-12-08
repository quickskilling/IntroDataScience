# Copilot-Assisted Coding

Learn to code with AI as your pair programming partner.

---

## 1. What is GitHub Copilot?

GitHub Copilot is an AI coding assistant that helps you write code faster and learn as you go.

### Key Features

**Code Completion 💡**

- Suggests code as you type
- Understands context
- Generates entire functions
- Multiple languages

**Code Explanation 📖**

- Explains what code does
- Breaks down complex logic
- Helps you understand libraries
- Great for learning!

**Code Generation 🤖**

- Writes code from comments
- Generates test cases
- Creates boilerplate
- Suggests improvements

**Chat Interface 💬**

- Ask coding questions
- Get explanations
- Debug errors
- Learn concepts

---

## 2. Setting Up Copilot in VS Code

### Install the Extension

1. Open VS Code
2. Click Extensions (Ctrl/Cmd + Shift + X)
3. Search for "GitHub Copilot"
4. Click Install
5. Sign in with your GitHub account

### Get Access

**Free for:**

- Verified students ([GitHub Student Developer Pack](https://education.github.com/pack))
- Verified teachers
- Open source maintainers

**Paid for:**

- Individual developers ($10/month)
- Organizations

**Trial:**

- Free 30-day trial for everyone!

### Verify It's Working

1. Create a new Python file: `test.py`
2. Type: `def calculate_average(`
3. Copilot should suggest code!
4. Press Tab to accept

---

## 3. How Copilot Works

### The Technology

- Built on OpenAI's Codex model
- Trained on billions of lines of public code
- Understands context from your file
- Learns patterns from your coding style

### What Copilot Can Do

**✅ Excellent at:**

- Completing common patterns
- Writing boilerplate code
- Generating simple functions
- Suggesting variable names
- Converting comments to code
- Providing multiple options

**❌ Be careful with:**

- Complex algorithms (verify logic!)
- Security-sensitive code
- Novel/unique problems
- Domain-specific calculations
- Business logic

### Privacy

- Your code isn't used to train the model
- You can opt out of telemetry
- Check your organization's policies
- Read the [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)

---

## 4. Effective Prompting

The key to great Copilot suggestions is writing clear comments!

### Good Comments

**Be Specific:**

```python
# Bad: Calculate something
# Good: Calculate the average test score for students with > 85% attendance

def calculate_average_high_attendance(df):
    # Copilot suggests accurate code!
```

**Include Context:**

```python
# Load student data from CSV, filter for age > 15,
# and return the top 10 students by test score

import polars as pl

def get_top_students(filepath):
    # Copilot understands what you want!
```

**Use Examples:**

```python
# Convert temperature from Celsius to Fahrenheit
# Example: 0°C = 32°F, 100°C = 212°F

def celsius_to_fahrenheit(celsius):
    # Copilot generates: return (celsius * 9/5) + 32
```

### Descriptive Function Names

```python
# Good: Copilot understands intent
def filter_high_scoring_students(df, threshold=80):
    # Suggestion: return df.filter(pl.col("test_score") > threshold)

# Less clear
def filter_students(df, x):
    # Copilot is less certain what to do
```

### Break Down Problems

```python
# Instead of one big function, break it down:

# Step 1: Load the sales data from JSON
sales = pl.read_json("data/raw/sales.json")

# Step 2: Filter for transactions in 2024
sales_2024 = sales.filter(pl.col("date").str.starts_with("2024"))

# Step 3: Calculate total sales by category
category_totals = sales_2024.group_by("product_category").agg(
    pl.sum("total_amount").alias("total")
)

# Each step gives Copilot clear context!
```

---

## 5. Copilot Features

### Inline Suggestions (Tab to Accept)

As you type, Copilot suggests completions:

```python
# Type this:
def calculate_

# Copilot suggests:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Press Tab to accept
# Press Esc to reject
```

**Multiple Suggestions:**

- Press `Alt/Option + ]` for next suggestion
- Press `Alt/Option + [` for previous suggestion

### Copilot Chat

Ask questions in natural language!

**Open Chat:**

- Click the chat icon in the sidebar
- Or press `Ctrl/Cmd + Shift + I`

**Example Questions:**

```
"How do I read a CSV file with Polars?"
"Explain this code: df.group_by('category').agg(pl.mean('value'))"
"What's wrong with this function?"
"How do I create a bar chart with Plotly?"
```

### Explain Code

**Right-click on code** → "Copilot: Explain This"

```python
# Select this code and ask Copilot to explain:
result = (
    df.filter(pl.col("age") > 18)
    .group_by("category")
    .agg(pl.mean("score"))
    .sort("score", descending=True)
)

# Copilot explains: "This code filters the DataFrame for rows where
# age is greater than 18, groups by category, calculates the mean
# score for each category, and sorts by score in descending order."
```

### Fix Errors

When you have an error:

1. **Right-click** on the error
2. Select **"Copilot: Fix This"**
3. Copilot suggests a fix!

```python
# Error: NameError: name 'polars' is not defined
result = polars.read_csv("data.csv")

# Copilot suggests: Add import statement
import polars as pl
result = pl.read_csv("data.csv")
```

### Generate Tests

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Type: "test for calculate_average"
# Copilot generates:

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([5]) == 5
```

---

## 6. Best Practices

### Review All Suggestions ✅

**Always check:**

- Does the logic make sense?
- Are there edge cases?
- Is it efficient?
- Does it match your requirements?

**Example:**

```python
# Copilot suggests:
def divide_numbers(a, b):
    return a / b

# You should add:
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Learn from the Code 📚

Don't just accept suggestions—understand them!

**Good workflow:**

1. Accept Copilot's suggestion
2. Read through the code
3. Ask Copilot Chat: "Explain this code"
4. Try modifying it yourself
5. Run it to see it work

**Example:**

```python
# Copilot suggests:
df_sorted = df.sort("test_score", descending=True)

# Ask yourself:
# - What does descending=True do?
# - What happens to null values?
# - Can I sort by multiple columns?

# Experiment:
df_sorted = df.sort(["grade_level", "test_score"], descending=[False, True])
```

### Don't Blindly Accept 🚫

**Be cautious when:**

- The code is complex
- It's security-related
- You don't understand it
- It's domain-specific logic

**Example:**

```python
# Copilot might suggest:
def calculate_gpa(grades):
    return sum(grades) / len(grades)

# But you know GPAs use weighted averages with credits!
def calculate_gpa(grades, credits):
    total_points = sum(g * c for g, c in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits
```

### Use as a Learning Tool 🎓

**Learning workflow:**

1. **Try yourself first** - Attempt the problem
2. **Get stuck?** - Ask Copilot for help
3. **Compare** - How does Copilot's solution differ?
4. **Understand** - Why is Copilot's approach better/different?
5. **Practice** - Try a similar problem yourself

**Example:**

```python
# Your attempt:
students_over_80 = []
for row in df.iter_rows():
    if row['test_score'] > 80:
        students_over_80.append(row)

# Copilot's suggestion:
students_over_80 = df.filter(pl.col("test_score") > 80)

# Learning: Polars has built-in filtering! Much cleaner.
```

---

## 7. Example Workflow: Building a Data Analysis with Copilot

Let's walk through a real analysis using Copilot:

### Step 1: Define the Goal

```python
# Analyze sales data to find:
# 1. Total sales by product category
# 2. Average transaction value by region
# 3. Top 5 best-selling products

import polars as pl
import plotly.express as px
```

### Step 2: Load Data (with Copilot)

```python
# Load sales data from JSON file
sales = pl.read_json("data/raw/sales.json")

# View the first few rows to understand structure
sales.head()
```

_Copilot helps with the exact syntax!_

### Step 3: Calculate Metrics (with Copilot)

```python
# Calculate total sales by product category
category_sales = sales.group_by("product_category").agg(
    pl.sum("total_amount").alias("total_sales")
).sort("total_sales", descending=True)

# Calculate average transaction value by region
region_avg = sales.group_by("region").agg(
    pl.mean("total_amount").alias("avg_transaction")
)

# Find top 5 best-selling products by quantity
top_products = sales.group_by("product_name").agg(
    pl.sum("quantity").alias("total_quantity")
).sort("total_quantity", descending=True).head(5)
```

_Copilot suggests aggregations based on your comments!_

### Step 4: Visualize (with Copilot)

```python
# Create bar chart of sales by category
fig_category = px.bar(
    category_sales,
    x="product_category",
    y="total_sales",
    title="Total Sales by Product Category"
)
fig_category.show()

# Create bar chart of average transaction by region
fig_region = px.bar(
    region_avg,
    x="region",
    y="avg_transaction",
    title="Average Transaction Value by Region"
)
fig_region.show()
```

_Copilot knows Plotly syntax!_

### Step 5: Review and Refine

```python
# You notice: Need to handle edge cases
# Ask Copilot Chat: "How do I filter out null values in Polars?"

# Copilot suggests:
sales_clean = sales.drop_nulls(subset=["total_amount"])

# Now re-run your analysis with clean data!
```

---

## 8. When to Use Copilot vs. Think Independently

### Use Copilot When:

**✅ Learning new syntax**

```python
# "How do I join two DataFrames in Polars?"
# Copilot shows you the syntax
```

**✅ Writing boilerplate**

```python
# "Create a function to load and validate CSV data"
# Copilot generates the structure
```

**✅ Stuck on a problem**

```python
# You've been stuck for 10 minutes
# Ask Copilot for ideas
```

**✅ Exploring alternatives**

```python
# "What are different ways to filter this data?"
# Copilot shows options
```

### Think Independently When:

**🧠 Learning fundamentals**

- Don't use Copilot for practice exercises at first
- Try solving on your own first
- Use Copilot to check your work

**🧠 Understanding concepts**

- Make sure you understand what the code does
- Don't move on until you get it
- Ask "why" not just "how"

**🧠 Problem-solving**

- Break down the problem yourself
- Think through the logic
- Consider edge cases

**🧠 Domain expertise**

- Your specific business rules
- Domain calculations
- Unique requirements

---

## 9. Ethical Considerations

### Understanding Your Code

**You are responsible for:**

- Code quality
- Correctness
- Security
- Ethical implications

**Always:**

- Understand before shipping
- Test thoroughly
- Review for biases
- Check licenses (for copied patterns)

### Academic Integrity

**For students:**

- Check your school's AI policy
- Use Copilot as a tutor, not a homework-doer
- Learn from suggestions, don't just copy
- Your learning is the goal!

**In this course:**

- ✅ Use Copilot to understand concepts
- ✅ Use it when stuck
- ✅ Learn from its suggestions
- ❌ Don't use it to skip learning

### Copilot Etiquette

**Good practices:**

- Give credit: "Generated with Copilot assistance"
- Verify accuracy
- Improve suggestions
- Report issues (wrong/harmful suggestions)

---

## 10. Troubleshooting Copilot

### Suggestions Not Appearing

**Solutions:**

1. Check Copilot is enabled (bottom status bar)
2. Sign in to GitHub
3. Check subscription is active
4. Reload VS Code
5. Check extension settings

### Suggestions Are Wrong

**Solutions:**

1. Provide more context in comments
2. Be more specific
3. Try rephrasing
4. Ask Copilot Chat for explanation
5. Use your judgment!

### Copilot Is Slow

**Solutions:**

1. Check internet connection
2. Reduce open files
3. Restart VS Code
4. Check GitHub status

---

## Keyboard Shortcuts

| Action              | Shortcut             |
| ------------------- | -------------------- |
| Accept suggestion   | Tab                  |
| Reject suggestion   | Esc                  |
| Next suggestion     | Alt/Opt + ]          |
| Previous suggestion | Alt/Opt + [          |
| Open Copilot Chat   | Ctrl/Cmd + Shift + I |
| Inline Chat         | Ctrl/Cmd + I         |

---

## Example Conversations with Copilot Chat

### Question 1: Learning Syntax

```
You: "How do I create a line chart with Plotly Express showing temperature over time?"

Copilot: "Here's how to create a line chart with Plotly Express:

import plotly.express as px
import polars as pl

df = pl.read_csv("weather.csv")
fig = px.line(df, x="date", y="temperature", title="Temperature Over Time")
fig.show()

The px.line() function creates a line chart. The x parameter is your time axis,
y is the value to plot, and title adds a chart title."
```

### Question 2: Debugging

```
You: "I'm getting 'AttributeError: 'DataFrame' object has no attribute 'groupby''. What's wrong?"

Copilot: "In Polars, the method is group_by() with an underscore, not groupby().

Change:
df.groupby("category")

To:
df.group_by("category")

This is different from Pandas which uses groupby() without an underscore."
```

### Question 3: Understanding Code

```
You: "Explain what this does:
df.with_columns((pl.col("price") * 1.1).alias("price_with_tax"))"

Copilot: "This code adds a new column called 'price_with_tax' to the DataFrame.

Breaking it down:
- pl.col("price") - references the price column
- * 1.1 - multiplies by 1.1 (adds 10%)
- .alias("price_with_tax") - names the new column
- with_columns() - adds this as a new column

The original DataFrame isn't modified; it returns a new DataFrame with the extra column."
```

---

## Practice Exercise

Try using Copilot to solve this problem:

**Task:** Load the students dataset, filter for students with test scores above 80, group by grade level, and calculate the average attendance rate for each grade. Then create a bar chart.

**Workflow:**

1. Write comments describing each step
2. Let Copilot suggest code
3. Review and understand each suggestion
4. Run the code
5. Debug if needed with Copilot's help

**Solution approach:**

```python
# Load students dataset from CSV
import polars as pl
import plotly.express as px

students = pl.read_csv("data/raw/students.csv")

# Filter for students with test scores above 80
high_scorers = students.filter(pl.col("test_score") > 80)

# Group by grade level and calculate average attendance
attendance_by_grade = high_scorers.group_by("grade_level").agg(
    pl.mean("attendance_rate").alias("avg_attendance")
)

# Create bar chart
fig = px.bar(
    attendance_by_grade,
    x="grade_level",
    y="avg_attendance",
    title="Average Attendance for High Scorers by Grade"
)
fig.show()
```

---

## Next Steps

- Use Copilot as you work through `example_notebooks/`
- Ask Copilot for help during `exercises/`
- Try the mini project with Copilot as your pair programmer
- Experiment! Ask Copilot questions as you learn

---

**Official Resources:**

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Copilot in VS Code](https://code.visualstudio.com/docs/editor/artificial-intelligence)
- [Copilot Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)

---

**Copilot is your AI pair programmer—use it to learn faster and code better! 🤖✨**
