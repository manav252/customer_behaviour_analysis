# Customer Behaviour Analysis Insights

## Executive Summary

This project analyzes retail customer shopping behavior to identify revenue drivers, customer segments, and purchasing patterns. The project includes Python analysis, SQL queries, a Streamlit dashboard, and existing Power BI report artifacts.

## Data Quality Notes

- The dataset contains 3,900 customer purchase records.
- Column names are standardized into snake_case for Python and SQL workflows.
- Duplicate records are removed before analysis.
- Purchase amount is converted to a numeric field for revenue analysis.

## Key Insights

- Category-level revenue helps identify which merchandise groups contribute most to total sales.
- Customer segments based on previous purchases separate new, returning, and loyal shoppers.
- Subscription status, discount usage, and purchase frequency can be compared against average order value to support marketing decisions.
- Seasonal revenue patterns can help guide inventory planning and campaign timing.

## Business Impact

- Marketing teams can use customer segments to target loyalty, reactivation, and first-purchase campaigns.
- Merchandising teams can use category and season insights for product planning.
- The dashboard gives non-technical stakeholders a quick way to scan revenue and behavior trends.

## Dashboard Artifacts

- `app.py` provides a Streamlit dashboard for Python-based analytics.
- `reports/customer_behavior_dashboard.pbix` is included as a Power BI file.
- PDF and PPTX report artifacts are available in `reports/`.

## Limitations

- The dataset is transactional and does not include profit margins, campaign spend, or web/app behavior.
- Predictive modeling is not included because there is no clear churn or future purchase target in the current dataset.

## Future Improvements

- Add customer lifetime value segmentation if repeat transaction history becomes available.
- Add cohort analysis by first purchase season.
- Export dashboard screenshots from Power BI and Streamlit for README display.
- Add a repeat-purchase prediction model if a future target variable is defined.
