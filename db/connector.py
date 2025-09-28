from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError


def create_db_engine(db_uri: str):
    try:
        engine = create_engine(db_uri)
        return engine
    except SQLAlchemyError as e:
        raise RuntimeError(f"Database connection failed: {e}")
