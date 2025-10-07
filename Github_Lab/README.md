## 🚀 MLOps Lab 2 – Automated Testing and CI with GitHub Actions  

This repository documents **Samruddhi Bansod’s customized implementation** of *MLOps Lab 1 (IE-7374)*.  
It extends the professor’s starter repository by introducing **modular code, dual testing frameworks, CI pipelines, and improved repository organization.**

---

## 🧭 Objective
To create a reproducible MLOps workflow that automatically:
1. Builds a Python project in a virtual environment.  
2. Executes both **Pytest** and **Unittest** suites on every push to GitHub.  
3. Reports results through **GitHub Actions** and artifact uploads.  

---

## 🧱 Repository Structure
mlopslab1/
│
├── .github/
│ └── workflows/
│ ├── pytest_action.yml # CI for pytest
│ └── unittest_action.yml # CI for unittest
│
├── Github_Lab/
│ ├── src/
│ │ ├── energy_metrics.py # Core lab code
│ │ └── lab2.py # Example runner
│ │
│ ├── test/
│ │ ├── test_pytest.py
│ │ └── test_unittest.py
│ │
│ ├── requirements.txt # Dependencies
│ ├── Makefile
│ └── README.md
│
└── .gitignore

---

## ⚙️ Key Modules
### 🔹 `energy_metrics.py`
Implements practical energy-calculation utilities used in power-systems analytics:

| Function | Description |
|-----------|-------------|
| `compute_efficiency()` | Calculates efficiency (%) = output / input × 100 |
| `compute_power_factor()` | Returns P/S (clipped 0-1) |
| `rms()` | Root-Mean-Square of input list |
| `thd_fundamental()` | Total Harmonic Distortion (%) |

### 🔹 Tests
Two frameworks ensure reliability:
- **Pytest:** concise assert-based tests.  
- **Unittest:** class-based structured tests with assertions.

### 🔹 Makefile shortcuts
```bash
make install     # install dependencies
make test        # run both suites
make pytest      # run only pytest
make unittest    # run only unittest

## 🧩 How This Repo Differs from the Professor’s
## 🧩 How This Repo Differs from the Professor’s

| **Feature** | **Professor’s Repository** | **This Implementation** |
|--------------|-----------------------------|---------------------------|
| **Code Module** | `calculator.py` (simple math) | `energy_metrics.py` (real-world engineering metrics) |
| **Testing** | Only Pytest demo | Dual frameworks (**Pytest + Unittest**) |
| **Structure** | Single flat folder | Hierarchical `Github_Lab/src` and `Github_Lab/test` |
| **Workflows** | One basic YAML | Two modernized CI files (latest Actions versions) |
| **Environment** | Manual `pip` installs | Automated `Makefile` + `requirements.txt` |
| **Error Handling** | Minimal | Added type checks & exceptions |
| **Artifacts** | None | JUnit XML upload for test history |
| **Python Version** | 3.8 only | Compatible 3.8 – 3.11 |

## 📈 Results and Validation
All workflows execute successfully in GitHub Actions:
Each green check mark (✅) represents a successful run of:
Testing with Pytest
Python Unittests

### ✨ Author
Samruddhi Bansod
Master’s in Data Analytics Engineering, Northeastern University
Course: IE-7374 MLOps (Fall 2025)
