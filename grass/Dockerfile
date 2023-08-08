FROM python:3.11-slim-buster

WORKDIR /grass

#db
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# dependencies
RUN pip install --upgrade pip
COPY requirements.txt
RUN pip install -r requirements.txt

COPY . .