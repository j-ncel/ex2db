from core.migrator import migrate


def test_migrate(sample_excel, tmp_path):
    db_path = tmp_path / "migrated.db"
    uri = f"sqlite:///{db_path}"
    report = migrate(file_path=sample_excel, db_uri=uri)
    assert "Sheet1" in report
    assert report["Sheet1"]["status"] == "success"
