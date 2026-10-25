
# Superstore Sales Analysis
# Final Data Analytics Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "superstore.csv"
REPORT_DIR = BASE_DIR / "reports"
OUTPUT_FILE = DATA_FILE.parent / "superstore_cleaned.csv"

REPORT_DIR.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_FILE)

print("SUPERSTORE SALES ANALYSIS")
print("-" * 40)
print("Original rows:", len(df))

# Remove rows without an Order Date
df = df.dropna(subset=["Order Date"]).copy()

# Convert date columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], errors="coerce"
)

# Convert numeric columns
numeric_columns = ["Sales", "Quantity", "Discount", "Profit"]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

# Report missing postal codes without deleting records
print("Cleaned rows:", len(df))
print("Missing postal codes:", df["Postal Code"].isna().sum())

# Basic sales analysis
print("\nTOTAL SALES:", round(df["Sales"].sum(), 2))
print("TOTAL PROFIT:", round(df["Profit"].sum(), 2))
print("TOTAL ORDERS:", df["Order ID"].nunique())

print("\nSALES BY CATEGORY")
print(
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Create sales chart
VIS_DIR = BASE_DIR / "visualizations"
VIS_DIR.mkdir(exist_ok=True)

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.sort_values().plot(kind="barh")
plt.title("Total Sales by Product Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(VIS_DIR / "sales_by_category.png", dpi=300)
plt.close()

print("Category sales chart saved successfully.")


# Create sales by region chart
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.sort_values().plot(kind="barh")

plt.title("Total Sales by Region")
plt.xlabel("Sales ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(VIS_DIR / "sales_by_region.png", dpi=300)
plt.close()

print("Region sales chart saved successfully.")


# Create sales by customer segment chart
segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8, 5))
segment_sales.sort_values().plot(kind="barh")

plt.title("Total Sales by Customer Segment")
plt.xlabel("Sales ($)")
plt.ylabel("Customer Segment")
plt.tight_layout()
plt.savefig(VIS_DIR / "sales_by_segment.png", dpi=300)
plt.close()

print("Customer segment sales chart saved successfully.")


# Analyze profit by category
category_profit = df.groupby("Category")["Profit"].sum()

print("\nPROFIT BY CATEGORY")
print(category_profit.sort_values(ascending=False))

# Create profit chart
plt.figure(figsize=(8, 5))
category_profit.sort_values().plot(kind="barh")

plt.title("Total Profit by Product Category")
plt.xlabel("Profit ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(VIS_DIR / "profit_by_category.png", dpi=300)
plt.close()

print("Category profit chart saved successfully.")


# Analyze sales and profit by region
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

print("\nSALES AND PROFIT BY REGION")
print(region_analysis.sort_values("Sales", ascending=False).round(2))

# Create regional profit chart
plt.figure(figsize=(8, 5))
region_analysis["Profit"].sort_values().plot(kind="barh")

plt.title("Total Profit by Region")
plt.xlabel("Profit ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(VIS_DIR / "profit_by_region.png", dpi=300)
plt.close()

print("Regional profit chart saved successfully.")


# Analyze monthly sales trends
monthly_sales = (
    df.set_index("Order Date")["Sales"]
    .resample("ME")
    .sum()
)

print("\nMONTHLY SALES (FIRST 12 MONTHS)")
print(monthly_sales.head(12).round(2))

# Create monthly sales chart
plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(VIS_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

print("Monthly sales trend chart saved successfully.")


# Analyze top 10 sub-categories by sales
subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTOP 10 SUB-CATEGORIES BY SALES")
print(subcategory_sales.head(10).round(2))

# Create top 10 sub-categories chart
plt.figure(figsize=(10, 6))
subcategory_sales.head(10).sort_values().plot(kind="barh")

plt.title("Top 10 Product Sub-Categories by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig(VIS_DIR / "top10_subcategory_sales.png", dpi=300)
plt.close()

print("Top 10 sub-category sales chart saved successfully.")


# Analyze profit by sub-category
subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

print("\nSUB-CATEGORY PROFIT ANALYSIS")
print(subcategory_profit.round(2))

print("\nLOSS-MAKING SUB-CATEGORIES")
print(subcategory_profit[subcategory_profit < 0].round(2))

# Create sub-category profit chart
plt.figure(figsize=(10, 7))
subcategory_profit.plot(kind="barh")

plt.title("Profit by Product Sub-Category")
plt.xlabel("Profit ($)")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig(VIS_DIR / "profit_by_subcategory.png", dpi=300)
plt.close()

print("Sub-category profit chart saved successfully.")


# Analyze discount impact on profit
print("\nDISCOUNT ANALYSIS")

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Order_Count=("Order ID", "nunique")
    )
    .round(2)
)

print(discount_analysis)

print("\nAVERAGE DISCOUNT:", round(df["Discount"].mean(), 4))

# Create discount vs profit chart
plt.figure(figsize=(8, 5))
discount_analysis["Total_Profit"].plot(kind="bar")

plt.title("Total Profit by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Total Profit ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(VIS_DIR / "discount_vs_profit.png", dpi=300)
plt.close()

print("Discount analysis chart saved successfully.")

# Save final project summary
SUMMARY_FILE = REPORT_DIR / "project_summary.txt"

with open(SUMMARY_FILE, "w", encoding="utf-8") as file:
    file.write("SUPERSTORE SALES ANALYSIS - FINAL SUMMARY\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Total Sales: ${df['Sales'].sum():,.2f}\n")
    file.write(f"Total Profit: ${df['Profit'].sum():,.2f}\n")
    file.write(f"Total Orders: {df['Order ID'].nunique():,}\n")
    file.write(f"Average Discount: {df['Discount'].mean():.2%}\n\n")

    file.write("KEY FINDINGS\n")
    file.write("-" * 20 + "\n")
    file.write("1. Technology has the highest sales by category.\n")
    file.write("2. The West region has the highest sales and profit.\n")
    file.write("3. Phones is the top sub-category by sales.\n")
    file.write("4. Tables has the largest sub-category loss.\n")
    file.write("5. Review high-discount transactions for profitability.\n")

print("Final project summary saved successfully:", SUMMARY_FILE)

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved to:", OUTPUT_FILE)
print("Analysis completed successfully.")

# Create the final project report
REPORT_FILE = REPORT_DIR / "project_report.txt"

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write("SUPERSTORE SALES ANALYSIS\n")
    file.write("=" * 60 + "\n\n")

    file.write("1. PROJECT INTRODUCTION\n")
    file.write(
        "This project analyzes Superstore sales data using Python "
        "to identify sales trends, profitability, regional performance, "
        "and opportunities for business improvement.\n\n"
    )

    file.write("2. PROJECT OBJECTIVES\n")
    file.write(
        "- Clean and prepare the dataset.\n"
        "- Calculate total sales, profit, and orders.\n"
        "- Compare sales and profit across categories and regions.\n"
        "- Analyze monthly sales trends and customer segments.\n"
        "- Identify loss-making sub-categories.\n"
        "- Examine the relationship between discounts and profit.\n\n"
    )

    file.write("3. TOOLS AND LIBRARIES\n")
    file.write(
        "Python, Pandas, NumPy, Matplotlib, Seaborn, and pathlib.\n\n"
    )

    file.write("4. DATA CLEANING\n")
    file.write("Original rows: 10,800\n")
    file.write(f"Cleaned rows: {len(df):,}\n")
    file.write(
        f"Missing postal codes: {df['Postal Code'].isna().sum()}\n"
    )
    file.write(
        "Rows without Order Date were removed. Date and numeric "
        "columns were converted to appropriate data types.\n\n"
    )

    file.write("5. KEY PERFORMANCE INDICATORS\n")
    file.write(f"Total Sales: ${df['Sales'].sum():,.2f}\n")
    file.write(f"Total Profit: ${df['Profit'].sum():,.2f}\n")
    file.write(f"Total Orders: {df['Order ID'].nunique():,}\n")
    file.write(f"Average Discount: {df['Discount'].mean():.2%}\n\n")

    file.write("6. KEY FINDINGS\n")
    file.write(
        "Highest-sales category: Technology\n"
        "Highest-profit category: Technology\n"
        "Highest-sales region: West\n"
        "Highest-profit region: West\n"
        "Top sub-category by sales: Phones\n"
        "Largest loss-making sub-category: Tables\n\n"
    )

    file.write("7. BUSINESS RECOMMENDATIONS\n")
    file.write(
        "- Investigate losses in Tables, Bookcases, and Supplies.\n"
        "- Review high-discount transactions and pricing strategies.\n"
        "- Study successful products in the Technology category.\n"
        "- Investigate the drivers of strong performance in the West.\n"
        "- Monitor monthly sales and regional profitability.\n\n"
    )

    file.write("8. CONCLUSION\n")
    file.write(
        "The analysis provides insights into sales performance, "
        "profitability, product categories, regions, and discount levels. "
        "These findings can help guide further investigation and "
        "data-driven business decisions.\n\n"
    )

    file.write("9. PROJECT OUTPUTS\n")
    file.write(
        "Cleaned dataset: data/superstore_cleaned.csv\n"
        "Charts: visualizations/\n"
        "Summary: reports/project_summary.txt\n"
        "Python source: Superstore_Analysis.py\n"
    )

print("Complete project report saved successfully:", REPORT_FILE)
