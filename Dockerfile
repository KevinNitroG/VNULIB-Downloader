FROM python:3.12.3-alpine

LABEL authors="KevinNitro <kevinnitro@duck.com>"
LABEL name="VNULIB Downloader"
LABEL repository="https://github.com/KevinNitroG/VNULIB-Downloader"

WORKDIR /app

RUN apk update
RUN apk add libxml2 libxlt

COPY requirements/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY assets/images/error_page.jpg /app/assets/images/
COPY assets/utils/ascii_banner.txt /app/assets/utils/
COPY config-docker.yml /app/config.yml

COPY main.py /app/
COPY src/ /app/src/

RUN apk add chromium
RUN apk add chromium-chromedriver

CMD ["python", "main.py"]
