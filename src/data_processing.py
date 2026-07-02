from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "customer_shopping_behavior.csv"


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert raw CSV column names into SQL/Python-friendly snake_case names."""
    cleaned_df = df.copy()
    cleaned_df.columns = (
        cleaned_df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
    )
    return cleaned_df


def load_customer_data(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and lightly clean the customer shopping behavior dataset."""
    df = pd.read_csv(path)
    df = clean_column_names(df)
    df = df.drop_duplicates()
    df["purchase_amount_usd"] = pd.to_numeric(
        df["purchase_amount_usd"], errors="coerce"
    )
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 24, 34, 44, 54, 100],
        labels=["18-24", "25-34", "35-44", "45-54", "55+"],
    )
    return df
