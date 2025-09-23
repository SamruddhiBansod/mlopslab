# src/main.py
from typing import Any, Dict, List, Optional, Union

from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

# Import compatible both as package and as script
try:  # package
    from .train import train_model, load_metrics
    from .predict import predict_one, ModelNotTrained
    from .data import load_wine_dataset
except ImportError:  # script inside src/
    from train import train_model, load_metrics
    from predict import predict_one, ModelNotTrained
    from data import load_wine_dataset

app = FastAPI(
    title="Wine Random Forest API (Flops Lab)",
    description="Train & serve a RandomForestClassifier on the sklearn Wine dataset.",
    version="1.2.0",
)

# ---------- Schemas ----------

class TrainRequest(BaseModel):
    n_estimators: int = Field(200, ge=10, le=5000, description="Number of trees in the forest.")
    max_depth: Optional[int] = Field(None, ge=1, description="Maximum depth of each tree.")
    random_state: int = Field(42, description="Random seed for reproducibility.")
    test_size: float = Field(0.2, gt=0, lt=0.5, description="Fraction for test split.")

class TrainResponse(BaseModel):
    accuracy: float
    test_size: float
    n_classes: int
    n_features: int
    feature_names: List[str]
    target_names: List[str]
    model_path: str
    trained_at: float

class PredictRequest(BaseModel):
    # Accept either a list[float] (length 13) or dict[str, float] keyed by feature names.
    features: Union[List[float], Dict[str, float]]

class PredictResponse(BaseModel):
    prediction_index: int
    prediction_label: str
    class_probabilities: Dict[str, float]
    feature_order: List[str]

# ---------- Endpoints ----------

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}

@app.get("/features")
def features() -> Dict[str, List[str]]:
    """
    Return Wine feature names and target class names.
    Works even before training.
    """
    m = load_metrics()
    if m and "feature_names" in m and "target_names" in m:
        return {"feature_names": m["feature_names"], "target_names": m["target_names"]}
    _, _, meta = load_wine_dataset()
    return {"feature_names": meta["feature_names"], "target_names": meta["target_names"]}

@app.post("/train", response_model=TrainResponse)
def train(req: TrainRequest) -> Any:
    return train_model(
        n_estimators=req.n_estimators,
        max_depth=req.max_depth,
        random_state=req.random_state,
        test_size=req.test_size,
    )

@app.get("/metrics")
def metrics() -> Dict[str, Any]:
    m = load_metrics()
    if not m:
        raise HTTPException(status_code=404, detail="No metrics found. Train a model first.")
    return m

@app.post(
    "/predict",
    response_model=PredictResponse,
)
def predict(
    req: PredictRequest = Body(
        ...,
        examples={
            "as_list_in_dataset_order": {
                "summary": "List of 13 floats in sklearn Wine feature order",
                "description": "Send a 13-length list matching the order from /features.",
                "value": {
                    "features": [14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0]
                },
            },
            "as_named_dict": {
                "summary": "Dict keyed by Wine feature names",
                "description": "Send a dict mapping feature name -> value. Use /features to see names.",
                "value": {
                    "features": {
                        "alcohol": 14.23,
                        "malic_acid": 1.71,
                        "ash": 2.43,
                        "alcalinity_of_ash": 15.6,
                        "magnesium": 127.0,
                        "total_phenols": 2.8,
                        "flavanoids": 3.06,
                        "nonflavanoid_phenols": 0.28,
                        "proanthocyanins": 2.29,
                        "color_intensity": 5.64,
                        "hue": 1.04,
                        "od280/od315_of_diluted_wines": 3.92,
                        "proline": 1065.0
                    }
                },
            },
        },
    )
) -> Any:
    try:
        return predict_one(req.features)
    except ModelNotTrained as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
