This is simple flask application to read the scheduled alerts from a server, and send analysis based on interval.
Please follow the below steps to run the application.
1. Create a virtual environment.
2. Activate the environment.
3. Install the packages required using 
<b>pip install -r requirements.txt </b>
2. Run the application locally by running
<b>python alertanalyser.py</b>

As of now only one schedule is there to check any new product is available in the list for last 1 day alerted item.
You can add more schedules by adding new section under the below line in alertanalyser.py.

I have added the interval as 15 seconds for demo purpose you can change based on your choice.

scheduler.add_job(func=check_new_product_available_in_interval, trigger="interval", seconds=15)

You can add more schedule function and configure
Eg. Configurations given below
<b> scheduler.add_job(func=check_price-reduced, trigger="interval", day_of_week=0) -> This will run the schedule in every monday. </b>

Other schedule options:

year (int|str) – 4-digit year

month (int|str) – month (1-12)

day (int|str) – day of month (1-31)

week (int|str) – ISO week (1-53)

day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)

hour (int|str) – hour (0-23)

minute (int|str) – minute (0-59)

second (int|str) – second (0-59)

start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)

end_date (datetime|str) – latest possible date/time to trigger on (inclusive)

timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

jitter (int|None) – delay the job execution by jitter seconds at most

Find more: https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html