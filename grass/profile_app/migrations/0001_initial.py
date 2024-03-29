# Generated by Django 4.0.4 on 2023-08-18 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile_app.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Название компании')),
                ('about_company', models.TextField(blank=True, verbose_name='О компании')),
                ('count_of_employees', models.PositiveIntegerField(default=0, verbose_name='Количество работников')),
                ('region', models.CharField(blank=True, max_length=50, verbose_name='Регион регистрации компании')),
                ('inn', models.BigIntegerField(blank=True, default=9999999999, verbose_name='Инн организации')),
                ('field_of_activity', models.CharField(blank=True, max_length=150, verbose_name='Сфера деятельности')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон компании')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email компании')),
                ('site', models.CharField(blank=True, max_length=200, verbose_name='Сайт компании')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logo', models.ImageField(blank=True, upload_to=profile_app.models.user_directory_path, verbose_name='Лого')),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='имя')),
                ('surname', models.CharField(blank=True, max_length=100, verbose_name='фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('gender', models.PositiveSmallIntegerField(choices=[(0, 'Мужчина'), (1, 'Женщина')], default=0, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('career_objective', models.CharField(blank=True, max_length=150, null=True, verbose_name='Желаемая должность')),
                ('desired_salary', models.IntegerField(blank=True, default=1000, verbose_name='Желаемая зарплата')),
                ('about_me', models.TextField(blank=True, max_length=2000, verbose_name='О себе')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('site', models.CharField(blank=True, max_length=200, verbose_name='Сайт портфолио')),
                ('level_foreign_language', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'A0'), (1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1')], default=0, verbose_name='уровень иностранного языка')),
                ('photo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=profile_app.models.user_directory_path, verbose_name='фото')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Регион проживания')),
                ('relocate', models.PositiveSmallIntegerField(choices=[(0, 'Готов'), (1, 'Не готов')], default=0, verbose_name='Готовность к переезду')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=150, verbose_name='Название компании')),
                ('type_employment', models.PositiveSmallIntegerField(choices=[(0, 'Полная занятость'), (1, 'Частичная занятость'), (2, 'Стажировка'), (3, 'Практика'), (4, 'Вахта'), (5, 'Удаленная работа')], default=0, verbose_name='Тип занятости')),
                ('job_function', models.CharField(blank=True, max_length=100, verbose_name='Должность')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Место (город) работы')),
                ('at_now_time', models.BooleanField(verbose_name='по настоящее время')),
                ('work_responsibilities', models.TextField(blank=True, verbose_name='обязанности на рабочем месте')),
                ('year_of_start_job', models.DateField(blank=True, null=True, verbose_name='год начала работы')),
                ('year_of_end_job', models.DateField(blank=True, null=True, verbose_name='год окончания работы')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exp', related_query_name='exp', to='profile_app.profile', verbose_name='профиль пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_institution', models.CharField(blank=True, max_length=100, verbose_name='Учебное заведение')),
                ('speciality', models.CharField(blank=True, max_length=200, verbose_name='название специальности')),
                ('level_of_education', models.PositiveSmallIntegerField(choices=[(0, 'среднее'), (1, 'СПО'), (2, 'высшее бакалавриат'), (3, 'высшее специалитет'), (4, 'высшее магистратура'), (5, 'высшее ученая степень')], default=0, verbose_name='Уровень образования')),
                ('year_of_start_edu', models.DateField(blank=True, null=True, verbose_name='год начала обучения')),
                ('year_of_end_edu', models.DateField(blank=True, null=True, verbose_name='год окончания обучения')),
                ('diploma_certificate', models.FileField(blank=True, upload_to=profile_app.models.user_profile_directory_path, verbose_name='Диплом или сертификат')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', related_query_name='education', to='profile_app.profile', verbose_name='профиль пользователя')),
            ],
        ),
    ]
