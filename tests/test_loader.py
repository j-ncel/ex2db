from excel.loader import load_excel


def test_load_excel(sample_excel):
    sheets = load_excel(sample_excel)
    assert "Sheet1" in sheets
    assert not sheets["Sheet1"].empty
