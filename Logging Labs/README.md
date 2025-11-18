## 📘 Logging Labs : Breast Cancer Classification with RandomForest + Python Logging 

What this lab demonstrates:
---------------------------

This lab is an extended version of the basic logging example from class.
Instead of only printing simple log messages, it shows how logging is used
in a *real* machine learning pipeline using the Breast Cancer dataset.

Key things this lab does:

1. Uses the built-in Python `logging` module.
2. Configures logging with timestamps, logger name, level, and message.
3. Creates a custom logger for the ML pipeline (`ml_pipeline_bc`).
4. Loads the Breast Cancer dataset from `sklearn.datasets`.
5. Splits the data into training and test sets, and logs their shapes.
6. Trains a `RandomForestClassifier` and logs when training starts/ends.
7. Makes predictions and logs the model accuracy.
8. Demonstrates logging exceptions with full traceback:
   - Division by zero (`ZeroDivisionError`)
   - Invalid integer conversion (`ValueError`)
9. Shows how to:
   - Log to the console (default behavior)
   - Log using a separate logger with handlers (`handler_example_bc`)
   - Log error messages with stack traces for easier debugging.

In short:
---------
This lab shows how logging is used to *monitor and debug* a real ML workflow,
not just to print messages. It’s closer to what you would do in industry for
tracking data pipelines, model training, and errors.
"""

##
# 🆚 Comparison: My Lab vs Professor’s Lab

| Feature | Professor’s Lab | My Lab |
|--------|------------------|--------|
| Dataset | None (simple print logs) | Breast Cancer dataset (`sklearn`) |
| Model | None | RandomForestClassifier |
| Pipeline Logging | ❌ | ✔ Full ML pipeline |
| Exception Logging | Basic | Multiple exceptions + traceback |
| File Logging | ❌ | ✔ Saves `.log` file |
| Custom Logger | Minimal | ✔ Named loggers (`ml_pipeline_bc`) |
| Handlers | None | ✔ StreamHandler + FileHandler |

# ▶️ How to Run the Lab

## **Option 1 — Google Colab**
1. Open the notebook  
2. Runtime → Run all  
3. Logs will appear in cell outputs  
4. `.log` files will be created automatically  

## **Option 2 — Local Machine**
```bash
pip install -r requirements.txt
python your_logging_file.py

```
## Created By
Samruddhi Bansod
Northeastern University
