FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install cron

WORKDIR /app/alertanalyser
COPY requirements.txt /app/alertanalyser

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "alertanalyser.py"]
