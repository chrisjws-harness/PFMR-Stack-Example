FROM python:3.8.0-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt


COPY app.py ./
COPY config.ini ./


CMD python3 app.py