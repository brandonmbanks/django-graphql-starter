FROM python:3.7.3-slim-stretch

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home app
USER app

WORKDIR /home/app

COPY . .
