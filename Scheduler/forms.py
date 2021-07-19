from django import forms

class CreateNewSchedule(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

class CreateNewActivity(forms.Form):
    name = forms.CharField(label="Name", max_length=25, required=True)
    day = forms.CharField(label="Day", max_length=10, required=True)
    time = forms.CharField(label="Time", max_length=10, required=True)