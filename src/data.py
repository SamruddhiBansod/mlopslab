# src/data.py
from typing import Tuple, Dict, Any
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_wine_dataset() -> Tuple[Any, Any, Dict[str, Any]]:
    """
    Loads the sklearn Wine dataset.
    Returns:
        X: ndarray (n_samples, n_features)
        y: ndarray (n_samples,)
        meta: dict(feature_names, target_names)
    """
    ds = load_wine()
    X, y = ds.data, ds.target
    meta = {
        "feature_names": list(ds.feature_names),
        "target_names": list(ds.target_names),
    }
    return X, y, meta

def train_test_split_wine(
    test_size: float = 0.2,
    random_state: int = 42,
):
    """
    Stratified train/test split.
    Returns:
        X_train, X_test, y_train, y_test, meta
    """
    X, y, meta = load_wine_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test, meta
