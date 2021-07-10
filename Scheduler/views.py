from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Table, Activity
from .forms import CreateNewSchedule
from .time_values import TIME_VALUES
# Create your views here.

def home(response):
    if response.method == "POST":
        form = CreateNewSchedule(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Table(name=n)
            t.save()
            return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewSchedule()
    return render(response, "main/home.html", {"form":form})

def contact(response):
    return render(response, "main/contact.html", {})

def schedule(response, id):
    t = Table.objects.get(id=id)
    if response.method == "POST":
        if response.POST.get("add"):
            name = response.POST.get("name")
            day = response.POST.get("day")
            time = response.POST.get("time")
            t.activity_set.create(text=name, day=day, time=time)
            """To clear POST request we gotta redirect to the same page, i'm not really sure if this is proper solution but it works just fine so i'll leave it like this sorry :/"""    
            return HttpResponseRedirect("/%i" %id) 
            
    return render(response, "main/create.html", {'rangeHour':range(24), 
                                                'rangeMinute':range(0,60,30), 
                                                'rangeDays':['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'], 
                                                'table':t,
                                                'TIME_VALUES':TIME_VALUES})
