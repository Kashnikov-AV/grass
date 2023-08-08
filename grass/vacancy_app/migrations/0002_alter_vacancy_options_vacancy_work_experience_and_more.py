# Generated by Django 4.0.4 on 2023-07-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name_plural': 'vacancies'},
        ),
        migrations.AddField(
            model_name='vacancy',
            name='work_experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='working_mode',
            field=models.CharField(max_length=200, verbose_name='Тип занятости'),
        ),
    ]