from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Profile, Company, Education, ExpJob
from vacancy_app.models import Vacancy
from .forms import (ProfileMainInfoForm, ProfileAboutMeForm,
                    ProfileEducationForm, CompanyContactDataForm,
                    ProfileContactDataForm, CompanyMainInfoForm,
                    ProfileExpForm, CompanyAboutMeForm)
from vacancy_app.forms import VacancyForm
from datetime import datetime
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


@login_required
def hx_delete_education(request, pk):
    edu_object = request.user.profile.educations.get(pk=pk)
    edu_object.delete()

    edu_list = request.user.profile.educations.all()
    return render(request, 'profile_app/partials/entity-card-education.html', {
        'object_list': edu_list,
    })

@login_required
@require_http_methods(["GET", "POST"])
def hx_update_view(request, pk, model, form):
    if model == 'Profile':
        my_model = Profile
    elif model == 'Company':
        my_model = Company
    elif model == 'Education':
        my_model = Education
    elif model == 'ExpJob':
        my_model = ExpJob
    elif model == 'Vacancy':
        my_model = Vacancy

    object_model = get_object_or_404(my_model, pk=pk)

    if request.method == "POST":
        #profile forms
        if form == 'ProfileAboutMeForm':
            object_form = ProfileAboutMeForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-about-me.html'
        elif form == 'ProfileEducationForm':
            object_form = ProfileEducationForm(request.POST, request.FILES, instance=object_model)
            template = 'profile_app/partials/modal-education-update.html'
        elif form == 'ProfileContactDataForm':
            object_form = ProfileContactDataForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-contact-data-profile.html'
        elif form == 'ProfileMainInfoForm':
            object_form = ProfileMainInfoForm(request.POST, request.FILES, instance=object_model)
            template = 'profile_app/partials/modal-main-information.html'
        elif form == 'ProfileExpForm':
            object_form = ProfileExpForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-exp-job-update.html'


        #company forms
        elif form == 'CompanyMainInfoForm':
            object_form = CompanyMainInfoForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-main-information-company.html'
        elif form == 'CompanyContactDataForm':
            object_form = CompanyContactDataForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-contact-data-company.html'
        elif form == 'CompanyAboutMeForm':
            object_form = CompanyAboutMeForm(request.POST, instance=object_model)
            template = 'profile_app/partials/modal-about-company.html'
        #vacancy forms
        elif form == 'VacancyForm':
            object_form = VacancyForm(request.POST, instance=object_model)
            template = 'vacancy_app/partials/modal-vacancy-update.html'

        if object_form.is_valid():
            object_form.save()
            return HttpResponseClientRefresh()
    else:
        # profile forms
        if form == 'ProfileAboutMeForm':
            object_form = ProfileAboutMeForm(instance=object_model)
            template = 'profile_app/partials/modal-about-me.html'
        elif form == 'ProfileEducationForm':
            object_form = ProfileEducationForm(instance=object_model)
            template = 'profile_app/partials/modal-education-update.html'
        elif form == 'ProfileContactDataForm':
            object_form = ProfileContactDataForm(instance=object_model)
            template = 'profile_app/partials/modal-contact-data-profile.html'
        elif form == 'ProfileMainInfoForm':
            if object_model.gender is None:
                object_model.gender = 0
            if object_model.relocate is None:
                object_model.relocate = 0
            object_form = ProfileMainInfoForm(instance=object_model, initial={'gender': int(object_model.gender), 'relocate': int(object_model.relocate)})
            template = 'profile_app/partials/modal-main-information.html'
        elif form == 'ProfileExpForm':
            object_form = ProfileExpForm(instance=object_model)
            template = 'profile_app/partials/modal-exp-job-update.html'

        # company forms
        elif form == 'CompanyMainInfoForm':
            object_form = CompanyMainInfoForm(instance=object_model)
            template = 'profile_app/partials/modal-main-information-company.html'
        elif form == 'CompanyContactDataForm':
            object_form = CompanyContactDataForm(instance=object_model)
            template = 'profile_app/partials/modal-contact-data-company.html'
        elif form == 'CompanyAboutMeForm':
            object_form = CompanyAboutMeForm(instance=object_model)
            template = 'profile_app/partials/modal-about-company.html'
        # vacancy forms
        elif form == 'VacancyForm':
            object_form = VacancyForm(instance=object_model)
            template = 'vacancy_app/partials/modal-vacancy-update.html'

    return render(request, template, {
        'form': object_form,
        'model': object_model,
    })


@login_required
@require_http_methods(["GET", "POST"])
def hx_create_profile_education_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileEducationForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.instance.profile = profile
            form.save()
            return HttpResponseClientRefresh()
    else:
        form = ProfileEducationForm()
    return render(request, 'profile_app/partials/modal-education-add.html', {
        'form': form
    })


class ProfileEducationListView(LoginRequiredMixin, ListView):
    template_name = 'profile_app/partials/modal-education.html'
    model = Education

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(profile=self.request.user.profile)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'profile_app/profile.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        # add extra field
        profile = Profile.objects.get(pk=self.object.pk)
        educations = profile.educations.all()
        context['educations'] = educations
        exps = profile.exp.all()
        context['exps'] = exps
        try:
            context["age"] = datetime.now().year - profile.birth_date.year
            context["end_age"] = self.right_end(int(context["age"]))
        except Exception:
            context["age"] = 0
            context["end_age"] = self.right_end(int(context["age"]))

        return context

    # правильное склонение лет год года
    def right_end(self, data: int) -> str:
        if data % 10 == 1:
            return "год"
        elif data % 10 > 1 and data % 10 < 5:
            return "года"
        elif data % 100 > 10 and data % 100 < 21:
            return "лет"
        else:
            return "лет"


class ProfileCompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'profile_app/company-profile.html'
    model = Company

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileCompanyDetailView, self).get_context_data(*args, **kwargs)
        # add extra field
        company = Company.objects.get(pk=self.object.pk)
        context['vacancies'] = vacancies = Vacancy.objects.filter(company=company)
        return context


class ProfileExpListView(LoginRequiredMixin, ListView):
    template_name = 'profile_app/partials/modal-exp-job.html'
    model = ExpJob

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(profile=self.request.user.profile)


@login_required
@require_http_methods(["GET", "POST"])
def hx_create_profile_exp_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileExpForm(request.POST or None)
        if form.is_valid():
            form.instance.profile = profile
            form.save()
            return HttpResponseClientRefresh()
    else:
        form = ProfileExpForm()
    return render(request, 'profile_app/partials/modal-exp-job-add.html', {
        'form': form
    })

@login_required
def hx_delete_exp(request, pk):
    exp_object = request.user.profile.exp.get(pk=pk)
    exp_object.delete()

    exp_list = request.user.profile.exp.all()
    return render(request, 'profile_app/partials/entity-card-exp.html', {
        'object_list': exp_list,
    })