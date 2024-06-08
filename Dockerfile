FROM python:3.12.3-alpine

LABEL authors="KevinNitro <kevinnitro@duck.com>"
LABEL name="VNULIB Downloader"
LABEL repository="https://github.com/KevinNitroG/VNULIB-Downloader"

WORKDIR /app

COPY requirements/requirements.txt /app/

COPY assets/images/error_page.jpg /app/assets/images/
COPY assets/utils/ascii_banner.txt /app/assets/utils/
COPY config-docker.yml /app/config.yml

COPY main.py /app/
COPY src/ /app/src/

RUN apk update
# https://gist.github.com/deliro/509b663093ff0f49c1b71e1876597ccb
RUN apk add --no-cache --virtual .build-deps \
      g++ \
      python3-dev \
      libxml2 \
      libxml2-dev && \
    apk add libxslt-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

RUN apk add --no-cache chromium chromium-chromedriver

CMD ["python", "main.py"]
