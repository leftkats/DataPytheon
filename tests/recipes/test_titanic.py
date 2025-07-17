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
        "sibsp",
        "parch",
        "fare",
        "embarked",
        "class",
        "who",
        "adult_male",
        "alone"
    }
    
    missing_cols = expected_cols - set(df.columns)
    print(f"Missing columns: {missing_cols}")
    assert not missing_cols, f"Missing expected columns: {missing_cols}"

    # Check that 'embarked' column has more than one categorical values
    assert df["embarked"].nunique() > 1, "'embarked' column should have more than one unique value"

    # Check that no null values exist in the DataFrame
    assert df.isnull().sum().sum() == 0, "DataFrame should not contain any null values"

    # Check that some rows exist
    assert len(df) > 0, "DataFrame should not be empty"
    