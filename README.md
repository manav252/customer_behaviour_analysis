# Customer Behaviour Analysis

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243)
![SQL](https://img.shields.io/badge/SQL-Analytics-4479A1)
![Power%20BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![License](https://img.shields.io/badge/License-MIT-green)

End-to-end customer shopping behavior analytics project using Python, SQL, and Power BI.

## Problem Statement

Retail teams need to understand revenue drivers, customer segments, purchase frequency, product preferences, and promotion behavior. This project analyzes customer shopping data to identify category-level performance, customer segments, and business insights that can support merchandising and marketing decisions.

## Dataset / Source

The dataset is stored in `data/customer_shopping_behavior.csv` and contains customer demographics, product categories, purchase amount, location, season, discount usage, previous purchases, and payment behavior.

## Tech Stack

- Python
- Pandas
- NumPy
- SQL / PostgreSQL
- Power BI
- PowerPoint

## Workflow

1. Load customer shopping data.
2. Clean column names and remove duplicates.
3. Engineer age groups and customer segments.
4. Run SQL analysis for revenue, products, subscriptions, and repeat buyers.
5. Build Power BI dashboard views.
6. Summarize insights in reports and presentation artifacts.

## Methodology

- Standardized raw CSV column names into snake_case.
- Created age groups and customer segments based on previous purchases.
- Used SQL aggregation and window functions for business questions.
- Prepared dashboard artifacts for executive-style reporting.

## Key Features

- Revenue by category
- Subscription vs spending
- Discount behavior
- Customer segmentation
- Top products per category
- Power BI dashboard artifact

## Results / Insights

- Category-level revenue helps identify high-performing product groups.
- Previous purchases can segment customers into new, returning, and loyal groups.
- Subscription and discount usage can be compared against total revenue and average spend.

## Screenshots

Add exported Power BI screenshots to `screenshots/`.

## How to Run Locally

```bash
pip install -r requirements.txt
pytest -q
```

SQL queries are available in `src/customer_analysis.sql`.

## Folder Structure

```text
.
├── data/
├── docs/
├── reports/
├── screenshots/
├── src/
├── tests/
├── README.md
└── requirements.txt
```

## Future Improvements

- Add an automated Python EDA notebook.
- Export cleaned data for Power BI.
- Add churn or repeat-purchase prediction if a suitable target is defined.
