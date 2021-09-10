import requests
import json
import os
import atexit

from flask import Flask
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

app = Flask(__name__)

app.config.from_pyfile(os.path.join(".", "app.properties"), silent=False)

mail = Mail(app)

ALERT_SCHEDULER_INFORMER_HOST = app.config.get('ALERT_SCHEDULER_INFORMER_HOST')
GET_SCHEDULES_URL = '/api/ebayalert/'
GET_ALERTS_URL = '/api/schedule/{0}/alerts/'
GET_ITEMS_URL = '/api/alert/{0}/items/'


def check_new_product_available_in_interval():
    with app.app_context():
        get_schedule_url = ALERT_SCHEDULER_INFORMER_HOST + GET_SCHEDULES_URL
        schedule_datas = requests.get(get_schedule_url)
        schedules = json.loads(schedule_datas.content)
        for schedule in schedules:
            current_time = datetime.utcnow()
            one_day_deducted_time = current_time - timedelta(days=1)
            get_alerts_per_schedule_url =  ALERT_SCHEDULER_INFORMER_HOST + GET_ALERTS_URL.format(schedule['id']) + '?alert_send_at__gte=%s' %str(one_day_deducted_time) 
            alerts_res = requests.get(get_alerts_per_schedule_url)
            alert_json = alerts_res.json()
            if alert_json:
                last_alert_id = alert_json[0]['id']
                first_alert_id = alert_json[-1]['id']
                get_last_items_url = ALERT_SCHEDULER_INFORMER_HOST + GET_ITEMS_URL.format(str(last_alert_id))
                get_first_items_url = ALERT_SCHEDULER_INFORMER_HOST + GET_ITEMS_URL.format(str(first_alert_id))
                last_items = requests.get(get_last_items_url)
                first_items = requests.get(get_first_items_url)
                last_item_titles = [x['title'] for x in last_items.json()]
                first_item_titles = [x['title'] for x in first_items.json()]
                inter = set(first_item_titles).intersection(last_item_titles)
                new_items_available = set(last_item_titles).difference(inter)
                if len(new_items_available):
                    message = json.dumps(list(new_items_available))
                    new_items = [x for x in last_items.json() if x['title'] in list(new_items_available)]
                    html = "<ul>"
                    for item in new_items:
                        html += '''<li> %s : Price : %s - %s <br> <a href="%s">Book Now</a></li>''' %(item['title'], 
                            item['price'], item['currency'], item['webUrl'])
                    html += "</ul>"

                    msg = Message(
                                'New Items Available for purchase for your search %s' % schedule['search_phrase'],
                                sender ='jobyalungal@gmail.com',
                                recipients = [schedule['email_address']]
                               )
                    msg.html = html
                    mail.send(msg)
            else:
                return


scheduler = BackgroundScheduler()
scheduler.add_job(func=check_new_product_available_in_interval, trigger="interval", seconds=15)
scheduler.start()


if __name__ == '__main__':
    atexit.register(lambda: scheduler.shutdown())
    app.run(debug = False)
