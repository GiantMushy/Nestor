# Generated by Django 4.2.11 on 2024-05-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_profile_ssn_remove_profile_description_and_more'),
        ('company', '0003_company_image_delete_companyimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='image',
            new_name='logo',
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(default='empty', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default='empty', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=9999),
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
