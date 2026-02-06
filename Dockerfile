FROM python:3.10-slim

# Set working directory
WORKDIR /app

# System dependencies (important for ML + SHAP)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy full project
COPY . .

# Hugging Face uses PORT 7860
ENV PORT=7860

# Expose port
EXPOSE 7860

# Run Flask app
CMD ["python", "app.py"]
