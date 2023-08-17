FROM python:3.11-slim-bullseye

WORKDIR /grass

# env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#db
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR \grass

# dependencies
RUN pip install --upgrade pip
COPY requirements.txt
RUN pip install -r requirements.txt



COPY . .