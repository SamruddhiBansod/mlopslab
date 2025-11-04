import re, os, glob
import pandas as pd
import matplotlib.pyplot as plt

def clean_text(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s\?\!\-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def load_datasets(path: str) -> pd.DataFrame:
    files = sorted(glob.glob(os.path.join(path, "*.csv")))
    frames = [pd.read_csv(f) for f in files]
    df = pd.concat(frames, ignore_index=True)
    if 'text' not in df.columns or 'label' not in df.columns:
        raise ValueError("CSV must contain 'text' and 'label' columns.")
    df['text_clean'] = df['text'].astype(str).map(clean_text)
    return df

def plot_label_counts(df, col='label'):
    ax = df[col].value_counts().sort_index().plot(kind='bar')
    ax.set_xlabel(col); ax.set_ylabel("count"); ax.set_title("Label counts")
    plt.tight_layout()
    return ax