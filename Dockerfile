FROM python:3.11-alpine

ARG run_env
ENV env $run_env

LABEL maintainer="Karbolin Ivan"

WORKDIR ./usr/project

VOLUME ./usr/project/allure_reports

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./ ./

CMD pytest -m "$env" -s -v --alluredir=allure_reports