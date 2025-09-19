FROM python:3.9.7-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    gcc libffi-dev musl-dev ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
