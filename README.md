This application made with:
1. Django application called alertservice which will be the backend for storing the schedules and associated models.
2. React frontend which communicate to the django backend and pass the user entries.
3. Flask application (alertanalyser) which talks to Django application and analyse the records send to the user, get insites about the the alerts, and then send the insites to user.



Setting up the applications:
1. Clone the repo.
2. Move to the base folder.
3. Change alertanalyser/app.properties and add the required information for sending the mail.
4. Change alertservice/alertservice/local_settings.py, with your email details to send the alerts to user, also get the ebay app ID from this link https://developer.ebay.com , This app_id is used for searching in ebay app based on the user input.
3. from the base directory, where the docker-compose.yaml is there, run <b> docker-compose build </b>
4. Once the build is completed, run <b> docker-compose up </b> to bring up the application.
5. run docker ps -a to see all required components are up and running or not.
6. Get the container ID of <b> ebayalert_django </b> then run <b> docker exec -it <Container ID of Django> bash service cron start </b>.
7. Navigate to http://localhost:3000, And create the schedules.

 Please find the architeture diagram below.
  
![alertsystem](https://user-images.githubusercontent.com/8805606/132820577-e3d5ddb8-2075-44a7-ae86-cac28242f35a.jpg)

