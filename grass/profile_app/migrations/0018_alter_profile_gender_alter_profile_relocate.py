# Generated by Django 4.0.4 on 2023-08-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0017_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.BooleanField(blank=True, choices=[(0, 'Мужчина'), (1, 'Женщина')], default=False, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relocate',
            field=models.BooleanField(blank=True, choices=[(0, 'Готов'), (1, 'Не готов')], default=False, verbose_name='Готовность к переезду'),
        ),
    ]