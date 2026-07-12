from unittest.mock import MagicMock
from core.migrator import Migrator


def test_migrate(sample_excel, tmp_path):
    db_path = tmp_path / "migrated.db"
    uri = f"sqlite:///{db_path}"
    migrator = Migrator(uri)
    report = migrator.migrate(file_path=sample_excel)
    assert "Sheet1" in report
    assert report["Sheet1"]["status"] == "success"


def test_migrator_dependency_injection():
    mock_cleaner = MagicMock()
    migrator = Migrator(db_uri="sqlite:///:memory:", cleaner=mock_cleaner)
    assert migrator.cleaner == mock_cleaner
