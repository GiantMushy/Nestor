# Generated by Django 4.2.11 on 2024-05-14 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_application_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
