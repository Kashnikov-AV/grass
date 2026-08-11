from django.db import models
from django.contrib.auth import get_user_model
from sorl.thumbnail import ImageField

GENDER_CHOICES = (
    (0, 'Мужчина'),
    (1, 'Женщина'),
)

RELOCATE = (
    (0, 'Готов'),
    (1, 'Не готов')
)

EDU_CHOICES = (
    (0, 'среднее'),
    (1, 'СПО'),
    (2, 'высшее бакалавриат'),
    (3, 'высшее специалитет'),
    (4, 'высшее магистратура'),
    (5, 'высшее ученая степень'),
)

LANGUAGE_CHOICES = (
    (0, 'A0'),
    (1, 'A1'),
    (2, 'A2'),
    (3, 'B1'),
    (4, 'B2'),
    (5, 'C1'),
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def user_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.profile.pk, filename)


class Profile(models.Model):
    class Meta:
        ordering = ['pk']

    user_model = get_user_model()

    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='пользователь', primary_key=True, )
    name = models.CharField(max_length=100, blank=True, verbose_name='имя')
    surname = models.CharField(max_length=100, blank=True, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    gender = models.PositiveSmallIntegerField(default=0, verbose_name="Пол", choices=GENDER_CHOICES)
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    career_objective = models.CharField(null=True, blank=True, verbose_name="Желаемая должность", max_length=150)
    desired_salary = models.IntegerField(verbose_name="Желаемая зарплата", blank=True, default=1000)
    about_me = models.TextField(max_length=2000, blank=True, verbose_name='О себе')
    email = models.EmailField(blank=True, verbose_name='Email', max_length=100)
    phone = models.CharField(blank=True, max_length=20, verbose_name='Телефон')
    site = models.CharField(blank=True, max_length=200, verbose_name='Сайт портфолио')
    level_foreign_language = models.PositiveSmallIntegerField(blank=True,
                                                              verbose_name='уровень иностранного языка',
                                                              choices=LANGUAGE_CHOICES,
                                                              default=0
                                                              )
    photo = ImageField(upload_to=user_directory_path, verbose_name='фото', name='photo', blank=True, null=True)
    city = models.CharField(blank=True, max_length=50, verbose_name='Регион проживания')
    relocate = models.PositiveSmallIntegerField(default=0, verbose_name='Готовность к переезду', choices=RELOCATE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(f'{self.user.pk} {self.name} {self.surname}')

    def get_absolute_url(self):
        return f'/profile/{self.user.pk}'

    @property
    def get_site_url(self):
        if 'http' not in self.site :
            return 'http://'+self.site
        else:
            return self.site

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.photo.delete(save=False)

        # now, delete the object
        super(Profile, self).delete(*args, **kwargs)


class Education(models.Model):
    class Meta:
        ordering = ['pk']

    profile = models.ForeignKey(to=Profile,
                                on_delete=models.CASCADE,
                                related_name="educations",
                                related_query_name="education",
                                verbose_name='профиль пользователя')
    edu_institution = models.CharField(max_length=100, blank=True, verbose_name='Учебное заведение')
    speciality = models.CharField(max_length=200, blank=True, verbose_name='название специальности')
    level_of_education = models.PositiveSmallIntegerField(verbose_name="Уровень образования",
                                                          choices=EDU_CHOICES,
                                                          default=0
                                                          )
    year_of_start_edu = models.DateField(blank=True, verbose_name='год начала обучения', null=True)
    year_of_end_edu = models.DateField(blank=True, verbose_name='год окончания обучения', null=True)
    diploma_certificate = models.FileField(upload_to=user_profile_directory_path, blank=True, verbose_name='Диплом или сертификат')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(f'profile-{self.profile.pk} {self.edu_institution} {self.speciality}')

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.diploma_certificate.delete(save=False)

        # now, delete the object
        super(Education, self).delete(*args, **kwargs)


class Company(models.Model):
    class Meta:
        verbose_name_plural = "companies"
        ordering = ['pk']
        
    user_model = get_user_model()

    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='company',
                                primary_key=True, verbose_name='Пользователь')
    company_name = models.CharField(max_length=100, blank=True, verbose_name='Название компании')
    about_company = models.TextField(blank=True, verbose_name='О компании')
    count_of_employees = models.PositiveIntegerField(verbose_name='Количество работников', default=0)
    region = models.CharField(blank=True, max_length=50, verbose_name='Регион регистрации компании')
    inn = models.BigIntegerField(blank=True, verbose_name='Инн организации', default=9999999999)
    field_of_activity = models.CharField(blank=True, max_length=150, verbose_name='Сфера деятельности')
    phone = models.CharField(blank=True, max_length=20, verbose_name='Телефон компании')
    email = models.EmailField(blank=True, max_length=100, verbose_name='Email компании')
    site = models.CharField(blank=True, max_length=200, verbose_name='Сайт компании')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    logo = models.ImageField(upload_to=user_directory_path, verbose_name='Лого', name='logo', blank=True)

    def __str__(self):
        return str(self.company_name)

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.logo.delete(save=False)

        # now, delete the object
        super(Company, self).delete(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return f'/profile/{self.user.pk}/company'

    @property
    def get_site_url(self):
        if 'http' not in self.site:
            return 'http://' + self.site
        else:
            return self.site


EMPLOYMENT_CHOICES = (
    (0, 'Полная занятость'),
    (1, 'Частичная занятость'),
    (2, 'Стажировка'),
    (3, 'Практика'),
    (4, 'Вахта'),
    (5, 'Удаленная работа')
)


class ExpJob(models.Model):
    profile = models.ForeignKey(to=Profile,
                                on_delete=models.CASCADE,
                                related_name="exp",
                                related_query_name="exp",
                                verbose_name='профиль пользователя')

    company_name = models.CharField(max_length=150, blank=True, verbose_name='Название компании')
    type_employment = models.PositiveSmallIntegerField(verbose_name='Тип занятости', choices=EMPLOYMENT_CHOICES, default=0)
    job_function = models.CharField(max_length=100, blank=True, verbose_name='Должность')
    city = models.CharField(blank=True, max_length=50, verbose_name='Место (город) работы')
    at_now_time = models.BooleanField(verbose_name='по настоящее время')
    work_responsibilities = models.TextField(verbose_name='обязанности на рабочем месте', blank=True)
    year_of_start_job = models.DateField(blank=True, verbose_name='год начала работы', null=True)
    year_of_end_job = models.DateField(blank=True, verbose_name='год окончания работы', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'profile-{self.profile.pk} {self.company_name}')
