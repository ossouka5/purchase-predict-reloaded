"""Tests basiques pour le projet purchase-predict-reloaded"""
import os


def test_imports():
    """Vérifie que les imports fonctionnent"""
    import pandas as pd
    import numpy as np

    # Utilise les imports pour éviter flake8
    assert pd is not None
    assert np is not None


def test_data_folder_exists():
    """Vérifie que le dossier data existe"""
    assert os.path.exists("data")
