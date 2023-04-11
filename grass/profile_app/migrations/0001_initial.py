# Generated by Django 4.0.4 on 2022-10-22 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile_app.models




class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile_company', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Название компании')),
                ('about_company', models.TextField(blank=True, verbose_name='О компании')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(blank=True, upload_to=profile_app.models.user_directory_path, verbose_name='Лого')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='имя')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('gender', models.CharField(blank=True, choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Мужчина', max_length=10, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('career_objective', models.CharField(blank=True, max_length=150, null=True, verbose_name='Желаемая должность')),
                ('salary_min', models.IntegerField(blank=True, null=True, verbose_name='Минимальная зарплата')),
                ('salary_max', models.IntegerField(blank=True, null=True, verbose_name='Максимальная зарплата')),
                ('work_experience', models.IntegerField(blank=True, null=True, verbose_name='Опыт работы')),
                ('skills', models.TextField(blank=True, max_length=2000, verbose_name='Навыки')),
                ('level_of_education', models.CharField(blank=True, choices=[('среднее', 'среднее'), ('СПО', 'СПО'), ('высшее', 'высшее')], max_length=100, verbose_name='Уровень образования')),
                ('edu_institution', models.CharField(blank=True, max_length=100, verbose_name='Учебное заведение')),
                ('diplomas_certificates', models.CharField(blank=True, max_length=100, verbose_name='Дипломы и сертификаты')),
                ('photo', models.ImageField(blank=True, upload_to=profile_app.models.user_directory_path, verbose_name='фото')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
