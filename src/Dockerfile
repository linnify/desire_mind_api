ARG BASE_IMAGE="python:3.7.4-alpine"
FROM $BASE_IMAGE

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache netcat-openbsd curl libstdc++ lapack

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

WORKDIR /app

COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc g++ libstdc++ musl-dev postgresql-dev lapack-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /app

CMD /app/run.sh
