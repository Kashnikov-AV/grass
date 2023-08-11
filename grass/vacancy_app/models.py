from django.db import models
from profile_app.models import Company

EMPLOYMENT_CHOICES = (
    (0, 'Полная занятость'),
    (1, 'Частичная занятость'),
    (2, 'Стажировка'),
    (3, 'Практика'),
    (4, 'Вахта'),
    (5, 'Удаленная работа')
)

WORKEXP_CHOICES = (
    (0, 'Без опыта работы'),
    (1, 'Прошел стажировку'),
    (2, '1 - 3 года'),
    (3, 'от 3-х лет'),
    (4, 'от 5-ти лет'),
    (5, '10+ лет')
)


# Create your models here.
class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = "vacancies"

    job_name = models.CharField(max_length=150, verbose_name="Название вакансии")
    salary_min = models.PositiveIntegerField(verbose_name="Минимальная зарплата", default=0)
    salary_max = models.PositiveIntegerField(verbose_name="Максимальная зарплата", default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy')
    location = models.CharField(max_length=150, verbose_name="Место положения")
    responsibilities = models.TextField(verbose_name="Возможности")
    requirements = models.TextField(verbose_name="Требования")
    work_experience = models.IntegerField(verbose_name="Опыт работы", choices=WORKEXP_CHOICES, default=0)
    working_mode = models.PositiveSmallIntegerField(verbose_name='Тип занятости',
                                                       choices=EMPLOYMENT_CHOICES, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/vacancy/{self.pk}'

    def __str__(self):
        return f'{self.company.pk} {self.job_name}'

    def get_work_exp_end(self):
        if self.work_experience == 1:
            return f'от 1 года'
        else:
            return f'от {self.work_experience} лет'


# class Skill(models.Model):
#     title = None
#     slug = None

