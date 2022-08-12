FROM python:3.8-slim-buster

ENV PYTHONUNBEFFERED 1
RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

