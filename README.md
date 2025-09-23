# README.md

## 🎥 Video Explanation
FastAPI Lab – Wine Classifier

## ✍️ Blog
FastAPI Lab-1: Serving a Wine Classifier API

---

## 🔎 Overview

In this Lab, we will learn how to expose ML models as APIs using **FastAPI** and **uvicorn**.

- **FastAPI**: A modern, high-performance web framework for building APIs in Python based on standard Python type hints.  
- **uvicorn**: An ASGI (Asynchronous Server Gateway Interface) web server implementation for Python, commonly used to serve FastAPI applications.

### Workflow

1. Train a **Random Forest Classifier** on the Wine dataset from scikit-learn.  
2. Serve the trained model as an API using FastAPI + uvicorn.  
3. Expose endpoints for training, prediction, and metrics.

---

## ⚙️ Setting up the lab

1. Create a virtual environment (e.g., `wine_fastapi_env`).  
2. Activate the environment and install the required packages:
   ```bash
   pip install -r requirements.txt

## 📂 Project Structure
mlops_labs
└── fastapi_lab1
    ├── assets/                 # optional screenshots/docs
    ├── wine_fastapi_env/       # virtual environment (not pushed to GitHub)
    ├── models/                 # trained models stored here
    │   └── wine_rf.joblib
    ├── src/
    │   ├── __init__.py
    │   ├── data.py
    │   ├── main.py
    │   ├── predict.py
    │   └── train.py
    ├── README.md
    └── requirements.txt

## Running the Lab
# Step 1. Train the Random Forest model
From the project root:
uvicorn src.main:app --reload
Then go to Swagger UI and hit POST /train.

# Step 2. Serving the API
The FastAPI app runs automatically on:
http://127.0.0.1:8000/docs

# Step 3. Testing endpoints
GET /features → Shows feature names and class names.
POST /train → Trains the Random Forest model.
GET /metrics → Shows accuracy and metadata.
POST /predict → Predict by sending either:
A list of 13 floats
A dict keyed by feature names
POST /predict/params → Manually input 13 values via Swagger UI fields.


## 📸 API Screenshots

### 🔹 Train Endpoint
![](assets/train.png)

### 🔹 Predict Endpoint
![](assets/predict.png)

### 🔹 Health Check
![](assets/health.png)

## 🛠 Tech Stack
FastAPI (API framework)
scikit-learn (ML model)
Uvicorn (ASGI server)

## 🔄 Comparison: Professor’s FastAPI Lab vs. My WineFastAPI Lab

| Aspect          | Professor’s Lab (Original)      | My Lab (Modified)                  |
|-----------------|---------------------------------|------------------------------------|
| **Dataset**     | Iris dataset (4 features)       | Wine dataset (13 features)         |
| **Algorithm**   | Decision Tree Classifier        | Random Forest Classifier           |
| **Endpoints**   | `/train`, `/predict`, `/metrics`| `/train`, `/predict`, `/predict/params`, `/features`, `/metrics` |
| **Output**      | Iris flower class label         | Wine class label + probabilities   |

## Created By
**Samruddhi Bansod**  
Northeastern University 