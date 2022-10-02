from django.forms import ModelForm
from django import forms
from .models import Vacancy


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"
        exclude = ['company']
        widgets = {
            'job_name': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
            'salary_min': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
            'salary_max': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
            'company': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
            'location': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
            'responsibilities': forms.Textarea(attrs={
                'class': 'textarea is-primary'
            }),
            'requirements': forms.Textarea(attrs={
                'class': 'textarea is-primary'
            }),
            'working_mode': forms.TextInput(attrs={
                'class': 'input is-primary'
            }),
        }
