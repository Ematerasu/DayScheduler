from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Table, Activity
from .forms import CreateNewSchedule, CreateNewActivity
from .time_values import TIME_VALUES
from hashids import Hashids
from .serializers import ActivitySerializer, TableSerializer
from rest_framework import viewsets
# Create your views here.
hashids = Hashids(min_length=16)

# ViewSets define the view behavior.
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

def home(response):
    if response.method == "POST":
        form = CreateNewSchedule(response.POST)
        if response.POST.get("create"):
            if form.is_valid():
                n = form.cleaned_data["name"]
                t = Table(name=n)
                t.save()
                return HttpResponseRedirect("/%s" %hashids.encode(t.id))
        elif response.POST.get("load"):
            if form.is_valid():
                n = form.cleaned_data["name"]
                t = Table.objects.get(name=n)
                return HttpResponseRedirect("/%s" %hashids.encode(t.id))
    else:
        form = CreateNewSchedule()
    return render(response, "main/home.html", {"form":form})

def contact(response):
    return render(response, "main/contact.html", {})

def schedule(response, id):
    try:
        t = Table.objects.get(id=int(hashids.decode(id)[0]))
    except:
        t = None
    
    if response.method == "POST":
        if response.POST.get("add"):
            form = CreateNewActivity(response.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                day = form.cleaned_data["day"]
                start = form.cleaned_data["start"]
                end = form.cleaned_data["end"]
                temp = []
                start_idx = TIME_VALUES.index(start)
                end_idx = TIME_VALUES.index(end)
                for i in range(start_idx, end_idx):
                    temp.append(TIME_VALUES[i])
                t.activity_set.create(text=name, day=day, time=temp)
        elif response.POST.get("delete"):
            t.activity_set.filter(id=response.POST.get("id")).delete()
        """To clear POST request we gotta redirect to the same page, i'm not really sure if this is proper solution but it works just fine so i'll leave it like this sorry :/"""
        return HttpResponseRedirect("/%s" %hashids.encode(t.id))
    return render(response, "main/create.html", {'rangeHour':range(24), 
                                                'rangeMinute':range(0,60,30), 
                                                'rangeDays':['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'], 
                                                'table':t,
                                                'TIME_VALUES':TIME_VALUES})
