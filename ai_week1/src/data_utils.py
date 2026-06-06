import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV and show a quick summary."""
    df = pd.read_csv(path)
    print(df.info())
    print(df.describe(include='all'))
    return df
