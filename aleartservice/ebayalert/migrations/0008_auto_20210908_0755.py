# Generated by Django 3.2.6 on 2021-09-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebayalert', '0007_rename_aleat_send_at_alertinfo_alert_send_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=1024)),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=1024)),
                ('webUrl', models.CharField(max_length=2048)),
            ],
        ),
        migrations.RemoveField(
            model_name='alertinfo',
            name='schedule_info',
        ),
        migrations.AddField(
            model_name='alertinfo',
            name='items',
            field=models.ManyToManyField(blank=True, editable=False, to='ebayalert.AlertItem'),
        ),
    ]
