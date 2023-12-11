from django.shortcuts import render
from .making_graphs import get_plot
# Create your views here.
def graphs(request):
    chart = get_plot()
    return render(request, 'analytics_app/graphs.html')