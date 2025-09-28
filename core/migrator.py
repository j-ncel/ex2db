from excel.loader import load_excel
from excel.cleaner import clean_dataframe
from excel.validator import validate_dataframe
from db.connector import create_db_engine
from db.schema_builder import build_table_schema
from db.writer import write_dataframe_to_db


def migrate(file_path: str, db_uri: str, sheet_names: list = None) -> dict:
    report = {}
    sheets = load_excel(file_path, sheet_names)
    engine = create_db_engine(db_uri)

    for sheet_name, df in sheets.items():
        try:
            df_clean = clean_dataframe(df)
            validation = validate_dataframe(df_clean)
            table_name = sheet_name.replace(" ", "").lower()
            table = build_table_schema(df_clean, table_name=table_name)
            write_dataframe_to_db(df_clean, table, engine)

            report[sheet_name] = {
                "status": "success",
                "rows": len(df_clean),
                "columns": list(df_clean.columns),
                "validation": validation,
                "table": table_name
            }
        except Exception as e:
            report[sheet_name] = {
                "status": "error",
                "message": str(e)
            }

    return report
