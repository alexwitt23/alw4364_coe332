FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV FLASK_ENV=development
COPY requirements.txt .
COPY homework03 .
COPY homework02 homework02

RUN python3 -m pip install -r requirements.txt

EXPOSE 5038

CMD ["python3", "app.py"]
