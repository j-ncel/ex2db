from db.schema_builder import build_table_schema


def test_build_table_schema(sample_df):
    table = build_table_schema(sample_df, "users")
    assert table.name == "users"
    assert any(col.primary_key for col in table.columns)
