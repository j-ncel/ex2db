from db.schema_builder import SchemaBuilder


def test_build_table_schema(sample_df):
    builder = SchemaBuilder()
    table = builder.build_table_schema(sample_df, "users")
    assert table.name == "users"
    assert any(col.primary_key for col in table.columns)
