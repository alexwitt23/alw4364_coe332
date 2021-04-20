FROM python:3.9

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY source /app
WORKDIR /app

ENTRYPOINT ["python"]
COMMAND ["app.py"]
