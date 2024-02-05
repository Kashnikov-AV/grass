from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import methods

# Create your views here.
@login_required
def draw_charts(request):

    top_jobs_hist = methods.get_top_jobs()
    min_salary_hist = methods.get_avg_salary_hist()
    req_exp_chart = methods.get_req_exp_chart()
    exp_salary_scat = methods.get_exp_salary_scat()
    top_req = methods.get_top_req()
    top_job_salary = methods.get_top_job_salary
    hist_co = methods.get_hist_co()
    hist_workmod = methods.get_hist_workmod()
    hist_date = methods.get_hist_date()

    return render(request, "analytics_app/analytics.html", {"bar_chart": min_salary_hist,
                                                            'hist_chart': top_jobs_hist,
                                                            "scatter_chart": exp_salary_scat,
                                                            "pie_chart": req_exp_chart,
                                                            'top_req' : top_req,
                                                            'top_job_salary' : top_job_salary,
                                                            'hist_co' : hist_co,
                                                            'hist_workmod' : hist_workmod,
                                                            'hist_date' : hist_date,
                                                            }
                  )