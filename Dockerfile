# https://docs.djangoproject.com/en/2.0/intro/tutorial01
FROM python:3
WORKDIR /udiomproj
RUN pip install Django==2.0.5
ENTRYPOINT tail -f /etc/hosts
