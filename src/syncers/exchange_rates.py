"""
Exchange Rates Syncer
----------------------
Fetches real-time exchange rates using the Frankfurter API.
Source: https://www.frankfurter.app/

Steps:
- Calls the public API (no API key required)
- Retrieves exchange rates for a given base currency
- Converts the result into a pandas DataFrame
"""

import pandas as pd
import requests


def fetch_exchange_rates(base_currency="USD"):
    """
    Fetches latest exchange rates for the given base currency.

    Parameters:
        base_currency (str): ISO 4217 code (e.g., 'USD', 'EUR', 'GBP')

    Returns:
        pd.DataFrame: Tidy DataFrame with rates and metadata
    """
    url = f"https://api.frankfurter.app/latest?from={base_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"API request failed with status {response.status_code}: {response.text}"
        )

    data = response.json()

    # Flatten into DataFrame
    df = pd.DataFrame(list(data["rates"].items()), columns=["currency", "rate"])
    df["base"] = data["base"]
    df["date"] = data["date"]

    return df


# Example usage
if __name__ == "__main__":
    df = fetch_exchange_rates("USD")
    print(df.head())
