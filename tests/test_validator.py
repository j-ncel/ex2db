from excel.validator import validate_dataframe


def test_validate_dataframe(sample_df):
    report = validate_dataframe(sample_df)
    assert "missing_values" in report
    assert report["duplicate_rows"] == 0
