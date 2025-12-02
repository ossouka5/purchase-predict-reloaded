"""Tests basiques pour le projet purchase-predict-reloaded"""


def test_imports():
    """Vérifie que les imports fonctionnent"""
    import pandas as pd
    import numpy as np

    # Utilise les imports pour éviter flake8
    assert pd is not None
    assert np is not None
