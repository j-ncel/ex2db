from excel.loader import ExcelLoader


def test_load_excel(sample_excel):
    loader = ExcelLoader(sample_excel)
    sheets = loader.load()
    assert "Sheet1" in sheets
    assert not sheets["Sheet1"].empty
