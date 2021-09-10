FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install cron

WORKDIR /app/aleartservice
COPY requirements.txt /app/aleartservice


COPY conf/schedule-cron /etc/cron.d/schedule-cron
RUN chmod 0644 /etc/cron.d/schedule-cron
RUN crontab /etc/cron.d/schedule-cron
RUN touch /var/log/cron.log

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["service", "cron", "start"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:7777"]
