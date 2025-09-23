# src/train.py
import time
from pathlib import Path
from typing import Dict, Any, Optional

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Import compatible both as package and as script
try:  # when running as package (uvicorn src.main:app)
    from .data import train_test_split_wine
except ImportError:  # when running inside src/ (uvicorn main:app)
    from data import train_test_split_wine

# Store artifacts at project_root/models/
MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATH = MODEL_DIR / "wine_rf.joblib"
METRICS_PATH = MODEL_DIR / "metrics.joblib"

def train_model(
    n_estimators: int = 200,
    max_depth: Optional[int] = None,
    random_state: int = 42,
    test_size: float = 0.2,
) -> Dict[str, Any]:
    """
    Train a RandomForestClassifier on the Wine dataset and persist model + metrics.
    """
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    X_train, X_test, y_train, y_test, meta = train_test_split_wine(
        test_size=test_size, random_state=random_state
    )

    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1,
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    bundle = {
        "model_type": "RandomForestClassifier",
        "model": clf,
        "feature_names": meta["feature_names"],
        "target_names": meta["target_names"],
        "trained_at": time.time(),
        "random_state": random_state,
        "params": {"n_estimators": n_estimators, "max_depth": max_depth},
    }
    joblib.dump(bundle, MODEL_PATH)

    metrics = {
        "accuracy": float(acc),
        "test_size": float(test_size),
        "n_classes": len(meta["target_names"]),
        "n_features": len(meta["feature_names"]),
        "feature_names": meta["feature_names"],
        "target_names": meta["target_names"],
        "model_path": str(MODEL_PATH),
        "trained_at": bundle["trained_at"],
    }
    joblib.dump(metrics, METRICS_PATH)
    return metrics

def load_metrics() -> Dict[str, Any]:
    """
    Load metrics if they exist, else {}.
    """
    if METRICS_PATH.exists():
        loaded = joblib.load(METRICS_PATH)
        if isinstance(loaded.get("accuracy"), (int, float)):
            loaded["accuracy"] = float(loaded["accuracy"])
        return loaded
    return {}
