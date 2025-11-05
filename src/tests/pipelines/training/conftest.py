# src/tests/pipelines/training/conftest.py
import pytest
import pandas as pd
import joblib
from pathlib import Path


@pytest.fixture(scope="module")
def model():
    """Charge le modèle entraîné"""
    model_path = Path("data/06_models/model.pkl")
    return joblib.load(model_path)


@pytest.fixture(scope="module")
def X_test():
    """Charge les données de test"""
    return pd.read_csv("data/05_model_input/X_test.csv")


@pytest.fixture(scope="module")
def y_test():
    """Charge les labels de test"""
    return pd.read_csv("data/05_model_input/y_test.csv").values.flatten()
