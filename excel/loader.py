import pandas as pd
from typing import Dict, List


def load_excel(file_path: str, sheet_names: List[str] = None) -> Dict[str, pd.DataFrame]:
    try:
        xls = pd.ExcelFile(file_path)
        sheets_to_load = sheet_names or xls.sheet_names
        return {sheet: xls.parse(sheet) for sheet in sheets_to_load}
    except Exception as e:
        raise RuntimeError(f"Failed to load Excel file: {e}")
