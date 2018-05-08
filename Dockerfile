# https://docs.docker.com/compose/django
FROM python:3

# "Force stdin, stdout and stderr to be totally unbuffered. On systems where it matters, also put stdin, stdout and stderr in binary mode."
#   - https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
