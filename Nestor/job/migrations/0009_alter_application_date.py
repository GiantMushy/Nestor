# Generated by Django 4.2.11 on 2024-05-14 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_application_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 14, 13, 27, 9, 322161, tzinfo=datetime.timezone.utc)),
        ),
    ]