FROM python:slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    wget \
    libgomp1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install gcloud SDK
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-462.0.1-linux-x86_64.tar.gz && \
    tar -xf google-cloud-cli-*.tar.gz && \
    ./google-cloud-sdk/install.sh --quiet && \
    rm google-cloud-cli-*.tar.gz
ENV PATH="/google-cloud-sdk/bin:${PATH}"

WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Set entrypoint
CMD ["python", "pipeline/training_pipeline.py"]