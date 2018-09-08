FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y vim

RUN mkdir /anymind
WORKDIR /anymind
ADD . /anymind/
RUN pip install -r requirements.txt
