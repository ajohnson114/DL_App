FROM python:3.9-alpine
WORKDIR /DL_APP
COPY requirements.txt . 

# Install build dependencies including a C++ compiler and BLAS
RUN apk update \
    && apk add --no-cache build-base openblas-dev \
    && rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt
COPY src src
EXPOSE 7860
ENTRYPOINT ["python", "./src/app.py"]
