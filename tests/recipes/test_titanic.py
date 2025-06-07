import pandas as pd

from src.recipes.titanic import load_titanic_data


def test_load_titanic_data_returns_dataframe():
    df = load_titanic_data()

    # Check that output is a DataFrame
    assert isinstance(df, pd.DataFrame), "Expected a pandas DataFrame"

    # Check for expected columns (a subset)
    expected_cols = {
        "survived",
        "pclass",
        "sex",
        "age",
        "sibsp",
        "parch",
        "fare",
        "embarked",
    }
    missing_cols = expected_cols - set(df.columns)
    assert not missing_cols, f"Missing expected columns: {missing_cols}"

    # Check no critical nulls remain in 'age' or 'embarked'
    assert df["age"].isnull().sum() == 0, "'age' column should have no nulls"
    assert df["embarked"].isnull().sum() == 0, "'embarked' column should have no nulls"

    # Check that some rows exist
    assert len(df) > 0, "DataFrame should not be empty"
