**MLOps Data Labs (Snorkel + Weak Supervision)- Data Labeling Lab — Customer Support Intent Classification** 

Multi-class weak supervision for customer support utterances.

## 🚀 Overview
This lab demonstrates how to use **weak supervision** and **Snorkel** for *customer intent classification* in support chat data.  
Instead of manually labeling thousands of messages, we create labeling functions (LFs) that use pattern-based heuristics to automatically assign probabilistic labels, which are then denoised with a **LabelModel**.

The dataset contains customer support queries grouped into 5 intents:
1. `order_status` – tracking or delivery questions  
2. `refund` – requests for returns or refunds  
3. `account_help` – login, password, or profile issues  
4. `product_info` – questions about product features or specs  
5. `complaint` – negative feedback or dissatisfaction

## 📚 Contents
| File | Description |
|------|--------------|
| `01_customer_intent_labeling.ipynb` | Builds labeling functions and trains a Snorkel `LabelModel` |
| `02_customer_intent_augmentation_tutorial.ipynb` | Demonstrates data augmentation for balanced training |
| `03_customer_intent_slicing_tutorial.ipynb` | Evaluates model robustness on different data slices |
| `utils.py` | Helper utilities (load datasets, visualize label counts) |
| `requirements.txt` | Python dependencies |
| `data/` | Contains CSVs for 5 support categories |
| `README.md` | Project overview (this file) |

---

## 🧩 Dependencies
```bash
pip install snorkel==0.9.9 pandas numpy scikit-learn matplotlib
## Run in Colab
1. Upload this folder or the zip to Colab.
2. In each notebook, install: `!pip -q install snorkel scikit-learn pandas matplotlib`

Notebooks:
1. `01_customer_intent_labeling.ipynb` — Snorkel labeling functions + LabelModel.
2. `02_customer_intent_augmentation_tutorial.ipynb` — Simple augmentation + baseline classifier.
3. `03_customer_intent_slicing_tutorial.ipynb` — Slice-aware analysis.
```
## 🧩 Difference from Original MLOps Data Labeling Lab

| Aspect | Professor’s Lab (Spam Detection) | **Samruddhi’s Lab (Customer Intent Classification)** |
|:--------|:----------------------------------|:----------------------------------------------------|
| **Domain & Objective** | Detects spam vs. non-spam messages (binary classification) | Identifies customer support query intent across 5 categories (multi-class) |
| **Dataset** | Single `spam.csv` dataset (UCI SMS Spam Collection) | Five curated CSVs (`Support01-Orders.csv` … `Support05-Complaints.csv`) totaling 300 samples |
| **Labeling Functions & Analysis** | 3–4 regex-based spam indicators (“win”, “free”, “money”) | 6+ domain-specific LFs for order tracking, refunds, account issues, product info, and complaints with slice-based robustness tests |
| **Deliverables & Structure** | One notebook (`01_spam_tutorial.ipynb`) | Three modular notebooks (`01_labeling`, `02_augmentation`, `03_slicing`) plus organized data, utils, and README for reproducible MLOps workflow |

### Author:
Samruddhi Bansod
Northeastern University
