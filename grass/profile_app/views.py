from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, UpdateView
from .models import Profile, Company
from vacancy_app.models import Vacancy
from .forms import ProfileForm, ProfileCompanyForm
from datetime import datetime


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_app/profile_form.html'
    form_class = ProfileForm
    model = Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'profile_app/profile.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # add extra field
        profile = Profile.objects.get(user_id=self.request.user.id)
        try:
            context["age"] = datetime.now().year - profile.birth_date.year
            context["end_age"] = self.right_end(int(context["age"]))
            context["end_exp"] = self.right_end(int(profile.work_experience))
        except:
            context["age"] = 0

        return context

    #правильное склонение лет год года
    def right_end(self, data: int) -> str:
        if data % 10 == 1:
            return "год"
        elif data < 5 and data % 10 > 1 and data % 100 < 10:
            return "года"
        elif data % 100 > 10 and data % 100 < 21:
            return "лет"
        else:
            return "лет"


class ProfileCompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'profile_app/profile_company.html'
    model = Company

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileCompanyDetailView, self).get_context_data(*args, **kwargs)
        # add extra field
        context['vacancies'] = vacancies = Vacancy.objects.filter(company=self.request.user.id)
        return context


class ProfileCompanyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_app/profile_company_form.html'
    form_class = ProfileCompanyForm
    model = Company


class CompanyListView(LoginRequiredMixin, ListView):
    template_name = 'profile_app/companies.html'
    model = Company

