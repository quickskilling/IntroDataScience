# Plotly Visualization

Create beautiful, interactive visualizations with Plotly.

---

## 1. What is Plotly?

Plotly is a powerful visualization library that creates interactive, publication-quality charts.

### Key Features

**Interactive by Default 🖱️**

- Hover to see values
- Zoom and pan
- Click to filter
- Download as image

**Beautiful 🎨**

- Professional themes
- Customizable colors
- Smooth animations
- Publication-ready

**Web-Ready 🌐**

- Exports to HTML
- Works in notebooks
- Shareable dashboards
- Mobile-friendly

**Versatile 📊**

- 40+ chart types
- 3D plots
- Maps
- Statistical charts

---

## 2. Plotly Express vs Graph Objects

Plotly has two APIs: Express (simple) and Graph Objects (detailed).

### Plotly Express (px)

**Use when:** You want quick, beautiful plots with minimal code

```python
import plotly.express as px

# One line to create a chart!
fig = px.scatter(df, x="age", y="test_score", title="Age vs Score")
fig.show()
```

**Pros:**

- Concise syntax
- Smart defaults
- Perfect for exploration
- Great for beginners

### Graph Objects (go)

**Use when:** You need fine-grained control

```python
import plotly.graph_objects as go

# More verbose but more control
fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
fig.update_layout(title="Custom Plot")
fig.show()
```

**Pros:**

- Complete control
- Build complex layouts
- Custom interactivity
- Advanced features

**For this course:** We start with Plotly Express (px), then show Graph Objects when needed!

---

## 3. Basic Plot Types

### Line Charts

**Use for:** Time series, trends, continuous data

```python
import plotly.express as px
import polars as pl

# Load weather data
df = pl.read_csv("data/raw/weather.csv")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="temperature_high",
    title="Daily High Temperature"
)
fig.show()
```

**Customizations:**

```python
fig = px.line(
    df,
    x="date",
    y="temperature_high",
    title="Daily High Temperature",
    labels={"temperature_high": "Temperature (°C)", "date": "Date"},
    line_shape="spline",  # Smooth curves
    markers=True          # Show data points
)
```

### Bar Charts

**Use for:** Comparing categories, counts

```python
# Load sales data
sales = pl.read_json("data/raw/sales.json")

# Sales by category
category_sales = sales.group_by("product_category").agg(
    pl.sum("total_amount").alias("total_sales")
)

# Create bar chart
fig = px.bar(
    category_sales,
    x="product_category",
    y="total_sales",
    title="Sales by Product Category"
)
fig.show()
```

**Horizontal bars:**

```python
fig = px.bar(
    category_sales,
    x="total_sales",      # Swap x and y
    y="product_category",
    orientation='h',       # Horizontal
    title="Sales by Category"
)
```

**Grouped bars:**

```python
# Sales by category and region
fig = px.bar(
    sales.group_by(["product_category", "region"]).agg(pl.sum("total_amount")),
    x="product_category",
    y="total_amount",
    color="region",        # Group by region
    barmode="group",       # Side-by-side bars
    title="Sales by Category and Region"
)
```

### Scatter Plots

**Use for:** Relationships between variables, correlations

```python
students = pl.read_csv("data/raw/students.csv")

# Attendance vs test score
fig = px.scatter(
    students,
    x="attendance_rate",
    y="test_score",
    title="Attendance vs Test Score",
    trendline="ols"  # Add trend line
)
fig.show()
```

**Color by category:**

```python
fig = px.scatter(
    students,
    x="attendance_rate",
    y="test_score",
    color="grade_level",  # Color by grade
    size="age",           # Size by age
    hover_data=["name"],  # Show name on hover
    title="Attendance vs Test Score by Grade"
)
```

### Histograms

**Use for:** Distributions, frequency counts

```python
# Distribution of test scores
fig = px.histogram(
    students,
    x="test_score",
    nbins=20,
    title="Distribution of Test Scores"
)
fig.show()
```

**Overlaid distributions:**

```python
fig = px.histogram(
    students,
    x="test_score",
    color="grade_level",  # Overlay by grade
    barmode="overlay",    # Overlap bars
    opacity=0.7,          # Make transparent
    title="Test Score Distribution by Grade"
)
```

---

## 4. Customization

### Colors and Themes

```python
# Built-in color scales
fig = px.bar(
    df,
    x="category",
    y="value",
    color="category",
    color_discrete_sequence=px.colors.qualitative.Set3  # Color palette
)

# Custom colors
fig = px.bar(
    df,
    x="category",
    y="value",
    color_discrete_map={
        "A": "#FF6B6B",
        "B": "#4ECDC4",
        "C": "#45B7D1"
    }
)

# Continuous color scale
fig = px.scatter(
    df,
    x="x",
    y="y",
    color="value",
    color_continuous_scale="Viridis"  # Color gradient
)
```

**Available themes:**

```python
import plotly.io as pio

# Set global theme
pio.templates.default = "plotly_white"  # Clean white background

# Other themes: "plotly", "plotly_dark", "ggplot2", "seaborn", "simple_white"
```

### Labels and Titles

```python
fig = px.scatter(df, x="age", y="score")

# Update labels
fig.update_layout(
    title="Student Performance Analysis",
    title_font_size=20,
    xaxis_title="Student Age (years)",
    yaxis_title="Test Score (out of 100)",
    font=dict(family="Arial", size=12)
)
```

### Legends and Annotations

```python
# Customize legend
fig.update_layout(
    legend=dict(
        title="Legend Title",
        orientation="h",      # Horizontal
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Add text annotation
fig.add_annotation(
    x=50,
    y=90,
    text="High performers",
    showarrow=True,
    arrowhead=2
)

# Add shape (rectangle, circle, line)
fig.add_shape(
    type="rect",
    x0=40, x1=60, y0=80, y1=100,
    fillcolor="yellow",
    opacity=0.2,
    line_width=0
)
```

---

## 5. Interactive Features

Plotly charts are interactive by default! Here's what users can do:

### Hover Information

```python
# Customize hover text
fig = px.scatter(
    students,
    x="attendance_rate",
    y="test_score",
    hover_name="name",              # Bold name on hover
    hover_data={
        "age": True,                 # Show age
        "grade_level": True,         # Show grade
        "attendance_rate": ":.1f",   # Format to 1 decimal
        "test_score": False          # Don't show (already axis)
    }
)
```

**Custom hover template:**

```python
fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>" +
                  "Score: %{y:.1f}<br>" +
                  "Attendance: %{x:.1f}%<br>" +
                  "<extra></extra>"  # Remove trace name
)
```

### Zoom and Pan

Users can:

- **Drag**: Pan the view
- **Scroll**: Zoom in/out
- **Double-click**: Reset view
- **Click-drag**: Zoom to selection

```python
# Control zoom behavior
fig.update_xaxes(fixedrange=True)  # Disable x-axis zoom
fig.update_yaxes(fixedrange=True)  # Disable y-axis zoom
```

### Click to Filter

```python
# Enable click to filter
fig = px.bar(df, x="category", y="value")
fig.update_traces(
    marker_line_color='rgb(8,48,107)',
    marker_line_width=1.5
)
```

---

## 6. Subplots and Multiple Charts

### Side-by-Side Subplots

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Create subplot structure
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Temperature High", "Temperature Low")
)

# Add traces
df = pl.read_csv("data/raw/weather.csv")

fig.add_trace(
    go.Scatter(x=df["date"], y=df["temperature_high"], name="High"),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df["date"], y=df["temperature_low"], name="Low"),
    row=1, col=2
)

fig.update_layout(height=400, title_text="Weather Comparison")
fig.show()
```

### Stacked Subplots

```python
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=("Sales Over Time", "Sales by Category")
)

# Top plot: Line chart
fig.add_trace(
    go.Scatter(x=dates, y=values, name="Sales"),
    row=1, col=1
)

# Bottom plot: Bar chart
fig.add_trace(
    go.Bar(x=categories, y=totals, name="Categories"),
    row=2, col=1
)

fig.update_layout(height=600, showlegend=False)
fig.show()
```

### Mixed Chart Types

```python
fig = make_subplots(
    rows=2, cols=2,
    specs=[
        [{"type": "scatter"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "pie"}]
    ],
    subplot_titles=("Scatter", "Bar", "Line", "Pie")
)

# Add different chart types
fig.add_trace(go.Scatter(x=[1,2,3], y=[4,5,6]), row=1, col=1)
fig.add_trace(go.Bar(x=[1,2,3], y=[4,5,6]), row=1, col=2)
fig.add_trace(go.Scatter(x=[1,2,3], y=[6,5,4]), row=2, col=1)
fig.add_trace(go.Pie(labels=["A","B","C"], values=[1,2,3]), row=2, col=2)

fig.update_layout(height=600, showlegend=False)
fig.show()
```

---

## 7. Integrating with Polars DataFrames

Plotly works seamlessly with Polars!

### Direct Integration

```python
import polars as pl
import plotly.express as px

# Load data with Polars
df = pl.read_csv("data/raw/students.csv")

# Plot directly (Plotly handles Polars DataFrames)
fig = px.scatter(df, x="attendance_rate", y="test_score")
fig.show()
```

### Polars → Plotly Pipeline

```python
# Wrangle with Polars, visualize with Plotly
result = (
    pl.read_json("data/raw/sales.json")
    .group_by("product_category")
    .agg(
        pl.sum("total_amount").alias("total_sales"),
        pl.count().alias("num_transactions")
    )
    .sort("total_sales", descending=True)
)

# Create visualization
fig = px.bar(
    result,
    x="product_category",
    y="total_sales",
    title="Sales by Category",
    text="num_transactions"  # Show count on bars
)
fig.show()
```

### Convert if Needed

```python
# If Plotly doesn't recognize format, convert to dict
polars_df = pl.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

fig = px.scatter(
    polars_df.to_dict(),  # Convert to dictionary
    x="x",
    y="y"
)
```

---

## 8. Exporting Plots

### Save as HTML

```python
fig.write_html("plot.html")

# Open in browser to view
# File is self-contained and interactive!
```

### Save as Image

```python
# Requires kaleido package
# Install: uv add kaleido

fig.write_image("plot.png")
fig.write_image("plot.jpg")
fig.write_image("plot.pdf")
fig.write_image("plot.svg")  # Vector format
```

### Control Size

```python
fig.write_image("plot.png", width=1200, height=800)
```

### Show in Marimo

Plots display automatically in Marimo notebooks:

```python
import marimo as mo
import plotly.express as px

fig = px.scatter(df, x="x", y="y")
fig  # Just reference the figure - it displays automatically!
```

---

## 9. Gallery of Examples

### Example 1: Time Series with Range Selector

```python
weather = pl.read_csv("data/raw/weather.csv")

fig = px.line(
    weather,
    x="date",
    y=["temperature_high", "temperature_low"],
    title="Temperature Range Over Time"
)

# Add range selector
fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all", label="All")
        ])
    )
)

fig.show()
```

### Example 2: Box Plot for Distributions

```python
students = pl.read_csv("data/raw/students.csv")

fig = px.box(
    students,
    x="grade_level",
    y="test_score",
    color="grade_level",
    title="Test Score Distribution by Grade"
)
fig.show()
```

### Example 3: Heatmap

```python
# Correlation matrix style
import numpy as np

data = np.random.randn(10, 10)

fig = px.imshow(
    data,
    labels=dict(x="Variable X", y="Variable Y", color="Value"),
    title="Heatmap Example",
    color_continuous_scale="RdBu"
)
fig.show()
```

### Example 4: Pie Chart

```python
sales = pl.read_json("data/raw/sales.json")

category_counts = sales.group_by("product_category").count()

fig = px.pie(
    category_counts,
    values="count",
    names="product_category",
    title="Sales Distribution by Category"
)
fig.show()
```

### Example 5: Animated Scatter

```python
# Animate over time (requires data with time dimension)
fig = px.scatter(
    df,
    x="gdp",
    y="life_expectancy",
    animation_frame="year",  # Animate by year
    animation_group="country",
    size="population",
    color="continent",
    hover_name="country",
    log_x=True,
    range_x=[100, 100000],
    range_y=[25, 90]
)
fig.show()
```

### Example 6: 3D Scatter

```python
fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    color="category",
    title="3D Scatter Plot"
)
fig.show()
```

---

## 10. Complete Dashboard Example

Here's a real-world dashboard combining multiple visualizations:

```python
import polars as pl
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load and prepare data
sales = pl.read_json("data/raw/sales.json")

# Aggregate data
category_sales = sales.group_by("product_category").agg(
    pl.sum("total_amount").alias("total")
).sort("total", descending=True)

region_sales = sales.group_by("region").agg(
    pl.sum("total_amount").alias("total")
).sort("total", descending=True)

daily_sales = sales.group_by("date").agg(
    pl.sum("total_amount").alias("total")
).sort("date")

payment_counts = sales.group_by("payment_method").count()

# Create dashboard with 4 subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Sales by Category",
        "Sales by Region",
        "Daily Sales Trend",
        "Payment Methods"
    ),
    specs=[
        [{"type": "bar"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "pie"}]
    ]
)

# Add traces
fig.add_trace(
    go.Bar(
        x=category_sales["product_category"],
        y=category_sales["total"],
        name="Category",
        marker_color="#FF6B6B"
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=region_sales["region"],
        y=region_sales["total"],
        name="Region",
        marker_color="#4ECDC4"
    ),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(
        x=daily_sales["date"],
        y=daily_sales["total"],
        name="Daily",
        mode="lines",
        line=dict(color="#45B7D1", width=2)
    ),
    row=2, col=1
)

fig.add_trace(
    go.Pie(
        labels=payment_counts["payment_method"],
        values=payment_counts["count"],
        name="Payment"
    ),
    row=2, col=2
)

# Update layout
fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Sales Dashboard",
    title_font_size=24
)

fig.show()
```

---

## Common Patterns

### Pattern 1: Quick Exploration

```python
# Fast exploration with Plotly Express
df = pl.read_csv("data.csv")

px.scatter(df, x="x", y="y").show()
px.histogram(df, x="value").show()
px.box(df, x="category", y="value").show()
```

### Pattern 2: Publication-Quality Chart

```python
fig = px.scatter(df, x="x", y="y")

fig.update_layout(
    template="simple_white",
    font=dict(family="Arial", size=14),
    title=dict(text="Professional Chart", font_size=20),
    xaxis_title="X Variable (units)",
    yaxis_title="Y Variable (units)",
    width=800,
    height=600
)

fig.write_image("publication_chart.pdf")
```

### Pattern 3: Interactive Dashboard

```python
# Combine data wrangling and visualization
import marimo as mo
import polars as pl
import plotly.express as px

# Cell 1: Create filters
category_filter = mo.ui.dropdown(
    options=["All"] + df["category"].unique().to_list(),
    value="All"
)

# Cell 2: Filter and plot (reactive!)
filtered = (
    df if category_filter.value == "All"
    else df.filter(pl.col("category") == category_filter.value)
)

fig = px.scatter(filtered, x="x", y="y", title=f"Category: {category_filter.value}")
fig
```

---

## Quick Reference

```python
import plotly.express as px

# Line chart
px.line(df, x="date", y="value")

# Bar chart
px.bar(df, x="category", y="value")

# Scatter plot
px.scatter(df, x="x", y="y", color="category")

# Histogram
px.histogram(df, x="value", nbins=20)

# Box plot
px.box(df, x="category", y="value")

# Pie chart
px.pie(df, values="value", names="category")

# Heatmap
px.imshow(matrix)

# Customize
fig.update_layout(title="My Chart", template="plotly_white")
fig.update_traces(marker_size=10)

# Save
fig.write_html("chart.html")
fig.write_image("chart.png")  # Requires kaleido
```

---

## Next Steps

- Practice with `example_notebooks/03_plotting.py`
- Try exercises in `exercises/ex02_wrangle_and_plot.py`
- Build your dashboard in `exercises/ex03_mini_project.py`
- Explore [Plotly documentation](https://plotly.com/python/)

---

**Official Resources:**

- [Plotly Python Documentation](https://plotly.com/python/)
- [Plotly Express API](https://plotly.com/python-api-reference/plotly.express.html)
- [Plotly Community](https://community.plotly.com/)

---

**Create beautiful, interactive visualizations with Plotly! 📊✨**
