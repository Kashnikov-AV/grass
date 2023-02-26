from django.db import models
from django.contrib.auth import get_user_model

GENDER_CHOICES = (
    (0, 'Мужчина'),
    (1, 'Женщина'),
)

EDU_CHOICES = (
    (0,'среднее'),
    (1,'СПО'),
    (2,'высшее бакалавриат'),
    (3,'высшее специалитет'),
    (4,'высшее магистратура'),
    (5, 'высшее ученая степень'),
)

LANGUAGE_CHOICES = (
    (0,'A0'),
    (1,'A1'),
    (2,'A2'),
    (3,'B1'),
    (4,'B2'),
    (5, 'C1'),
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user_model = get_user_model()

    # желаемая должность
    #desired_position = models.ForeignKey()

    # регион поиска работы
    # city

    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='пользователь', primary_key=True, )
    name = models.CharField(max_length=100, blank=True, verbose_name='имя')
    surname = models.CharField(max_length=100, blank=True, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    gender = models.PositiveSmallIntegerField(blank=True,
                                              verbose_name="Пол",
                                              choices=GENDER_CHOICES,
                                              default=0
                                              )
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения", )
    career_objective = models.CharField(null=True, blank=True, verbose_name="Желаемая должность", max_length=150)
    salary_min = models.IntegerField(verbose_name="Минимальная зарплата", blank=True, null=True)
    salary_max = models.IntegerField(verbose_name="Максимальная зарплата", blank=True, null=True)
    work_experience = models.IntegerField(verbose_name="Опыт работы", blank=True, null=True)
    skills = models.TextField(max_length=2000, blank=True, verbose_name='Навыки')
    level_of_education = models.PositiveSmallIntegerField(blank=True,
                                                          verbose_name="Уровень образования",
                                                          choices=EDU_CHOICES,
                                                          default=0
                                                          )
    level_foreign_language = models.PositiveSmallIntegerField(blank=True,
                                                              verbose_name='уровень иностранного языка',
                                                              choices=LANGUAGE_CHOICES,
                                                              default=0
                                                              )
    edu_institution = models.CharField(max_length=100, blank=True, verbose_name='Учебное заведение')
    diplomas_certificates = models.CharField(max_length=100, blank=True, verbose_name='Дипломы и сертификаты')
    photo = models.ImageField(upload_to=user_directory_path, verbose_name='фото', name='photo', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return f'/profile/{self.user.pk}'


class Company(models.Model):
    user_model = get_user_model()

    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='profile_company',
                                primary_key=True, verbose_name='Пользователь')
    company_name = models.CharField(max_length=100, blank=True, verbose_name='Название компании')
    about_company = models.TextField(blank=True, verbose_name='О компании')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    logo = models.ImageField(upload_to=user_directory_path, verbose_name='Лого', name='logo', blank=True)

    def __str__(self):
        return str(self.company_name)

    def get_absolute_url(self):
        return f'/profile/{self.user.pk}/company'
