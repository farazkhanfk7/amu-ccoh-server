# Generated by Django 3.1.4 on 2021-04-29 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210429_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 12, 12, 53, 460365)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 12, 12, 53, 460404)),
        ),
        migrations.AlterField(
            model_name='oxygensupply',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 12, 12, 53, 461071)),
        ),
    ]
