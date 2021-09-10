# Generated by Django 3.2.6 on 2021-09-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebayalert', '0004_rename_email_field_alertscheduler_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertscheduler',
            name='interval',
            field=models.PositiveSmallIntegerField(choices=[(2, '2 minutes'), (10, '10 minute'), (30, '30 minutes')], default=30),
        ),
    ]