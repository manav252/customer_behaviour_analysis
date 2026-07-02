import pandas as pd


def add_customer_segments(df: pd.DataFrame) -> pd.DataFrame:
    """Create simple customer segments from previous purchase counts."""
    featured_df = df.copy()
    featured_df["customer_segment"] = pd.cut(
        featured_df["previous_purchases"],
        bins=[-1, 1, 10, float("inf")],
        labels=["New", "Returning", "Loyal"],
    )
    return featured_df
