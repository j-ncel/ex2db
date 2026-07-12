from excel.validator import ExcelValidator


def test_validate_dataframe(sample_df):
    validator = ExcelValidator()
    report = validator.validate(sample_df)
    assert "missing_values" in report
    assert report["duplicate_rows"] == 0
