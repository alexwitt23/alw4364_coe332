FROM python:3.9

WORKDIR /
ADD requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY src /app
WORKDIR /app

ENTRYPOINT ["python3"]
