terraform {
  required_version = ">= 1.0.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.4"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Enable required APIs
resource "google_project_service" "cloudfunctions" {
  service = "cloudfunctions.googleapis.com"
}

resource "google_project_service" "cloudbuild" {
  service = "cloudbuild.googleapis.com"
}

resource "google_project_service" "storage" {
  service = "storage.googleapis.com"
}

# Bucket where you upload heart_disease_data.csv
resource "google_storage_bucket" "upload_bucket" {
  name                        = "${var.project_id}-dataset-upload"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = true
}

# Bucket where processed summary files will be written
resource "google_storage_bucket" "processed_bucket" {
  name                        = "${var.project_id}-dataset-processed"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = true
}

# Bucket to store Cloud Function source code zip
resource "google_storage_bucket" "function_bucket" {
  name                        = "${var.project_id}-function-source"
  location                    = var.region
  uniform_bucket_level_access = true
  force_destroy               = true
}

# Zip the Cloud Function source code from ./function directory
data "archive_file" "function_zip" {
  type        = "zip"
  source_dir  = "${path.module}/function"
  output_path = "${path.module}/function.zip"
}

# Upload the zipped function code to the function source bucket
resource "google_storage_bucket_object" "function_archive" {
  name   = "function.zip"
  bucket = google_storage_bucket.function_bucket.name
  source = data.archive_file.function_zip.output_path
}

# Cloud Function (1st gen) triggered when a file is finalized in the upload bucket
resource "google_cloudfunctions_function" "dataset_processor" {
  name        = "dataset-processor-fn"
  description = "Processes CSV datasets on upload and writes summary stats"
  runtime     = "python310"
  region      = var.region

  available_memory_mb   = 256
  timeout               = 60
  entry_point           = "process_file"

  # Source code
  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = google_storage_bucket_object.function_archive.name

  # Set env var for processed bucket name
  environment_variables = {
    PROCESSED_BUCKET = google_storage_bucket.processed_bucket.name
  }

  # Trigger when new object is created in upload bucket
  event_trigger {
    event_type = "google.storage.object.finalize"
    resource   = google_storage_bucket.upload_bucket.name
  }

  depends_on = [
    google_project_service.cloudfunctions,
    google_project_service.cloudbuild,
    google_project_service.storage
  ]
}

output "upload_bucket_name" {
  value       = google_storage_bucket.upload_bucket.name
  description = "Upload your heart_disease_data.csv to this bucket."
}

output "processed_bucket_name" {
  value       = google_storage_bucket.processed_bucket.name
  description = "The Cloud Function will write summary files to this bucket."
}
