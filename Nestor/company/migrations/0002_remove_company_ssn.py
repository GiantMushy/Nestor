# Generated by Django 4.2.11 on 2024-05-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='SSN',
        ),
    ]
