FROM python:3.7-alpine

RUN apk add --no-cache bash git && \
    pip --no-cache-dir install --upgrade pip && \
    pip --no-cache-dir install pytest-selenium
