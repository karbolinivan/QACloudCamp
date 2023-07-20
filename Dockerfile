#FROM python:3.11-alpine
#
#WORKDIR /usr/project
#
#VOLUME /usr/project/allure_results
#
#RUN apk add --no-cache bash
#
#COPY requirements.txt .
#
#RUN apk add --no-cache --virtual .build-deps build-base \
#    && pip3 install --no-cache-dir -r requirements.txt \
#    && apk del .build-deps
#
#COPY . .

FROM python:3.11-alpine

WORKDIR ./usr/project

VOLUME ./usr/project/allure_reports

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN python3 -m venv venv

RUN source venv/bin/activate

RUN pip3 install -r requirements.txt

COPY . .