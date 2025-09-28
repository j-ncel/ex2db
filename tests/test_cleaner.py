from excel.cleaner import clean_dataframe


def test_clean_dataframe(sample_df):
    cleaned = clean_dataframe(sample_df)
    assert all(col.islower() for col in cleaned.columns)
    assert cleaned["name"].dtype.name == "string"
