# Superstore Sales Analysis

## 1. Project Overview

This project analyzes Superstore sales data using Python and Power BI to understand sales performance, profitability, regional trends, customer segments, and discount patterns. The goal is to generate actionable insights that support data-driven business decisions.

## 2. Problem Statement

The business needs to understand which product categories, sub-categories, regions, and customer segments generate the most sales and profit. The analysis also investigates loss-making products and the relationship between discounts and profitability to identify opportunities for improvement.

## 3. Objectives

- Clean and prepare the dataset for analysis.
- Calculate key performance indicators (KPIs).
- Analyze sales and profit by category, region, and customer segment.
- Examine monthly sales trends.
- Identify loss-making sub-categories.
- Investigate the relationship between discounts and profit.
- Develop a Power BI dashboard to communicate business performance.

## 4. Dataset Description

The project uses a Superstore retail sales dataset containing order information, product categories, customer segments, geographic regions, sales, discounts, and profit.

- Original records: 10,800
- Cleaned records: 9,994
- Missing postal codes: 11

## 5. Tools and Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook or Python script
- Power BI
- Git and GitHub

## 6. Data Cleaning and Preparation

The following preparation steps were performed:

- Inspected the dataset structure and data types.
- Removed rows without Order Date where required.
- Converted date and numeric columns to appropriate data types.
- Checked for missing values and data-quality issues.
- Prepared the cleaned dataset for analysis.
- Saved the cleaned data as `superstore_cleaned.csv`.

## 7. Exploratory Data Analysis (EDA)

The analysis examined descriptive statistics, sales and profit distributions, product performance, regional performance, customer segments, monthly trends, and discount patterns.

### Key Performance Indicators

| Metric | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Average Discount | 15.62% |

### EDA Findings

- Technology generated the highest sales among the three main product categories.
- The West region led in sales and profit.
- Phones was the top sub-category by sales.
- Tables was the largest loss-making sub-category.
- Discount and profit patterns were investigated to understand potential effects on profitability.

Correlation analysis and outlier investigation should be documented with the actual results from the analysis before final submission.

## 8. Data Visualizations

Nine charts were created to communicate the findings:

1. [Sales by Category](visualizations/sales_by_category.png)
2. [Profit by Category](visualizations/profit_by_category.png)
3. [Sales by Region](visualizations/sales_by_region.png)
4. [Profit by Region](visualizations/profit_by_region.png)
5. [Sales by Customer Segment](visualizations/sales_by_segment.png)
6. [Monthly Sales Trend](visualizations/monthly_sales_trend.png)
7. [Profit by Sub-category](visualizations/profit_by_subcategory.png)
8. [Discount vs. Profit](visualizations/discount_vs_profit.png)
9. [Top 10 Sub-categories by Sales](visualizations/top10_subcategory_sales.png)

## 9. Power BI Dashboard

The interactive Power BI dashboard presents important business metrics and sales performance.

Dashboard components include:

- KPI cards for Total Sales, Total Profit, and Total Orders.
- Sales by Category.
- Sales by Region.
- Profit by Category.
- Sales Contribution by Category.
- Sales Trend Over Time.
- Category and Order Date slicers.

The dashboard allows users to filter the report and compare business performance across categories and time periods.

**Dashboard file:** `week 6.pbix`

## 10. Key Business Insights

1. **Category performance:** Technology generated the highest sales and profit among the main categories.
2. **Regional performance:** The West region led in sales and profit.
3. **Product performance:** Phones was the top sub-category by sales.
4. **Loss-making products:** Tables recorded the largest sub-category loss.
5. **Discounts and profitability:** Discount patterns should be reviewed to identify transactions where discounts may reduce profit.
6. **Sales monitoring:** Monthly sales trends can help identify seasonal patterns and changes in demand.

## 11. Business Recommendations

1. Investigate Tables, Bookcases, and Supplies to identify the reasons for losses and assess pricing, costs, and discount policies.
2. Review high-discount transactions and establish discount policies that protect profitability.
3. Study successful Technology products to identify practices that may be useful for other categories.
4. Investigate the factors behind the West region's performance.
5. Monitor monthly sales and regional profitability regularly.

## 12. Project Structure

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
├── week 6.pbix
└── README.md
```

## 13. Conclusion

The project demonstrates how Python-based data cleaning, exploratory data analysis, visualization, and an interactive Power BI dashboard can reveal important retail business patterns. The findings support better decisions about product performance, discounts, regional sales, and profitability.

## Author

Yamuna Sree
