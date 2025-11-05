# src/tests/pipelines/processing/conftest.py
import pytest
from kedro.io import DataCatalog, MemoryDataset
from purchase_predict_reloaded.pipelines.loading.nodes import load_csv_from_bucket
from purchase_predict_reloaded.pipelines.processing.nodes import encode_features


@pytest.fixture(scope="module")
def project_id():
    return "learned-pier-457806-f5"


@pytest.fixture(scope="module")
def primary_folder():
    return "blent-formation-ml-engineer-data-btl/primary/data-test.csv"


@pytest.fixture(scope="module")
def dataset_not_encoded(project_id, primary_folder):
    return load_csv_from_bucket(project_id, primary_folder)


@pytest.fixture(scope="module")
def test_ratio():
    return 0.3


@pytest.fixture(scope="module")
def dataset_encoded(dataset_not_encoded):
    return encode_features(dataset_not_encoded)["features"]


@pytest.fixture(scope="module")
def catalog_test(dataset_not_encoded, test_ratio):
    catalog = DataCatalog(
        {
            "primary": MemoryDataset(dataset_not_encoded),
            "params:test_ratio": MemoryDataset(test_ratio),
        }
    )
    return catalog
