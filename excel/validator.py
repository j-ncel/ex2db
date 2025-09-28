import pandas as pd
from typing import Dict


def validate_dataframe(df: pd.DataFrame) -> Dict[str, any]:
    report = {
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum(),
        "column_types": df.dtypes.apply(lambda x: str(x)).to_dict(),
        "empty_columns": [col for col in df.columns if df[col].isnull().all()]
    }
    return report
