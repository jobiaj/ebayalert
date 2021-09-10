Django application for storing the schedules and associated models.
Please find the information below to setup the application in local

1. Create a virtual environment and install packages using pip install -r requirements.txt.
2. Create a postgres database and override the information in local_settings.py
If you haven’t done that before, I suggest reading this wonderful tutorial from DigitalOcean.

Link : https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
3. Change the required informations like email, Ebay appID etc in local_settings.py
4. Run migration: <b> python manage.py migrate </b>
5. Start the application: <b> python manage.py runserver 0.0.0.0:8000 </b>
6. You can run the tests by running python manage.py test
7. Go to http://localhost:7777/docs/ to see the api swagger page and get the information about the available apis in the application.
8. Correct the path in conf/schedule-cron to call the check_schedules.sh placed in the ebayalert/batch/ folder.
9. run crontab -e in ur linux/centos machine and paste the edited content in the schedule-cron to the opened window and save.
10. Now you have a cron running to see any matured schedule which will call ebay service and get the information and send to the user.

