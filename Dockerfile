FROM python:3.8-slim-bullseye

# Install system dependencies needed to build pyzstd
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libc-dev \
    libzstd-dev \
    awscli \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install transformers accelerate

CMD ["python", "app.py"]
