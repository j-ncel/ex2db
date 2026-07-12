import pandas as pd
import numpy as np


class ExcelCleaner:
    def __init__(self, lowercase_columns: bool = True, strip_whitespace: bool = True):
        self.lowercase_columns = lowercase_columns
        self.strip_whitespace = strip_whitespace

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if self.lowercase_columns:
            df.columns = (
                df.columns
                .astype(str)
                .str.strip()
                .str.lower()
                .str.replace(r"[^\w]+", "_", regex=True)
                .str.strip("_")
            )
        else:
            df.columns = (
                df.columns
                .astype(str)
                .str.strip()
                .str.replace(r"[^\w]+", "_", regex=True)
                .str.strip("_")
            )

        for col in df.select_dtypes(include=["object", "string"]).columns:
            df[col] = df[col].astype("string")
            if self.strip_whitespace:
                df[col] = df[col].str.strip()
            df[col] = (
                df[col]
                .replace({"": np.nan, "N/A": np.nan, "null": np.nan}, regex=False)
            )

        return df
