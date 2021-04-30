# Generated by Django 3.1.4 on 2021-04-29 12:38

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210429_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ICU', 'ICU'), ('BEDS', 'BEDS'), ('VENTILATOR', 'VENTILATOR')], default=1, max_length=19),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oxygensupplier',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 8, 50, 708582)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 8, 50, 707857)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 8, 50, 707888)),
        ),
        migrations.AlterField(
            model_name='oxygensupplier',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 18, 8, 50, 708617)),
        ),
    ]