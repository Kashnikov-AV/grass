from django import forms
from .models import Profile, Company, Education, ExpJob
from datetime import date

YEARS = [(f'{year}-01-01', str(year)) for year in range(1900, date.today().year + 6)]

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

GENDER_CHOICES = (
    (0, 'Мужчина'),
    (1, 'Женщина'),
)

RELOCATE = ((0, 'Готов'),
            (1, 'Не готов')
)


class ProfileAboutMeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me',)


class ProfileContactDataForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('site', 'email', 'phone',)


class ProfileMainInfoForm(forms.ModelForm):
    gender = forms.TypedChoiceField(
        coerce=lambda x: int(x),
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(),
        initial=0
    )
    relocate = forms.TypedChoiceField(
        coerce=lambda x: int(x),
        choices=RELOCATE,
        widget=forms.RadioSelect(),
        initial=1
    )

    class Meta:
        model = Profile
        fields = ('name', 'surname', 'patronymic', 'birth_date', 'gender', 'relocate',
                  'desired_salary', 'career_objective', 'city', 'level_foreign_language', 'photo')
        widgets = {
                    'level_foreign_language': forms.Select(choices=LANGUAGE_CHOICES),
                    'birth_date': forms.SelectDateWidget(years=[x for x in range(1910, date.today().year)]),
                }


class ProfileEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('edu_institution',
                  'speciality',
                  'level_of_education',
                  'year_of_start_edu',
                  'year_of_end_edu',
                  'diploma_certificate',
                  )
        widgets = {
                    'level_of_education': forms.Select(choices=EDU_CHOICES, attrs={
                        "class": "select",
                    }),
                    'year_of_start_edu': forms.Select(choices=YEARS, attrs={
                        "class": "select",
                    }),
                    'year_of_end_edu': forms.Select(choices=YEARS, attrs={
                        "class": "select",
                    }),
                }


class ProfileExpForm(forms.ModelForm):
    class Meta:
        model = ExpJob
        fields = ('company_name', 'type_employment', 'job_function', 'city',
                  'at_now_time', 'work_responsibilities', 'year_of_start_job', 'year_of_end_job')
        widgets = {
            'year_of_start_job': forms.SelectDateWidget(years=[x for x in range(1910, date.today().year + 1)],
                                                        attrs={'required': 'required'},
                                                        ),
            'year_of_end_job': forms.SelectDateWidget(years=[x for x in range(1910, date.today().year + 1)],
                                                      attrs={'required': 'required'},
                                                      ),
        }


class CompanyMainInfoForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'count_of_employees', 'region', 'inn', 'field_of_activity', 'logo')


class CompanyContactDataForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('site', 'email', 'phone',)

class CompanyAboutMeForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('about_company',)




