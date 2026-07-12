from excel.cleaner import ExcelCleaner


def test_clean_dataframe(sample_df):
    cleaner = ExcelCleaner()
    cleaned = cleaner.clean(sample_df)
    assert all(col.islower() for col in cleaned.columns)
    assert cleaned["name"].dtype.name == "string"


def test_clean_dataframe_configured(sample_df):
    cleaner = ExcelCleaner(lowercase_columns=False)
    cleaned = cleaner.clean(sample_df)
    assert "Name" in cleaned.columns
    assert "Is_Active" in cleaned.columns
