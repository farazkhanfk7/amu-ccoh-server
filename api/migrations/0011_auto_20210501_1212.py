# Generated by Django 3.1.4 on 2021-05-01 06:42

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210430_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.CharField(blank=True, default='', max_length=200)),
                ('contact', models.CharField(blank=True, default='', max_length=30)),
                ('other_contact', models.CharField(blank=True, default='', max_length=30)),
                ('availablity', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('tags', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Oximeter', 'Pulse Oximeter'), ('Remdesivir', 'Remdesivir'), ('Nebulizer', 'Nebulizer')], max_length=29, null=True)),
                ('remarks', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 727509))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 727532))),
            ],
        ),
        migrations.AlterField(
            model_name='hospital',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 725962)),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 725997)),
        ),
        migrations.AlterField(
            model_name='oxygensupplier',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 726743)),
        ),
        migrations.AlterField(
            model_name='oxygensupplier',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 12, 12, 30, 726767)),
        ),
    ]