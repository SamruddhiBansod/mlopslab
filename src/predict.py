# src/predict.py
from pathlib import Path
from typing import Dict, Any, List, Union

import joblib
import numpy as np

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "wine_rf.joblib"

class ModelNotTrained(Exception):
    """Raised when prediction is requested before training."""
    pass

def _load_bundle() -> Dict[str, Any]:
    if not MODEL_PATH.exists():
        raise ModelNotTrained("Model not trained yet. Call POST /train first.")
    return joblib.load(MODEL_PATH)

def _features_from_payload(
    payload: Union[List[float], Dict[str, float]],
    feature_names: List[str],
) -> np.ndarray:
    """
    Accept either a 13-length list (dataset order) or a dict keyed by feature names.
    Return (1, n_features) array.
    """
    if isinstance(payload, list):
        arr = np.array(payload, dtype=float)
        if arr.shape[0] != len(feature_names):
            raise ValueError(f"Expected {len(feature_names)} features, got {arr.shape[0]}.")
        return arr.reshape(1, -1)

    if isinstance(payload, dict):
        try:
            vec = [payload[name] for name in feature_names]
        except KeyError as ke:
            missing = str(ke).strip("'")
            raise ValueError(f"Missing feature '{missing}' in payload.") from None
        return np.asarray(vec, dtype=float).reshape(1, -1)

    raise ValueError("Payload must be a list[float] or dict[str, float].")

def predict_one(payload: Union[List[float], Dict[str, float]]) -> Dict[str, Any]:
    """
    Predict a single example and return index, label, probabilities, and feature order.
    """
    bundle = _load_bundle()
    clf = bundle["model"]
    feature_names = bundle["feature_names"]
    target_names = bundle["target_names"]

    X = _features_from_payload(payload, feature_names)
    pred_idx = int(clf.predict(X)[0])
    probs = clf.predict_proba(X)[0].tolist()

    return {
        "prediction_index": pred_idx,
        "prediction_label": target_names[pred_idx],
        "class_probabilities": {name: float(prob) for name, prob in zip(target_names, probs)},
        "feature_order": feature_names,
    }
