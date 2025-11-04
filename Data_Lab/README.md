# Data Labeling Lab — Customer Support Intent Classification

Multi-class weak supervision for customer support utterances.

**Intents (labels):**
- order_status
- refund
- account_help
- product_info
- complaint

## Run in Colab
1. Upload this folder or the zip to Colab.
2. In each notebook, install: `!pip -q install snorkel scikit-learn pandas matplotlib`

Notebooks:
1. `01_customer_intent_labeling.ipynb` — Snorkel labeling functions + LabelModel.
2. `02_customer_intent_augmentation_tutorial.ipynb` — Simple augmentation + baseline classifier.
3. `03_customer_intent_slicing_tutorial.ipynb` — Slice-aware analysis.