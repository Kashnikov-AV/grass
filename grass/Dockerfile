FROM python:3.11-slim-bullseye

# WORKDIR /grass

# env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# настройка установка нужных пакетов
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
   && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000
# dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt