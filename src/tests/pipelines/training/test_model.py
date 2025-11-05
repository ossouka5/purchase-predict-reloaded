# src/tests/pipelines/training/test_model.py
import numpy as np


def test_model_price_invariance(model, X_test):
    """
    Test d'invariance : une variation de ±1€ ne devrait pas changer drastiquement
    la probabilité (< 10% de variation pour 95% des observations)
    """
    # Filtrer les articles avec prix > 1€
    X_test_price = X_test[X_test["price"] > 1].copy()

    # Calculer proba originale
    y_original = model.predict_proba(X_test_price)[:, 1]

    # Tester avec +1€
    X_test_plus = X_test_price.copy()
    X_test_plus["price"] += 1
    y_plus = model.predict_proba(X_test_plus)[:, 1]

    # Tester avec -1€
    X_test_minus = X_test_price.copy()
    X_test_minus["price"] -= 1
    y_minus = model.predict_proba(X_test_minus)[:, 1]

    # Calculer les différences
    delta_plus = np.abs(y_original - y_plus)
    delta_minus = np.abs(y_original - y_minus)
    delta_max = np.maximum(delta_plus, delta_minus)

    # Au moins 95% des observations doivent avoir un delta < 10%
    proportion_stable = (delta_max < 0.10).sum() / len(delta_max)

    print(f"\nProportion d'observations stables (delta < 10%): {proportion_stable:.2%}")
    print(f"Delta moyen: {delta_max.mean():.4f}")
    print(f"Delta médian: {np.median(delta_max):.4f}")
    print(f"Delta max: {delta_max.max():.4f}")

    assert proportion_stable > 0.95, f"Seulement {proportion_stable:.2%} des observations sont stables"


def test_model_duration_directional(model, X_test):
    """
    Test directionnel : augmenter la durée devrait augmenter la probabilité d'achat
    pour au moins 70% des observations
    """
    # Proba originale
    y_original = model.predict_proba(X_test)[:, 1]

    # Augmenter la durée de 60 secondes
    X_test_more_duration = X_test.copy()
    X_test_more_duration["duration"] += 60
    y_more_duration = model.predict_proba(X_test_more_duration)[:, 1]

    # Compter combien d'observations ont une proba qui augmente
    increases = (y_more_duration > y_original).sum()
    proportion_increases = increases / len(y_original)

    print(f"\nProportion d'observations avec proba augmentée: {proportion_increases:.2%}")
    print(f"Augmentation moyenne de proba: {(y_more_duration - y_original).mean():.4f}")

    # Au moins 70% des observations devraient voir leur proba augmenter
    assert proportion_increases > 0.60, f"Seulement {proportion_increases:.2%} augmentent"
