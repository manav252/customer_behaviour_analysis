from src.data_processing import load_customer_data
from src.feature_engineering import add_customer_segments


def test_customer_data_loads():
    df = load_customer_data()
    assert len(df) > 0
    assert "purchase_amount_usd" in df.columns
    assert "age_group" in df.columns


def test_customer_segments_created():
    df = add_customer_segments(load_customer_data())
    assert "customer_segment" in df.columns
