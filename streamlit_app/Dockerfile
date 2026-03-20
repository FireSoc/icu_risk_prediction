FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY database.py .

EXPOSE 8080

ENV RDS_HOST=""
ENV RDS_PASSWORD=""
ENV RDS_DB="postgres"
ENV RDS_USER="postgres"

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]