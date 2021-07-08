from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return render(response, "main/base.html", {})

def create(response):
    return render(response, "main/create.html", {'rangeHour':range(24), 'rangeMinute':range(0,60,15)})
