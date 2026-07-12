import pandas as pd
from typing import Dict, List


class ExcelLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self, sheet_names: List[str] = None) -> Dict[str, pd.DataFrame]:
        try:
            xls = pd.ExcelFile(self.file_path)
            sheets_to_load = sheet_names or xls.sheet_names
            return {sheet: xls.parse(sheet) for sheet in sheets_to_load}
        except Exception as e:
            raise RuntimeError(f"Failed to load Excel file: {e}")
