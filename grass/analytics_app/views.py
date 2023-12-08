from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def graphs(request):
    return render(request, 'analytics_app/graphs.html')