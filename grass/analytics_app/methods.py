import plotly.express as px
from vacancy_app.models import Vacancy, WORKEXP_CHOICES, EMPLOYMENT_CHOICES
from profile_app.models import Company, Profile, ExpJob, Education
from django.db.models import Count
import pandas as pd
import plotly.graph_objects as go

#Убрать время, оставить дату, надо поучиться работать с DateTime
def get_hist_date():
    date = Vacancy.objects.values('created_at')
    df = pd.DataFrame(date)
    fig_hist = px.histogram(df).update_xaxes(categoryorder='total descending')
    hist_date = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return hist_date


#Имена вместо цифр, сделать более удобочитаемым
def get_hist_workmod():
    workmod = Vacancy.objects.values('working_mode').annotate(cnt=Count('working_mode'))
    df = pd.DataFrame(workmod)
    dwe = dict(EMPLOYMENT_CHOICES)
    for x in workmod:
        x['workmod'] = dwe[x['working_mode']]
    fig_hist = px.histogram(df).update_xaxes(categoryorder='total descending')
    hist_workmod = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return hist_workmod

#Заменить на имена, сделать меньше компаний, создать по убыванию
def get_hist_co():
    company = Vacancy.objects.values('company')
    df = pd.DataFrame(company)
    fig_hist = px.histogram(df).update_xaxes(categoryorder='total descending')
    hist_co = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return hist_co


#Сделать множество, чтобы не повторялись вакансии и у - Зп, х - имя вакансии
def get_top_job_salary():
    values = Vacancy.objects.values('job_name','salary_min')
    df = pd.DataFrame(values)
    counts = df['job_name'].value_counts()
    res = df[~df['job_name'].isin(counts[counts < 250].index)]
    fig_hist = px.histogram(res['salary_min'])
    top_job_sal = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return top_job_sal


#To do: Разбить дату, сделать без скобок и тд
def get_top_req():
    req = Vacancy.objects.values('requirements')
    df = pd.DataFrame(req).dropna()
    df = df.loc[df['requirements'] != 'NULL']
    # counts = df['req'].value_counts()
    # res = df[~df['req'].isin(counts[counts < 100].index)]
    fig_hist = px.histogram(req).update_xaxes(categoryorder='total descending')
    fig_hist.update_layout(
        xaxis_title="Требования",
        yaxis_title="Встречаемость",
        showlegend=False)
    top_req = fig_hist.to_html(full_html=False, include_plotlyjs=False)
    return top_req

#To DO: Доделать, оформить, подумоть, у одной профессии одно значние зп сделать
def get_exp_salary_scat():
    exp_salary = Vacancy.objects.values('work_experience', 'salary_min')
    df = pd.DataFrame(exp_salary)
    fig_scatter = px.scatter(df,x='salary_min',y='work_experience')
    scatter_chart = fig_scatter.to_html(full_html=True, include_plotlyjs=False)
    return scatter_chart

def get_top_jobs():
    top_jobs = Vacancy.objects.values('job_name')
    df = pd.DataFrame(top_jobs)
    counts = df['job_name'].value_counts()
    res = df[~df['job_name'].isin(counts[counts < 250].index)]
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