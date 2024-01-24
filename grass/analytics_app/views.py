from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import plotly.express as px
from vacancy_app.models import Vacancy, WORKEXP_CHOICES
from profile_app.models import Company, Profile, ExpJob, Education
from django.db.models import Count
import pandas as pd
import plotly.graph_objects as go

def get_exp_salary_scat():
    exp = Vacancy.objects.values('work_experience', 'salary_min')
    salary = Vacancy.objects.values('salary_min')
    df = pd.DataFrame(exp)
    fig_scatter = px.scatter(df,x='work_experience',y='salary_min')
    scatter_chart = fig_scatter.to_html(full_html=True, include_plotlyjs=False)
    return scatter_chart

def get_top_jobs():
    top_jobs = Vacancy.objects.values('job_name')
    df = pd.DataFrame(top_jobs)
    counts = df['job_name'].value_counts()
    res = df[~df['job_name'].isin(counts[counts < 100].index)]
    fig_hist = px.histogram(res).update_xaxes(categoryorder='total descending')
    fig_hist.update_layout(
        xaxis_title="Вакансии",
        yaxis_title="Востребованность",
        showlegend=False)
    job_hist = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return job_hist

def get_avg_salary_hist():
    min_salary = Vacancy.objects.values('salary_min').filter(salary_min__lt=110000)
    df = pd.DataFrame(min_salary)
    fig_hist = px.histogram(df,nbins=20)
    fig_hist.update_layout(
        xaxis_title="Средняя зарлата",
        yaxis_title="Количество предложений",
        showlegend=False,
        bargap=0.1)
    salary_hist = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return salary_hist

def get_req_exp_chart():
    # Pie Chart
    workexp_count = Vacancy.objects.values('work_experience').annotate(cnt=Count('work_experience'))
    dwe = dict(WORKEXP_CHOICES)
    for x in workexp_count:
        x['work_experience'] = dwe[x['work_experience']]

    df = pd.DataFrame(workexp_count)
    fig_pie = px.pie(df, values='cnt', names='work_experience', height=350)
    fig_pie.update_layout(legend=dict(
        yanchor="top",
        y=-0.05,
        xanchor="left",
        x=0.01
    ))
    exp_chart = fig_pie.to_html(full_html=False, include_plotlyjs=False)
    return exp_chart


# Create your views here.
@login_required
def draw_charts(request):

    # Scatter Chart
    df = px.data.iris()
    fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length", color="species", height=300, hover_data=['petal_width'])

    # Line Chart
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")

    fig_line = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year", height=300)
    fig_line.update_traces(textposition="bottom right")



    line_chart = fig_line.to_html(full_html=False, include_plotlyjs=False)
    top_jobs_hist = get_top_jobs()
    min_salary_hist = get_avg_salary_hist()
    req_exp_chart = get_req_exp_chart()
    exp_salary_scat = get_exp_salary_scat()

    return render(request, "analytics_app/analytics.html", {"bar_chart": min_salary_hist,
                                                            'hist_chart': top_jobs_hist,
                                                            "scatter_chart": exp_salary_scat,
                                                            "line_chart": line_chart,
                                                            "pie_chart": req_exp_chart,
                                                            }
                  )