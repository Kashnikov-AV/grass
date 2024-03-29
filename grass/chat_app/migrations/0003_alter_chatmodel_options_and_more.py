# Generated by Django 4.2.3 on 2024-01-23 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat_app', '0002_remove_userchatprofilemodel_name_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmodel',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='chatnotification',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='userchatprofilemodel',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='chatmodel',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat_app.room', verbose_name='room'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=150, unique=True, verbose_name='room name'),
        ),
        migrations.AlterField(
            model_name='userchatprofilemodel',
            name='online_status',
            field=models.BooleanField(default=False, verbose_name='online status'),
        ),
        migrations.AlterField(
            model_name='userchatprofilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
