import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Exercise 3: Mini Project - Sales Analysis Dashboard 🎯
        
        **Put everything together in a real data analysis project!**
        
        **Estimated time:** 60 minutes
        
        **Your Mission:**
        You're a data analyst for a retail company. Your manager needs insights about sales performance to make business decisions. Create a comprehensive analysis with visualizations.
        
        **Deliverables:**
        1. Data cleaning and preparation
        2. Key business metrics
        3. Multiple visualizations
        4. Written insights and recommendations
        
        **Instructions:**
        - Work through each section
        - Write code AND analysis
        - Create professional visualizations
        - Think like a data analyst!
        
        ---
        """
    )
    return


@app.cell
def __():
    import polars as pl
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import marimo as mo
    return go, make_subplots, mo, pl, px


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 1: Load and Understand the Data
        
        First, load the sales dataset and get familiar with it.
        """
    )
    return


@app.cell
def __(pl):
    # TODO: Load the sales.json file
    sales = pl.read_json("../data/raw/sales.json")
    
    # TODO: Display the first 10 rows to understand the structure
    
    return (sales,)


@app.cell
def __(sales):
    # TODO: Answer these questions about the dataset:
    # 1. How many transactions are in the dataset?
    # 2. What is the date range?
    # 3. How many unique customers?
    # 4. How many unique products?
    # 5. What are all the regions?
    
    print("Dataset Overview:")
    print(f"Total transactions: ???")  # Fix this
    print(f"Date range: ??? to ???")  # Fix this
    print(f"Unique customers: ???")  # Fix this
    print(f"Unique products: ???")  # Fix this
    print(f"Regions: ???")  # Fix this
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 2: Data Cleaning
        
        Clean the data to prepare it for analysis.
        """
    )
    return


@app.cell
def __(sales, pl):
    # TODO: The data has some quality issues. Fix them:
    # 1. Convert date column to datetime type
    # 2. Product names have inconsistent capitalization - standardize them
    # 3. Add a "month" column (extract from date)
    # 4. Add a "day_of_week" column (extract from date)
    # 5. Create a "profit_margin" column (assume 30% profit margin: total_amount * 0.30)
    
    sales_clean = (
        sales
        # Add your data cleaning steps here
    )
    
    # Verify your cleaning
    print("Cleaned dataset:")
    return (sales_clean,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 3: Calculate Key Business Metrics
        
        Calculate important metrics that your manager cares about.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Calculate these metrics:
    # 1. Total revenue
    # 2. Total profit (sum of profit_margin column)
    # 3. Average transaction value
    # 4. Total number of transactions
    
    total_revenue = 0  # Fix this
    total_profit = 0  # Fix this
    avg_transaction = 0  # Fix this
    total_transactions = 0  # Fix this
    
    print("=== KEY BUSINESS METRICS ===")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Average Transaction: ${avg_transaction:,.2f}")
    print(f"Total Transactions: {total_transactions:,}")
    return avg_transaction, total_profit, total_revenue, total_transactions


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 4: Category Analysis
        
        Analyze performance by product category.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Create a summary by product_category with:
    # - Total revenue
    # - Total profit
    # - Number of transactions
    # - Average transaction value
    # Sort by total revenue descending
    
    category_summary = None  # Write your analysis here
    
    print("Category Performance:")
    return (category_summary,)


@app.cell
def __(category_summary, px):
    # TODO: Create a bar chart showing revenue by category
    # Make it professional:
    # - Sorted by revenue (highest to lowest)
    # - Custom color scheme
    # - Clear title and labels
    # - Format y-axis to show currency
    
    fig_category = None
    
    # Uncomment when ready:
    # fig_category.show()
    return (fig_category,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 5: Regional Analysis
        
        Compare performance across regions.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Create a regional summary with:
    # - Total revenue per region
    # - Total transactions per region
    # - Average transaction value per region
    
    regional_summary = None
    
    return (regional_summary,)


@app.cell
def __(go, make_subplots, regional_summary):
    # TODO: Create a subplot figure with 2 charts:
    # 1. Bar chart of revenue by region
    # 2. Bar chart of number of transactions by region
    # This helps identify high-revenue vs high-volume regions
    
    fig_regional = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Revenue by Region", "Transactions by Region")
    )
    
    # Add your traces here
    
    fig_regional.update_layout(
        height=400,
        showlegend=False,
        title_text="Regional Performance Comparison"
    )
    
    # Uncomment when ready:
    # fig_regional.show()
    return (fig_regional,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 6: Time-Based Analysis
        
        Understand how sales vary over time.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Calculate daily total sales
    # Group by date and sum the total_amount
    
    daily_sales = None
    
    return (daily_sales,)


@app.cell
def __(daily_sales, px):
    # TODO: Create a line chart showing daily sales trends
    # Add:
    # - A rolling average line to smooth out noise (optional, advanced)
    # - Clear title and axis labels
    # - Grid lines for readability
    
    fig_daily = None
    
    # Uncomment when ready:
    # fig_daily.show()
    return (fig_daily,)


@app.cell
def __(sales_clean):
    # TODO: Calculate sales by day of week
    # Which day has the highest sales? Lowest?
    
    dow_sales = None
    
    print("Sales by Day of Week:")
    return (dow_sales,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 7: Payment Method Analysis
        
        Understand customer payment preferences.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Analyze by payment method:
    # - Count transactions
    # - Calculate total revenue
    # - Calculate percentage of total transactions
    
    payment_summary = None
    
    return (payment_summary,)


@app.cell
def __(payment_summary, px):
    # TODO: Create a pie chart showing the distribution of payment methods
    # Use the transaction counts
    
    fig_payment = None
    
    # Uncomment when ready:
    # fig_payment.show()
    return (fig_payment,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 8: Advanced - Customer Behavior
        
        Dig deeper into customer patterns.
        """
    )
    return


@app.cell
def __(sales_clean):
    # TODO: Analyze customer behavior:
    # Group by customer_id and calculate:
    # - Total amount spent (lifetime value)
    # - Number of transactions
    # - Average transaction size
    # - Favorite payment method (mode)
    
    customer_summary = None
    
    return (customer_summary,)


@app.cell
def __(customer_summary):
    # TODO: Identify VIP customers (top 10% by total spend)
    
    # Calculate the 90th percentile threshold
    vip_threshold = 0  # Fix this
    
    vip_customers = None  # Filter customers above threshold
    
    print(f"VIP Customer threshold: ${vip_threshold:,.2f}")
    print(f"Number of VIP customers: {len(vip_customers) if vip_customers is not None else 0}")
    return vip_customers, vip_threshold


@app.cell
def __(customer_summary, px):
    # TODO: Create a histogram of customer lifetime values
    # This shows the distribution of customer spending
    
    fig_customer_dist = None
    
    # Uncomment when ready:
    # fig_customer_dist.show()
    return (fig_customer_dist,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 9: Create an Executive Dashboard
        
        Combine your best visualizations into one dashboard.
        """
    )
    return


@app.cell
def __(
    category_summary,
    daily_sales,
    go,
    make_subplots,
    payment_summary,
    regional_summary,
):
    # TODO: Create a 2x2 dashboard with:
    # Top-left: Revenue by Category (bar)
    # Top-right: Revenue by Region (bar)
    # Bottom-left: Daily Sales Trend (line)
    # Bottom-right: Payment Methods (pie)
    
    # This is challenging! Use make_subplots with specs
    
    dashboard = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Revenue by Category",
            "Revenue by Region", 
            "Daily Sales Trend",
            "Payment Methods"
        ),
        specs=[
            [{"type": "bar"}, {"type": "bar"}],
            [{"type": "scatter"}, {"type": "pie"}]
        ]
    )
    
    # TODO: Add traces for each subplot
    # Use row and col parameters in add_trace()
    
    dashboard.update_layout(
        height=800,
        showlegend=True,
        title_text="Sales Performance Dashboard"
    )
    
    # Uncomment when ready:
    # dashboard.show()
    return (dashboard,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## Step 10: Insights and Recommendations
        
        Write your analysis! This is what makes you a data analyst, not just a coder.
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ### TODO: Write Your Analysis Here
        
        Answer these questions based on your analysis:
        
        **1. Top Performing Categories**
        - Which product category generates the most revenue?
        - Which category has the highest profit margin?
        - Your insight: [Write your observation]
        
        **2. Regional Performance**
        - Which region is strongest? Weakest?
        - Are there opportunities for growth in underperforming regions?
        - Your recommendation: [Write your recommendation]
        
        **3. Temporal Patterns**
        - Are there clear trends over time (seasonality, growth, decline)?
        - Which days of the week are busiest?
        - Your insight: [Write your observation]
        
        **4. Customer Behavior**
        - What percentage of customers are VIPs?
        - What is the typical customer lifetime value?
        - Your recommendation for customer retention: [Write your recommendation]
        
        **5. Payment Preferences**
        - What is the most popular payment method?
        - Should the company prioritize certain payment methods?
        - Your insight: [Write your observation]
        
        **6. Key Recommendations for Management**
        
        Based on your analysis, what are your top 3 recommendations?
        
        1. [Your recommendation]
        2. [Your recommendation]
        3. [Your recommendation]
        
        ---
        
        **Remember:** Good data analysis tells a story. Don't just report numbers - explain what they mean and what actions should be taken!
        """
    )
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 🎉 Congratulations!
        
        You've completed a real data analysis project from start to finish!
        
        **What you accomplished:**
        - ✅ Loaded and cleaned real-world data
        - ✅ Calculated business metrics
        - ✅ Performed multi-dimensional analysis
        - ✅ Created professional visualizations
        - ✅ Built an executive dashboard
        - ✅ Delivered insights and recommendations
        
        **This is exactly what data analysts do in real jobs!**
        
        **What's next?**
        - Compare with `solutions/ex03_mini_project.py`
        - Experiment with the data - ask your own questions!
        - Try analyzing different datasets
        - Build your own projects
        
        **You're now ready to:**
        - Analyze data independently
        - Create dashboards for stakeholders
        - Answer business questions with data
        - Continue learning advanced techniques
        
        ---
        
        ## Keep Learning! 🚀
        
        **Next steps in your data science journey:**
        1. **Statistical Analysis**: Learn about correlations, distributions, hypothesis testing
        2. **Machine Learning**: Build predictive models with scikit-learn
        3. **Advanced Visualization**: Master Plotly, create interactive dashboards
        4. **Big Data**: Work with larger datasets using DuckDB or Spark
        5. **Real Projects**: Find datasets on Kaggle and build your portfolio
        
        **Resources:**
        - Polars documentation: https://pola-rs.github.io/polars/
        - Plotly documentation: https://plotly.com/python/
        - Kaggle datasets: https://www.kaggle.com/datasets
        - GitHub for portfolio: Share your projects!
        
        **Great job completing this course! 🎊**
        """
    )
    return


if __name__ == "__main__":
    app.run()
