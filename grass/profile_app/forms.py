from django import forms
from .models import Profile, Company


YEARS = [year for year in range(1900, 2020)]


class ProfileForm(forms.ModelForm):
    YEARS = [year for year in range(1920, 2020)]

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'birth_date': forms.SelectDateWidget(years=YEARS, attrs={
                "class": "select",
            })
        }


class ProfileCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'company_name': forms.TextInput(attrs={
                "class": "input is-primary"
            }),
            'about_company': forms.Textarea(attrs={
                "class": "textarea is-primary"
            }),
        }

