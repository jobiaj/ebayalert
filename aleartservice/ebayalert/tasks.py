# -*- coding: utf-8 -*-
from builtins import str
__author__ = 'Jobi AJ'

import json
import time
import logging
import datetime
import pytz
import os

from django.core.mail import send_mail
from django.core import serializers
from django.db import transaction
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from django.core.mail import EmailMessage

from ebayalert.models import AlertScheduler, AlertInfo, AlertItem
from ebayalert import get_email_body

logger = logging.getLogger(__name__)


def send_matured_alerts():
    try:
        schedules = AlertScheduler.objects.all()
        for schedule in schedules:
            last_run_at = schedule.aleat_created_at if schedule.last_run_at is None else schedule.last_run_at
            current_time = timezone.now()
            difference_delta = current_time - last_run_at
            difference_in_min = difference_delta.total_seconds() / 60
            if difference_in_min >= schedule.interval:
                print("Sending mail...")
                subject = 'Search results for %s' % schedule.search_phrase
                item_summary = get_email_body.get_search_items_list(schedule.search_phrase)
                message = get_email_body.get_search_items_body(schedule.search_phrase, item_summary)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [schedule.email_address, ]
                msg = EmailMessage(subject, message, email_from, recipient_list)
                msg.content_subtype = "html"
                msg.send()
                schedule.last_run_at = timezone.now()
                schedule.save()
                record_alert_details(schedule, item_summary)
                logger.info("Send Search result to %s" %schedule.email_address)

    except Exception as e:
        logger.exception(e)
        logger.exception("Error occured while sending the result to user: ")

def record_alert_details(schedule, item_summary):
    alert_info = AlertInfo.objects.create(schedule=schedule)
    item_ids = []
    for item in item_summary:
        alert_item = AlertItem.objects.create(item_id=item['itemId'], 
                                             title=item['title'],
                                             price=item['price']['value'],
                                             currency=item['price']['currency'],
                                             webUrl=item['itemWebUrl'])
        item_ids.append(alert_item.id)
    alert_info.items.clear()
    alert_info.items.add(*item_ids)
