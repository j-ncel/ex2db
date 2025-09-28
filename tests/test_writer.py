from db.connector import create_db_engine
from db.writer import write_dataframe_to_db
from db.schema_builder import build_table_schema


def test_write_dataframe_to_db(tmp_path, sample_df):
    db_path = tmp_path / "test.db"
    engine = create_db_engine(f"sqlite:///{db_path}")
    table = build_table_schema(sample_df, "users")
    success = write_dataframe_to_db(sample_df, table, engine)
    assert success
