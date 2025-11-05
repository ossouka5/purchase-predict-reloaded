# src/tests/pipelines/loading/test_nodes.py
import pandas as pd
from purchase_predict_reloaded.pipelines.loading.nodes import load_csv_from_bucket


def test_load_csv_from_bucket(project_id, primary_folder):
    df = load_csv_from_bucket(project_id, primary_folder)
    assert type(df) == pd.DataFrame
    assert df.shape[1] == 16
    assert "purchased" in df
