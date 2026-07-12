import pandas as pd
from typing import Dict


class ExcelValidator:
    def __init__(self, check_duplicates: bool = True, check_empty_cols: bool = True):
        self.check_duplicates = check_duplicates
        self.check_empty_cols = check_empty_cols

    def validate(self, df: pd.DataFrame) -> Dict[str, any]:
        report = {
            "missing_values": df.isnull().sum().to_dict(),
            "column_types": df.dtypes.apply(lambda x: str(x)).to_dict(),
        }
        if self.check_duplicates:
            report["duplicate_rows"] = int(df.duplicated().sum())
        if self.check_empty_cols:
            report["empty_columns"] = [col for col in df.columns if df[col].isnull().all()]
        return report
