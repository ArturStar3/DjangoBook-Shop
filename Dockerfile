FROM python:3.11

ADD . /myshop/
WORKDIR /myshop/

RUN pip install -r requirements.txt