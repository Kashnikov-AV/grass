from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import plotly.express as px
from vacancy_app.models import Vacancy, WORKEXP_CHOICES
from profile_app.models import Company, Profile, ExpJob, Education
from django.db.models import Count
import pandas as pd

def get_req_exp_chart():
    # Pie Chart
    workexp_count = Vacancy.objects.values('work_experience').annotate(cnt=Count('work_experience'))
    dwe = dict(WORKEXP_CHOICES)
    for x in workexp_count:
        x['work_experience'] = dwe[x['work_experience']]

    df = pd.DataFrame(workexp_count)
    print(df)
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

    # Bar Chart
    wide_df = px.data.medals_wide()

    fig_bar = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input", height=300)

    # Scatter Chart
    df = px.data.iris()
    fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length", color="species", height=300, hover_data=['petal_width'])

    # Line Chart
    df = px.data.gapminder().query("country in ['Canada', 'Botswana']")

    fig_line = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year", height=300)
    fig_line.update_traces(textposition="bottom right")



    bar_chart = fig_bar.to_html(full_html=False, include_plotlyjs=False)
    scatter_chart = fig_scatter.to_html(full_html=True, include_plotlyjs=False)
    line_chart = fig_line.to_html(full_html=False, include_plotlyjs=False)

    req_exp_chart = get_req_exp_chart()

    return render(request, "analytics_app/analytics.html", {"bar_chart": bar_chart ,
                                                            "scatter_chart": scatter_chart,
                                                            "line_chart": line_chart,
                                                            "pie_chart": req_exp_chart,
                                                            }
                  )