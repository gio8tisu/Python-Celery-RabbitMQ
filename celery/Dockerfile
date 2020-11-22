FROM python:3.6-slim

ARG CELERY_VERSION=4.1.1
ENV CELERY_VERSION="$CELERY_VERSION"
ARG CELERY_BROKER_URL=amqp://guest@rabbit
ENV CELERY_BROKER_URL="$CELERY_BROKER_URL"

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user

RUN pip install \
    celery=="$CELERY_VERSION" \
    pymongo

COPY celeryconfig.py .

USER user
ENTRYPOINT ["celery", "worker"]
