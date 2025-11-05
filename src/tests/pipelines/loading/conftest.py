import pytest
from kedro.io import DataCatalog, MemoryDataset


@pytest.fixture(scope="module")
def project_id():
    return "learned-pier-457806-f5"


@pytest.fixture(scope="module")
def primary_folder():
    return "blent-formation-ml-engineer-data-btl/primary/data-test.csv"  # Sans gs://


@pytest.fixture(scope="module")
def catalog_test(project_id, primary_folder):
    catalog = DataCatalog(
        {
            "params:project": MemoryDataset(project_id),
            "params:bucket_path": MemoryDataset(primary_folder),
        }
    )
    return catalog
