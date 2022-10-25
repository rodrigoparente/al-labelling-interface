FROM python:3.8-slim-bullseye

ARG ENV_NAME=prod

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app && \
    adduser --system --no-create-home --disabled-login lauryn && \
    chown -R lauryn /app

COPY requirements/ ./requirements/
RUN pip install --no-cache-dir -r requirements/${ENV_NAME}.txt

WORKDIR /app
USER lauryn

COPY . /app

CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
