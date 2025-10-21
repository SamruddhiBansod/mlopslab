from flask import Flask, request, render_template, render_template_string
import pickle
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

HERE = Path(__file__).parent
TEMPLATES = HERE.parent / "templates"   # 👈 templates folder is outside src

app = Flask(__name__, template_folder=str(TEMPLATES))

def load_pickle(fname: str):
    p = HERE / fname
    if not p.exists():
        raise FileNotFoundError(f"Missing file: {p}")
    with open(p, "rb") as f:
        return pickle.load(f)

# Log template info right away (no decorator needed)
app.logger.info(f"Template folder resolved to: {TEMPLATES.resolve()}")
if TEMPLATES.exists():
    app.logger.info(f"Templates found: {[p.name for p in TEMPLATES.iterdir()]}")
else:
    app.logger.warning("❌ Templates directory not found!")

app.logger.info("Loading model artifacts...")
model = load_pickle("news_model.pkl")
target_names = load_pickle("target_names.pkl")
app.logger.info("✅ Model artifacts loaded.")

@app.route("/health")
def health():
    return "ok"

@app.route("/", methods=["GET"])
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Template error: {e}")
        return render_template_string("""
            <h2>Template Not Found</h2>
            <p>Make sure <code>index.html</code> is inside <strong>templates</strong> at project root.</p>
        """)

@app.route("/predict", methods=["POST"])
def predict():
    text = (request.form.get("news_text") or "").strip()
    if not text:
        return render_template("index.html", prediction="⚠️ Please paste some news text first.")
    pred_idx = model.predict([text])[0]
    category = target_names[pred_idx]
    return render_template("index.html", prediction=f"This news belongs to: {category}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
