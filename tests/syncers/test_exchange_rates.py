import pandas as pd

from src.syncers.exchange_rates import fetch_exchange_rates


def test_fetch_exchange_rates_returns_dataframe():
    df = fetch_exchange_rates("USD")

    # Check return type
    assert isinstance(df, pd.DataFrame), "Expected a pandas DataFrame"

    # Check required columns
    expected_columns = {"currency", "rate", "base", "date"}
    assert expected_columns.issubset(df.columns), (
        f"Missing expected columns: {expected_columns - set(df.columns)}"
    )

    # Check if at least one rate exists
    assert len(df) > 0, "Expected at least one exchange rate row"

    # Optional: check types
    assert df["currency"].dtype == object, (
        "'currency' should be of type object (string)"
    )
    assert pd.api.types.is_numeric_dtype(df["rate"]), "'rate' should be numeric"
