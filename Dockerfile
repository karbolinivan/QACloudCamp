FROM python:3.10.10-buster

WORKDIR /usr/project

VOLUME /usr/project/allure_results

RUN apk update && apk upgrade && apk add --no-cache bash

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps build-base \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .