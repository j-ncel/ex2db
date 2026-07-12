from db.connector import DatabaseConnector
from db.writer import DatabaseWriter
from db.schema_builder import SchemaBuilder


def test_write_dataframe_to_db(tmp_path, sample_df):
    db_path = tmp_path / "test.db"
    connector = DatabaseConnector(f"sqlite:///{db_path}")
    engine = connector.engine
    builder = SchemaBuilder()
    table = builder.build_table_schema(sample_df, "users")
    writer = DatabaseWriter(engine)
    success = writer.write_dataframe(sample_df, table)
    assert success
