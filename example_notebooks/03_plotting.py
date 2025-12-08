import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Data Visualization with Plotly 📊
        
        **Welcome!** Learn to create beautiful, interactive visualizations.
        
        **What you'll learn:**
        - Line charts (trends over time)
        - Bar charts (categorical comparisons)
        - Scatter plots (relationships)
        - Histograms (distributions)
        - Customizing plots
        - Interactive features
        
        **Estimated time:** 45 minutes
        
        ---
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 1. Setup and Load Data""")
    return


@app.cell
def __():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    
    # Load datasets
    try:
        weather = pl.read_parquet("../data/raw/weather.parquet")
    except:
        weather = pl.read_csv("../data/raw/weather.csv")
    
    sales = pl.read_json("../data/raw/sales.json")
    students = pl.read_csv("../data/raw/students.csv")
    
    print("✓ Data loaded successfully!")
    return go, pl, px, sales, students, weather


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 2. Line Charts - Trends Over Time""")
    return


@app.cell
def __(px, weather):
    # Simple line chart
    fig = px.line(
        weather.head(30),  # First 30 days
        x="date",
        y="temperature_high",
        title="Daily High Temperature (First 30 Days)"
    )
    fig
    return (fig,)


@app.cell
def __(px, weather):
    # Multiple lines on one chart
    fig = px.line(
        weather.head(90),
        x="date",
        y=["temperature_high", "temperature_low"],
        title="Temperature Range (First 90 Days)",
        labels={"value": "Temperature (°C)", "variable": "Type"}
    )
    fig
    return (fig,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 3. Bar Charts - Categorical Comparisons""")
    return


@app.cell
def __(pl, px, students):
    # Count by category
    by_subject = students.group_by("subject").agg([
        pl.count().alias("count")
    ])
    
    fig = px.bar(
        by_subject,
        x="subject",
        y="count",
        title="Number of Students by Subject",
        color="subject"
    )
    fig
    return (by_subject, fig)


@app.cell
def __(pl, px, sales):
    # Sales by category
    category_sales = sales.group_by("product_category").agg([
        pl.col("total_amount").sum().alias("revenue")
    ]).sort("revenue", descending=True)
    
    fig = px.bar(
        category_sales,
        x="product_category",
        y="revenue",
        title="Total Revenue by Product Category",
        labels={"product_category": "Category", "revenue": "Revenue ($)"},
        color="revenue",
        color_continuous_scale="Blues"
    )
    fig
    return (category_sales, fig)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 4. Scatter Plots - Relationships""")
    return


@app.cell
def __(px, students):
    # Relationship between two variables
    fig = px.scatter(
        students,
        x="attendance_rate",
        y="test_score",
        title="Test Score vs Attendance Rate",
        labels={"attendance_rate": "Attendance (%)", "test_score": "Test Score"},
        trendline="ols",  # Add trend line
        color="subject",
        size="age",
        hover_data=["name"]
    )
    fig
    return (fig,)


@app.cell
def __(px, weather):
    # Weather relationships
    fig = px.scatter(
        weather,
        x="humidity",
        y="precipitation",
        title="Humidity vs Precipitation",
        labels={"humidity": "Humidity (%)", "precipitation": "Precipitation (mm)"},
        color="temperature_high",
        color_continuous_scale="RdYlBu_r"
    )
    fig
    return (fig,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 5. Histograms - Distributions""")
    return


@app.cell
def __(px, students):
    # Distribution of a single variable
    fig = px.histogram(
        students,
        x="test_score",
        title="Distribution of Test Scores",
        labels={"test_score": "Test Score"},
        nbins=10,
        color_discrete_sequence=["steelblue"]
    )
    fig
    return (fig,)


@app.cell
def __(px, weather):
    # Compare distributions
    fig = px.histogram(
        weather,
        x="temperature_high",
        title="Distribution of High Temperatures",
        labels={"temperature_high": "Temperature (°C)"},
        nbins=20,
        marginal="box"  # Add box plot on top
    )
    fig
    return (fig,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 6. Customizing Colors and Labels""")
    return


@app.cell
def __(pl, px, students):
    # Create data
    by_grade = students.group_by("grade_level").agg([
        pl.col("test_score").mean().alias("avg_score")
    ]).sort("grade_level")
    
    # Customized bar chart
    fig = px.bar(
        by_grade,
        x="grade_level",
        y="avg_score",
        title="Average Test Score by Grade Level",
        labels={
            "grade_level": "Grade",
            "avg_score": "Average Score"
        },
        color="avg_score",
        color_continuous_scale=["red", "yellow", "green"],
        text="avg_score"
    )
    
    # Update layout
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    fig.update_layout(
        font=dict(size=14),
        showlegend=False,
        plot_bgcolor="white"
    )
    
    fig
    return (by_grade, fig)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 7. Box Plots - Statistical Summary""")
    return


@app.cell
def __(px, students):
    # Box plot to show distribution
    fig = px.box(
        students,
        x="subject",
        y="test_score",
        title="Test Score Distribution by Subject",
        color="subject",
        points="all"  # Show all points
    )
    fig
    return (fig,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 8. Subplots - Multiple Charts""")
    return


@app.cell
def __(go, pl, weather):
    from plotly.subplots import make_subplots
    
    # Prepare monthly data
    weather_monthly = weather.with_columns([
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed")
    ]).with_columns([
        pl.col("date_parsed").dt.month().alias("month")
    ]).group_by("month").agg([
        pl.col("temperature_high").mean().alias("avg_high"),
        pl.col("precipitation").sum().alias("total_precip")
    ]).sort("month")
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Average High Temperature by Month", "Total Precipitation by Month")
    )
    
    # Add traces
    fig.add_trace(
        go.Bar(x=weather_monthly["month"], y=weather_monthly["avg_high"], name="Temp"),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=weather_monthly["month"], y=weather_monthly["total_precip"], name="Precip", marker_color="steelblue"),
        row=2, col=1
    )
    
    # Update layout
    fig.update_xaxes(title_text="Month", row=2, col=1)
    fig.update_yaxes(title_text="Temperature (°C)", row=1, col=1)
    fig.update_yaxes(title_text="Precipitation (mm)", row=2, col=1)
    
    fig.update_layout(height=600, showlegend=False, title_text="Weather Summary")
    
    fig
    return fig, make_subplots, weather_monthly


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 9. Time Series with Date Aggregation""")
    return


@app.cell
def __(pl, px, sales):
    # Prepare daily sales data
    daily_sales = sales.with_columns([
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed")
    ]).group_by("date_parsed").agg([
        pl.col("total_amount").sum().alias("daily_revenue")
    ]).sort("date_parsed")
    
    # Create time series plot
    fig = px.line(
        daily_sales,
        x="date_parsed",
        y="daily_revenue",
        title="Daily Sales Revenue Over Time",
        labels={"date_parsed": "Date", "daily_revenue": "Revenue ($)"}
    )
    
    fig.update_traces(line_color="darkgreen")
    fig.update_layout(hovermode="x unified")
    
    fig
    return (daily_sales, fig)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 10. Interactive Features""")
    return


@app.cell
def __(px, sales):
    # Rich interactive plot with multiple dimensions
    fig = px.scatter(
        sales.head(100),  # First 100 transactions
        x="unit_price",
        y="total_amount",
        size="quantity",
        color="product_category",
        hover_data=["product_name", "payment_method", "region"],
        title="Sales Analysis (First 100 Transactions)",
        labels={
            "unit_price": "Unit Price ($)",
            "total_amount": "Total Amount ($)"
        }
    )
    
    fig.update_layout(
        hovermode="closest",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    
    fig
    return (fig,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 11. Heatmap - Correlation Matrix""")
    return


@app.cell
def __(go, weather):
    # Calculate correlation matrix
    numeric_cols = ["temperature_high", "temperature_low", "precipitation", "humidity", "wind_speed"]
    corr_data = weather.select(numeric_cols).to_pandas().corr()
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=corr_data.values,
        x=corr_data.columns,
        y=corr_data.columns,
        colorscale="RdBu",
        zmid=0,
        text=corr_data.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10}
    ))
    
    fig.update_layout(
        title="Weather Variables Correlation Matrix",
        width=600,
        height=600
    )
    
    fig
    return corr_data, fig, numeric_cols


@app.cell(hide_code=True)
def __(mo):
    mo.md(r"""## 12. Pie Chart - Proportions""")
    return


@app.cell
def __(pl, px, sales):
    # Sales by region
    region_sales = sales.group_by("region").agg([
        pl.col("total_amount").sum().alias("revenue")
    ])
    
    fig = px.pie(
        region_sales,
        values="revenue",
        names="region",
        title="Sales Distribution by Region",
        hole=0.3  # Make it a donut chart
    )
    
    fig.update_traces(textinfo='percent+label')
    
    fig
    return (fig, region_sales)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 13. Combining Everything
        
        Let's create a comprehensive sales dashboard:
        """
    )
    return


@app.cell
def __(go, pl, sales):
    from plotly.subplots import make_subplots
    
    # Prepare data
    monthly = sales.with_columns([
        pl.col("date").str.strptime(pl.Date, "%Y-%m-%d").alias("date_parsed")
    ]).with_columns([
        pl.col("date_parsed").dt.month().alias("month")
    ]).group_by("month").agg([
        pl.col("total_amount").sum().alias("revenue")
    ]).sort("month")
    
    by_category = sales.group_by("product_category").agg([
        pl.col("total_amount").sum().alias("revenue")
    ]).sort("revenue", descending=True)
    
    by_region = sales.group_by("region").agg([
        pl.col("total_amount").sum().alias("revenue")
    ])
    
    # Create dashboard
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Monthly Revenue Trend", "Revenue by Category", 
                       "Revenue by Region", "Transactions by Payment Method"),
        specs=[[{"type": "scatter"}, {"type": "bar"}],
               [{"type": "bar"}, {"type": "pie"}]]
    )
    
    # Monthly trend
    fig.add_trace(
        go.Scatter(x=monthly["month"], y=monthly["revenue"], mode='lines+markers', name="Monthly"),
        row=1, col=1
    )
    
    # By category
    fig.add_trace(
        go.Bar(x=by_category["product_category"], y=by_category["revenue"], name="Category"),
        row=1, col=2
    )
    
    # By region
    fig.add_trace(
        go.Bar(x=by_region["region"], y=by_region["revenue"], name="Region"),
        row=2, col=1
    )
    
    # Payment methods
    payment = sales.group_by("payment_method").agg([pl.count().alias("count")])
    fig.add_trace(
        go.Pie(labels=payment["payment_method"], values=payment["count"], name="Payment"),
        row=2, col=2
    )
    
    fig.update_layout(height=800, showlegend=False, title_text="Sales Dashboard")
    
    fig
    return by_category, by_region, fig, make_subplots, monthly, payment


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 🎉 Excellent Work!
        
        You've mastered data visualization with Plotly! You now know:
        - ✅ Line charts for trends
        - ✅ Bar charts for comparisons
        - ✅ Scatter plots for relationships
        - ✅ Histograms for distributions
        - ✅ Box plots for statistical summaries
        - ✅ Heatmaps for correlations
        - ✅ Pie charts for proportions
        - ✅ Subplots for dashboards
        - ✅ Interactive features and customization
        
        **Next step:** Start practicing with Exercise 1 in the `exercises/` folder!
        """
    )
    return


@app.cell
def __():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
