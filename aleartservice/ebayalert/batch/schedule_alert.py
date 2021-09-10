# -*- coding: utf-8 -*-
__author__ = 'Rajmohan H'


import os
import site
import django


import logging
from logging.handlers import RotatingFileHandler
os.environ['TZ'] = 'UTC'



root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
site.addsitedir(root_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aleartservice.settings")
django.setup()
from django.conf import settings
from ebayalert import tasks
tasks.send_matured_alerts()

