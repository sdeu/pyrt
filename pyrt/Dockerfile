FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt /usr/tmp/requirements.txt
RUN pip install -r /usr/tmp/requirements.txt

COPY . /usr/src/app
RUN pip install -e /usr/src/app
