import pandas as pd
import joblib
from typing import Any


def load_model(model_path: str) -> Any:
    """Charge le modèle entraîné depuis un fichier pickle."""
    return joblib.load(model_path)


def predict(model: Any, X: pd.DataFrame) -> pd.DataFrame:
    """Fait les prédictions sur X."""
    preds = model.predict_proba(X)[:, 1]  # Probabilité de la classe positive
    return pd.DataFrame({"prediction": preds}, index=X.index)
