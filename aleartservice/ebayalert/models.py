from django.db import models, transaction
from django.utils import timezone, dateformat
from django.conf import settings

class AlertScheduler(models.Model):
    MIN2, MIN10, MIN30 = 2, 10, 30
    ALERT_INTERVAL = ((MIN2, '2 minutes'), (MIN10, '10 minute'), (MIN30, '30 minutes'))

    search_phrase = models.CharField(max_length=1024)
    email_address = models.EmailField(max_length=254)
    interval = models.PositiveSmallIntegerField(choices=ALERT_INTERVAL,
                                              default=MIN30)
    aleat_created_at = models.DateTimeField('Alert Created', default=timezone.now)
    last_run_at = models.DateTimeField('Last alert send at', blank=True, null=True)

    def _str_(self):
        return self.search_item

    @transaction.atomic
    def save(self, *args, **kwargs):
        super(AlertScheduler, self).save(*args, **kwargs)


class AlertInfo(models.Model):
    schedule = models.ForeignKey(
        'AlertScheduler', on_delete=models.CASCADE)
    items = models.ManyToManyField(
        'AlertItem', editable=False, blank=True)
    alert_send_at = models.DateTimeField('Alert Send At', default=timezone.now)


class AlertItem(models.Model):
    item_id = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    price = models.FloatField()
    currency = models.CharField(max_length=1024)
    webUrl = models.CharField(max_length=2048)