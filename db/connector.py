from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError


class DatabaseConnector:
    def __init__(self, db_uri: str):
        self.db_uri = db_uri
        self._engine = None

    @property
    def engine(self) -> Engine:
        if self._engine is None:
            try:
                self._engine = create_engine(self.db_uri)
            except SQLAlchemyError as e:
                raise RuntimeError(f"Database connection failed: {e}")
        return self._engine
