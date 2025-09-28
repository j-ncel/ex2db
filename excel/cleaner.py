import pandas as pd
import numpy as np


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[^\w]+", "_", regex=True)
        .str.strip("_")
    )

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string")
        df[col] = (
            df[col]
            .str.strip()
            .replace({"": np.nan, "N/A": np.nan, "null": np.nan}, regex=False)
        )

    return df
