# https://docs.docker.com/compose/django
FROM python:3
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
