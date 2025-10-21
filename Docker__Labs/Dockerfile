# Use a stable Python for scikit-learn stack
FROM python:3.11-slim

# Make Python friendlier in containers
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Work inside /app
WORKDIR /app

# Install deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code into the image
COPY src/ /app/src/
COPY templates/ /app/templates/

# Train during build so the image ships with the model
WORKDIR /app/src
RUN python model_training.py

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
