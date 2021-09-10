from django.test import TestCase
from django.core import mail

from ebayalert.models import *

class ScheduleTestCase(TestCase):
    def setUp(self):
        AlertScheduler.objects.create(search_phrase="Test1", email_address="jobyalungal@gmail.com", interval=2)
        AlertScheduler.objects.create(search_phrase="Test2", email_address="jobyalungal1@gmail.com", interval=2)


    def test_email_correct(self):
        test1 = AlertScheduler.objects.get(search_phrase="Test1")
        cat = AlertScheduler.objects.get(search_phrase="Test2")
        self.assertNotEqual(test1.email_address, "jobyalungal1@gmail.com")

    def test_email_format(self):
        obj = AlertScheduler.objects.create(search_phrase="Test2", email_address="jobyalungal1", interval=2)
        print(obj)

    def test_send_mail(self):
       mail.send_mail(
            'Subject here',
            'Here is the message.',
            'jobyalungal@gmail.com',
            ['jobyalungal@gmail.com']
        )
       self.assertEqual(len(mail.outbox), 1)
       self.assertEqual(mail.outbox[0].subject, 'Subject here')
       self.assertEqual(mail.outbox[0].body, 'Here is the message.')
       self.assertEqual(mail.outbox[0].from_email,'jobyalungal@gmail.com')