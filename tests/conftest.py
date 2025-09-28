import pytest
import pandas as pd
from sample.generate_excel_sample import generate_excel_sample


@pytest.fixture(scope="module")
def sample_excel(tmp_path_factory):
    path = tmp_path_factory.mktemp("data") / "sample.xlsx"
    generate_excel_sample(filename=str(path), num_rows=10)
    return str(path)


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "ID": [1, 2],
        "Name": ["Alice", "Bob"],
        "Age": [30, 25],
        "Is Active": [True, False]
    })
