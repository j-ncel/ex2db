from typing import List
from excel.loader import ExcelLoader
from excel.cleaner import ExcelCleaner
from excel.validator import ExcelValidator
from db.connector import DatabaseConnector
from db.schema_builder import SchemaBuilder
from db.writer import DatabaseWriter


class Migrator:
    def __init__(self, db_uri: str, connector=None, cleaner=None, validator=None, schema_builder=None):
        self.db_uri = db_uri
        self.connector = connector or DatabaseConnector(self.db_uri)
        self.cleaner = cleaner or ExcelCleaner()
        self.validator = validator or ExcelValidator()
        self.schema_builder = schema_builder or SchemaBuilder()

    def migrate(self, file_path: str, sheet_names: List[str] = None) -> dict:
        report = {}
        loader = ExcelLoader(file_path)
        sheets = loader.load(sheet_names)
        engine = self.connector.engine
        writer = DatabaseWriter(engine)

        for sheet_name, df in sheets.items():
            try:
                df_clean = self.cleaner.clean(df)
                validation = self.validator.validate(df_clean)
                table_name = sheet_name.replace(" ", "").lower()
                table = self.schema_builder.build_table_schema(df_clean, table_name=table_name)
                writer.write_dataframe(df_clean, table)

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
