FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ncbi-blast+ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir numpy==2.2.6 && \
    pip install --no-cache-dir .

CMD ["python", "src/analysis.py"]
