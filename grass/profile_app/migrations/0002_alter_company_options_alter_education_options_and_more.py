# Generated by Django 4.2.3 on 2024-01-23 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['pk'], 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['pk']},
        ),
    ]
