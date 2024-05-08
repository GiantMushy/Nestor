# Generated by Django 4.2.11 on 2024-05-08 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_profile_ssn_remove_profile_description_and_more'),
        ('common', '0002_jobcategory_skillgenre_alter_skills_genre'),
        ('applicant', '0003_applicant_delete_skills_alter_education_applicant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='references',
            name='applicant',
        ),
        migrations.AddField(
            model_name='applicant',
            name='bio',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='phone',
            field=models.CharField(default='empty', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.CreateModel(
            name='CVSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.skills')),
            ],
        ),
        migrations.CreateModel(
            name='CVReferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.references')),
            ],
        ),
        migrations.CreateModel(
            name='CVExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.experience')),
            ],
        ),
        migrations.CreateModel(
            name='CVEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.education')),
            ],
        ),
    ]