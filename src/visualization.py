import pandas as pd


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Return category-level revenue for charts or Power BI validation."""
    return (
        df.groupby("category", as_index=False)["purchase_amount_usd"]
        .sum()
        .sort_values("purchase_amount_usd", ascending=False)
    )
