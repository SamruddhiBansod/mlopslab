# 🧪 Terraform Lab — Serverless Dataset Processing Pipeline (GCP)

This project implements a **serverless, event-driven data pipeline** on Google Cloud using **Terraform**, **Cloud Storage**, and **Cloud Functions**.  
Instead of provisioning a virtual machine (like the professor’s lab), this solution uses **modern cloud-native architecture** where uploading a dataset automatically triggers processing.

When a CSV file (e.g., `heart_disease_data.csv`) is uploaded to the **upload bucket**, a Cloud Function executes and:

1. Reads the CSV file  
2. Extracts metadata (row count, column names)  
3. Computes basic stats (like average age if available)  
4. Writes a `.summary.txt` output into a **processed bucket**

This entire workflow is deployed and managed through Terraform.

---

## 🚀 Features

- Infrastructure-as-Code (IaC) with Terraform  
- Serverless Cloud Function (Python, no dependencies)  
- Event-driven pipeline (auto-trigger on file upload)  
- Two-bucket architecture (upload → processed)  
- Lightweight: uses only a few MB of resources  
- Uses real dataset (`heart_disease_data.csv`)  
- No VMs, no Docker, no ongoing compute costs  

---

## 📁 Project Structure

```text
terraform-gcf-dataset-lab/
│
├── main.tf
├── variables.tf
├── terraform.tfvars
│
└── function/
      └── main.py
```
## ⚙️ How to Use

### 1️⃣ Authenticate with Google Cloud

Make sure the Google Cloud CLI (`gcloud`) is installed and then run:

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```
2️⃣ Configure Terraform variables

Create or edit terraform.tfvars in the project root:
```
project_id = "mlops-terraform-labs"   # your GCP project ID
region     = "us-central1"            # or any supported region
```

Terraform will automatically read these values when you run plan or apply.

3️⃣ Deploy the infrastructure

From the project root (terraform-gcf-dataset-lab/):
```
terraform init
terraform plan
terraform apply
```
## 🆚 Comparison: Professor’s Lab vs My Lab

| Topic | Professor’s Lab | **My Lab (Serverless Architecture)** |
|-------|------------------|----------------------------------------|
| Compute Type | VM (Compute Engine) | **Cloud Functions – serverless** |
| Trigger Method | Manual run | **Automatic on dataset upload** |
| Dataset Usage | None | **Processes `heart_disease_data.csv`** |
| Cost & Scaling | Higher cost, fixed VM | **Near-zero cost, auto-scales** |
| Workflow Type | Static infrastructure | **Event-driven data pipeline** |

### Created By:
Samruddhi Bansod
Northeastern University
