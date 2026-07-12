from sqlalchemy import Table
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd


class DatabaseWriter:
    def __init__(self, engine: Engine):
        self.engine = engine

    def write_dataframe(self, df: pd.DataFrame, table: Table) -> bool:
        try:
            table.metadata.create_all(self.engine)

            with self.engine.begin() as conn:
                conn.execute(table.insert(), df.to_dict(orient="records"))

            return True
        except SQLAlchemyError as e:
            raise RuntimeError(f"Failed to write data to DB: {e}")
