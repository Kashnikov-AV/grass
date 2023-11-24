from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vacancy
from .forms import VacancyForm
from profile_app.models import Company
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
def hx_delete_vacancy(request, pk):
    vacancy_object = request.user.company.vacancy.get(pk=pk)
    vacancy_object.delete()

    vacancy_list = request.user.company.vacancy.all()
    return render(request, 'vacancy_app/partials/entity-card-vacancy.html', {
        'object_list': vacancy_list,
    })


@login_required
@require_http_methods(["GET", "POST"])
def hx_create_company_vacancy_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST or None)
        if form.is_valid():
            form.instance.company = company
            form.save()
            return HttpResponseClientRefresh()
    else:
        form = VacancyForm()
    return render(request, 'vacancy_app/partials/modal-vacancy-add.html', {
        'form': form
    })


class CompanyVacancyListView(LoginRequiredMixin, ListView):
    template_name = 'vacancy_app/partials/modal-vacancy.html'
    model = Vacancy

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(company=self.request.user.company)


class VacancyListView(ListView):
    template_name = 'vacancy_app/vacancies.html'
    paginate_by = 8
    model = Vacancy


class CompanyVacancyDetailView(DetailView):
    template_name = 'vacancy_app/vacancy-detail.html'
    model = Vacancy