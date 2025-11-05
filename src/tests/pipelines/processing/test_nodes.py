# src/tests/pipelines/processing/test_nodes.py
import pandas as pd
import numpy as np
from purchase_predict_reloaded.pipelines.processing.nodes import (
    encode_features,
    split_dataset,
)

BALANCE_THRESHOLD = 0.1
MIN_SAMPLES = 5000


def test_encode_features(dataset_not_encoded):
    df = encode_features(dataset_not_encoded)["features"]
    # Checking column 'purchased' that all values are either 0 or 1
    assert df["purchased"].isin([0, 1]).all()
    # Checking that all columns are numeric
    print("\n=== Types des colonnes ===")
    print(df.dtypes)
    print("\n=== Colonnes non-numériques ===")
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df.dtypes[col]):
            print(f"{col}: {df[col].dtype}")
            print(f"Exemples: {df[col].head()}")

    for col in df.columns:
        assert pd.api.types.is_numeric_dtype(df.dtypes[col]), f"Colonne {col} n'est pas numérique!"


def test_split_dataset(dataset_encoded, test_ratio):
    X_train, y_train, X_test, y_test = split_dataset(dataset_encoded, test_ratio).values()
    # Checks both sets size
    assert X_train.shape[0] == y_train.shape[0]
    assert X_test.shape[0] == y_test.shape[0]
    assert X_train.shape[0] + X_test.shape[0] == dataset_encoded.shape[0]
    # Note that train_test_split of scikit-learn use np.ceil for test split
    assert np.ceil(dataset_encoded.shape[0] * test_ratio) == X_test.shape[0]
