# Generated by Django 3.1.4 on 2021-04-29 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210429_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oxygensupplier',
            old_name='contact2',
            new_name='other_contact',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 15, 48, 415972)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 15, 48, 416104)),
        ),
        migrations.AlterField(
            model_name='oxygensupplier',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 15, 48, 416678)),
        ),
        migrations.AlterField(
            model_name='oxygensupplier',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 15, 48, 416700)),
        ),
    ]
