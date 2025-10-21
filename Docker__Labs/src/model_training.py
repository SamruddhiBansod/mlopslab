# src/model_training.py
import pickle
from pathlib import Path
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

HERE = Path(__file__).parent

def main():
    print("📥 Loading 20 Newsgroups dataset...")
    data = fetch_20newsgroups(subset='all')

    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    model = make_pipeline(
        TfidfVectorizer(stop_words='english', max_df=0.9),
        MultinomialNB()
    )

    print("🚀 Training model...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained with accuracy: {acc:.2f}")

    with open(HERE / "news_model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open(HERE / "target_names.pkl", "wb") as f:
        pickle.dump(data.target_names, f)

    print("💾 Model and target names saved successfully!")

if __name__ == "__main__":
    main()
