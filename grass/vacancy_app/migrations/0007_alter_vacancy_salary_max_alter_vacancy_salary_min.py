# Generated by Django 4.0.4 on 2023-08-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy_app', '0006_alter_vacancy_work_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(default=0, verbose_name='Максимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(default=0, verbose_name='Минимальная зарплата'),
        ),
    ]
