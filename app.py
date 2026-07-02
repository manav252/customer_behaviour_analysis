from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.data_processing import load_customer_data
from src.feature_engineering import add_customer_segments
from src.visualization import revenue_by_category


PROJECT_ROOT = Path(__file__).resolve().parent


@st.cache_data
def get_data() -> pd.DataFrame:
    """Load cleaned customer shopping data for dashboard use."""
    df = load_customer_data(PROJECT_ROOT / "data" / "customer_shopping_behavior.csv")
    return add_customer_segments(df)


def draw_bar(data: pd.DataFrame, x: str, y: str, title: str, color: str = "#2F80ED") -> None:
    """Render a reusable dashboard bar chart."""
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=data, x=x, y=y, ax=ax, color=color)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="x", rotation=25)
    st.pyplot(fig, use_container_width=True)


st.set_page_config(
    page_title="Customer Behaviour Analysis",
    page_icon="C",
    layout="wide",
)

st.title("Customer Behaviour Analysis")
st.caption("Retail analytics dashboard using Python, Pandas, SQL-ready data, and Power BI artifacts.")

df = get_data()

overview_tab, revenue_tab, segments_tab, behavior_tab = st.tabs(
    ["Overview", "Revenue Insights", "Customer Segments", "Purchase Behavior"]
)

with overview_tab:
    total_customers = df["customer_id"].nunique()
    total_revenue = df["purchase_amount_usd"].sum()
    average_order_value = df["purchase_amount_usd"].mean()
    repeat_purchase_median = df["previous_purchases"].median()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Customers", f"{total_customers:,}")
    col2.metric("Total Revenue", f"${total_revenue:,.0f}")
    col3.metric("Avg Purchase", f"${average_order_value:,.2f}")
    col4.metric("Median Previous Purchases", f"{repeat_purchase_median:.0f}")

    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head(20), use_container_width=True)

with revenue_tab:
    col1, col2 = st.columns(2)
    with col1:
        category_revenue = revenue_by_category(df)
        draw_bar(category_revenue, "category", "purchase_amount_usd", "Revenue by Category")
    with col2:
        season_revenue = (
            df.groupby("season", as_index=False)["purchase_amount_usd"]
            .sum()
            .sort_values("purchase_amount_usd", ascending=False)
        )
        draw_bar(season_revenue, "season", "purchase_amount_usd", "Revenue by Season", "#27AE60")

    location_revenue = (
        df.groupby("location", as_index=False)["purchase_amount_usd"]
        .sum()
        .sort_values("purchase_amount_usd", ascending=False)
        .head(10)
    )
    draw_bar(location_revenue, "location", "purchase_amount_usd", "Top 10 Locations by Revenue", "#9B51E0")

with segments_tab:
    col1, col2 = st.columns(2)
    with col1:
        segment_summary = (
            df.groupby("customer_segment", observed=True)
            .agg(customers=("customer_id", "count"), avg_spend=("purchase_amount_usd", "mean"))
            .reset_index()
        )
        draw_bar(segment_summary, "customer_segment", "customers", "Customer Count by Segment")
    with col2:
        draw_bar(segment_summary, "customer_segment", "avg_spend", "Average Spend by Segment", "#F2994A")

    subscription_summary = (
        df.groupby("subscription_status", as_index=False)["purchase_amount_usd"]
        .mean()
        .rename(columns={"purchase_amount_usd": "avg_purchase_amount"})
    )
    draw_bar(subscription_summary, "subscription_status", "avg_purchase_amount", "Average Purchase by Subscription Status")

with behavior_tab:
    col1, col2 = st.columns(2)
    with col1:
        discount_summary = (
            df.groupby("discount_applied", as_index=False)["purchase_amount_usd"]
            .mean()
            .rename(columns={"purchase_amount_usd": "avg_purchase_amount"})
        )
        draw_bar(discount_summary, "discount_applied", "avg_purchase_amount", "Average Purchase by Discount Usage")
    with col2:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df["review_rating"], bins=12, kde=True, ax=ax, color="#2F80ED")
        ax.set_title("Review Rating Distribution")
        st.pyplot(fig, use_container_width=True)

    frequency_revenue = (
        df.groupby("frequency_of_purchases", as_index=False)["purchase_amount_usd"]
        .mean()
        .sort_values("purchase_amount_usd", ascending=False)
    )
    draw_bar(frequency_revenue, "frequency_of_purchases", "purchase_amount_usd", "Average Purchase by Frequency")
