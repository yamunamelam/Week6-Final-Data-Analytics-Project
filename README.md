# Superstore Sales Analysis

## Project Overview
This project analyzes Superstore sales data using Python to identify sales trends, evaluate profitability, compare regional performance, and generate actionable business insights.

## Objectives
- Clean and prepare sales data.
- Calculate key performance indicators (KPIs).
- Analyze sales and profit by category, region, and customer segment.
- Examine monthly sales trends.
- Identify loss-making sub-categories.
- Investigate the relationship between discounts and profit.

## Tools and Technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- pathlib
- Git and GitHub

## Dataset and Data Cleaning
- Original records: 10,800
- Cleaned records: 9,994
- Missing postal codes: 11
- Rows without Order Date were removed.
- Date and numeric columns were converted to appropriate data types.

## Key Performance Indicators

| Metric | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Average Discount | 15.62% |

## Key Findings
- Technology generated the highest sales and profit among the categories.
- The West region led in sales and profit.
- Phones was the top sub-category by sales.
- Tables was the largest loss-making sub-category.

## Visualizations

The project includes eight charts:

1. [Sales by Category](visualizations/sales_by_category.png)
2. [Profit by Category](visualizations/profit_by_category.png)
3. [Sales by Region](visualizations/sales_by_region.png)
4. [Profit by Region](visualizations/profit_by_region.png)
5. [Sales by Customer Segment](visualizations/sales_by_segment.png)
6. [Monthly Sales Trend](visualizations/monthly_sales_trend.png)
7. [Profit by Sub-category](visualizations/profit_by_subcategory.png)
8. [Discount vs. Profit](visualizations/discount_vs_profit.png)
9. [Top 10 Sub-categories by Sales](visualizations/top10_subcategory_sales.png)

## Business Recommendations
- Investigate losses in Tables, Bookcases, and Supplies.
- Review high-discount transactions and pricing strategies.
- Study successful Technology products.
- Investigate the factors behind the West region's performance.
- Monitor monthly sales and regional profitability.

## Project Structure

```text
Week6-Final-Data-Analytics-Project/
├── data/
│   ├── superstore.csv
│   └── superstore_cleaned.csv
├── reports/
│   ├── project_report.txt
│   └── project_summary.txt
├── visualizations/
│   ├── discount_vs_profit.png
│   ├── monthly_sales_trend.png
│   ├── profit_by_category.png
│   ├── profit_by_region.png
│   ├── profit_by_subcategory.png
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   ├── sales_by_segment.png
│   └── top10_subcategory_sales.png
├── Superstore_Analysis.py
└── README.md
```

## Conclusion
This analysis demonstrates how Python-based data cleaning, exploratory data analysis, and visualization can reveal important business patterns and support data-driven decision-making.

## Author
Yamuna Sree
